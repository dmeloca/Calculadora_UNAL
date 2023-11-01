import pickle

fundamentos_de_matematicas = {
    'nombre': 'Fundamentos de matemáticas',
    'id': 'fundamentosdematematicas',
    'código': 2015168,
    'creditos': 4,
    'obligatoria': 1,
    'tipo': 'fundamentación'
    }
calculo_diferencial = {
    'nombre': 'Cálculo diferencial en una variable',
    'id': 'calculodiferencial',
    'código': 2016377,
    'creditos': 4,
    'obligatoria': 1,
    'tipo': 'fundamentación'
    }
introduccion_ciencias_computacion = {
    'nombre': 'Introducción ciencias computación',
    'id': 'introduccioncienciascomputacion',
    'código': 2026573,
    'creditos': 3,
    'obligatoria': 1,
    'tipo': 'disciplinar'
    }
algebra_lineal = {
    'nombre': 'Algebra lineal básica',
    'id': 'algebralineal',
    'código': 2015555,
    'creditos': 4,
    'obligatoria': 1,
    'tipo': 'fundamentación'
    }
calculo_integral = {
    'nombre': 'Cálculo integral en una variable',
    'id':'calculointegral',
    'código': 2015556,
    'creditos': 4,
    'obligatoria': 1,
    'tipo': 'fundamentación'
    }
sistemas_numericos = {
    'nombre': 'Sistemas numéricos',
    'id':'sistemasnumericos',
    'código': 2015181,
    'creditos': 4,
    'obligatoria': 1,
    'tipo': 'fundamentación'
}

programacion_orientada = {
    'nombre': 'programación orientada a objetos',
    'id': 'programacion',
    'código': 2016375,
    'creditos': 3,
    'obligatoria': 1,
    'tipo': 'fundamentación'
    }
intro_conjuntos = {
    'nombre': 'Introducción teoría de conjuntos',
    'id': 'introduccionteoriadeconjuntos',
    'código': 2025819,
    'creditos': 4,
    'obligatoria': 1,
    'tipo': 'fundamentación'
    }
calculo_vectorial = {
    'nombre': 'Cálculo vectorial',
    'id': 'calculovectorial',
    'código': 2015162,
    'creditos': 4,
    'obligatoria': 1,
    'tipo': 'fundamentación'
    }
probabilidad = {
    'nombre': 'probabilidad',
    'id': 'probabilidad',
    'código':   2015178,
    'creditos': 4,
    'obligatoria': 1,
    'tipo': 'fundamentación'
    }
estructura_datos = {
    'nombre': 'Estructura de datos',
    'id': 'estructura de datos',
    'código': 2016699,
    'creditos': 3,
    'obligatoria': 1,
    'tipo': 'fundamentación'
    }
