def run():
    objetivo = int(input('Escribe un numero: '))
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1
    
    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene raiz cuadrada exacta')
        
        
if __name__ == "__main__":
    run()