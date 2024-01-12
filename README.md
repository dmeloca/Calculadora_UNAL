# Calculadora UNAL
### Este es un proyecto para hacer el cálculo de los requisitos necesarios para la doble titulación en la Universidad Nacional de Colombia.

## Proceso
### 1. Aplicación para consola
Como primer paso del proyecto, se realizo la estructura básica del programa; por ejemplo, las funciones para la comparación de los diccionarios que contienen las materias propias de cada programa. 
En este caso, simplemente descargar el ".py" y ejecutarlo.
### 2. Aplicación con interfaz gráfica
Luego, se realizó la interfaz gráfica con tkinter y se modificó lo necesario para su correcto e intuitivo funcionamiento con este nuevo arreglo.
De este programa hay dos versiones una con tkinter básico (/GraficInterface/main.py) y otro con ttkbootstrap (/GraficInterface/ttkbootsrap) el cual mejora un poco el diseño del programa inicial

### 3.Aplicación con lector de pdf
El programa en la rama main, coge una ruta dispuesta y extrae todo el texto del pdf ubicado allí.
En la rama "readingPDF" esta el programa con commits un poco más adelantados, pues se esta contruyendo el algoritmo para el cálculo de la doble titulación, por el momento solo extrae información del usuario (Nombre, programa y P.A.P.A)

## Librerias
#### 1. Pickle
#### 2. tkinter
#### 3. fitz
