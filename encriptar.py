FILENAME = "bruno.txt"

def gerar_dicionario_char():
    """Generate a dict to map chars to numbers."""
    alfabeto = "abcdefghijklmnopqrstuvwxyz "
    dicionario_char = {}
 
    for i in range(len(alfabeto)):
        dicionario_char.update({alfabeto[i]: i + 2})
 
    return dicionario_char
 
 
def to_int(char):
    """Transform a char to number based on the generated map."""
    dicionario_char = gerar_dicionario_char()
    return dicionario_char[char]
 
 
def encriptar(texto_original, e, n):
    """Encripte um texto usando rsa."""
    chars_encriptados = []
    for char in texto_original:
        chars_encriptados.append(str((to_int(char) ** e) % n))
 
    texto_encriptado = " ".join(chars_encriptados)
    print(f"Frase encriptada: {texto_encriptado}")
 
    with open(FILENAME, 'w') as arquivo:
        arquivo.write(texto_encriptado)
 
 
def from_int(number: int) -> str:
    """Transform a number to char based on the generated map."""
    dicionario_char = gerar_dicionario_char()
    for k, v in dicionario_char.items():
        if number == v:
            return k
 
 
def decriptar(d, n):
    """Decrypt a encrypted text string with rsa."""
    with open(FILENAME, 'r') as arquivo:
        texto_encriptado = arquivo.read()
 
    chars_encriptados = texto_encriptado.split(" ")
    decrypted_text = ""
    for enc_char in chars_encriptados:
        decrypted_text += from_int((int(enc_char) ** d) % n)
    return decrypted_text
 
 
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
    # d = int(input("Entre com o valor de \"d\": "))
    encriptar(texto, e, n)
    # dec_text = decriptar(d, n)
    # print(f"A frase descriptografada é: {dec_text}")
    
 
if __name__ == "__main__":
    rsa()
