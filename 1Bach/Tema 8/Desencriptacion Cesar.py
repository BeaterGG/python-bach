texto_encriptado = input("Ingrese el texto encriptado: ")
clave = int(input("Ingrese la clave de encriptación (número entero): "))

texto_desencriptado = ''.join(chr(ord(c) - clave) for c in texto_encriptado)
print("Texto desencriptado:", texto_desencriptado)
