f=open("1.txt",'r')
texto=f.read()
f.close()

f = open("1.txt", "w")
name=input("Nombre de la canción: ")
aut=input("Nombre del autor: ")
f.write(name+" - "+aut+"\n"+texto)
f.close()

f = open("1.txt", "r")
print(f.read())