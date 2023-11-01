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



cc = [fundamentos_de_matematicas, calculo_diferencial, introduccion_ciencias_computacion, algebra_lineal,calculo_integral,sistemas_numericos,programacion_orientada,intro_conjuntos,calculo_vectorial,probabilidad,estructura_datos,introduccion_analisis_real,ecuaciones_diferenciales,algoritmos,algebra_abstracta,intro_teoria_computacion,elementos_computador,sistemas_operativos,analisis_numerico_1]

with open('pensum_cc.pkl', 'wb') as archivo:
    pickle.dump(cc, archivo)

