import pickle
##MATH
fundamentos_de_matematicas = {
    'nombre': 'Fundamentos de matemáticas',
    'id': 'fundamentosdematematicas',
    'codigo': 2015168,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '1000001 Matemáticas básicas',
    'tipo': 'fundamentación'
}

calculo_diferencial_en_una_variable = {
    'nombre': 'Cálculo diferencial en una variable',
    'id': 'calculodiferencial',
    'codigo': 2016377,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '1000001 Matemáticas básicas',
    'tipo': 'fundamentación'
}

introduccion_la_teoria_de_conjuntos = {
    'nombre': 'Introducción a la Teoría de Conjuntos',
    'id': 'introduccionteoriadeconjuntos',
    'codigo': 2025819,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2015168 Fundamentos de matemáticas',
    'tipo': 'fundamentación'
}

algebra_lineal_basica = {
    'nombre': 'Álgebra lineal básica',
    'id': 'algebralineal',
    'codigo': 2015555,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '1000001 Matemáticas básicas',
    'tipo': 'fundamentación'
}

calculo_integral_en_una_variable = {
    'nombre': 'Cálculo integral en una variable',
    'id': 'calculointegral',
    'codigo': 2015556,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2016377 Cálculo diferencial en una variable',
    'tipo': 'fundamentación'
}

sistemas_numericos = {
    'nombre': 'Sistemas numéricos',
    'id': 'sistemasnumericos',
    'codigo': 2015181,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2015168 Fundamentos de matemáticas',
    'tipo': 'fundamentación'
}

calculo_de_ecuaciones_diferenciales_ordinarias = {
    'nombre': 'Cálculo de ecuaciones diferenciales ordinarias',
    'id': 'ecuacionesdiferenciales',
    'codigo': 2016342,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2015556 Cálculo integral en una variable',
    'tipo': 'fundamentación'
}

calculo_vectorial = {
    'nombre': 'Cálculo vectorial',
    'id': 'calculovectorial',
    'codigo': 2015162,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2015556 Cálculo integral en una variable',
    'tipo': 'fundamentación'
}

mecanica_newtoniana = {
    'nombre': 'Mecánica Newtoniana',
    'id': 'mecanicanewtoniana',
    'codigo': 2015176,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2016377 Cálculo diferencial en una variable',
    'tipo': 'fundamentación'
}

fundamentos_de_electricidad_y_magnetismo = {
    'nombre': 'Fundamentos de electricidad y magnetismo',
    'id': 'fundamentosdeelectricidadymagnetismo',
    'codigo': 1000017,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2016377 Cálculo diferencial en una variable',
    'tipo': 'fundamentación'
}

fundamentos_de_oscilaciones_ondas_y_optica = {
    'nombre': 'Fundamentos de oscilaciones, ondas y óptica',
    'id': 'fundamentosdeoscilacionesondasyoptica',
    'codigo': 2015170,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2016377 Cálculo diferencial en una variable',
    'tipo': 'fundamentación'
}

fundamentos_de_mecanica_de_fluidos = {
    'nombre': 'Fundamentos de mecánica de fluidos',
    'id': 'fundamentosdemecanicadefluidos',
    'codigo': 2015169,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '2016377 Cálculo diferencial en una variable',
    'tipo': 'fundamentación'
}

funda_fisica_moderna = {
    'nombre': 'Fundamentos de física moderna',
    'id': 'fundamentosdefisicamoderna',
    'codigo': 2015167,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '2016377 Cálculo diferencial en una variable',
    'tipo': 'fundamentación'
}

mecanica_analitica_I = {
    'nombre': 'Mecánica analitica I',
    'id': 'mecanicaanaliticaI',
    'codigo': 2016679,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '2015176 Mecánica Newtoniana',
    'tipo': 'fundamentación'
}

mecanica_analitica_II = {
    'nombre': 'Mecánica analitica II',
    'id': 'mecanicaanaliticaII',
    'codigo': 2016677,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '2016679 Mecánica analitica I',
    'tipo': 'fundamentación'
}

introduccion_a_la_optimizacion = {
    'nombre': 'Introducción a la optimización',
    'id': 'introduccionalaoptimizacion',
    'codigo': 2015173,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2015555 Álgebra lineal básica',
    'tipo': 'disciplinar'
}

