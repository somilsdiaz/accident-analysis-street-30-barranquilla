# -*- coding: utf-8 -*-
"""

# **Análisis de Accidentes de Tránsito en la Calle 30 de Barranquilla: Factores Temporales y Tendencias**

![unnamed.png](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Logo_uninorte_colombia.jpg/360px-Logo_uninorte_colombia.jpg)

*   Autor: **Somil Sandoval Diaz**

Base de datos de los accidentes registrados en la calle 30 de Barranquilla, Colombia. La fuente de datos reposa en [Datos Abiertos](https://www.datos.gov.co/) , de manera especifica pueden consultar: [Accidentes de Tránsito Barranquilla Calle 30](https://www.datos.gov.co/Transporte/accidentes-calle-30-2015-2019/sefb-a755)
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""Creamos el `DataFrame` con la base de datos alojada en el servidor de Datos Abiertos:"""

df_trans = pd.read_csv('https://www.datos.gov.co/api/views/yb9r-2dsi/rows.csv?accessType=DOWNLOAD');

"""Los cincos primeros registros del DataFrame `df_trans` son:"""

df_trans.head(5)

"""Creamos una nueva columna en nuestro dataframe con el objetivo de manipular la fecha (dia,mes,año, y hora)"""

fecha = pd.to_datetime(df_trans['FECHA_ACCIDENTE']);
hora  = pd.to_datetime(df_trans['HORA_ACCIDENTE'],format='%I:%M:%S:%p');
fecha_total = fecha+pd.to_timedelta(hora.dt.hour,unit='hr');
df_trans['fecha'] = fecha_total;
df_trans.head(5)

"""**Análisis Trimestral de Accidentes de Tránsito en la Calle 30 de Barranquilla (2015-2019).** Se realizará  un `lineplot` en el cual se detalle el total de accidentes por trimestre del año. 
*Para esto: Se creo una nueva columna en el DataFrame `df_trans` en donde se indique el trimestre al cual pertenece el accidente, luego, empleando esta columna, ejecute la función de agregación apropiada.*

"""

columns = ['fecha'];
Primer_trimestre = (fecha.month>=1)&(fecha.month<=3);
Segundo_trimestre = (fecha.month>=4)&(fecha.month<=6);
Tercer_trimestre = (fecha.month>=7)&(fecha.month<=9);
Cuarto_trimestre = (fecha.month>=10)&(fecha.month<=12);
df_new = df_trans.copy(deep=True);
df_new['Trimestre'] = 'Otro';
df_new.loc[Primer_trimestre,'Trimestre'] = 'Primer trimestre';
df_new.loc[Segundo_trimestre,'Trimestre'] = 'Segundo trimestre';
df_new.loc[Tercer_trimestre,'Trimestre'] = 'Tercer trimestre';
df_new.loc[Cuarto_trimestre,'Trimestre'] = 'Cuarto trimestre';

columns = ['Trimestre','CANTIDAD_ACCIDENTES'];
grupos = ['Trimestre'];
agg_formula = {'sum'};
filtro = fecha.year<2020;
df_new2 = df_new[filtro][columns].groupby(by=grupos).agg(agg_formula);
df_new2.reset_index(inplace=True);
df_new2.columns=['Trimestre','Cantidad de accidentes'];
sns.set_style("white")

sns.set_style('darkgrid');
g = sns.lineplot(data=df_new2, x="Trimestre", y="Cantidad de accidentes")

"""**CONCLUSION**

Analizando la representacion de los datos en la anterior grafica, es posible afirmar que **historicamente** el trimestre numero cuatro ha sido el trimestre con la **mayor cantidad** de **accidentes** de transitos **registrados** en la calle 30 de Barranquilla, Colombia. Tambien podemos identificar un **comportamiento creciente** en la frecuencia con la ocurren los accidentes a medida que trascurren los trimestres en el año, lo cual, se ve **respaldado** por analisis posteriores, en donde se observa una **tendencia al aumento** de los casos de accidentes a medida que pasan los meses en el año.

**Distribución de Accidentes según el Momento del Día: Análisis por Categorías de Jornada** Se han dividido los dias en las siguientes jornadas (categorías):

1.   Jornada Laboral Mañana (8:00 a.m. - 11:59 m.)
2.   Jornada Laboral Tarde (2:00 p.m. - 5:59 p.m.)
3.   Horas Pico Mañana (6:00 a.m. - 7:59 a.m.)
4.   Horas Pico Tarde (12:00 p.m. - 1:59 p.m.)
5.   Tiempos Muertos (por fuera de los horarios previamente establecidos)

El siguiente `lineplot` contiene el total de accidentes vía la categorización propuesta.
"""

