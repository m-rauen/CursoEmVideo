Algoritmo "semnome"
Var
n1,C,ST:inteiro


Inicio
      C <- 1
      ST <- 0
      enquanto (C<=7) faca
               escreva("Por favor, informe o ", C,"o algarismo: ")
               leia(n1)
               C <- C+1
               ST <- ST+n1
      fimenquanto
      escreval(" Acabou")
      escreva("Soma Total: ",ST)
Fimalgoritmo