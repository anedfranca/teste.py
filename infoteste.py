nome = "ana" #string
idade = 15 #int
altura = 1.63 #float
gosto_de = "rosa"
#is_male = True / False #bool
  
print (f"meu nome é {nome}")
print (f"gosto de {gosto_de}")
print (f"tenho {idade}")


nome = input("Digite seu nome: ")
idade = int (input(f"Qual a sua idade {nome}? "))
nascimento = 2023 - idade
print(f"seu nome é {nome}, sua idade é {idade} e você nasceu em {nascimento}")


num1 = 4 
num2 = 4.2
print (type(num1))
print (type(num2))
a = float (num1)
print (a)
print (type(a))
b = int (num2)
print (b)
print (type(b))


num1 = 4 
num2 = 2
print (num1 + num2)
print (num1 - num2)
print (num1 * num2)
print (num1 / num2) #resultado c num quebrado ou int#
print (num1 % num2) #resto da divisao#
print (num1 ** num2) #exponenciacao#
print (num1 // num2) #result com num int/arredondado#

print ((3 + 5) *( 7 + 3))

print (abs(-15)) #num absoluto#
print (pow(3,3)) #exponencial#
print (max(6,9,2,4))
print (min(6,4,-45))
print (round(8.9)) #arredondar#

import math 
print (math.floor(8.99999)) #arrendoda p baixo#
print (math.ceil(8.00001)) #arrdonda p cima#
print (math.sqrt(10))

num1 = int(input ("Digite um numero: "))
num2 = int(input ("Digite outro numero: "))
resultado = num1 + num2
print(f"o resultado é: {resultado}")

familia = ["Leonardo", "Michelly", "Ane", "Luisa"]
print(familia[0]) #primeiro nome
print(familia[-1]) #de tras pra frente. -1 seria o ultimo nome
print(familia[2:]) #a partir do 2
print(familia[2:4])#do 2 ao 4. lembrando que começa do 0
familia[1] = "Luisa"#fica na posicao determinada
familia.extend(["Luciene", "Camilo"]) #adicionar lista na outra
familia.append("Petra") #adicionar apenas um valor/nome na lista
familia.insert(3, "Petra") #ficar na posicao determinada mas sem substituir
familia.pop() #remove o ultimo 
familia.remove("Michelly") #remove c base no nome
familia.clear() #limpa a lista
print(familia.index("luisa")) # mostra qual posicao q esse nome aparece primeiro
print(familia.count("Luisa")) #conta quantos nomes iguais tem na lista
print(familia) #para aparecer