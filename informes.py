import proyecto 

def informe_poblacion(ruta_datos, ruta_paises):
    datos = proyecto.leer_json(ruta_datos)
    paises = proyecto.leer_json(ruta_paises)
    codigo_iso3 = input("\nIngrese el código ISO3 del país para el informe: ").upper()
    pais_encontrado = next((p for p in paises if p["codigo_iso3"] == codigo_iso3), None)
    if not pais_encontrado:
        print("El país ingresado no se encuentra en el registro")
        return
    try:
        ano_inicio = int(input("Ingrese el año de inicio: "))
        ano_fin = int(input("Ingrese el año de fin: "))
        if ano_inicio > ano_fin:
            print("El año de inicio no puede ser mayor que el año de fin.")
            return
        datos_filtrados = [
            d for d in datos
            if d["codigo_iso3"] == codigo_iso3 and ano_inicio <= d["ano"] <= ano_fin
        ]
        if not datos_filtrados:
            print("No hay datos de población para este país en el período seleccionado.")
            return

        print(f"**** INFORME DE POBLACIÓN PARA {pais_encontrado['nombre']} ({codigo_iso3}) ****")
        print("───────────────────────────────────")
        for d in sorted(datos_filtrados, key=lambda x: x["ano"]):
            print(f"Año: {d['ano']} | Población: {d['valor']} {d['unidad']}")
        print("───────────────────────────────────")
    except ValueError:
        print("Ingrese valores numéricos válidos para los años.")

def informe_crecimiento_poblacional(ruta_datos, ruta_paises):
    datos = proyecto.leer_json(ruta_datos)
    paises = proyecto.leer_json(ruta_paises)

    codigo_iso3 = input("\nIngrese el código ISO3 del país para el informe: ").upper()

    pais_encontrado = None
    for p in paises:
        if p["codigo_iso3"] == codigo_iso3:
            pais_encontrado = p
            break

    if not pais_encontrado:
        print("El país ingresado no se encuentra en el registro.")
        return
    
    datos_pais = []

    for dato in datos:
        if dato["codigo_iso3"] == codigo_iso3:
            datos_pais.append(dato)

    if len(datos_pais) < 2:
        print("No hay suficientes datos para calcular el crecimiento poblacional.")
        return
    
    datos_pais = sorted(datos_pais, key=lambda dato: dato["ano"])

    print(f"**** INFORME DE CRECIMIENTO POBLACIONAL PARA {pais_encontrado['nombre']} ({codigo_iso3}) ****")
    print(f"{'Año':<10}{'Población':<20}{'Crecimiento %':<15}")

    for i in range(1, len(datos_pais)):  
        año_actual = datos_pais[i]["ano"]  
        poblacion_actual = datos_pais[i]["valor"]  
        poblacion_anterior = datos_pais[i - 1]["valor"]  

        if poblacion_anterior == 0:
            crecimiento = 0
        else:
            crecimiento = ((poblacion_actual - poblacion_anterior) / poblacion_anterior) * 100

        print(f"{año_actual:<10}{poblacion_actual:<20.2f}{crecimiento:<15.2f}%")
if __name__ == "__main__":
    print ("**** BIENVENIDO A LOS REGISTROS *****")
    ruta_datos = "poblacion.json"
    ruta_paises = "paises.json"
    while True:
        opc=int(input("Elija la opción que desea realizar: \n1. Informes de población \n2. Informes de crecimiento poblacional: \n3. Salir"))
        if opc==1:
            informe_poblacion(ruta_datos, ruta_paises)
        elif opc==2:
            informe_crecimiento_poblacional(ruta_datos, ruta_paises)
        elif opc==3:
            print("Saliendo...")
            break
        else:
            print("Ingrese una opcion valida")



