import warnings
warnings.filterwarnings('ignore')

import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

import pandas as pd
from pyDOE2 import fracfact
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import pingouin as pg

#? Variable de respuesta
Y = np.array([7.37, 4.52, 2.17, 3.25, 3.44, 11.99, 3.12, 0.97, 5.24,
              3.41, 4.72, 10.02, 4.23, 4.28, 12.15, 6.29, 3.61, 22.22,
              1.30, 7.73, 1.63, 2.11, 23.18, 0.79, 2.54, 1.35, 28.24,
              26.32, 2.24, 6.70, 3.15, 0.31])

discriminador = 1

maximo = 4

tolerancia = 100000

#? Hacer la matriz del experimento
factor_names = ['A', 'B', 'C', 'D', 'E', 'ABC', 'ABD', 'BCDE']

names = ''
mod = ''
new_names = []
p = len(factor_names)
for i in range(p):
    piv = factor_names[i]
    if i < p-1:
        names += f'{piv} '
        if 'C' in piv:
            piv = piv.replace('C', 'F')  
        
        mod += f'{piv}+'         

    else:
        names += piv
        if 'C' in piv:
            piv = piv.replace('C', 'F')

        mod += piv

    new_names.append(piv)

print(new_names)
Datos = fracfact(names)

#? Agregar el nombre a las columnas
Datos = pd.DataFrame(Datos, columns=new_names)

#? Agregar la respuesta
Datos['Y'] = Y

print(Datos)

model_formula = f'Y~({mod})**{maximo}'

#? Ajustar el modelo
mod1 = ols(model_formula, data=Datos).fit()
print(mod1.summary())

convinaciones = list(mod1.bse.index.values)[1:]

anova_table = []

excluidos = ''
for i in convinaciones:
    df = pg.anova(dv='Y', between=i.split(':'), data=Datos, detailed=True)
    m = df.to_numpy().tolist()
    try:
        ing = m[-2]
    except:
        ing = m[-1]

    if ing[1] < discriminador:
        l = str(ing[0].replace(' ', ''))
        m = l.replace('*',':')
        excluidos += f'-{m}'
    else:
        anova_table.append(ing)

print(excluidos)

print(anova_table)

anova = pd.DataFrame(anova_table, columns=['Source', 'SS', 'DF', 'MS', 'F', 'p-unc', 'np2'])
print(anova.to_string())

# Array para guardar los renglones eliminados
removed_rows = []

# Diccionario para rastrear los valores únicos en la tercera columna
unique_values = {}

# Lista para los renglones finales (sin duplicados)
final_rows = []

for row in anova_table:
    third_column_value = int(row[1]*tolerancia)
    if third_column_value not in unique_values:
        unique_values[third_column_value] = row
        final_rows.append(row)
    else:
        removed_rows.append(row)

anova_m = pd.DataFrame(final_rows, columns=['Source', 'SS', 'DF', 'MS', 'F', 'p-unc', 'np2'])
print("Anova mejorado")
print(anova_m.to_string())

print("\nRenglones eliminados:")
print(removed_rows)

r_r_l = len(removed_rows)

for i in range(r_r_l):
    x = str(removed_rows[i][0].replace(' ', ''))
    y = x.replace('*',':')
    excluidos += f'-{y}'

print(f'\nExcluidos: {excluidos}')

mod2 = ols(model_formula+excluidos, data=Datos).fit()
print(mod2.summary())

anova_table_2 = anova_lm(mod2, typ=2)
print("\nTabla ANOVA de una vía:")
print(anova_table_2)
