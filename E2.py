from os import system
system("cls")
print ("¿Cuántos Km ha recorrido su coche hoy?")
x = int (input("Ha recorrido hoy Km : "))
print ("¿Y cuántas horas llevas hoy con el coche?")
y = int (input("Llevo estas horas hoy : "))
suma = int (x / y)
print ("Esta ha sido la velocidad media : ",suma)