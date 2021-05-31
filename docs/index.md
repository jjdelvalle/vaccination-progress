# Progreso de vacunación en Guatemala

Este proyecto no está asociado de ninguna forma con el MSPAS, OWID, o ninguna institución oficial.
El proyecto fue desarrollado en [mi](https://github.com/jjdelvalle) tiempo libre ([@imaginarytl](https://twitter.com/imaginarytl) en Twitter).
El proyecto se desarrolló bajo la licencia MIT.

El bot revisara los datos constantemente durante el día entre las 8 y 20 horas, lo cual significa que generalmente los tuits de actualización serán enviados a las 8 de la mañana.

## Fuente de datos

Los datos son obtenidos de la siguiente fuente:

* [OWID COVID-19 Data](https://github.com/owid/covid-19-data/tree/master/public/data/vaccinations)

Esto se hace por conveniencia ya que se ofrecen los ultimos datos de vacunación en un archivo `csv`, el cual es más fácilmente digerible.
Los datos de OWID son alimentados directamente por MSPAS. En efecto, las cifras reportadas acá son las cifras oficiales presentadas por las autoridades.

Adicionalmente, se utiliza una cifra de 12,293,144 personas para el cálculo de porcentajes.
Esta cifra representa a toda persona mayor a 12 años según [proyecciones del INE](https://www.ine.gob.gt/ine/proyecciones/) al año 2021 basadas en el [censo poblacional 2018](https://www.censopoblacion.gt/graficas).
Ya que Guatemala es un país muy joven, vacunar solamente a los adultos mayores de edad no es suficiente para alcanzar una inmunidad de rebaño.
La población abajo de 18 años representa casi el 40% de la población entera del país por lo que no se puede ignorar en el proceso de vacunación.

La vacuna de Pfizer/BioNTech reporta ser [efectiva y segura para niños mayores de 12 años](https://www.pfizer.com/news/press-release/press-release-detail/pfizer-biontech-announce-positive-topline-results-pivotal).
Esta vacuna, y próximas vacunas que sean demostradas seguras para niños y niñas, serán necesarias para países jóvenes como Guatemala.

## Cálculos

### Inmunidad de rebaño

No existe un consenso científico de un porcentaje necesario para llegar a inmunidad de rebaño.
Sin embargo, algunos expertos sugieren un porcentaje entre 60 y 70, y [otros hasta un porcentaje de 85%](https://www.cnbc.com/2020/12/16/cnbc-transcript-dr-anthony-fauci-speaks-with-cnbcs-meg-tirrell-live-during-the-cnbc-healthy-returns-livestream-today.html).
Debido a esto, el estimado para la inmunidad resulta ser bastante conservador al elegir un numero como 75%.
Este es el porcentaje utilizado para la estimación.
Así mismo, este se deberá aplicar sobre la cifra *total* poblacional, no solo sobre la población que se podrá vacunar.
Esto significa que la cifra meta para la inmunidad de rebaño es de 12.9M de personas.

El cálculo resulta siendo entonces `(POBLACIÓN META - vacunados) * 2 / vacunas diarias`.

Esto es correcto bajo las siguientes suposiciones:

1. Los números de vacunación reportados son correctos
1. Una meta del 75% para la inmunidad de rebaño
1. La población recibirá dos dosis antes de completar el esquema de vacunación y
1. El ritmo de los últimos días se mantendrá

### Número de vacunas al día

Los datos calculados por OWID proveen un promedio de vacunas diarias administradas según los datos de los días más recientes.
Este número se utilizar para calcular la fecha estimada para la inmunidad.
La ventaja de esto es que nos permite controlar un poco la variabilidad que se tiene en un día a día y funciona muy bien en países en donde la oferta de vacunas es relativamente constante.
En el caso de Guatemala, en donde los periodos de vacunación son irregulares y la oferta de vacunas no es constante, este número no resulta ser tan estable para este tipo de cálculo.
Esto resultará en tener un estimado bastante optimista después de un periodo corto de vacunación activa.
También resultará en un estimado bastante pesimista en periodos en donde la oferta de vacunas es muy baja.

Es probable que este cálculo se modifique en un futuro para tomar en cuenta la situación específica de Guatemala y su oferta de vacunas esporádica.

## Notas aclaratorias

* Los cálculos no toman en cuenta que al transcurrir los años más gente será elegible para obtener la vacuna y se deberán tomar en cuenta para el total de población a vacunar.
* La población total que se está considerando son adultos mayores a 12 años. Esto implica la importación de vacunas seguras para niños.

## Librerías utilizadas

* `pandas`
* `numpy`
* `tweepy`

## Agradecimientos

Gracias al Laboratorio de Datos ([@labdatosgt](https://twitter.com/labdatosgt)) por compartir su metodología al calcular estimados de vacunación y fuentes de datos.

