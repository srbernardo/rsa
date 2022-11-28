import math

def chavePublica():
    def mdc(a,b):
        while(True):
            if(a % b == 0):
                return b
            else:
                temp = a % b
                a = b
                b = temp

    def primo(numero):
        if(numero < 0):
            return False
        raiz = int(math.sqrt(numero))
        for i in range(2,raiz + 1):
            if numero % i == 0:
                return False
        return True

    while True: 
        p = int(input("Digite um número primo P: "))
        q = int(input("Digite um número primo Q: "))
        teste_p = primo(p)
        teste_q = primo(q)

        if(teste_p == True and teste_q == True):
            break
        else:
            print("-----")
            print("{} é primo: {}\n{} é primo: {}".format(p,teste_p,q,teste_q))
            print("Par de números inválido!\nDigite novamente.\n-----")
    
    n = p*q
    phi = (p-1)*(q-1)

    while True:
        e = int(input("Digite um número 'e' comprimo a {}: ".format(phi)))

        if( (mdc(e,phi)==1) and (e > 1) and (e < phi) ):
            break
        else:
            print("Número Inválido!\nDigite novamente.\n-----")
    
    print("\nChave pública: n = {} e = {}".format(n,e))
    chave_publica = {
        "n": n,
        "e": e
    }
    with open("chave-publica.txt", 'w') as arquivo:
        arquivo.write(str(chave_publica)) 

    print("Verifique o arquivo 'chave-publica.txt'\n")
