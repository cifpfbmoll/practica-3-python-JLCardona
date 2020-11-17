from os import system
system("cls")
print ("Dime una fecha")
dia = int (input ("Día de la fecha : "))
mes = int (input ("Mes de la fecha : "))
año = int (input ("Año de la fecha : "))
if (dia <= 0) or (dia > 31) or (mes <= 0) or (mes > 12) or (año <= 0):
    print(dia,"/",mes,"/",año, "  ¡La fecha es INCORRECTA!")
elif (mes == 2 and dia > 28) or (mes == 4 and dia > 30) or (mes == 6 and dia > 30) or (mes == 9 and dia > 30) or (mes == 11 and dia > 30):
    print(dia,"/", mes ,"/", año , "  ¡La fecha es INCORRECTA!")
else:
    print(dia,"/", mes ,"/", año , "  ¡La fecha es CORRECTA!")