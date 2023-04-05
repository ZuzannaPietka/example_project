# trojkat
import math
a = 10
b = 20
c = 15
h = 12

obwod = a + b + c
pole = int((h * a) / 2)

print("Obwod trojkata wynosi " + str(obwod) + ", zas pole wynisi " + str(pole) + ".")

obwod_prost = 2*a+2*b
pole_prost = a * b
print("Obwod prostokąta wynosi " + str(obwod_prost) + ", zas pole wynisi " + str(pole_prost) + ".")

r = 10;

obwod_kolo = 2*math.pi*r
pole_kolo = math.pi*r**2
print("Obwod koła wynosi " + str(obwod_kolo) + ", zas pole wynisi " + str(pole_kolo) + ".")

d= 10
obwod_trapez = a+b+c+d
pole_trapez = ((a+b)*h)/2
print("Obwod trapezu wynosi " + str(obwod_trapez) + ", zas pole wynisi " + str(pole_trapez) + ".")



