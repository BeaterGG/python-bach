texto_original = input("Introduce el texto a encriptar: ")
clave = int(input("Introduce la clave de encriptación (número entero): "))

texto_encriptado = ''.join(chr(ord(c) + clave) for c in texto_original)

f=open("texto encriptado.txt",'w')
f.write(texto_encriptado)
f.close()

f = open("texto encriptado.txt", "r")
print(f.read())