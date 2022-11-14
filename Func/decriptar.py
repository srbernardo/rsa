def mainDecriptar():  
  def euclides_estendido(e, b):
      if (e == 0):
          return b, 0, 1
      mdc, s1, t1 = euclides_estendido(b % e, e)    
      s = t1 - (b // e) * s1
      t = s1
      return mdc, s, t

  def inverso(e, phi):
      e = e % phi
      b = 1 % phi    
      s1 = 0
      t1 = 0
      d, s1, t1 = euclides_estendido(e, phi)
      if(b % d != 0):
          return 0
      else:
          if(s1 < 0):
              phi = phi // d
              return s1 + phi
          elif(s1 > phi):
              phi = phi // d
              return s1 % phi
          else:
              return s1

  def decifrar(msg_decriptada, alfabeto_numero, alfabeto):
    mensagem_decifrada = []

    for i in range(0,len(msg_decriptada)):
      for j in range(0,len(alfabeto_numero)):
        if(msg_decriptada[i] == alfabeto_numero[j]):
          mensagem_decifrada.append(alfabeto[j])
    
    return (''.join(mensagem_decifrada))

  p = int(input("DIGITE O 'p': "))
  q = int(input("DIGITE O 'q': "))
  e = int(input("DIGITE O 'e': "))

  phi = (p-1)*(q-1)
  n = p*q

  arquivo = open('./bruno.txt', 'r')
  msg = arquivo.read().split(" ")

  msg_decriptada = []

  for i in range(0,len(msg)):
    msg_decriptada.append( (int(msg[i]) ** inverso(e,phi)) % n)

  alfabeto = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v','w', 'x','y','z',' ']
  alfabeto_numero = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]

  final = decifrar(msg_decriptada, alfabeto_numero, alfabeto)
  print (f"\n{final}\n")
