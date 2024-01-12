palabra=input("Dime una palabra y te digo sus consonantes:")

consonantes = ("b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z","B","C","D","F","G","H","J","K","L","M","N","Ñ","P","Q","R","S","T","V","W","X","Y","Z")

for x in consonantes:
    if x in palabra:
        print(x)
        
