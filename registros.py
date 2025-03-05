import json
from proyecto import leer_json
    
# A. Obtener todos los datos de población para India desde 2000 hasta 2023
def poblacion_india(datos):
    resultado = []
    pais=str(input("Ingrese el nombre del país: "))
    for i in datos:
        if i["pais"] == pais and 2000 <= i["ano"] <= 2023:
            resultado.append(i)
    return resultado
# B. Listar los países con su información de código ISO y código ISO3.
def lista_paises(paises):
    for pais in paises:
        print(f"Nombre: {pais['nombre']}, Código ISO: {pais['codigo_iso']}, Código ISO3: {pais['codigo_iso3']}")
# C. Datos de población para el indicador 'SP.POP.TOTL'.
def datos_poblacion_total(datos):
    resultado = []
    for d in datos:
        if d["indicador_id"] == "SP.POP.TOTL":
            resultado.append(d)
    return resultado
# D. Obtener los datos de población de los últimos 10 años para todos los países.
def poblacion_ultimos_10(datos):
    anio_actual = 2025
    resultado = []
    for d in datos:
        if (anio_actual - 10) <= d["ano"] <= anio_actual:
            resultado.append(d)
    return resultado
# E. Total de población para India en el año 2022.
def poblacion_por_pais_anio(datos, codigo_iso3, anio=2022):
    for d in datos:
        if d["codigo_iso3"] == codigo_iso3 and d["ano"] == anio:
            print(f"Población de {codigo_iso3} en el año {anio}: {d['valor']:,.0f} habitantes")
            return d["valor"] 
    print(f"No se encontraron datos de población para {codigo_iso3} en el año {anio}.")
    return None
# F. Población total registrada antes del año 2000.
def poblacion_antes_2000(datos):
    total = sum(d["valor"] for d in datos if d["ano"] < 2000)
    if total:
        print(f"Población total registrada antes del año 2000: {total} habitantes")
    else:
        print("No hay datos de población registrados antes del año 2000.")
    return total
# G. Población total registrada después del año 2010.
def poblacion_despues_2010(datos):
    total = sum(d["valor"] for d in datos if d["ano"] > 2010) 
    if total:
        print(f"Población total registrada después del año 2010: {total:,.0f} habitantes")
    else:
        print("No hay datos de población registrados después del año 2010.")
    return total
# H. Porcentaje de crecimiento de la población de India entre 2010 y 2020.
def crecimiento_poblacional(datos, codigo_iso3, inicio=2010, fin=2020):
    poblacion_inicio = None
    poblacion_fin = None
    for d in datos:
        if d["codigo_iso3"] == codigo_iso3:
            if d["ano"] == inicio:
                poblacion_inicio = d["valor"]
            elif d["ano"] == fin:
                poblacion_fin = d["valor"]
    if poblacion_inicio is not None and poblacion_fin is not None:
        crecimiento = ((poblacion_fin - poblacion_inicio) / poblacion_inicio) * 100
        print(f"Crecimiento poblacional de {codigo_iso3} entre {inicio} y {fin}: {crecimiento:.2f}%")
        return crecimiento
    else:
        print(f"No se encontraron datos suficientes para {codigo_iso3} en {inicio} y {fin}.")
        return None
# I. Población de India en el año 2023 (si está disponible).
def poblacion_2023(datos, codigo_iso3):
    for d in datos:
        if d["codigo_iso3"] == codigo_iso3 and d["ano"] == 2023:
            print(f"Población de {codigo_iso3} en 2023: {d['valor']} habitantes")
            return d["valor"]
    print(f"No hay datos de población para {codigo_iso3} en 2023.")
    return None
# J. Obtener el año con la población más baja para India.
def anio_menor_poblacion(datos, codigo_iso3):
    poblaciones = [(dato["ano"], dato["valor"]) for dato in datos if dato["codigo_iso3"] == codigo_iso3]
    if poblaciones:
        anio_min, poblacion_min = min(poblaciones, key=lambda x: x[1])
        print(f"Año con menor población en {codigo_iso3}: {anio_min} ({poblacion_min} habitantes)")
        return anio_min, poblacion_min
    print(f"No hay datos de población registrados para {codigo_iso3}.")
    return None, None
# K. Número de registros de población por año.
def registros_por_anio(datos, codigo_iso3):
    conteo = {}
    for d in datos:
        if d["codigo_iso3"] == codigo_iso3:
            conteo[d["ano"]] = conteo.get(d["ano"], 0) + 1
    print(f"Registros de población por año en {codigo_iso3}: {conteo}")
    return conteo
