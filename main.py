import numpy as np

from Limpiar_modelo import limp_mod
from Grafica import grafica_modelo

#? Variable de respuesta
Y = np.array([7.37, 4.52, 2.17, 3.25, 3.44, 11.99, 3.12, 0.97, 5.24,
              3.41, 4.72, 10.02, 4.23, 4.28, 12.15, 6.29, 3.61, 22.22,
              1.30, 7.73, 1.63, 2.11, 23.18, 0.79, 2.54, 1.35, 28.24,
              26.32, 2.24, 6.70, 3.15, 0.31])

Y_n = 'Y'

discriminante = 1

maximo = 4

nombre_factores = ['A', 'B', 'C', 'D', 'E', 'ABC', 'ABD', 'BCDE']

Tabla, Anova, modelo_ajustado, formula_modelo = limp_mod(_Fn=nombre_factores, 
                                                        _Y=Y, _Y_n=Y_n, 
                                                        _disc=discriminante, 
                                                        _max=maximo)

""" print(f'\nFormula de modelo:\n{formula_modelo}\n')
print(f'\nTabla anova:\n{Anova}\n')
print(f'\nModelo ajustado:\n{modelo_ajustado.summary()}\n') """

grafica_modelo(modelo=modelo_ajustado, 
               nombre='prub.png', 
               fontsize=15, 
               inicio=1, 
               final=5, 
               largo=8,
               mostrar=True,
               color='#913C1E')