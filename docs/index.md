# Progreso de vacunación en Guatemala

Este proyecto no está asociado de ninguna forma con el MSPAS, OWID, o ninguna institución oficial. El proyecto fue desarrollado en el tiempo libre de [@jjdelvalle](https://github.com/jjdelvalle). El proyecto se desarrolló bajo la licencia MIT.

El bot revisara los datos constantemente durante el día entre las 8 y 20 horas, lo cual significa que generalmente los tuits de actualización serán enviados a las 8 de la mañana.

## Fuente de datos

Los datos son obtenidos de la siguiente fuente:

* [OWID COVID-19 Data](https://github.com/owid/covid-19-data/tree/master/public/data/vaccinations)

Esto se hace por conveniencia ya que se ofrecen los ultimos datos de vacunación en un archivo `csv`, el cual es más fácilmente digerible.
Los datos de OWID son alimentados directamente por MSPAS. En efecto, las cifras reportadas acá son las cifras oficiales presentadas por las autoridades.

Adicionalmente, se utiliza una cifra de 8,244,536 personas para el cálculo de porcentajes y proyecciones de inmunidad de rebaño.
Esta cifra representa a toda persona mayor a 20 años según el [censo poblacional 2018](https://www.censopoblacion.gt/graficas).

## Cálculos

### Inmunidad de rebaño

No existe un consenso científico de un porcentaje necesario para llegar a inmunidad de rebaño.
Sin embargo, algunos expertos sugieren un porcentaje entre 60 y 70, y [otros hasta un porcentaje de 85%](https://www.cnbc.com/2020/12/16/cnbc-transcript-dr-anthony-fauci-speaks-with-cnbcs-meg-tirrell-live-during-the-cnbc-healthy-returns-livestream-today.html).
Debido a esto, el estimado para la inmunidad resulta ser bastante conservador al elegir un numero como 75%.

### Número de vacunas al día

Los datos calculados por OWID proveen un promedio de vacunas diarias administradas según los datos de los días más recientes.
Este número se utilizar para calcular la fecha estimada para la inmunidad.
La ventaja de esto es que nos permite controlar un poco la variabilidad que se tiene en un día a día y funciona muy bien en países en donde la oferta de vacunas es relativamente constante.
En el caso de Guatemala, en donde los periodos de vacunación son irregulares y la oferta de vacunas no es constante, este número no resulta ser tan estable para este tipo de cálculo.
Esto resultará en tener un estimado bastante optimista después de un periodo corto de vacunación activa.
También resultará en un estimado bastante pesimista en periodos en donde la oferta de vacunas es muy baja.

Es probable que este cálculo se modifique en un futuro para tomar en cuenta la situación específica de Guatemala y su oferta de vacunas esprádica.

## Notas aclaratorias

* Los cálculos no toman en cuenta que al transcurrir los años más gente será elegible para obtener la vacuna y se deberán tomar en cuenta para el total de población a vacunar.
* La población total que se está considerando son adultos mayores a 20 años. Sin embargo algunas vacunas ya están siendo aprobadas para ser aplicadas en personas mayores de 16 o incluso de 12 años.

## Librerías utilizadas

* `pandas`
* `tweepy`
