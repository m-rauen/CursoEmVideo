Algoritmo "DESAFIO_SorteadorNum_2.0"

Var
Plp, Sort,C,Chs: inteiro


Inicio
	   escreval("SORTEADOR DE NÚMEROS:")
      escreval("-----------------------------------------------------")
      escreval("O computador gerará um número aleatório entre 0 e 10.")
      escreval("Só valem números inteiros, portanto: 0,1,2,3,...,10")
      escreval("-----------------------------------------------------")
      Sort <- randI(10)
      C <- 1
      enquanto (C<=4) faca
               Sort <- randi(10)
               escreva("Informe seu palpite: ")
               leia(Plp)
               se (Plp<>Sort) entao
                  Chs <- 4-C
                  escreval("Infelizmente, você errou!!")
                  escreval("O número sorteado foi: ",Sort)
                  escreval("Você ainda tem ",Chs," chances.")
                  C <- C+1
                  escreval("-----------------------------------------------------")
               senao
                    se (Plp=Sort) entao
                       escreval("Parabéns, você acertou!!")
                       escreval(Sort," = ",Plp)
                       C <- C+5
                    fimse
               fimse
      fimenquanto


Fimalgoritmo