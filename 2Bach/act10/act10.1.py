f=open("1.txt",'w')
f.write("I, I will be king\nAnd you, you will be queen\nThough nothing, will drive them away\nWe can beat them, just for one day\nWe can be heroes, just for one day")
f.close()

f = open("1.txt", "r")
print(f.read())