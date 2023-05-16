n1 = float(input("ingrese la primera nota: "))
n2 = float(input("ingrese la segunda nota: "))
n3 = float(input("ingrese la tercera nota: "))
n4 = float(input("ingrese la cuarta nota:  "))
n5 = float(input("ingrese la qunta nota:   "))

def calcularNota(n1,n2,n3,n4,n5):
    return (n1*0.1.5)+ (n2*0.3)+ (n3*0.2.5)+ (n4*0.1)+ (n5*0.2)

Nota_final = calcularNota(n1,n2,n3,n4,n5)

print("la nota final de el semestre de el estudiante es: ",round(Nota_final,2))