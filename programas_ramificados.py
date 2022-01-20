def run():
         
    usuario1 = input("Usuario 1 ingrese su nombre: ")
    edad1 = int(input(usuario1 + " Ingrese su edad: "))
    usuario2 = input("Usuario 2 ingrese su nombre: ")
    edad2 = int(input(usuario2 + " Ingrese su edad: "))

    if edad1 > edad2:
       print(usuario2 + " es menor que " + usuario1)
    elif edad1 < edad2:
       print(usuario2 + " es mayor que " + usuario1)
    else:
       print(usuario1 + " tiene la misma edad que " + usuario2)    


if __name__ == "__main__":
    run()