# L. Países con un crecimiento poblacional mayor al 2% anual en los últimos 5 años.
def paises_crecimiento_alto(datos):
    anio_actual = 2023
    paises_crecimiento = []
    paises = {dato["codigo_iso3"] for dato in datos}
    for pais in paises:
        poblacion_reciente = None
        poblacion_pasada = None
        for dato in datos:
            if dato["codigo_iso3"] == pais:
                if dato["ano"] == anio_actual:
                    poblacion_reciente = dato["valor"]
                elif dato["ano"] == anio_actual - 5:
                    poblacion_pasada = dato["valor"]
        if poblacion_reciente and poblacion_pasada:
            crecimiento_anual = ((poblacion_reciente - poblacion_pasada) / poblacion_pasada) * 100 / 5
            if crecimiento_anual > 2:
                paises_crecimiento.append((pais, crecimiento_anual))
    if paises_crecimiento:
        print("Países con crecimiento mayor al 2% anual en los últimos 5 años:")
        for pais, crecimiento in paises_crecimiento:
            print(f"  - {pais}: {crecimiento:.2f}% anual")
    else:
        print("No hay países con un crecimiento mayor al 2% anual en los últimos 5 años.")
    return paises_crecimiento
# M. Listar los años en los que la población de India superó los 1,000 millones.
def anios_poblacion_mayor_mil_millones(datos, codigo_iso3):
    anios = [d["ano"] for d in datos if d["codigo_iso3"] == codigo_iso3 and d["valor"] > 1_000_000_000]
    if anios:
        print(f"Años en los que la población de {codigo_iso3} superó los 1,000 millones: {anios}")
    else:
        print(f"{codigo_iso3} nunca ha superado los 1,000 millones de habitantes.")
    return anios
# N. Obtener la población total registrada para todos los países en el año 2000.
def poblacion_total_anio(datos, anio=2000):
    """Calcula la población total de todos los países en un año específico."""
    total = sum(d["valor"] for d in datos if d["ano"] == anio)
    if total:
        print(f"Población total mundial en el año {anio}: {total} habitantes")
    else:
        print(f"No hay datos de población para el año {anio}.")
    return total
#M. Obtener la población menos registrada para India en los últimos 20 años.
def poblacion_mas_baja_ultimos_20_anios(datos, codigo_iso3):
    anio_actual = 2023
    poblaciones = [(d["ano"], d["valor"]) for d in datos if d["codigo_iso3"] == codigo_iso3 and d["ano"] >= anio_actual - 20]
    if poblaciones:
        anio_min, poblacion_min = min(poblaciones, key=lambda x: x[1])
        print(f"Población más baja de {codigo_iso3} en los últimos 20 años: {poblacion_min} habitantes en {anio_min}")
        return anio_min, poblacion_min
    print(f"No hay suficientes datos de población para {codigo_iso3} en los últimos 20 años.")
    return None, None
#O. Promedio de población registrada por año para India desde 1980 hasta 2020.
def promedio_poblacion(datos, codigo_iso3, inicio=1980, fin=2020):
    poblaciones = [d["valor"] for d in datos if d["codigo_iso3"] == codigo_iso3 and inicio <= d["ano"] <= fin]
    if poblaciones:
        promedio = sum(poblaciones) / len(poblaciones)
        print(f"Promedio de población en {codigo_iso3} entre {inicio} y {fin}: {promedio} habitantes")
        return promedio
    print(f"No hay datos suficientes de población para {codigo_iso3} entre {inicio} y {fin}.")
    return None
#P. Cantidad de años con datos de población disponibles para India.
def cantidad_anios_con_datos(datos, codigo_iso3):
    anios = {d["ano"] for d in datos if d["codigo_iso3"] == codigo_iso3}
    print(f"{codigo_iso3} tiene datos de población en {len(anios)} años diferentes.")
    return len(anios)
#Q. Listar los países con datos de población disponibles para cada año entre 2000 y 2023.
def paises_con_datos_por_anio(datos, inicio=2000, fin=2023):
    datos_por_anio = {anio: set() for anio in range(inicio, fin + 1)}
    for d in datos:
        if inicio <= d["ano"] <= fin:
            datos_por_anio[d["ano"]].add(d["codigo_iso3"])
    for anio, paises in datos_por_anio.items():
        print(f" Año {anio}: {len(paises)} países con datos")
    return datos_por_anio
