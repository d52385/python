print("Divisores de un número(número 1) que son múltiplos de otro número(número 2)")
print("introduzca los números:")
N_a = int(input("número 1:"))
N_b = int(input("númmero 2:"))
contador = 0
print("los divisores de ",N_a)
for divisor in range(1,N_a+1):
    if (N_a % divisor)==0 and (divisor%N_b)==0 :
        contador += 1
        print(divisor,"es divisor")
        
print("el numero ",N_a," tiene ",contador," divisores")
#divisores de un número(N_a) que son múltiplos de otro número(N_b)
