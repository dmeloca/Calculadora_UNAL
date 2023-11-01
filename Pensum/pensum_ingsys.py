import pickle

#####  Ingeniería de Sistemas  #####

### Fundamentación

## Matemáticas

# Cálculo Diferencial

calculo_diferencial_ing = {
    'nombre': 'Cálculo Diferencial',
    'id': 'calculodiferencial',
    'codigo': 1000004,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '1000001 Matemáticas básicas',
    'tipo': 'fundamentación'
}

# Cálculo Integral

calculo_integral_ing = {
    'nombre': 'Cálculo Integral',
    'id': 'calculointegral',
    'codigo': 1000005,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '1000004 Cálculo Diferencial',
    'tipo': 'fundamentación'
}

# Cálculo varias variables

calculo_varias_variables = {
    'nombre': 'Cálculo en Varias Variables',
    'id': 'calculoenvariasvariables',
    'codigo': 1000006,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '1000005 Cáluclo Integral',
    'tipo': 'fundamentación'
}

# Álgebra Lineal

algebra_lineal = {
    'nombre': 'Álgebra Lineal',
    'id': 'algebralineal',
    'codigo': 1000003,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '1000004 Cálculo Diferencial',
    'tipo': 'fundamentación'
}

## Probabilidad y Estadística

## Física

fundamentos_mecanica = {
    'nombre': 'Fundamentos de Mecánica',
    'id': 'fundamentosdemecanica',
    'codigo': 1000019,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '1000004 Cálculo Diferencial',
    'tipo': 'fundamentación'
}

fundamentos_electricidad_magnetismo = {
    'nombre': 'Fundamentos de Electricidad y Magnetismo',
    'id': 'fundamentosdeelectricidadymagnetismo',
    'codigo': 1000017,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '1000005 Cálculo Integral',
    'tipo': 'fundamentación'
}

## Ciencias de la Computación

# Mates Discretas 1

mates_discretas_1 = {
    'nombre': 'Matemáticas Discretas',
    'id': 'matematicasdiscretas',
    'codigo': 2025963,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '1000003 Álgebra Lineal',
    'tipo': 'fundamentación'
}

# Mates Discretas 2

# Métodos Numéricos

# Algoritmos

# Introducción a la Teoría de Computación

## Ciencias Económicas y Administrativas

# Ingeniería Económica

# Gerencia y Gestión de Proyectos



### Formación Profesional

## Métodos y Tecnologías de Software

# Programación

programacion_computadores = {
    'nombre': 'Programación de Computadores',
    'id': 'programaciondecomputadores',
    'codigo': 2015734,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 0,
    'tipo': 'disciplinar'
}

# POO

poo = {
    'nombre': 'Programación Orientada a Objetos',
    'id': 'programacionorientadaobjetos',
    'codigo': 2016375,
    'creditos': 3,
    'obligatoria': 1,
    'prerrequisito': '2015734 Programación de Computadores',
    'tipo': 'disciplinar'
}

# Estructuras de Datos

# Lenguajes

# Ingeniería de Software 1

# Ingeniería de Software 2

# Arquitectura de Software

## Infraestructura Computacional, Comunicaciones e Información

# Elementos de Computadores

elementos_de_computadores = {
    'nombre': 'Elementos de Computadores',
    'id': 'elementosdecomputadores',
    'codigo': 2016698,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '2025975 Introducción a la Ingeniería de Sistemas y Computación',
    'tipo': 'disciplinar'
}

# Arquitectura de Computadores

# Computación distribuida y Paralela

# Sistemas Operativos

# Redes de Computadores

# Información y Comunicaciones

# Criptografía y Seguridad de la Información

# Bases de Datos

bases_de_datos = {
    'nombre': 'Bases de Datos',
    'id': 'basesdedatos',
    'codigo': 2016353,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '2016375 Programación Orientada a Objetos',
    'tipo': 'disciplinar'
}

# Sistemas de Información

# Arquitectura de Infraestructura

## Comunicación Aplicada



## Sistemas Inteligentes



## Modelos, Sistemas, Optimización y Simulación



# Modelos y Simulación


# Optimización

# Modelos Estocásticos y Simulación en Computación

# Pensamiento Sistémico

pensamiento_sistemico = {
    'nombre': 'Pensamiento Sistémico',
    'id': 'pensamientosistemico',
    'codigo': 2016703,
    'creditos': 3,
    'obligatoria': 1,
    'prerrequisito': 0,
    'tipo': 'disciplinar'
}

## Contexto Profesional y Proyectos de Ingeniería

# Introducción a la Ingeniería de Sistemas y Computación

introduccion_ing_sistemas = {
    'nombre': 'Introducción a la Ingeniería de Sistemas y Computación',
    'id': 'introduccioningenieriasistemas',
    'codigo': 2025975,
    'creditos': 3,
    'obligatoria': 1,
    'prerrequisito': 0,
    'tipo': 'disciplinar'
}

# Taller Interdisciplinario de Creación y Gestión

## Trabajo de Grado

