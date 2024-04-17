def ingresar_temperaturas():
    datos_temperatura = []
    for i in range(8):
        temperatura_dia = []
        print(f"Ingrese las temperaturas del día {i+1}:")
        for j in range(20):
            temperatura = float(input(f"Ingrese temperatura {j+1}: "))
            temperatura_dia.append(temperatura)
        datos_temperatura.append(temperatura_dia)
    return datos_temperatura

def calcular_temperatura_media(datos_temperatura):
    # Inicializar la suma de temperaturas
    suma_temperaturas = 0
    
    # Iterar sobre los datos de temperatura
    for temperatura in datos_temperatura:
        suma_temperaturas += temperatura
    
    # Calcular la temperatura media
    temperatura_media = suma_temperaturas / len(datos_temperatura)
    
    return temperatura_media

# Obtener datos de temperatura ingresados por el usuario
datos_temperatura = ingresar_temperaturas()

# Calcular temperatura media para cada día y mostrar los resultados
for i, dia in enumerate(datos_temperatura):
    temperatura_media_dia = calcular_temperatura_media(dia)
    print(f"Temperatura media del día {i+1}: {temperatura_media_dia}")
