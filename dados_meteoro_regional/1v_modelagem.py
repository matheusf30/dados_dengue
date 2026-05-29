#!/usr/bin/env python
# coding: utf-8

#
##################################################
###
### Script inicial para a modelagem
###
### Versão 1
###
### Etapa 1: Abrindo os arquivos CSV
###
### Autoria: Everton Weber Galliani - 2026/03/13
###
##################################################
#

#BIBLIOTECAS
import numpy as np
import pandas as pd
import geopandas as gpd
import xarray as xr
import regionmask
from epiweeks import Week
from epiweeks import Year
from matplotlib import pyplot as plt
from matplotlib import colors as cls

from datetime import date, datetime, timedelta
import sys
import os

t0 = datetime.now()
print(f"Início da execução: {t0}")

#Definindo os caminhos e arquivos
_path = "/home/sifapsc/scripts/scripts_everton/regionais/dados_meteoro_regional"
_casos_file = "/casos_regional_total.csv"
_focos_file = "/focos_regional_total.csv"
_tmax_file = "/tmax_serie_regional_2000_2024.csv"
_tmed_file = "/tmed_serie_regional_2000_2024.csv"
_tmin_file = "/tmin_serie_regional_2000_2024.csv"
_prec_file = "/prec_serie_regional_2000_2024.csv"

#Abrindo os arquivos
casos = pd.read_csv(f"{_path}{_casos_file}")
focos = pd.read_csv(f"{_path}{_focos_file}")
tmax = pd.read_csv(f"{_path}{_tmax_file}")
tmed = pd.read_csv(f"{_path}{_tmed_file}")
tmin = pd.read_csv(f"{_path}{_tmin_file}")
prec = pd.read_csv(f"{_path}{_prec_file}")
arquivos = [casos, focos, tmax, tmed, tmin, prec]
for i in arquivos:
	i.index = pd.to_datetime(i["Semana"])
	print(i)

fig, ax = plt.subplots(2, 2, figsize = (20, 10))
ax[0][0].plot(casos["NORDESTE"].loc[pd.to_datetime("2020-01-01"):])
ax[0][1].plot(focos["NORDESTE"].loc[pd.to_datetime("2020-01-01"):])
ax[1][0].plot(tmax["NORDESTE"].loc[pd.to_datetime("2020-01-01"):])
ax[1][0].plot(tmed["NORDESTE"].loc[pd.to_datetime("2020-01-01"):])
ax[1][0].plot(tmin["NORDESTE"].loc[pd.to_datetime("2020-01-01"):])
ax[1][1].bar(prec.loc[pd.to_datetime("2020-01-01"):, "NORDESTE"].index, prec["NORDESTE"].loc[pd.to_datetime("2020-01-01"):])
plt.show()
print(f"Fim da execução: {datetime.now()}")
print(f"Tempo de execução: {datetime.now() - t0}")
