import os
import sys
import json
import logging
from datetime import datetime, timedelta

import tweepy
import numpy as np
import pandas as pd

from months import MONTHS_DICT

DATA_SOURCE = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv"
BAR_CHARS = 16
# People over 12 years old (according to INE projected data for 2021)
# NOTE: This number is still below the 75% threshold for herd immunity
# It represents only ~71% of the population
TOTAL_POP = 17109746
VAX_POP = 12293144

def logging_setup():
    logging.basicConfig(filename='logs/bot.log', level=logging.INFO, format='%(message)s')
    return

def should_tweet(df):
    final_line = None
    with open("logs/bot.log", "r") as log_file:
        for line in log_file:
            final_line = line
            pass
    if final_line is None:
        return True

    final_date = datetime.strptime(final_line[:10], '%Y-%m-%d')
    print(final_date, df['date'].values[-1])
    return (df.tail(1)['date'] > final_date).any()

# From https://github.com/imbstt/impf-progress-bot/blob/master/bot.py
def generate_bar(percentage, n_chars = None):
    if not n_chars:
       n_chars = BAR_CHARS
    num_filled = round(percentage*n_chars)
    num_empty = n_chars-num_filled
    display_percentage = str(round(percentage*100, 1))
    msg = '{}{} {}%'.format('▓'*num_filled, '░'*num_empty, display_percentage)
    return msg

def get_data():
    df = pd.read_csv(DATA_SOURCE)
    df = df.query("iso_code == 'GTM'").copy()
    df['date'] = pd.to_datetime(df['date'])
    df['vacc_change'] = df['people_vaccinated_per_hundred'].diff()
    df['full_vacc_change'] = df['people_fully_vaccinated_per_hundred'].diff()
    df['booster_change'] = df['total_boosters_per_hundred'].diff()
    return df.tail(14)

def get_auth():
    with open("config.json", "r") as json_data_file:
        credentials = json.load(json_data_file)

    consumer_key = credentials['CONSUMER_KEY']
    consumer_secret = credentials['CONSUMER_SECRET']
    access_key = credentials['ACCESS_KEY']
    access_secret = credentials['ACCESS_SECRET']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    return auth

def get_estimated_herd(df: pd.DataFrame, by: float = .75):
    """Return the estimated date to reach herd immunity

        Keyword arguments:
        df -- A dataframe of 1 row with the necessary information to calculate the date
        by -- A float that represents at what percentage of the population herd immunity is reached
    """
    df = df.tail(1)
    daily_vaccs = df['daily_vaccinations'].values[0]
    days_left = ((VAX_POP - df['people_vaccinated'].values[0] - df['people_fully_vaccinated'].values[0]) * 2 + df['people_vaccinated'].values[0]) // daily_vaccs
    estimated_date = datetime.now() + days_left * timedelta(days=1)
    est_str = estimated_date.strftime("%b %Y")
    month_str = est_str[:3]

    # Modify month string without having to resort to changing locale
    est_str = est_str.replace(month_str, MONTHS_DICT.get(month_str, month_str))
    return est_str

def main(dry_run):
    logging_setup()
    df = get_data()
    partial_vax = generate_bar(df['people_vaccinated_per_hundred'].values[-1] / 100)
    full_vax = generate_bar(df['people_fully_vaccinated_per_hundred'].values[-1] / 100)
    booster_bar = generate_bar(df['total_boosters_per_hundred'].values[-1] / 100)
    change_vax = f"(+{round(df['vacc_change'].values[-1], 2)}%) " if not np.isnan(df['vacc_change'].values[-1]) else ""
    change_fully_vax = f"(+{round(df['full_vacc_change'].values[-1], 2)}%) " if not np.isnan(df['full_vacc_change'].values[-1]) else ""
    change_booster = f"(+{round(df['booster_change'].values[-1], 2)}%) "  if not np.isnan(df['booster_change'].values[-1]) else ""

    tweet = f"{partial_vax} {change_vax}parcial\n{full_vax} {change_fully_vax}completa\n{booster_bar} {change_booster}refuerzo"

    auth = get_auth()
    twitter_api = tweepy.API(auth)

    if dry_run:
        print(tweet)
        print(f"Should it be tweeted? -- {should_tweet(df)}")
        return
    if should_tweet(df):
        twitter_api.update_status(tweet)
        last_date = df['date'].values[-1]
        ts = (last_date - np.datetime64('1970-01-01T00:00:00')) / np.timedelta64(1, 's')
        logging.info(f'{datetime.utcfromtimestamp(ts)} Tweet out')
    return

if __name__ == '__main__':
    dry_run = '--dry-run' in sys.argv or '-d' in sys.argv
    main(dry_run)

