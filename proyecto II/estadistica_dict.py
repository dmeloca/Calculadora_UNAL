Estadistica_descriptiva_y_explorativa = {
    'nombre': 'estadistica descriptiva y exploratoria',
    'id': 'estadisticadescriptivayexploratoria',
    'código': 2016366,
    'créditos': 4,
    'obligatoria': 1,
    'prerrequisito': 'N/A',
    'tipo': 'fundamentación'
    }
Optativa_comunicacion = {
    'nombre': ' ',
    'id': ' ',
    'codigo':' ',
    'creditos': ' ',
    'obligatoria': ' ',
    'prerrequisito': ' ',
    'tipo': ' ',
}
primer_estadistica = {
    'nombre': 'Primer semestre Estadistica',
    'children': [fundamentos_de_matematicas, calculo_diferencial, estadistica_descriptiva_y_exploratoria,optativa_comunicacion]
}
fundamentacion_en_ciencas = {
    'nombre:': ' ',
    'id': ' ',
    'codigo':' ',
    'creditos': ' ',
    'obligatoria': ' ',
    'prerrequisito': ' ',
    'tipo': ' ',
}
segundo_cc = {
    'nombre': 'Segundo Semestre ciencias de la computación',
    'children': [algebra_lineal, calculo_integral, sistemas_numericos, fundamentacion_en_ciencas]
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
    'nombre' : 'calculo_vectorial',
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