modelos_matematicos_1 = {
    'nombre': 'Modelos matemáticos 1',
    'id': 'modelosmatematicos1',
    'codigo': 2019082,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2016342 Cálculo de ecuaciones diferenciales ordinarias',
    'tipo': 'disciplinar'
}

introduccion_a_la_teoria_de_la_computacion = {
    'nombre': 'Introducción a la teoría de la computación',
    'id': 'introduccionalateoriadelacomputacion',
    'codigo': 2015174,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2025819 Introducción a la Teoría de Conjuntos',
    'tipo': 'disciplinar'
}

teoria_de_grafos = {
    'nombre': 'Teoría de grafos',
    'id': 'teoriadegrafos',
    'codigo': 2015184,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2025819 Introducción a la Teoría de Conjuntos',
    'tipo': 'disciplinar'
}
procesos_estocasticos = {
    'nombre': 'Procesos estocásticos',
    'id': 'procesosestocasticos',
    'codigo': 2015179,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2015155 Introducción al análisis real',
    'tipo': 'disciplinar'
}

analisis_estocastico = {
    'nombre': 'Análisis estocástico',
    'id': 'analisisestocastico',
    'codigo': 2015161,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2015179 Procesos estocásticos',
    'tipo': 'disciplinar'
}

teoria_de_conjuntos_1 = {
    'nombre': 'Teoría de conjuntos 1',
    'id': 'teoriadeconjuntos1',
    'codigo': 2016834,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2025819 Introducción a la Teoría de Conjuntos',
    'tipo': 'disciplinar'
}

teoria_de_modelos_1 = {
    'nombre': 'Teoría de modelos 1',
    'id': 'teoriademodelos1',
    'codigo': 2019092,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2025819 Introducción a la Teoría de Conjuntos',
    'tipo': 'disciplinar'
}

epistemologia_e_historia_de_la_matematica = {
    'nombre': 'Epistemología e historia de la matemática',
    'id': 'epistemologiaehistoriadelamatematica',
    'codigo': 2025384,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2015152 Grupos y anillos',
    'tipo': 'disciplinar'
}

anillos_y_modulos = {
    'nombre': 'Anillos y módulos',
    'id': 'anillosymodulos',
    'codigo': 2025580,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2015152 Grupos y anillos',
    'tipo': 'disciplinar'
}

teoria_de_numeros = {
    'nombre': 'Teoría de números',
    'id': 'teoriadenumeros',
    'codigo': 2015186,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2015153 Integración y Series',
    'tipo': 'disciplinar'
}

ecuaciones_diferenciales_ordinarias = {
    'nombre': 'Ecuaciones diferenciales ordinarias',
    'id': 'ecuacionesdiferencialesordinarias',
    'codigo': 2019074,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2015153 Integración y Series',
    'tipo': 'disciplinar'
}

ecuaciones_diferenciales_parciales_1 = {
    'nombre': 'Ecuaciones diferenciales parciales 1',
    'id': 'ecuacionesdiferencialesparciales1',
    'codigo': 2019075,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2015151 Análisis vectorial',
    'tipo': 'disciplinar'
}

geometria_diferencial_1 = {
    'nombre': 'Geometría diferencial 1',
    'id': 'geometriadiferencial1',
    'codigo': 2019078,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2015151 Análisis vectorial',
    'tipo': 'disciplinar'
}

introduccion_al_analisis_combinatorio = {
    'nombre': 'Introducción al Análisis Combinatorio',
    'id': 'introduccionalanalisiscombinatorio',
    'codigo': 2027312,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2015181 Sistemas numéricos',
    'tipo': 'disciplinar'
}

analisis_numerico_1 = {
    'nombre': 'Análisis numérico 1',
    'id': 'analisisnumerico1',
    'codigo': 2019072,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2015155 Introducción al análisis real',
    'tipo': 'disciplinar'
}

introduccion_al_analisis_real = {
    'nombre': 'Introducción al análisis real',
    'id': 'introduccionalanalisisreal',
    'codigo': 2015155,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2015162 Cálculo vectorial',
    'tipo': 'análdisciplinar'
}

