# Información General

Programa escrito en Python usando las librerías: pandas, pyDOE2 (fracfact), statsmodels.formula.api.ols, statsmodels.stats.anova.anova_lm y pingouin.

# Guía

## Instalar las bibliotecas necesarias:
```
pip install pandas pyDOE2 statsmodels pingouin
```

## Descargar el repositorio:
```
git clone https://github.com/GustavoRamos112/fractional-factorial-analysis.git
```

## Uso

En tu directorio de trabajo, copia los archivos "Grafica" y "Limpiar modelo". Cada uno de estos archivos contiene solo una función:

### Limpiar modelo

```
limp_mod(_Fn, _Y, _Y_n, _disc, _max, _tol=100000, _det=False, _C='F')
```

- _Fn = Nombre de los factores (lista) **Más información al final**
- _Y = Variable de respuesta (array de numpy)
- _Y_n = Nombre de la variable de respuesta (str)
- _disc = Discriminante, número mínimo que debe tener la suma de cuadrados para que la interacción se considere relevante en el modelo (float)
- _max = Número máximo para interacciones (2; x1:x2, 3; x1:x2:x3, ..., n; x1:x2:...:xn-1:xn) (int) **Más información al final**
- _tol = Número para la eliminación de renglones repetidos en la tabla de ANOVA, desaparecerá apenas encuentre un método para simplificar los factores (int)
- _det = Indica si quieres una limpieza detallada, donde se vayan mostrando en terminal todas las tablas y cálculos que se hacen (Por si quieres hacer un ajuste manual o corroborar este mismo) (bool)
- _C = Nombre que tendrá la variable C después de generar el modelo (str) **Más información al final**

Para la variable "_max", tengo la hipótesis de que debe ser de la forma k-1, donde k es el número de factores individuales (A, B, C, ..., X, Y, Z, no A:B, BSD = B:SD = B:S:D, etc).

Para _Fn, se usarán las letras en orden alfabético, sin embargo, para evitar problemas más adelante, la C se cambiará por F (a menos que se especifique otro nombre en _C).

La función devolverá 4 objetos:
1. Tabla de diseño = Es la tabla con los factores y el número de repeticiones
2. Tabla ANOVA = Tabla de ANOVA ya limpia de interacciones repetidas y también irrelevantes
3. Modelo = Modelo ya ajustado con ols.fit(), nos da las pendientes de cada interacción
4. Fórmula = La fórmula del modelo que es de la forma Y~(...)**_max + interacciones eliminadas

### Gráfica

```
grafica_modelo(modelo, nombre, fontsize=10, inicio=0, final=0, largo=18, ancho=6, _dpi=100, mostrar=False, color='blue', interacciones=[])
```

- modelo = Modelo ya ajustado (idealmente el que regresa la función anterior)
- nombre = Nombre con el que se guardará la imagen en la carpeta del trabajo (str)
- fontsize = Tamaño de letra para el título de cada gráfica (int)
- inicio = Permite elegir en qué interacción se iniciarán las gráficas (int)
- final = Permite elegir en qué interacción se terminarán las gráficas (int)
- largo, ancho = Indican el tamaño de la figura en pulgadas
- _dpi = Calidad de la imagen para cuando se guarde (int)
- mostrar = Indica si se quiere mostrar o no la gráfica luego de guardarse (usando matplotlib)
- color = Indica el color de las líneas de la gráfica (str color html)
- interacciones = Por si se quieren graficar ciertas interacciones, se dan en forma de lista (list)

Hay que tener en cuenta que las interacciones comienzan en 0, asi pues, Intercept es 0, A es 1 y asi sucesivamente (apoyarse de la tabla del modelo devuelta por la funcion anterior)

## Ejecutar main.py

Si usas mi perfil de PowerShell:
```
py main
```
Si no usas mi perfil de PowerShell:
```
python main.py
```

Si necesitas más ayuda o tienes alguna pregunta adicional, ¡házmelo saber!
