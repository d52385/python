#Imprimir los múltiplos de un número(p) que hay entre 1 y un extremo superior determinado
c=0 #contador  
n=int(input("Introduzca el extremos superior: "))
p=int(input("Introduzca un número: "))
print("Múltiplos de n entre 1 y %i:"%n)  
for i in range(1,n+1):  
 if i%p==0:  
  c+=1
  print(i)  
print("Existen %i múltiplos de %i en ese rango, incluidos los extremos"%(c,p))
