Algoritmo "semnome"

Var
N: Inteiro

Inicio
      escreva("Por favor, digite o ano: ")
      leia(N)
      se (N%400=0) entao
         escreva("Esse ano � bissexto")
      senao
           se (N%4=0) e (N%100<>0) entao
              escreva("Esse ano � bissexto")
           senao
                escreva("Esse ano n�o � bissexto")
           FimSe
      FimSe




Fimalgoritmo