introduccion_analisis_real = {
    'nombre': 'introducción al análisis real',
    'id': 'introduccionalanalisisreal',
    'código': 2015155,
    'creditos': 4,
    'obligatoria': 1,
    'tipo': 'fundamentación'
}
ecuaciones_diferenciales = {
    'nombre': 'ecuaciones diferenciales',
    'id': 'ecuacionesdiferenciales',
    'código' : 2016342,
    'creditos': 4,
    'obligatoria': 1,
    'tipo':'fundamentación'
}
algoritmos = {
    'nombre': 'algoritmos',
    'id': 'algoritmos',
    'código': 2016696,
    'creditos': 3,
    'obligatoria': 1,
    'tipo':'Disciplinar'
}
algebra_abstracta = {
    'nombre': 'Algebra abstracta y computacional',
    'id': 'algebraabstractaycomputacional',
    'código': 2026555,
    'creditos': 4,
    'obligatoria': 1,
    'tipo':'Disciplinar'
}
intro_teoria_computacion = {
    'nombre': 'Introducción a la teoría de la computación',
    'id': 'introduccionalateoriadelacomputacion',
    'código': 2015174,
    'creditos': 4,
    'obligatoria': 1,
    'tipo':'Disciplinar'
}
elementos_computador = {
    'nombre': 'Elementos de computador',
    'id': 'elementosdecomputador',
    'código': 2016698,
    'creditos': 3,
    'obligatoria': 1,
    'tipo':'Disciplinar'
}
sistemas_operativos = {
    'nombre': 'Sistemas operativos',
    'id': 'sistemasoperativos',
    'código': 2016707,
    'creditos': 3,
    'obligatoria': 1,
    'tipo':'Disciplinar'
}
analisis_numerico_1 = {
    'nombre': 'Análisis numérico I',
    'id': 'analisisnumericouno',
    'código': 2019072,
    'creditos': 4,
    'obligatoria': 1,
    'tipo':'Disciplinar'
}
# materias no obligatorias
analisis_de_bases_de_datos = {
    'nombre': 'Análisis de bases de datos',
    'id': 'analisisdebasesdedatos',
    'codigo': 2027641,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

introduccion_a_la_biologia_computacional = {
    'nombre': 'Introducción a la biología computacional',
    'id': 'introduccionalabiologiacomputacional',
    'codigo': 2025196,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

introduccion_a_la_inteligencia_artificial = {
    'nombre': 'Introducción a la inteligencia artificial',
    'id': 'introduccionalainteligenciaartificial',
    'codigo': 2027631,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

analisis_forense_digital = {
    'nombre': 'Análisis forense digital',
    'id': 'analisisforensedigital',
    'codigo': 2027309,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

fisica_computacional = {
    'nombre': 'Física computacional',
    'id': 'fisicacomputacional',
    'codigo': 2027632,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

introduccion_al_aprendizaje_de_maquina = {
    'nombre': 'Introducción al aprendizaje de máquina',
    'id': 'introduccionalaprendizajedemaquina',
    'codigo': 2027643,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

finanzas_computacionales = {
    'nombre': 'Finanzas computacionales',
    'id': 'finanzascomputacionales',
    'codigo': 2016740,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

ecuaciones_en_diferencias_finitas_y_sistemas_dinamicos = {
    'nombre': 'Ecuaciones en diferencias finitas y sistemas dinámicos',
    'id': 'ecuacionesendiferenciasfinitasysistemasdinamicos',
    'codigo': 2026519,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

introduccion_a_la_optimizacion = {
    'nombre': 'Introducción a la optimización',
    'id': 'introduccionalaoptimizacion',
    'codigo': 2015173,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

optimizacion = {
    'nombre': 'Optimización',
    'id': 'optimizacion',
    'codigo': 2025971,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

introduccion_al_modelamiento_matematico = {
    'nombre': 'Introducción al modelamiento matemático',
    'id': 'introduccionalmodelamientomatematico',
    'codigo': 2027630,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

introduccion_a_la_criptografia_y_a_la_teoria_de_informacion = {
    'nombre': 'Introducción a la criptografía y a la teoría de información',
    'id': 'introduccionalacriptografiayalateoríadeinformación',
'codigo': 2027311,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

teoria_de_la_codificacion = {
    'nombre': 'Teoría de la codificación',
    'id': 'teoriadelacodificacion',
    'codigo': 2027313,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

criptografia = {
    'nombre': 'Criptografía',
    'id': 'criptografia',
    'codigo': 2027310,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

arquitectura_de_computadores = {
    'nombre': 'Arquitectura de computadores',
    'id': 'arquitecturadecomputadores',
    'codigo': 2016697,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

compiladores = {
    'nombre': 'Compiladores',
    'id': 'compiladores',
    'codigo': 2027642,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

teoria_de_lenguajes_formales = {
    'nombre': 'Teoría de lenguajes formales',
    'id': 'teoriadelenguajesformales',
    'codigo': 2027628,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

logica_computacional = {
    'nombre': 'Lógica computacional',
    'id': 'logicacomputacional',
    'codigo': 2027629,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

teoria_de_la_recursion = {
    'nombre': 'Teoría de la recursión',
    'id': 'teoriadelarecursion',
    'codigo': 2019267,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

informatica_aplicada = {
    'nombre': 'Informática aplicada',
    'id': 'informaticaaplicada',
    'codigo': 2021834,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

mundos_virtuales = {
    'nombre': 'Mundos virtuales',
    'id': 'mundosvirtuales',
    'codigo': 2024065,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

fundamentos_de_fisica = {
    'nombre': 'Fundamentos de física',
    'id': 'fundamentosdefisica',
    'codigo': 2022689,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'fundamentación'
}

fundamentos_de_fisica_teorica = {
    'nombre': 'Fundamentos de física teórica',
    'id': 'fundamentosdefisicateorica',
    'codigo': 2016651,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'fundamentación'
}

mecanica_newtoniana = {
    'nombre': 'Mecánica newtoniana',
    'id': 'mecanicanewtoniana',
    'codigo': 2015176,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'fundamentación'
}

probabilidad_y_estadistica_fundamental = {
    'nombre': 'Probabilidad y estadística fundamental',
    'id': 'probabilidadyestadisticafundamental',
    'codigo': 1000013,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'fundamentación'
}

biologia_molecular_y_celular = {
    'nombre': 'Biología molecular y celular',
    'id': 'biologiamolecularycelular',
    'codigo': 1000010,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'fundamentación'
}

quimica_basica = {
    'nombre': 'Química básica',
    'id': 'quimicabasica',
    'codigo': 1000041,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'fundamentación'
}

grupos_y_anillos = {
    'nombre': 'Grupos y anillos',
    'id': 'gruposyanillos',
    'codigo': 2015152,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

introduccion_al_analisis_combinatorio = {
    'nombre': 'Introducción al análisis combinatorio',
    'id': 'introduccionalanalisiscombinatorio',
    'codigo': 2027312,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

teoria_de_grafos = {
    'nombre': 'Teoría de grafos',
    'id': 'teoriadegrafos',
    'codigo': 2015184,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo':'disciplinar'
}

cc = [fundamentos_de_matematicas, calculo_diferencial, introduccion_ciencias_computacion, algebra_lineal,calculo_integral,sistemas_numericos,programacion_orientada,intro_conjuntos,calculo_vectorial,probabilidad,estructura_datos,introduccion_analisis_real,ecuaciones_diferenciales,algoritmos,algebra_abstracta,intro_teoria_computacion,elementos_computador,sistemas_operativos,analisis_numerico_1,analisis_de_bases_de_datos, introduccion_a_la_biologia_computacional, introduccion_a_la_inteligencia_artificial, analisis_forense_digital, fisica_computacional, introduccion_al_aprendizaje_de_maquina, finanzas_computacionales, ecuaciones_en_diferencias_finitas_y_sistemas_dinamicos, introduccion_a_la_optimizacion, optimizacion, introduccion_al_modelamiento_matematico, introduccion_a_la_criptografia_y_a_la_teoria_de_informacion, teoria_de_la_codificacion, criptografia, arquitectura_de_computadores, compiladores, teoria_de_lenguajes_formales, logica_computacional, teoria_de_la_recursion, informatica_aplicada, mundos_virtuales, fundamentos_de_fisica, fundamentos_de_fisica_teorica, mecanica_newtoniana, probabilidad_y_estadistica_fundamental, biologia_molecular_y_celular, quimica_basica, grupos_y_anillos, introduccion_al_analisis_combinatorio, teoria_de_grafos]

with open('pensum_cc.pkl', 'wb') as archivo:
    pickle.dump(cc, archivo)
