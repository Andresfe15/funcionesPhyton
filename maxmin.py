def encontrar_maximo_minimo():
    valores = []
    cantidad_valores = int(input("Ingrese la cantidad de valores: "))
    
    for i in range(cantidad_valores):
        valor = float(input(f"Ingrese el valor {i+1}: "))
        valores.append(valor)
    
    if not valores:
        return None, None
    
    maximo = max(valores)
    minimo = min(valores)
    
    return maximo, minimo

# Ejemplo de uso
maximo, minimo = encontrar_maximo_minimo()
if maximo is not None and minimo is not None:
    print("Valor máximo:", maximo)
    print("Valor mínimo:", minimo)
else:
    print("No se han ingresado valores.")

