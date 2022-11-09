FILENAME = "bruno.txt"

def dicionario(char):
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    dicionario_char = {}
 
    for i in range(len(alfabeto)):
        dicionario_char.update({alfabeto[i]: i + 2})
 
    return dicionario_char[char] 
 
def encriptar(texto_original, e, n):
    chars_encriptados = []
    for char in texto_original:
        chars_encriptados.append(str((dicionario(char) ** e) % n))
 
    texto_encriptado = " ".join(chars_encriptados)
    print(f"Frase encriptada: {texto_encriptado}")
 
    with open(FILENAME, 'w') as arquivo:
        arquivo.write(texto_encriptado)
 
def rsa():    
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    nova_tentativa = True
    while nova_tentativa == True: 
        nova_tentativa = False
        texto = input("Escreva a mensagem a ser encriptada: ")
        texto = texto.lower()
        for char in texto:
            if char not in alfabeto: 
                print("Entrada possui caracteres não válidos. Escreva novamente")
                nova_tentativa = True
                break
    e = int(input("Entre com o valor de \"e\": "))
    n = int(input("Entre com o valor de \"n\": "))
    encriptar(texto, e, n)
 
if __name__ == "__main__":
    rsa()
