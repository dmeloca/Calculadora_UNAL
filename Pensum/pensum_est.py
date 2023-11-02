import pickle
Estadistica_descriptiva_y_explorativa = {
    'nombre': 'estadistica descriptiva y exploratoria',
    'id': 'estadisticadescriptivayexploratoria',
    'código': 2016366,
    'créditos': 4,
    'obligatoria': 1,
    'prerrequisito': 'N/A',
    'tipo': 'fundamentación'
    }
algebra_matricial ={
    'nombre': 'algebra matricial',
    'id': 'algebramatricial',
    'codigo': 2016378,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': algebra_lineal,
    'tipo': 'fundamentacion'
}
probabilidad ={
    'nombre': 'probabilidad',
    'id': 'probabilidad',
    'codigo': 2015178,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': calculo_integral,
    'tipo': 'fundamentacion'
}
calculo_vectorial = {
    'nombre' : 'Calculo vectorial',
    'id': 'calculovectorial',
    'codigo': 2015162,
    'creditos': 4,
    'obligatoria':1,
    'prerrequisito': calculo_integral,
    'tipo': 'fundamentacion'
}
inferencia_estadistica ={
    'nombre': 'inferencia_estadistica',
    'id': 'inferenciaestadistica',
    'codigo': 2016379,
    'creditos': 4,
    'obligatoria':1,
    'prerrequisito': probabilidad,
    'tipo':'fundamentacion'
}
biologia_general = {
    'nombre': 'Biología General',
    'id': 'biologiageneral',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

biologia_molecular_y_celular = {
    'nombre': 'Biología molecular y celular',
    'id': 'biologiamolecularycelular',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

fundamentos_de_ecologia = {
    'nombre': 'Fundamentos de ecología',
    'id': 'fundamentosdeecologia',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}
probabilidad_y_estadistica_fundamental = {
    'nombre': 'Probabilidad y estadística fundamental',
    'id': 'probabilidadyestadisticafundamental',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

bioestadistica_fundamental = {
    'nombre': 'Bioestadística fundamental',
    'id': 'bioestadisticafundamental',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

estadistica_social_fundamental = {
    'nombre': 'Estadística social fundamental',
    'id': 'estadisticasocialfundamental',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}
geometria_elemental = {
    'nombre': 'Geometría elemental',
    'id': 'geometriaelemental',
    'codigo': 0,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

conjuntos_y_combinatoria = {
    'nombre': 'Conjuntos y combinatoria',
    'id': 'conjuntosycombinatoria',
    'codigo': 0,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}
geometria_vectorial_y_analitica = {
    'nombre': 'Geometría vectorial y analítica',
    'id': 'geometriavectorialyanalitica',
    'codigo': 0,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

matematicas_discretas = {
    'nombre': 'Matemáticas discretas',
    'id': 'matematicasdiscretas',
    'codigo': 0,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}
principios_de_quimica = {
    'nombre': 'Principios de química',
    'id': 'principiosdequimica',
    'codigo': 0,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

quimica_organica_I = {
    'nombre': 'Química orgánica I',
    'id': 'quimicaorganicaI',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}
quimica_basica = {
    'nombre': 'Química básica',
    'id': 'quimicabasica',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

introduccion_a_la_ciencia_de_materiales = {
    'nombre': 'Introducción a la ciencia de materiales',
    'id': 'introduccionalacienciademateriales',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}
mecanica_newtoniana = {
    'nombre': 'Mecánica Newtoniana',
    'id': 'mecanicanewtoniana',
    'codigo': 0,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

fundamentos_de_fisica_moderna = {
    'nombre': 'Fundamentos de física moderna',
    'id': 'fundamentosdefisicamoderna',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

introduccion_al_analisis_real = {
    'nombre': 'Introducción al análisis real',
    'id': 'introduccionalanalisisreal',
    'codigo': 0,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'complementación matemática'
}

grupos_y_anillos = {
    'nombre': 'Grupos y anillos',
    'id': 'gruposyanillos',
    'codigo': 0,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'complementación matemática'
}
calculoDeEcuacionesDiferencialesOrdinarias = {
    'nombre': 'Cálculo de ecuaciones diferenciales ordinarias',
    'id': 'calculoDeEcuacionesDiferencialesOrdinarias',
    'codigo': 0,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'complementación matemática'
}

modelosMatematicos = {
    'nombre': 'Modelos matemáticos',
    'id': 'modelosMatematicos',
    'codigo': 0,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'complementación matemática'
}

analisisEstocastico = {
    'nombre': 'Análisis estocástico',
    'id': 'analisisEstocastico',
    'codigo': 0,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'complementación matemática'
}
programacionYMetodosNumericos = {
    'nombre': 'Programación y métodos numéricos',
    'id': 'programacionYMetodosNumericos',
    'codigo': 0,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'programación'
}

programacionDeComputadores = {
    'nombre': 'Programación de computadores',
    'id': 'programacionDeComputadores',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'programación'
}

programacionEnLenguajesEstadisticos = {
    'nombre': 'Programación en lenguajes estadísticos',
    'id': 'programacionEnLenguajesEstadisticos',
    'codigo': 0,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'programación'
}

est = ['estadistica descriptiva y exploratoria', 'algebra matricial', 'probabilidad', 'Calculo vectorial', 'inferencia_estadistica', 'Biología General', 'Biología molecular y celular', 'Fundamentos de ecología', 'Probabilidad y estadística fundamental', 'Bioestadística fundamental', 'Estadística social fundamental', 'Geometría elemental', 'Conjuntos y combinatoria', 'Geometría vectorial y analítica', 'Matemáticas discretas', 'Principios de química', 'Química orgánica I', 'Química básica', 'Introducción a la ciencia de materiales', 'Mecánica Newtoniana', 'Fundamentos de física moderna', 'Introducción al análisis real', 'Grupos y anillos', 'Cálculo de ecuaciones diferenciales ordinarias', 'Modelos matemáticos', 'Análisis estocástico', 'Programación y métodos numéricos', 'Programación de computadores', 'Programación en lenguajes estadísticos']

with open('pensum_est.pkl', 'wb') as archivo:
    pickle.dump(est, archivo)
    
