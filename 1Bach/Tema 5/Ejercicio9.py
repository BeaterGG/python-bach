import random 
x=15
while x!=0:
    e=["el equipo 1","nadie, quedaron empatados", "el equipo 2"]
    print("El ganador del partido es", random.choice(e))
    x=x-1