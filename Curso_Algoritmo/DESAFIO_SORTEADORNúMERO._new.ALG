Algoritmo "DESAFIO_SorteadorN�mero"

Var
Plp, Sort: inteiro


Inicio
      escreval("SORTEADOR DE N�MEROS:")
      escreval("-----------------------------------------------------")
      escreval("O computador gerar� um n�mero aleat�rio entre 0 e 5.")
      escreval("S� valem n�meros inteiros, portanto: 0,1,2,3,4 e 5.")
      escreval("-----------------------------------------------------")
      Sort <- randI(5)
      escreva("Por favor, informe seu palpite: ")
      leia(Plp)
      escreval("O n�mero gerado foi: ", Sort)
      se (Plp=Sort) entao
         escreva("Parab�ns, voc� acertou e ganhou o jogo!!")
      senao
           escreva("Infelizmente, voc� errou e perdeu o jogo!")
      fimse





Fimalgoritmo