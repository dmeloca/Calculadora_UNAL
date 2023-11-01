import unicodedata
import pickle

def strip_accents(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')
    s = s.replace(' ', '').lower()
    return s

def append_topic(usuario, id, carrera):
    for topic in carrera:
        if id == topic.get('id'):
            usuario.append(topic)
            return 0

def inscribir_materias(usuario, carrera):
    while True:
        answer = input(f"[*] Ingrese la materia que vió: \n")
        answer1 = strip_accents(answer)
        intento = append_topic(usuario, answer1, carrera)
        if intento != 0:
            a = input(f"[?] Desea ingresar {answer} (que no está en el listado) (S/N)")
            if a == "S" or a == "s":
                new_m = crear_materias(answer)
                new_m['id'] = f"{new_m['id']}_{intento}"
                usuario.append(new_m)
            else:
                print("[!] Materia No válida")
        if usuario:
            print("[-] Materias inscritas:")
            for i, materia in enumerate(usuario, start=1):
                print(f" |- {i}.", materia['nombre'])
        another = input("[!] Desea ingresar más materias (S/N)")
        if another.lower() == "n":
            break  # Salir del bucle si no desea ingresar más materias

    # Después de que el usuario termine de inscribir materias, ingresamos las notas.
    grade(usuario)
    
def crear_materias(nombre):
    id = strip_accents(nombre)
    codigo = int(input("[?] Ingrese el código de la materia (si no lo conoce ingrese un cero) "))
    credits = int(input("[?] Ingrese el número de créditos de la materia "))
    obligatoria = 0
    tipo = input("[?] Ingrese el tipo de la materia ")
    tempdict = {
        'nombre': nombre,
        'id': id,
        'código': codigo,
        'creditos': credits,
        'obligatoria': obligatoria,
        'tipo': tipo
    }
    return tempdict

def grade(usuario):
    creditxgrade = 0
    credits = 0
    # print('usuario', usuario)
    usuariosolomaterias = usuario.copy()
    for materia in usuariosolomaterias:
        perdida(materia)
        if materia['perdida'] == 1:
            intentos = int(
                input(f"[?] Cuantas veces vio {materia['nombre']}: "))
            for a in range(intentos):
                nota = float(input(
                    f"[?] Ingrese la nota que obtuvo en {materia['nombre']} (intento {a+1}): "))
                copia = materia.copy()
                intento = str(a)
                copia['id'] += intento
                copia['nota'] = nota
                copia["ponderación"] = nota * copia['creditos']
                usuario.append(copia)
                creditxgrade += copia['ponderación']
                credits += copia['creditos']
            usuario.remove(materia)
            # print('usuario', usuario)
        else:
            nota = float(
                input(f"[?] Ingrese la nota que obtuvo en {materia['nombre']}: "))
            materia['nota'] = nota
            materia["ponderación"] = nota * materia['creditos']
            creditxgrade += materia['ponderación']
            credits += materia['creditos']
    return creditxgrade, credits

def perdida(materia):
    answer = input(f"[?] Perdió la materia {materia['nombre']}? (S/N)")
    if answer.lower() == "s":
        materia['perdida'] = 1
    elif answer.lower() == "n":
        materia['perdida'] = 0
    else:
        print("[!] Ingrese un valor correcto")
def porcentajeAvance(carrera_usuario, carrera):
    creditos_aprobados = 0
    creditostotales = 0
    if carrera == 'cc':
        creditostotales = 139
    elif carrera == 'est':
        creditostotales = 132
    elif carrera == 'math':
        creditostotales = 131
    elif carrera == 'sis':
        creditostotales = 178
    for materia in carrera_usuario:
        if 'nota' in materia and materia['nota'] >= 3:
            creditos_aprobados += materia['creditos']
    if creditos_aprobados > 0:
        print(
            f"[!] Su porcentaje de avance es de: {(creditos_aprobados/creditostotales)*100}%")
    else:
        print("[!] No tiene creditos para calcular el porcentaje de avance.")

def papa(carrera_usuario):
    notas = 0
    creditos = 0
    for materia in carrera_usuario:
        if 'nota' in materia:
            notas += materia['nota'] * materia['creditos']
            creditos += materia['creditos']
    if creditos > 0:
        print(f"[!] Su PAPA es de: {notas/creditos}")
    else:
        print("[!] No se han ingresado notas para calcular el PAPA.")

def seleccionar_plan():
    carrera = input("[?] Ingrese qué carrera está cursando: Ciencias de la computación (cc), Estadística (est), Matemáticas (math), Ing. Sistemas (sis): ")
    if carrera.lower() == 'cc':
        with open('pensum_cc.pkl', 'rb') as archivo:
            cc = pickle.load(archivo)
        return cc
    elif carrera.lower() == 'est':
        with open('pensum_est.pkl', 'rb') as archivo:
            est = pickle.load(archivo)
        return est
    elif carrera.lower() == 'math':
        with open('pensum_math.pkl', 'rb') as archivo:
            math = pickle.load(archivo)
        return math
    elif carrera.lower() == 'sis':
        return 0
    else:
        print("[!] Carrera no encontrada")

def main():
    usuario = []
    carrera = seleccionar_plan()
    inscribir_materias(usuario, carrera)
    porcentajeAvance(usuario, 'cc')
    papa(usuario)

if __name__ == "__main__":
    main()