integracion_y_series = {
    'nombre': 'Integración y series',
    'id': 'integracionyseries',
    'codigo': 2015153,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2015155 Introducción al análisis real',
    'tipo': 'análdisciplinar'
}

analisis_vectorial = {
    'nombre': 'Análisis vectorial',
    'id': 'analisisvectorial',
    'codigo': 2015151,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2015149 Álgebra multilineal y formas canónicas',
    'tipo': 'análdisciplinar'
}

variable_compleja = {
    'nombre': 'Variable compleja',
    'id': 'variablecompleja',
    'codigo': 2015159,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2015155 Introducción al análisis real',
    'tipo': 'análdisciplinar'
}

topologia_general = {
    'nombre': 'Topología General',
    'id': 'topologiageneral',
    'codigo': 2015158,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2015155 Introducción al análisis real',
    'tipo': 'análdisciplinar'
}

grupos_y_anillos = {
    'nombre': 'Grupos y anillos',
    'id': 'gruposyanillos',
    'codigo': 2015152,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2025819 Introducción a la Teoría de Conjuntos',
    'tipo': 'disciplinar'
}

algebra_multilineal_y_formas_canonicas = {
    'nombre': 'Álgebra multilineal y formas canónicas',
    'id': 'algebramultilinealyformascanonicas',
    'codigo': 2015149,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2015152 Grupos y anillos',
    'tipo': 'disciplinar'
}

teoria_de_cuerpos = {
    'nombre': 'Teoría de cuerpos',
    'id': 'teoriadecuerpos',
    'codigo': 2015157,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2015152 Grupos y anillos',
    'tipo': 'disciplinar'
}

logica_matematica = {
    'nombre': 'Lógica matemática',
    'id': 'logicamatematica',
    'codigo': 2015156,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2015152 Grupos y anillos',
    'tipo': 'disciplinar'
}

programacion_y_metodos_numericos = {
    'nombre': 'Programación y métodos numéricos',
    'id': 'programacionymetodosnumericos',
    'codigo': 2015180,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2015555 Álgebra lineal básica',
    'tipo': 'fundamentación'
}

probabilidad = {
    'nombre': 'Probabilidad',
    'id': 'probabilidad',
    'codigo': 2015178,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '201',
    'tipo':'fundamentacion'
}
geometria_elemental = {
    'nombre': 'Geometría elemental',
    'id': 'geometriaelemental',
    'codigo': 2015172,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'fundamentación'
}

geometria_vectorial_y_analitica = {
    'nombre': 'Geometría vectorial y analítica',
    'id': 'geometriavectorialyanalitica',
    'codigo': 1000008,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'fundamentación'
}
math = [fundamentos_de_matematicas, calculo_diferencial_en_una_variable, introduccion_la_teoria_de_conjuntos, algebra_lineal_basica, calculo_integral_en_una_variable, sistemas_numericos, calculo_de_ecuaciones_diferenciales_ordinarias, calculo_vectorial, mecanica_newtoniana, fundamentos_de_electricidad_y_magnetismo, fundamentos_de_oscilaciones_ondas_y_optica, fundamentos_de_mecanica_de_fluidos, funda_fisica_moderna, mecanica_analitica_I, mecanica_analitica_II, introduccion_a_la_optimizacion, modelos_matematicos_1, introduccion_a_la_teoria_de_la_computacion, teoria_de_grafos, procesos_estocasticos, analisis_estocastico, teoria_de_conjuntos_1, teoria_de_modelos_1, epistemologia_e_historia_de_la_matematica, anillos_y_modulos, teoria_de_numeros, ecuaciones_diferenciales_ordinarias, ecuaciones_diferenciales_parciales_1, geometria_diferencial_1, introduccion_al_analisis_combinatorio, analisis_numerico_1, introduccion_al_analisis_real, integracion_y_series, analisis_vectorial, variable_compleja, topologia_general, grupos_y_anillos, algebra_multilineal_y_formas_canonicas, teoria_de_cuerpos, logica_matematica, programacion_y_metodos_numericos, probabilidad, geometria_elemental, geometria_vectorial_y_analitica]


with open('pensum_math.pkl', 'wb') as archivo:
    pickle.dump(math, archivo)
