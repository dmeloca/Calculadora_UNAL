import pickle
Estadistica_descriptiva_y_explorativa = {
    'nombre': 'estadistica descriptiva y exploratoria',
    'id': 'estadisticadescriptivayexploratoria',
    'código': 2016366,
    'creditos': 4,
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
    'prerrequisito': 'algebra_lineal',
    'tipo': 'fundamentacion'
}
probabilidad ={
    'nombre': 'probabilidad',
    'id': 'probabilidad',
    'codigo': 2015178,
    'creditos': 4,
    'obligatoria': 1,
    'prerrequisito': 'calculo_integral',
    'tipo': 'fundamentacion'
}
calculo_vectorial = {
    'nombre' : 'Calculo vectorial',
    'id': 'calculovectorial',
    'codigo': 2015162,
    'creditos': 4,
    'obligatoria':1,
    'prerrequisito': 'calculo_integral',
    'tipo': 'fundamentacion'
}
inferencia_estadistica ={
    'nombre': 'inferencia_estadistica',
    'id': 'inferenciaestadistica',
    'codigo': 2016379,
    'creditos': 4,
    'obligatoria':1,
    'prerrequisito': 'probabilidad',
    'tipo':'fundamentacion'
}

est = [Estadistica_descriptiva_y_explorativa, algebra_matricial, probabilidad, calculo_vectorial, inferencia_estadistica]
with open('pensum_est.pkl', 'wb') as archivo:
    pickle.dump(est, archivo)
    