#R. Población total de India en 2019.
def poblacion_2019(datos, codigo_iso3):
    for d in datos:
        if d["codigo_iso3"] == codigo_iso3 and d["ano"] == 2019:
            print(f"Población de {codigo_iso3} en 2019: {d['valor']:,.0f} habitantes")
            return d["valor"]
    print(f"No hay datos de población para {codigo_iso3} en 2019.")
    return None
#S. Años en los que la población de India creció más de 1 millón en comparación con el año anterior.
def anios_crecimiento_millon(datos, codigo_iso3):
    crecimiento = []
    datos_filtrados = sorted([dato for dato in datos if dato["codigo_iso3"] == codigo_iso3], key=lambda x: x["ano"])
    for i in range(1, len(datos_filtrados)):
        diferencia = datos_filtrados[i]["valor"] - datos_filtrados[i - 1]["valor"]
        if diferencia > 1_000_000:
            crecimiento.append(datos_filtrados[i]["ano"])
    print(f"{codigo_iso3} superó 1 millón de crecimiento en los años: {crecimiento}")
    return crecimiento
#T. Población registrada de India en cada década desde 1960.
def poblacion_por_decada(datos, codigo_iso3):
    decadas = {decada: None for decada in range(1960, 2030, 10)}
    for d in datos:
        if d["codigo_iso3"] == codigo_iso3:
            decada = (d["ano"] // 10) * 10
            decadas[decada] = d["valor"]
    for decada, poblacion in decadas.items():
        if poblacion:
            print(f"{codigo_iso3} en la década de {decada}: {poblacion} habitantes")
    return decadas
#U. Población total registrada para todos los países en 2023.
def poblacion_total_2023(datos):
    total = sum(dato["valor"] for dato in datos if dato["ano"] == 2023)
    print(f"Población total mundial en 2023: {total} habitantes")
    return total
#V. Años en los que no hay datos de población disponibles para India.
def anios_sin_datos(datos, codigo_iso3, inicio=1960, fin=2023):
    datos_disponibles = {dato["ano"] for dato in datos if dato["codigo_iso3"] == codigo_iso3}
    anios_faltantes = [anio for anio in range(inicio, fin + 1) if anio not in datos_disponibles]
    print(f"Años sin datos de población en {codigo_iso3}: {anios_faltantes}")
    return anios_faltantes
#X. Año con la población más alta registrada para India.
def anio_mayor_poblacion(datos, codigo_iso3):
    poblaciones = [(dato["ano"], dato["valor"]) for dato in datos if dato["codigo_iso3"] == codigo_iso3]
    if poblaciones:
        anio_max, poblacion_max = max(poblaciones, key=lambda x: x[1])
        print(f"Año con mayor población en {codigo_iso3}: {anio_max} ({poblacion_max:,.0f} habitantes)")
        return anio_max, poblacion_max
    print(f"No hay datos de población registrados para {codigo_iso3}.")
    return None, None
#Y. Años con datos de población disponibles para más de 50 países.
def anios_mas_de_50_paises(datos):
    conteo_anios = {}
    for dato in datos:
        conteo_anios[dato["ano"]] = conteo_anios.get(dato["ano"], set())
        conteo_anios[dato["ano"]].add(dato["codigo_iso3"])
    anios_50_paises = [anio for anio, paises in conteo_anios.items() if len(paises) > 50]
    print(f"Años con datos de más de 50 países: {anios_50_paises}")
    return anios_50_paises

if __name__ == "__main__":
    ruta_datos = "poblacion.json"
    ruta_paises = "paises.json"
    ruta_indicadores="indicadores.json"
    datos = leer_json(ruta_datos)
    paises = leer_json(ruta_paises)
    indicadores = leer_json(ruta_indicadores) 

    while True:
        opc = int(input(
            "\nSeleccione una opción:\n"
            "1. Obtener datos de población (2000-2023)\n"
            "2. Listar países\n"
            "3. Obtener datos de población para 'SP.POP.TOTL'\n"
            "4. Obtener datos de población de los últimos 10 años\n"
            "5. Total de población en 2022 para un país\n"
            "6. Población total registrada antes del 2000\n"
            "7. Población total registrada después del 2010\n"
            "8. Porcentaje de crecimiento de la población de India entre 2010 y 2020\n"
            "9. Población de India en el año 2023 (si está disponible)\n"
            "10. Obtener el año con la población más baja para India.\n"
            "11. Número de registros de población por año.\n"
            "12. Países con un crecimiento poblacional mayor al 2% anual en los últimos 5 años.\n"
            "13. Listar los años en los que la población de India superó los 1,000 millones\n"
            "14. Obtener la población total registrada para todos los países en el año 2000\n"
            "15. Obtener la población menos registrada para India en los últimos 20 años\n"
            "16. Promedio de población registrada por año para India desde 1980 hasta 2020\n"
            "17. Cantidad de años con datos de población disponibles para India.\n"
            "18. Listar los países con datos de población disponibles para cada año entre 2000 y 2023.\n"
            "19. Población total de India en 2019\n"
            "20. Años en los que la población de India creció más de 1 millón en comparación con el año anterior.\n"
            "21. Población registrada de India en cada década desde 1960.\n"
            "22. Población total registrada para todos los países en 2023.\n"
            "23. Años en los que no hay datos de población disponibles para India.\n"
            "24. Año con la población más alta registrada para India.\n"
            "25. Años con datos de población disponibles para más de 50 países.\n"
            "26. Salir\n"
            "Ingrese una opción: "
        ))

    
        if opc == 1:
            datos_poblacion = poblacion_india(datos)
            print(json.dumps(datos_poblacion, indent=4, ensure_ascii=False))
        elif opc == 2:
            lista_paises(paises)
        elif opc == 3:
            datos_indicador = datos_poblacion_total(datos)
            print(json.dumps(datos_indicador, indent=4, ensure_ascii=False))
        elif opc == 4:
            ultimos_10_anios = poblacion_ultimos_10(datos)
            print(json.dumps(ultimos_10_anios, indent=4, ensure_ascii=False))
        elif opc == 5:
            codigo_iso3 = input("Ingrese el código ISO3 del país: ").upper()
            poblacion_2022 = poblacion_por_pais_anio(datos, codigo_iso3, anio=2022)
        elif opc == 6:
            poblacion_antigua = poblacion_antes_2000(datos)
        elif opc == 7:
            poblacion_reciente = poblacion_despues_2010(datos)
        elif opc==8:
            codigo_iso3 = input("Ingrese el código ISO3 del país: ").upper()
            crecimiento_poblacional(datos, codigo_iso3)
        elif opc==9:
            codigo_iso3 = input("Ingrese el código ISO3 del país: ").upper()
            poblacion_2023(datos, codigo_iso3)
        elif opc==10:
            codigo_iso3 = input("Ingrese el código ISO3 del país: ").upper()
            anio_menor_poblacion(datos, codigo_iso3)
        elif opc==11:
            codigo_iso3 = input("Ingrese el código ISO3 del país: ").upper()
            registros_por_anio(datos, codigo_iso3)
        elif opc==12:
            paises_crecimiento_alto(datos)
        elif opc==13:
            codigo_iso3 = input("Ingrese el código ISO3 del país: ").upper()
            anios_poblacion_mayor_mil_millones(datos, codigo_iso3)
        elif opc==14:
            poblacion_total_anio(datos, anio=2000)
        elif opc==15:
            codigo_iso3 = input("Ingrese el código ISO3 del país: ").upper()
            poblacion_mas_baja_ultimos_20_anios(datos, codigo_iso3)
        elif opc==16:
            codigo_iso3 = input("Ingrese el código ISO3 del país: ").upper()
            promedio_poblacion(datos, codigo_iso3)
        elif opc==17:
            codigo_iso3 = input("Ingrese el código ISO3 del país: ").upper()
            cantidad_anios_con_datos(datos, codigo_iso3)
        elif opc==18:
            paises_con_datos_por_anio(datos)
        elif opc==19:
            codigo_iso3 = input("Ingrese el código ISO3 del país: ").upper()
            poblacion_2019(datos, codigo_iso3)
        elif opc==20:
            codigo_iso3 = input("Ingrese el código ISO3 del país: ").upper()
            anios_crecimiento_millon(datos, codigo_iso3)
        elif opc==21:
            codigo_iso3 = input("Ingrese el código ISO3 del país: ").upper()
            poblacion_por_decada(datos, codigo_iso3)
        elif opc==22:
            poblacion_total_2023(datos)
        elif opc==23:
            codigo_iso3 = input("Ingrese el código ISO3 del país: ").upper()
            anios_sin_datos(datos, codigo_iso3)
        elif opc==24:
            codigo_iso3 = input("Ingrese el código ISO3 del país: ").upper()
            anio_mayor_poblacion(datos, codigo_iso3)
        elif opc==25:
            anios_mas_de_50_paises(datos)
        elif opc == 26:
            print("Saliendo...")
            break
        else:
            print("Ingrese una opción válida.")


