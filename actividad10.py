user_name = input("Introduce tu nombre de usuario:")
name_password = input("Introduce tu contraseña:")

name = "Zamara"
password = "25"

while user_name != name and name_password != password:
    user_name = input("Introduzca su nombre de nuevo:")
    name_password = input("INtroduzca su contraseña de nuevo:")

print("Credenciales admitidas, puede continuar hacia delante.")