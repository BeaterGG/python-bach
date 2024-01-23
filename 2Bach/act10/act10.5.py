try:
    f=open("texto encriptado.txt",'r')
    texto_encriptado=f.read()
    f.close()
    print("\nTexto a desencriptar:\n",texto_encriptado,"\n")

    clave = int(input("Ingrese la clave de encriptación (número entero): "))
    texto_desencriptado = ''.join(chr(ord(c) - clave) for c in texto_encriptado)

    print("\nTexto desencriptado:\n", texto_desencriptado)
except:
    print("No existe el documento ¨texto encriptado.txt¨, por favor cree uno con el ejercicio anterior")