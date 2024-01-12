name=input("Hola, ¿Como te llamas?")
print("Hola",name, ", encantado de conocerte")
while True:
    print("")
    order=input("¿Que quieres saber (CITA, DATO, ANÉCDOTA, blanco para acabar)?")
    orderlow=order.lower()
    if orderlow=="cita":
        print("Si piensas que los usuarios de tus programas son idiotas, sólo los idiotas usarán tus programas – Linus Torvalds")
    elif orderlow=="anécdota":
        print("Ada Lovelace fue una matemática británica considerada la primera persona que escribió un algoritmo destinado a ser procesado por una máquina.")
    elif orderlow=="dato":
        print("El código binario es el lenguaje de las máquinas.")
    elif order=="":
        print("Hasta la vista,",name)
        break
    else:
        print("--> Opción incorrecta. Prueba otra vez.")