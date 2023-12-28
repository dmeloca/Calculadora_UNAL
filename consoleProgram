import unicodedata
import pickle
from math import ceil
carreraNombre = ''
materiasAprobadas = []
segundaCarreraNombre = ''
creditosmaterias = 0
creditostotalescc = 139
creditostotalesest = 141
creditostotalesmath = 140
creditostotalessis = 165


def strip_accents(s):
    s = ''.join(c for c in unicodedata.normalize(
        'NFD', s) if unicodedata.category(c) != 'Mn')
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
            a = input(
                f"[?] Desea ingresar {answer} (que no está en el listado) (S/N)")
            if a == "S" or a == "s":
                new_m = crear_materias(answer)
                new_m['id'] = f"{new_m['id']}"
                usuario.append(new_m)
                print('new_m', new_m)
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
    codigo = int(
        input("[?] Ingrese el código de la materia (si no lo conoce ingrese un cero) "))
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
    global materiasAprobadas
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
                if nota >= 3:
                    copia['perdida'] = 0
                    copia['id'] = materia['id']
                    copia["ponderación"] = nota * copia['creditos']
                    usuario.append(copia)
                    materiasAprobadas.append({'nombre': materia['nombre'], 'id': materia['id'], 'creditos': materia['creditos']})
                    creditxgrade += copia['ponderación']
                    credits += copia['creditos']
                else:
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
            materiasAprobadas.append(
                {'nombre': materia['nombre'], 'id': materia['id'], 'creditos': materia['creditos']})
            materia['nota'] = nota
            materia["ponderación"] = nota * materia['creditos']
            creditxgrade += materia['ponderación']
            credits += materia['creditos']
    for aprobado in materiasAprobadas:
        print('[!] MateriasAprobadas: ', aprobado['nombre'])
    return creditxgrade, credits


def perdida(materia):
    answer = input(f"[?] Perdió la materia {materia['nombre']}? (S/N)")
    if answer.lower() == "s":
        materia['perdida'] = 1
    elif answer.lower() == "n":
        materia['perdida'] = 0
    else:
        print("[!] Ingrese un valor correcto")


def creditosfnl(usuario, carrera):
    bolsadecreditos = 0
    bolsadecreditos1 = 0
    if carrera == 'cc':
        bolsadecreditos = creditostotalescc
    elif carrera == 'est':
        bolsadecreditos = creditostotalesest
    elif carrera == 'math':
        bolsadecreditos = creditostotalesmath
    elif carrera == 'sis':
        bolsadecreditos = creditostotalessis
    for materia in usuario:
        if materia['perdida'] == 0:
            bolsadecreditos1 += materia['creditos']*2
        if bolsadecreditos1 > bolsadecreditos/2:
            bolsadecreditos1 = bolsadecreditos/2
        else:
            bolsadecreditos1 -= materia['creditos']
    bolsadecreditos1 = ceil(bolsadecreditos1)
    print(f'[$] Usted tiene {bolsadecreditos1} creditos adicionales')
    return bolsadecreditos1


def porcentajeAvance(materiasAprobadas, carrera):
    creditos_aprobados = 0
    creditostotales = 0
    if carrera == 'cc':
        creditostotales = 139
    elif carrera == 'est':
        creditostotales = 141
    elif carrera == 'math':
        creditostotales = 140
    elif carrera == 'sis':
        creditostotales = 165
    for materia in materiasAprobadas:
        creditos_aprobados += materia['creditos']
    if creditos_aprobados > 0:
        print('[$] Creditos aprobados', creditos_aprobados)
        print(
            f"[!] Su porcentaje de avance es de: {(creditos_aprobados/creditostotales)*100}%")
        return (creditos_aprobados/creditostotales)*100
    else:
        print("[!] No tiene creditos para calcular el porcentaje de avance.")


