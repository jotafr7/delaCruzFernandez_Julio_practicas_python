nota_alumno = int(input("¿Cual es tu nota en el examen de Python?"))

if nota_alumno < 5:
    print("Tu nota es INSUFICIENTE para aprobar")

elif nota_alumno < 6:
    print("Tu nota es SUFICIENTE para aprobar")

elif nota_alumno < 7:
    print("Tu norta esta BIEN par aprobar")

elif nota_alumno < 9:
    print("Tu nota es de NOTABLE para aprobar")

else:
    print("Tu nota es SOBREALIEBTE para aprobar") 