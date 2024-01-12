texto_original = input("Ingrese el texto a encriptar: ")
clave = int(input("Ingrese la clave de encriptación (número entero): "))

texto_encriptado = ''.join(chr(ord(c) + clave) for c in texto_original)
print("Texto encriptado:", texto_encriptado)