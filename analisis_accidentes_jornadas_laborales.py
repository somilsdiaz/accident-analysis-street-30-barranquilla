# -*- coding: utf-8 -*-
"""

# **Análisis de Accidentes de Tránsito en la Calle 30 de Barranquilla: Comparativa de Jornadas Laborales y Variabilidad Mensual**

![unnamed.png](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Logo_uninorte_colombia.jpg/360px-Logo_uninorte_colombia.jpg)

*   Autor: **Somil Sandoval Diaz**

Base de datos de los accidentes registrados en la calle 30 de Barranquilla, Colombia. La fuente de datos reposa en [Datos Abiertos](https://www.datos.gov.co/) , de manera especifica pueden consultar: [Accidentes de Tránsito Barranquilla Calle 30](https://www.datos.gov.co/Transporte/accidentes-calle-30-2015-2019/sefb-a755)

Para nuestro análisis, procedemos a cargar las librerías de Python
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
fecha_total = fecha+pd.to_timedelta(hora.dt.hour,unit='hr')+pd.to_timedelta(hora.dt.minute,unit='min');
df_trans['fecha'] = fecha_total;

"""---

**Variabilidad de Accidentes de Tránsito según la Jornada Laboral: Análisis de Datos Mensuales** Los dias seran divididos en las siguientes jornadas (categorías):

1.   Jornada Laboral Mañana (8:00 a.m. - 12:30 p.m.)
2.   Jornada Laboral Tarde  (2:30 p.m. - 6:30 p.m.)

Se elaborará un `boxplot` con la variabilidad del total de accidentes por mes vía la categorización propuesta. Descarte el año 2020 de su análisis.
"""

columns = ['fecha'];
agg_formula = {'sum'};
fecha = df_trans['fecha'].dt;
horai1 = pd.to_datetime('8:00');
horai2 = pd.to_datetime('14:30');
horaf1 = pd.to_datetime('12:30');
horaf2 = pd.to_datetime('18:30');
laboral_mañana = (fecha_total.dt.time>=horai1.time())&(fecha_total.dt.time<=horaf1.time());
laboral_tarde = (fecha_total.dt.time>=horai2.time())&(fecha_total.dt.time<=horaf2.time());
df_n = df_trans.copy(deep=True);
df_n['Período'] = 'Otros';
df_n.loc[laboral_mañana,'Período'] = 'Jornada laboral mañana';
df_n.loc[laboral_tarde,'Período'] = 'Jornada laboral tarde';

columns = ['Período','CANTIDAD_ACCIDENTES'];
grupos = ['Período',fecha.day,fecha.month];
agg_formula = {'sum'};
filtro = fecha.year<2020;
df_n2 = df_n.loc[filtro][columns].groupby(by=grupos).agg(agg_formula);
df_n2.index.names = ['Periodo','Dia','Mes'];
df_n2.reset_index(inplace=True);
df_n2.columns=['Periodo','Dia','Mes','Cantidad de accidentes'];

df_n2

sns.boxplot(data=df_n2,x='Periodo',y='Cantidad de accidentes');
plt.xticks(rotation=45);

g = sns.FacetGrid(data=df_n2,row='Mes');
g.map(sns.boxplot,'Periodo','Cantidad de accidentes','Dia');
plt.xticks(rotation=45);

plt.figure(figsize=(17,5.7));
sns.boxplot(x="Mes", y="Cantidad de accidentes", hue="Periodo",data=df_n2, linewidth=2.3, palette="Spectral");

"""**CONCLUSIONES**

Analizando la variabilidad de la **cantidad de accidentes registrados** de acuerdo al **DIA DEL MES**, entonces, de los anteriores graficos podemos concluir que:


1. **Historiacamente**, en promedio, suele registrarse, **aunque no mucho, un poco mas de accidentes diarios** en la **jornada laboral mañana** que en la tarde.


3. Entre el **25% y el 75%** de la **cantidad de accidentes promedios** registrados **cada dia** en el **mes 1(Enero)** fue practicamente el mismo tanto en la jornada laboral mañana como tarde, esto mismo **tambien sucedió en los meses 6 y 12.**


4. Analizando los datos **del mes 4**, determinamos que, en **terminos de media**, aproximadamente el 50% de los accidentes **registrados diariamente** en la jornada laboral mañana, corresponde cerca **del 75% de los accidentes diarios** ocurridos en la jornada laboral tarde.


5. En los **meses 5 y 7**, hubo **una mayor cantidad promedio de accidentes diarios** en la **jornada laboral tarde** que en la mañana, y estos fueron los **unicos meses en donde ocurrió esto**, lo cual, podemos afirmar que hay una **alta posibilidad **de que se registren mas accidentes diarios en la **jornada laboral mañana** que en la jornada laboral tarde.


6. *Entre muchas cosas mas que se pueden concluir a partir de las anteriores graficas.*

---
"""