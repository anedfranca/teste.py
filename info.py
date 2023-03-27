minha_string = "meu texto"
print (minha_string.upper()) #deixar o texto maiusculo
print (minha_string.lower()) #deixar o texto minusculo
print (minha_string.capitalize()) #deixa a primeira letra maiuscula
print (minha_string.isupper()) 
print (minha_string.islower())
print (minha_string.strip()) #remover espaço no inicio ou final
print (minha_string.replace("meu", "qualquer")) #substitui uma letra,texto ou variavel por outra#
print (minha_string.replace("e", "E",1)) #substituiu apenas o primeiro 'e'
print (len(minha_string)) #contar quantas letras tem no texto
print (minha_string[4]) #dizer qual letra esta nessa casa conta a partir do 0
print (minha_string[0:3]) #as 3 primeiras letras de tras p frente conta a partir -1
print (minha_string.index("texto"))
#and: retorna um valoe verdadeiro se as duas expressoes forem veradeiras
#or: retorna um vlor falso as duas forem falsas
#not: not true(false); not false (true). verifica se as duas variaveis apontam para o mesmo objeto
#in: retorna verdadeiro se receber um item ocorrer pelo menos uma vez; flso caso contrario
#is antes da palavra pra saber se eh true or false
#[]lista; {}dicionario; ()tupla; 0 - zero; none - nulo

x="texto" in minha_string
print(x)

minha_string = """linha 1, 
linha 2,
linha 3"""
print(minha_string) 
ou
minha_string = "linha 1, \nlinha 2,\nlinha 3"
print(minha_string) #cada uma em uma linha
# \n quebra linha mesmo escrevendo na mesma linha
# """ quebra linha mas precisa quebrar no codigo
# a barra adiciona aspas no texto \" \" 

