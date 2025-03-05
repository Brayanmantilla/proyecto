import json
# Leer archivos JSON
def leer_json (ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            load=json.load(archivo)
            return load
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta}'")
        return[]
    except json.JSONDecodeError:
        print("Error: El archivo no tiene un formato JSON válido")
        return[]

def guardar_json(ruta, datos):
    try:
        with open(ruta, 'w', encoding='utf-8') as file:
            json.dump(datos, file, indent=4)
        print(f"Archivo '{ruta}' guardado correctamente.")
    except Exception as e:
        print(f"Error al guardar el archivo '{ruta}': {e}")


def agregar_dato_usuario(ruta_datos, ruta_paises, ruta_indicadores):
    datos = leer_json(ruta_datos)  # Leer datos actuales
    paises = leer_json(ruta_paises)  # Leer países disponibles
    indicadores = leer_json(ruta_indicadores)  # Leer indicadores disponibles
    print("Paises registrados")
    for pais in paises:
        print(f"- {pais['nombre']} ({pais['codigo_iso3']})")
    print("Indicadores registrados")
    for ind in indicadores:
        print(f"- {ind['id_indicador']}: {ind['descripcion']}")
    print("Datos registrados")
    for dato in datos:
        print(f"Año: {dato['ano']}, País: {dato['pais']}, Indicador: {dato['indicador_id']}, Valor: {dato['valor']} {dato['unidad']}")

## ESTO
ruta_datos="poblacion.json"
ruta_indicadores="indicadores.json"
ruta_paises="paises.json"

datos = leer_json(ruta_datos)  # Leer datos actuales
paises = leer_json(ruta_paises)  # Leer países disponibles
indicadores = leer_json(ruta_indicadores)  # Leer indicadores disponibles

while True:
        opc=int(input("Ingrese la opción que desea realizar: \n1. Ver indicadores, paises y datos disponibles \n2. Añadir indicador \n3. Añadir pais \n4. Añadir dato \n5. Salir"))
        if opc==1:
            agregar_dato_usuario(ruta_datos, ruta_paises, ruta_indicadores)
        elif opc==2:
                indicador_id = input("Ingrese el ID del indicador que desea consultar: ").upper()
                indicador_encontrado = next((i for i in indicadores if i["id_indicador"] == indicador_id), None)
                if indicador_encontrado:
                    print("El indicador ya se encuentra en el registro. Puede continuar")
                elif not indicador_encontrado:
                    print("**** REGISTRO NUEVO INDICADOR ****")
                    indicador_nuevo=input("Ingrese el nuevo indicador: ")
                    descripcion_nuevo=input("Ingrese la nueva descripcion: ")
                    nuevo_indicador={"id_indicador":indicador_nuevo,"descripcion":descripcion_nuevo}
                    indicadores.append(nuevo_indicador)
                    guardar_json(ruta_indicadores, indicadores)
                    print("Nuevo indicador agregado con éxito.")
                    indicador_encontrado=nuevo_indicador
        elif opc==3:
                # Validar país
                codigo_iso3 = input("\nIngrese el código ISO3 del país que desea consultar: ").upper()
                pais_encontrado = next((p for p in paises if p["codigo_iso3"] == codigo_iso3), None)
                if pais_encontrado:
                    print("El país ya se encuentra en el registro. Puede continuar")
                elif not pais_encontrado:
                    print("**** REGISTRO NUEVO PAIS ****")
                    pais_nuevo=input("Ingrese el nombre del país a agregar: ")
                    iso_nuevo= input("Ingrese codigo ISO: ")
                    iso3_nuevo=input("Ingrese codigo ISO3: ")
                    nuevo_pais={"nombre": pais_nuevo, "codigo_iso":iso_nuevo, "codigo_iso3": iso3_nuevo}
                    paises.append(nuevo_pais)
                    guardar_json(ruta_paises, paises)
                    print("Nuevo país agregado con éxito.")
                    pais_encontrado=nuevo_pais
        elif opc==4:
            # Pedir otros datos
            ano = int(input("Año: "))
            valor = float(input("Valor: "))
            estado = input("Estado (disponible/no disponible): ").lower()
            unidad = input("Unidad de medida: ")

            # Crear nuevo dato

            nuevo_dato = {
                "ano": ano,
                "pais": pais_encontrado["nombre"],
                "codigo_iso3": codigo_iso3,
                "indicador_id": indicador_id,
                "descripcion": indicador_encontrado["descripcion"],
                "valor": valor,
                "estado": estado,
                "unidad": unidad
            }
            datos.append(nuevo_dato)  
            guardar_json(ruta_datos, datos)  #Se modifica ruta_datos por ruta3 ya que eso lo definimos arriba
            print("✅ Nuevo dato agregado con éxito.")
        elif opc==5:
             print("Saliendo...")
             break
        else:
             print("Ingrese una opción valida")


