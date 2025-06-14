#verificar se o número inserido pelo usuário é valido para um tamanho de lista
while True:
    try:
        tam=int(input("Quantos valores terão na lista?:  "))
        if tam<0:
            print("O número digitado deve ser um inteiro positivo. Digite novamente:  ")
            continue
        break
    except ValueError:
        print("Digite um caractere válido: números inteiros positivos:  ")
        continue

#criando a lista e preenchendo com os inputs do usuário
intervalo=list()

for i in range(1,tam+1):
        
        #verificando se o número inserido é valido (inteiro)
        while True:
            try:
                num=int(input("Digite um número:  "))
                if num in intervalo:
                    print("Você ja escreveu esse número. Digite outro:  ")
                    continue
                else:
                    intervalo.append(num)
                break
             
            except ValueError:
                print("Digite caracteres válidos (inteiros positivos ou negativos)")
                continue

def sel_impares(intervalo):
    return[num for num in intervalo if num%2!=0]

impares=sel_impares(intervalo)
print("Os números ímpares da sua lista original",impares)