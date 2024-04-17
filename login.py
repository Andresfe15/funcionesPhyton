def login(usuario, contraseña, intentos):
    # Verificar si el nombre de usuario y la contraseña son correctos
    if usuario == "admin" and contraseña == "admin123*":
        return True, intentos
    else:
        # Incrementar el número de intentos si el inicio de sesión falla
        intentos += 1
        return False, intentos

# Ejemplo de uso
intentos = 0

while True:
    usuario_input = input("Ingrese su nombre de usuario: ")
    contraseña_input = input("Ingrese su contraseña: ")
    
    # Verificar el inicio de sesión
    inicio_sesion_exitoso, intentos = login(usuario_input, contraseña_input, intentos)
    
    if inicio_sesion_exitoso:
        print("Inicio de sesión exitoso.")
        break
    else:
        print("Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.")
        print(f"Número de intentos restantes: {3 - intentos}")

    if intentos >= 3:
        print("Número máximo de intentos alcanzado. Bloqueando el sistema.")
        break
