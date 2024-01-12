def print_segundos(h,m,s):
    t=h*3600+m*60+s
    print(t)
h=int(input("¿Horas? "))
m=int(input("¿Minutos? "))
s=int(input("¿Segundos? "))

print_segundos(h,m,s)