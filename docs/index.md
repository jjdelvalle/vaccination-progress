# Progreso de vacunación en Guatemala

## Fuente de datos

Los datos son obtenidos de la siguiente fuente:

* https://github.com/owid/covid-19-data/tree/master/public/data/vaccinations

Esto se hace por conveniencia ya que se ofrecen los ultimos datos de vacunación en un archivo `csv`, el cual es más fácilmente digerible.
Los datos de OWID son alimentados directamente por MSPAS. En efecto, las cifras reportadas acá son las cifras oficiales presentadas por las autoridades.

Adicionalmente, se utiliza una cifra de 8,244,536 personas para el cálculo de porcentajes y proyecciones de inmunidad de rebaño.
Esta cifra representa a toda persona mayor a 20 años según el [censo poblacional 2018](https://www.censopoblacion.gt/graficas).

## Cálculos

### Inmunidad de rebaño

No existe un consenso científico de un porcentaje necesario para llegar a inmunidad de rebaño.
Sin embargo, algunos expertos sugieren un porcentaje entre 60 y 70, y [otros hasta un porcentaje de 85%](https://www.cnbc.com/2020/12/16/cnbc-transcript-dr-anthony-fauci-speaks-with-cnbcs-meg-tirrell-live-during-the-cnbc-healthy-returns-livestream-today.html).
Debido a esto, el estimado para la inmunidad resulta ser bastante conservador al elegir un numero como 75%.
