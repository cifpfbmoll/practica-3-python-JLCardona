from os import system
system("cls")
nombre = str (input ("Introduzca el nombre del producto : "))
precio = float (input ("Introduzca el precio de dicho producto : "))
IVA = float ((precio * 0.21) + precio)
print ("El producto ", nombre , "tiene un valor de " , precio , "€ y sumandole el IVA su precio final es " , IVA , "€ en total")