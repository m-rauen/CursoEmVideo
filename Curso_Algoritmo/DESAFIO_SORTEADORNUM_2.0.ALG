Algoritmo "DESAFIO_SorteadorNum_2.0"

Var
Plp, Sort,C,Chs: inteiro


Inicio
	   escreval("SORTEADOR DE N�MEROS:")
      escreval("-----------------------------------------------------")
      escreval("O computador gerar� um n�mero aleat�rio entre 0 e 10.")
      escreval("S� valem n�meros inteiros, portanto: 0,1,2,3,...,10")
      escreval("-----------------------------------------------------")
      Sort <- randI(10)
      C <- 1
      enquanto (C<=4) faca
               Sort <- randi(10)
               escreva("Informe seu palpite: ")
               leia(Plp)
               se (Plp<>Sort) entao
                  Chs <- 4-C
                  escreval("Infelizmente, voc� errou!!")
                  escreval("O n�mero sorteado foi: ",Sort)
                  escreval("Voc� ainda tem ",Chs," chances.")
                  C <- C+1
                  escreval("-----------------------------------------------------")
               senao
                    se (Plp=Sort) entao
                       escreval("Parab�ns, voc� acertou!!")
                       escreval(Sort," = ",Plp)
                       C <- C+5
                    fimse
               fimse
      fimenquanto


Fimalgoritmo