columns = ['fecha'];
agg_formula = {'sum'};
laboral_mañana = (fecha.hour>=8)&(fecha.hour<12);
laboral_tarde = (fecha.hour>=14)&(fecha.hour<18);
pico_mañana = (fecha.hour>=6)&(fecha.hour<8);
pico_tarde = (fecha.hour>=12)&(fecha.hour<14);
df_new2 = df_trans.copy(deep=True);
df_new2['Período'] = 'Tiempos muertos';
df_new2.loc[laboral_mañana,'Período'] = 'Jornada laboral mañana';
df_new2.loc[laboral_tarde,'Período'] = 'Jornada laboral tarde';
df_new2.loc[pico_mañana,'Período'] = 'Hora picos mañna';
df_new2.loc[pico_tarde,'Período'] = 'Hora picos tarde';

columns = ['Período','CANTIDAD_ACCIDENTES'];
grupos = ['Período'];
agg_formula = {'sum'};
filtro = fecha.year<2020;
df_new3 = df_new2[filtro][columns].groupby(by=grupos).agg(agg_formula);
df_new3.reset_index(inplace=True);
df_new3.columns=['Período','Cantidad de accidentes'];



df_new3

plot = g = sns.lineplot(data=df_new3, x="Período", y="Cantidad de accidentes");
plt.xticks(rotation=45);

"""**CONCLUSION**

Historicamente es notable una **marcada diferencia** en la **concurencia de los accidentes** en conformidad al **momento u hora del dia**. Segun la representacion de los datos en la grafica, la mayor cantidad de accidentes han ocurridos entre las 2:00 pm y las 5:59 pm, seguido de otros puntos maximos en las horas comprendidas de la jornada laboral mañana y "tiempos muertos",  por lo cual, es factible afirmar que es mas probable que se registre o se de un **pico de accidentes diarios** entre el transcurso de la jornada laboral de la mañana, de la tarde o en "tiempos muertos".

**Análisis de la Variabilidad de Accidentes por Trimestre y Día de la Semana: Boxplots por Año** Teniendo en cuenta la categorización por trimestres detallada en el **la primera seccion*, se elaborara un `FacetGrid` en donde cada celda contenga un `boxplot` con la variabilidad del total de accidentes por trimestre. El número de columnas debe corresponder con el número de años y el número de filas con el número de días de la semana.

"""

columns = ['fecha'];
Primer_trimestre = (fecha.month>=1)&(fecha.month<=3);
Segundo_trimestre = (fecha.month>=4)&(fecha.month<=6);
Tercer_trimestre = (fecha.month>=7)&(fecha.month<=9);
Cuarto_trimestre = (fecha.month>=10)&(fecha.month<=12);
df_new4 = df_trans.copy(deep=True);
df_new4['Trimestre'] = 'Otro';
df_new4.loc[Primer_trimestre,'Trimestre'] = '1';
df_new4.loc[Segundo_trimestre,'Trimestre'] = '2';
df_new4.loc[Tercer_trimestre,'Trimestre'] = '3';
df_new4.loc[Cuarto_trimestre,'Trimestre'] = '4';


columns = ['fecha','Trimestre','CANTIDAD_ACCIDENTES','DIA_ACCIDENTE'];
grupos = [fecha.year,fecha.month,'Trimestre','DIA_ACCIDENTE'];
agregacion = {'sum'};
filtro = fecha.year<2020;
df_new_1 = df_new4[filtro][columns].groupby(by=grupos).agg(agregacion);
df_new_1.index.names = ['Año','Mes','Dia','Trimestre'];
df_new_1.reset_index(inplace=True);
df_new_1.columns = ['Año','Mes','Trimestre','Dia','Cantidad'];

df_new_1

g = sns.FacetGrid(data=df_new_1,col='Año', row='Dia');

g.map(sns.boxplot,'Trimestre','Cantidad');

"""**CONCLUSION**

Efectivamente se logra observar un **progresivo aumento** aunque no muy pronunciado, en la media de accidente ocurridos por trimestre del año, lo cual **tiene sentido y concuerda** con conclusiones anteriores. Tambien identificiamos que en el tercer trimestre del año 2016 hallamos **la media mas alta de accidentes** ocurridos **por mes en los dias viernes**, y la media mas baja registrada por meses corresponde al trimestre 3 del dia domingo del año 2019. Realmente hay un mundo de mucha informacion en el anterior FacetGrid, y podemos determinar y concluir demasiadas cosas en relacion a los porcentiles y otras cosas mas por nombrar.

---
"""