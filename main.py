##QUEST1

indice = 13
soma = 0
k = 0

while k < indice:
    k = k + 1
    soma = soma + k
print("O resultado é",soma,", porque o loop só para no momento em que o indice atingir 13 e, a cada repetição, é icrementado 1 e adicionado a variável 'soma'.")


##QUEST2: escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci 
#e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibo(n):
    f1, f2 = 0, 1 #os dois primeiros numeros da sequencia de Fibonacci
    #enquanto o número na sequência for menor que o digitado, haverá a atualização dos dois últimos números
    #do segmento
    while f2 < n:
        f1, f2 = f2, f1+f2
    return f2 == n #retorna verdadeiro se o número estiver na sequência
#armaza o numero digitado na variável 'numero'
numero = int(input("Digite um número"))

#chama a função fibo e printa o resultado que corresponde ao valor da função
if fibo(numero):
    print(f"{numero} pertence á sequência de Fibonacci.")
    
else:
    print(f"{numero} não é pertencente.")


##QUEST5

def inverteSrtring(string):
    
    #função para inverter umastring
    stringInvertida = '' #armazena a string invertida
    for char in string: #percorre cada caractere da string original
        stringInvertida = char +stringInvertida #adiciona o caractere no inicio da string invertida
    return stringInvertida

#O usuário pode digitar palavras quantas vezes quiser
while True:
    cxEntrada = input("Digite uma palavra.")
    stringInvertida = inverteSrtring(cxEntrada) #chama a função para inverter a palavra
    print("O valor invertido é: ", stringInvertida)
    
    continuar = input("Quer tentar de novo? (s/n)")
    if continuar.lower() != 's':
        break
    
