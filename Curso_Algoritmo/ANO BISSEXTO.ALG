Algoritmo "semnome"

Var
N: Inteiro

Inicio
      escreva("Por favor, digite o ano: ")
      leia(N)
      se (N%400=0) entao
         escreva("Esse ano é bissexto")
      senao
           se (N%4=0) e (N%100<>0) entao
              escreva("Esse ano é bissexto")
           senao
                escreva("Esse ano não é bissexto")
           FimSe
      FimSe




Fimalgoritmo