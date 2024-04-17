def calcular_area(ancho, largo):
    return ancho * largo

def calcular_perimetro(ancho, largo):
    return 2 * (ancho + largo)

def graficar_rectangulo(ancho, largo):
    for _ in range(largo):
        print("* " * ancho)

# Solicitar al usuario el ancho y el largo del rectángulo
ancho = float(input("Ingrese el ancho del rectángulo: "))
largo = float(input("Ingrese el largo del rectángulo: "))

# Calcular el área y el perímetro
area = calcular_area(ancho, largo)
perimetro = calcular_perimetro(ancho, largo)

# Imprimir el área y el perímetro
print(f"Área del rectángulo: {area}")
print(f"Perímetro del rectángulo: {perimetro}")

# Graficar el rectángulo
print("Rectángulo:")
graficar_rectangulo(int(ancho), int(largo))

