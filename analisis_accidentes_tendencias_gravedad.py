# -*- coding: utf-8 -*-
"""
# **Análisis de Accidentes de Tránsito en la Calle 30 de Barranquilla: Tendencias Anuales, Meses Críticos y Factores de Gravedad**

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

"""Estimados, en este punto del curso, ya son casi expertos en manejo de dataframes y por ello los felicito. Procedamos, **en cada punto haga el análisis correspondiente**.

**Tendencias Anuales: Meses con Mayor Incidencia de Accidentes** Mediante un gráfico [lineplot](https://seaborn.pydata.org/generated/seaborn.lineplot.html), en el cual, por año, se muestre el máximo número del total de accidentes ocurridos por mes.
"""

df_trans = pd.read_csv('https://www.datos.gov.co/api/views/yb9r-2dsi/rows.csv?accessType=DOWNLOAD');

fecha = pd.to_datetime(df_trans['FECHA_ACCIDENTE']);
hora  = pd.to_datetime(df_trans['HORA_ACCIDENTE'],format='%I:%M:%S:%p');
fecha_total = fecha+pd.to_timedelta(hora.dt.hour,unit='hr');
df_trans['Fecha'] = fecha_total;

columns = ['Fecha','CANTIDAD_ACCIDENTES'];
fechas = df_trans['Fecha'].dt;
grupos = [fechas.year,fechas.month];
formula = {'sum'};
df_trans1 = df_trans[columns].groupby(by=grupos).aggregate(formula);
df_trans1.index.names = ['Año','Mes'];
df_trans1.reset_index(inplace=True);
df_trans1.columns=['Año','Mes','Sum'];
df_trans1

columns = ['Año','Sum'];
grupos = ['Año'];
formula = {'max'};
df_trans2 = df_trans1[columns].groupby(by=grupos).aggregate(formula);
df_trans2.index.names = ['Año'];
df_trans2.reset_index(inplace=True);
df_trans2.columns=['Año','Maximo'];
df_trans2

sns.lineplot(data=df_trans2, x="Año", y="Maximo")

"""---

**Identificación de los Meses con Mayor Incidencia de Accidentes**
"""

columns = ['Fecha','CANTIDAD_ACCIDENTES'];
fechas = df_trans['Fecha'].dt;
grupos = [fechas.year,fechas.month];
formula = {'sum'};
df_trans3 = df_trans[columns].groupby(by=grupos).aggregate(formula);
df_trans3.index.names = ['Año','Mes'];
df_trans3.reset_index(inplace=True); #df_añomes = df_añomes.reset_index();
df_trans3.columns=['Año','Mes','Sum'];
df_trans3

columns = ['Mes','Sum'];
formula = {'sum'};
grupos = ['Mes'];
df_trans6 = df_trans3[columns].groupby(by=grupos).aggregate(formula);
df_trans6.index.names = ['Mes'];
df_trans6.reset_index(inplace=True);
df_trans6.columns=['Mes','total'];
df_trans6
df_trans6.sort_values(by=['total'],ascending=False)

"""Los meses **3,2,5,4 y 11** son los 5 meses con la **mayor cantidad de accidentes** *registrados* en el **intervalo de tiempo** correspondiente al **2015 hasta el mes 5 del 2020**.

**Análisis Horario de Accidentes por Día y Gravedad Usando FacetGrid** Se elaborará un `FacetGrid` en donde se muestre el total de accidentes por hora. El número de columnas debe corresponder con el número de años y el número de filas con el número de días de la semana. Discrimine (mediante la propiedad `hue`) la gravedad el accidente.
"""

columns = ['Fecha','GRAVEDAD_ACCIDENTE','CANTIDAD_ACCIDENTES','DIA_ACCIDENTE'];
fechas = df_trans['Fecha'].dt;
grupos = [fechas.year,'GRAVEDAD_ACCIDENTE','DIA_ACCIDENTE',fechas.hour];
formula = {'sum'};
df_transf = df_trans[columns].groupby(by=grupos).aggregate(formula);
df_transf.index.names = ['Año','Gravedad','dia','Hora'];
df_transf.reset_index(inplace=True);
df_transf.columns=['Año','Gravedad','dia','Hora','Cantidad'];
df_transf

sns.set_style('darkgrid')
g = sns.FacetGrid(df_transf,col='Año',row='dia',hue='Gravedad');
g.map(plt.plot,'Hora','Cantidad');
g.add_legend();
g.set_ylabels('Cantidad Accidentes');

"""---

**Visualización de la Variabilidad Anual de Accidentes Mensuales mediante Boxplot** Se elaborará un `boxplot` en donde se observe, por año, la variabilidad del total de accidentes por mes
"""

columns = ['Fecha','CANTIDAD_ACCIDENTES'];
fechas = df_trans['Fecha'].dt;
grupos = [fechas.year,fechas.month];
formula = {'sum'};
df_transe = df_trans[columns].groupby(by=grupos).aggregate(formula);
df_transe.index.names = ['Año','Mes'];
df_transe.reset_index(inplace=True);
df_transe.columns=['Año','mes','Cantidad'];
df_transe

df_transe.columns
sns.boxplot(data=df_añomesgravhora,x='Año',y='Cantidad',showfliers=True);

"""

---

"""