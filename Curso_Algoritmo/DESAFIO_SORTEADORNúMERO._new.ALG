Algoritmo "DESAFIO_SorteadorNúmero"

Var
Plp, Sort: inteiro


Inicio
      escreval("SORTEADOR DE NÚMEROS:")
      escreval("-----------------------------------------------------")
      escreval("O computador gerará um número aleatório entre 0 e 5.")
      escreval("Só valem números inteiros, portanto: 0,1,2,3,4 e 5.")
      escreval("-----------------------------------------------------")
      Sort <- randI(5)
      escreva("Por favor, informe seu palpite: ")
      leia(Plp)
      escreval("O número gerado foi: ", Sort)
      se (Plp=Sort) entao
         escreva("Parabéns, você acertou e ganhou o jogo!!")
      senao
           escreva("Infelizmente, você errou e perdeu o jogo!")
      fimse





Fimalgoritmo