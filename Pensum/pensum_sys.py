import pickle

#####  Ingeniería de Sistemas  #####

# Fundamentación

# Matemáticas

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

calculo_diferencial = {
    'nombre': 'Cálculo diferencial en una variable',
    'id': 'calculodiferencial',
    'código': 2016377,
    'creditos': 4,
    'obligatoria': 1,
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

calculo_integral = {
    'nombre': 'Cálculo integral en una variable',
    'id': 'calculointegral',
    'código': 2015556,
    'creditos': 4,
    'obligatoria': 1,
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

calculo_vectorial = {
    'nombre': 'Cálculo vectorial',
    'id': 'calculovectorial',
    'código': 2015162,
    'creditos': 4,
    'obligatoria': 1,
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

algebra_lineal_basica = {
    'nombre': 'Algebra lineal básica',
    'id': 'algebralineal',
    'código': 2015555,
    'creditos': 4,
    'obligatoria': 1,
    'tipo': 'fundamentación'
}

# Probabilidad y Estadística

probabilidad_estadistica_fundamental = {
    'nombre': 'Probabliidad y Estadística Fundamental',
    'id': 'probabilidadyestadisticafundamental',
    'codigo': 1000013,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '1000005 Cálculo Integral',
    'tipo': 'fundamentación'
}

probabilidad_fundamental = {
    'nombre': 'Probabilidad Fundamental',
    'id': 'probabilidadfundamental',
    'codigo': 0,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'fundamentación'
}

probabilidad = {
    'nombre': 'probabilidad',
    'id': 'probabilidad',
    'código': 2015178,
    'creditos': 4,
    'obligatoria': 1,
    'tipo': 'fundamentación'
}

# Física

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

# Ciencias de la Computación

# Mates Discretas 1

mates_discretas_1 = {
    'nombre': 'Matemáticas Discretas',
    'id': 'matematicasdiscretas1',
    'codigo': 2025963,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '1000003 Álgebra Lineal',
    'tipo': 'fundamentación'
}

sistemas_numericos = {
    'nombre': 'Sistemas numéricos',
    'id': 'sistemasnumericos',
    'código': 2015181,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '1000003 Álgebra Lineal',
    'tipo': 'fundamentación'
}

# Mates Discretas 2

mates_discretas_2 = {
    'nombre': 'Matemáticas Discretas 2',
    'id': 'matematicasdiscretas2',
    'codigo': 2025964,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '2025963 Matemáticas Discretas 1',
    'tipo': 'fundamentación'
}

intro_conjuntos = {
    'nombre': 'Introducción teoría de conjuntos',
    'id': 'introduccionteoriadeconjuntos',
    'código': 2025819,
    'creditos': 4,
    'obligatoria': 0,
    'tipo': 'fundamentación'
}

# Métodos Numéricos

metodos_numericos = {
    'nombre': 'Métodos Numéricos',
    'id': '',
    'codigo': 2015970,
    'creditos': 0,
    'obligatoria': 0,
    'prerrequisito': '1000006 Cálculo en Varias Variables',
    'tipo': 'fundamentación'
}

analisis_numerico_1 = {
    'nombre': 'Análisis numérico I',
    'id': 'analisisnumericouno',
    'código': 2019072,
    'creditos': 4,
    'obligatoria': 0,
    'tipo': 'Disciplinar'
}

# Algoritmos

algoritmos = {
    'nombre': 'Algoritmos',
    'id': 'algoritmos',
    'codigo': 2016696,
    'creditos': 3,
    'obligatoria': 1,
    'prerrequisito': '1000013 Probabilidad y Estadística Fundamental',
    'tipo': 'fundamentación'
}

# Introducción a la Teoría de Computación

introduccion_teoria_computacion = {
    'nombre': 'Introducción a la Teoría de Computación',
    'id': 'introduccionalateoriadecomputacion',
    'codigo': 2015174,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': '2025963 Matemáticas Discretas 1',
    'tipo': 'fundamentación'
}

# Ciencias Económicas y Administrativas

# Ingeniería Económica

ingenieria_economica = {
    'nombre': 'Ingeniería Económica',
    'id': 'ingenieriaeconomica',
    'codigo': 2015703,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'Cálculo Integral',
    'tipo': 'fundamentación'
}

ingenieria_economica_analisis_riesgo = {
    'nombre': 'Ingeniería Económica y Análisis de Riesgos',
    'id': 'ingenieriaeconomicayanalisisderiesgos',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'Cáluclo Integrla',
    'tipo': 'fundamentación'
}

modelos_economicos_computacionales = {
    'nombre': 'Modelos Económicos Computacionales',
    'id': 'modeloseconomicoscomputacionales',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'Cálculo Integral',
    'tipo': 'fundamentación'
}


# Gerencia y Gestión de Proyectos

gerencia_gestion_proyectos = {
    'nombre': 'Gerencia y Gestión de Proyectos',
    'id': 'gerenciaygestiondeproyectos',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'Cálculo Integral',
    'tipo': 'fundamentación'
}


# Formación Profesional

# Métodos y Tecnologías de Software

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

introduccion_ciencias_computacion = {
    'nombre': 'Introducción a las Ciencias de la Computación y Programación',
    'id': 'introduccioncienciascomputacion',
    'código': 2026573,
    'creditos': 3,
    'obligatoria': 0,
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

estructuras_de_datos = {
    'nombre': 'Estructuras de Datos',
    'id': 'estructurasdedatos',
    'codigo': 2016699,
    'creditos': 3,
    'obligatoria': 1,
    'prerrequisito': 'Programación Orientada a Objetos',
    'tipo': 'disciplinar'
}

# Lenguajes

lenguajes_de_programacion = {
    'nombre': 'Lenguajes de Programación',
    'id': 'lenguajesdeprogramacion',
    'codigo': 2025966,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
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
    'nombre': 'Teoría de Lenguajes Formales',
    'id': 'teoriadelenguajesformales',
    'codigo': 2027628,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

# Ingeniería de Software 1

ingenieria_de_software_1 = {
    'nombre': 'Ingeniería de Software 1',
    'id': 'ingenieriadesoftware1',
    'codigo': 2016701,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'Estructuras de Datos',
    'tipo': 'disciplinar'
}

# Ingeniería de Software 2

ingenieria_de_software_2 = {
    'nombre': 'Ingeniería de Software 2',
    'id': 'ingenieriadesoftware2',
    'codigo': 2016702,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'Ingeniería de Software',
    'tipo': 'disciplinar'
}

# Arquitectura de Software

arquitectura_de_software = {
    'nombre': 'Arquitectura de Software',
    'id': 'arquitecturadesoftware',
    'codigo': 2016716,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'Ingeniería de Software 2',
    'tipo': 'disciplinar'
}

# Infraestructura Computacional, Comunicaciones e Información

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

electronica_digital = {
    'nombre': 'Electrónica Digital',
    'id': 'electronicadigital',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'Introducción a la Ingeniería de Sistemas y Computación',
    'tipo': 'disciplinar'
}

# Arquitectura de Computadores

arquitectura_de_computadores = {
    'nombre': 'Arquitectura de Computadores',
    'id': 'arquitecturadecomputadores',
    'codigo': 2016697,
    'creditos': 3,
    'obligatoria': 1,
    'prerrequisito': 'Elementos de Computadores',
    'tipo': 'disciplinar'
}

# Computación distribuida y Paralela

computacion_distribuida_paralela = {
    'nombre': 'Computación Distribuida y Paralela',
    'id': 'computaciondistribuidayparalela',
    'codigo': 2025968,
    'creditos': 3,
    'obligatoria': 1,
    'prerrequisito': 'Algoritmos',
    'tipo': 'disciplinar'
}

# Sistemas Operativos

sistemas_operativos = {
    'nombre': 'Sistemas Operativos',
    'id': 'sistemasoperativos',
    'codigo': 2016707,
    'creditos': 3,
    'obligatoria': 1,
    'prerrequisito': 'Arquitectura de Computadores',
    'tipo': 'disciplinar'
}

# Redes de Computadores

redes_de_computadores = {
    'nombre': 'Redes de Computadores',
    'id': 'redesdecomputadores',
    'codigo': 2025967,
    'creditos': 3,
    'obligatoria': 1,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

# Información y Comunicaciones

teoria_informacion_sistemas_comunicaciones = {
    'nombre': 'Teoría de la Información y Sistemas de Comunicaciones',
    'id': 'teoriadelainformacionysistemasdecomunicaciones',
    'codigo': 2025994,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'Redes de Computadores',
    'tipo': 'disciplinar'
}

comunicaciones = {
    'nombre': 'Comunicaciones',
    'id': 'comunicaciones',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'Redes de Computadores',
    'tipo': 'disciplinar'
}

# Criptografía y Seguridad de la Información

introduccion_criptografia_seguridad_informacion = {
    'nombre': 'Introducción a la Criptografía y la Seguridad en la Informacion',
    'id': 'introduccionalacriptografiaylaseguridadenlainformacion',
    'codigo': 2025972,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'Algoritmos',
    'tipo': 'disciplinar'
}

informacion_codificacion_criptografia = {
    'nombre': 'Información, Codificación y Criptografía',
    'id': 'informacioncodificacionycriptografia',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'Algoritmos',
    'tipo': 'disciplinar'
}

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

analisis_bases_de_datos = {
    'nombre': 'Análisis de Bases de Datos',
    'id': 'analisisdebasesdedatos',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'Programación Orientada a Objetos',
    'tipo': 'disciplinar'
}

# Sistemas de Información

sistemas_de_informacion = {
    'nombre': 'Sistemas de Información',
    'id': 'sistemasdeinformacion',
    'codigo': 2025982,
    'creditos': 2,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

sistemas_de_informacion_gerencial = {
    'nombre': 'Sistemas de Información Gerencial',
    'id': 'sistemasdeinformaciongerencial',
    'codigo': 0,
    'creditos': 4,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

# Arquitectura de Infraestructura

arquitectura_infraestructura_gobierno_tics = {
    'nombre': 'Arquitectura de Infraestructura y Gobierno de TICs',
    'id': 'arquitecturadeinfraestructuraygobiernodetics',
    'codigo': 2025983,
    'creditos': 3,
    'obligatoria': 1,
    'prerrequisito': 'Sistemas de Informacion', 'Ingeniería de Software 2'
    'tipo': 'disciplinar'
}

# Comunicación Aplicada

computacion_visual = {
    'nombre': 'Computación Visual',
    'id': 'computacionvisual',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

tecnologia_visual = {
    'nombre': 'Tecnología Visual',
    'id': 'tecnologiavisual',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

analisis_forense_digital = {
    'nombre': 'Análisis forense digital',
    'id': 'analisisforensedigital',
    'codigo': 2027309,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

# Sistemas Inteligentes

introduccion_sistemas_inteligentes = {
    'nombre': 'Introducción a los Sistemas Inteligentes',
    'id': 'introduccionalossistemasinteligentes',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

inteligencia_artificial = {
    'nombre': 'Inteligencia Artificial',
    'id': 'inteligenciaartificial',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
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

introduccion_al_aprendizaje_de_maquina = {
    'nombre': 'Introducción al aprendizaje de máquina',
    'id': 'introduccionalaprendizajedemaquina',
    'codigo': 2027643,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': 'No requiere',
    'tipo': 'disciplinar'
}

inteligencia_artificial_minirobots = {
    'nombre': 'Inteligencia Artificial y Minirobots',
    'id': 'inteligenciaartificialyminirobots',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

tecnicas_de_inteligencia_artificial = {
    'nombre': 'Técnicas de Inteligencia Artificial',
    'id': 'tecnicasdeinteligenciaartificial',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

# Modelos, Sistemas, Optimización y Simulación

# Modelos y Simulación

modelos_simulacion = {
    'nombre': 'Modelos y Simulación',
    'id': 'modelosysimulacion',
    'codigo': 2025970,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
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

# Optimización

optimizacion = {
    'nombre': 'Optimización',
    'id': 'optimizacion',
    'codigo': 2025971,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
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

# Modelos Estocásticos y Simulación en Computación

modelos_estocasticos_simulacion_computacion = {
    'nombre': 'Modelos Estocásticos y Simulación en Computación y Comunicaciones',
    'id': 'modelosestocasticosysimulacionencomputacionycomunicaciones',
    'codigo': 2025969,
    'creditos': 3,
    'obligatoria': 1,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

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

# Contexto Profesional y Proyectos de Ingeniería

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

taller_proyectos_interdisciplinarios = {
    'nombre': 'Taller de Proyectos Interdisciplinarios',
    'id': 'tallerdeproyectosinterdisciplinarios',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

taller_invencion_creatividad = {
    'nombre': 'Taller de Invención y Creatividad',
    'id': 'tallerdeinvencionycreatividad',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

creacion_gestion_empresas = {
    'nombre': 'Creación y Gestión de Empresas',
    'id': 'creacionygestiondeempresas',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

fundamentos_administracion = {
    'nombre': 'Fundamentos de Administración',
    'id': 'fundamentosdeadministracion',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

gestion_tecnologica = {
    'nombre': 'Gestión Tecnológica',
    'id': 'gestiontecnologica',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

gestion_ciencia_tecnologia_innovacion = {
    'nombre': 'Gestión de la Ciencia, la Tecnología y la Innovación',
    'id': 'gestiondelaciencialatecnologiaylainnovacion',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

finanzas = {
    'nombre': 'Finanzas',
    'id': 'finanzas',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

finanzas_avanzadas = {
    'nombre': 'Finanzas Avanzadas',
    'id': 'finanzasavanzadas',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

# Trabajo de Grado

trabajo_investigativo = {
    'nombre': 'Trabajo Investigativo',
    'id': 'trabajoinvestigativo',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

practica_extension = {
    'nombre': 'Práctica de Extensión',
    'id': 'practicadeextension',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

asiganturas_posgrado = {
    'nombre': 'Asignaturas de Posgrado',
    'id': 'asignaturasdeposgrado',
    'codigo': 0,
    'creditos': 3,
    'obligatoria': 0,
    'prerrequisito': '',
    'tipo': 'disciplinar'
}

sis = [calculo_diferencial_ing, calculo_diferencial, calculo_integral, calculo_integral_ing, calculo_varias_variables, calculo_vectorial, algebra_lineal, algebra_lineal_basica, probabilidad_estadistica_fundamental, probabilidad_fundamental, probabilidad, fundamentos_mecanica, fundamentos_electricidad_magnetismo, mates_discretas_1, sistemas_numericos, mates_discretas_2, intro_conjuntos, metodos_numericos, analisis_numerico_1, algoritmos, introduccion_teoria_computacion, ingenieria_economica, ingenieria_economica_analisis_riesgo, modelos_economicos_computacionales, gerencia_gestion_proyectos, programacion_computadores, introduccion_ciencias_computacion, poo, estructuras_de_datos, lenguajes_de_programacion, compiladores, teoria_de_lenguajes_formales, ingenieria_de_software_1, ingenieria_de_software_2, arquitectura_de_software, elementos_de_computadores, electronica_digital, arquitectura_de_computadores, computacion_distribuida_paralela, sistemas_operativos, redes_de_computadores, teoria_informacion_sistemas_comunicaciones,
       comunicaciones, introduccion_criptografia_seguridad_informacion, informacion_codificacion_criptografia, bases_de_datos, analisis_bases_de_datos, sistemas_de_informacion, sistemas_de_informacion_gerencial, arquitectura_infraestructura_gobierno_tics, computacion_visual, tecnologia_visual, analisis_forense_digital, introduccion_sistemas_inteligentes, inteligencia_artificial, introduccion_a_la_inteligencia_artificial, introduccion_al_aprendizaje_de_maquina, inteligencia_artificial_minirobots, tecnicas_de_inteligencia_artificial, modelos_simulacion, modelos_matematicos_1, optimizacion, introduccion_a_la_optimizacion, modelos_estocasticos_simulacion_computacion, pensamiento_sistemico, introduccion_ing_sistemas, taller_proyectos_interdisciplinarios, taller_invencion_creatividad, creacion_gestion_empresas, fundamentos_administracion, gestion_tecnologica, gestion_ciencia_tecnologia_innovacion, finanzas, finanzas_avanzadas, trabajo_investigativo, practica_extension, asiganturas_posgrado]

with open('pensum_sys.pkl', 'wb') as archivo:
    pickle.dump(sis, archivo)
