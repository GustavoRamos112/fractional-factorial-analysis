import warnings
warnings.filterwarnings('ignore')

import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

import pandas as pd
from pyDOE2 import fracfact
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import pingouin as pg

def limp_mod(_Fn, _Y, _Y_n, _disc, _max, _tol=100000, _det=False, _C = 'F'):
    names = ''
    mod = ''
    new_names = []
    p = len(_Fn)
    for i in range(p):
        piv = _Fn[i]
        if i < p-1:
            names += f'{piv} '
            if 'C' in piv:
                piv = piv.replace('C', _C)  
            
            mod += f'{piv}+'         

        else:
            names += piv
            if 'C' in piv:
                piv = piv.replace('C', _C)

            mod += piv

        new_names.append(piv)

    Datos = fracfact(names)

    #? Agregar el nombre a las columnas
    Datos = pd.DataFrame(Datos, columns=new_names)

    #? Agregar la respuesta
    Datos[_Y_n] = _Y    

    model_formula = f'Y~({mod})**{_max}'

    #? Ajustar el modelo
    mod1 = ols(model_formula, data=Datos).fit()

    if _det:
        print(f"\nNombres nuevos:\n{new_names}")
        print(f"\nTabla del diseño:\n{Datos}")
        print(f"\nModelo ajustado completo:\n{mod1.summary()}")

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

        if ing[1] < _disc:
            l = str(ing[0].replace(' ', ''))
            m = l.replace('*',':')
            excluidos += f'-{m}'
        else:
            anova_table.append(ing)

    anova = pd.DataFrame(anova_table, columns=['Source', 'SS', 'DF', 'MS', 'F', 'p-unc', 'np2'])
    
    if _det:
        print(f"\nInteracciones que no cuplen con sum sq > {_disc}:\n{excluidos}")
        print(f"\nAnova completo:\n{anova.to_string()}")

    #? Array para guardar los renglones eliminados
    removed_rows = []

    #? Diccionario para rastrear los valores únicos en la tercera columna
    unique_values = {}

    #? Lista para los renglones finales (sin duplicados)
    final_rows = []

    for row in anova_table:
        third_column_value = int(row[1]*_tol)
        if third_column_value not in unique_values:
            unique_values[third_column_value] = row
            final_rows.append(row)
        else:
            removed_rows.append(row)

    anova_m = pd.DataFrame(final_rows, columns=['Source', 'SS', 'DF', 'MS', 'F', 'p-unc', 'np2'])        

    r_r_l = len(removed_rows)

    for i in range(r_r_l):
        x = str(removed_rows[i][0].replace(' ', ''))
        y = x.replace('*',':')
        excluidos += f'-{y}'
    
    if _det:
        print(f"\nRenglones eliminados:\n{removed_rows}")
        
        print(f"\nAnova mejorado:\n{anova_m.to_string()}")

        print(f'\nExcluidos:\n{excluidos}')
    
    _formula = model_formula+excluidos

    mod2 = ols(_formula, data=Datos).fit()

    anova_table_2 = anova_lm(mod2, typ=2)

    return Datos, anova_table_2, mod2, _formula