def seleccionar_plan_segunda_carrera(nombrePrimeraCarrera):
    carreraEscogida = 0
    materiasSegundaCarrera = []
    carrera = input(
        "[?] Ingrese para que carrera quiere hacer la doble : Ciencias de la computación (cc), Estadística (est), Matemáticas (math), Ing. Sistemas (sis): ")
    global segundaCarreraNombre
    segundaCarreraNombre = carrera
    if carrera.lower() == nombrePrimeraCarrera.lower():
        print("[!] No puede hacer doble titulación con la misma carrera")
        exit(0)
    if carrera.lower() == 'cc':
        with open('pensum_cc.pkl', 'rb') as archivo:
            carreraEscogida = pickle.load(archivo)
    elif carrera.lower() == 'est':
        with open('pensum_est.pkl', 'rb') as archivo:
            carreraEscogida = pickle.load(archivo)
    elif carrera.lower() == 'math':
        with open('pensum_math.pkl', 'rb') as archivo:
            carreraEscogida = pickle.load(archivo)
    elif carrera.lower() == 'sis':
        return 0
    else:
        print("[!] Carrera no encontrada")
        return 0
    for materia in carreraEscogida:
        materiasSegundaCarrera.append(
            {'id': materia['id'], 'creditos': materia['creditos']})
    # print('materiasSegundaCarrera', materiasSegundaCarrera)
    return materiasSegundaCarrera


def materiasHomologables(materiasAprobadas, materiasSegundaCarrera):
    materiasHomologables = []
    for materia in materiasAprobadas:
        for materia2 in materiasSegundaCarrera:
            if materia['id'] == materia2['id']:
                materiasHomologables.append(materia)
    for homologable in materiasHomologables:
        print('[!] Materias Homologables: ', homologable['nombre'])
    return materiasHomologables


def doble_titulacion(papa, porcentajeAvance, creditosNecesarios, creditosAdicionales):
    if porcentajeAvance >= 40:
        if papa >= 4.3:
            print('[+] FELICIDADES')
            print("[$] Usted elegible hacer doble titulación ")
        elif creditosAdicionales-creditosNecesarios >= 0:
            print('[+] FELICIDADES')
            print("[$] Usted elegible hacer doble titulación ")
        else:
            print('[!] Lo sentimos, no es elegible para hacer doble titulación')

    else:
        print('[!] Lo sentimos, no es elegible para hacer doble titulación')


def papa(carrera_usuario):
    notas = 0
    creditos = 0
    for materia in carrera_usuario:
        if 'nota' in materia:
            notas += materia['nota'] * materia['creditos']
            creditos += materia['creditos']
    if creditos > 0:
        print(f"[!] Su PAPA es de: {notas/creditos}")
        return notas/creditos
    else:
        print("[!] No se han ingresado notas para calcular el PAPA.")


def seleccionar_plan():
    carrera = input(
        "[?] Ingrese qué carrera está cursando: Ciencias de la computación (cc), Estadística (est), Matemáticas (math), Ing. Sistemas (sis): ")
    global carreraNombre
    carreraNombre = carrera
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
        exit(0)


def creditosNecesarios(nombreSegundaCarrera, materiasH):
    creditos = 0
    if nombreSegundaCarrera == 'cc':
        creditos = 139
    elif nombreSegundaCarrera == 'est':
        creditos = 141
    elif nombreSegundaCarrera == 'math':
        creditos = 140
    elif nombreSegundaCarrera == 'sis':
        creditos = 165
    for materia in materiasH:
        creditos -= materia['creditos']
    print('[*] Creditos necesarios ', creditos)
    return creditos


def main():
    usuario = []
    # esto va despues pero es para probar
    carrera = seleccionar_plan()
    inscribir_materias(usuario, carrera)
    porcentajeAvancev = porcentajeAvance(usuario, carreraNombre)
    papav = papa(usuario)
    materiasSegundaCarrera = seleccionar_plan_segunda_carrera(carreraNombre)
    materiasH = materiasHomologables(materiasAprobadas, materiasSegundaCarrera)
    creditosN = creditosNecesarios(segundaCarreraNombre, materiasH)
    creditosfnlv = creditosfnl(usuario, carreraNombre)
    doble_titulacion(papav, porcentajeAvancev, creditosN, creditosfnlv)


if __name__ == "__main__":
    main()
