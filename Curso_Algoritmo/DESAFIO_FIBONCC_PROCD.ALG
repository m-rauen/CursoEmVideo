Algoritmo "DESAFIO_Fiboncc_Procd"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 09/06/2021
Var
lim:inteiro

procedimento maxFib(var mx:inteiro)
var
t3,C,t1,t2:inteiro
inicio
      t1 <- 0
      escreva(t1)
      t2 <- 1
      escreva(t2)
      para C := 3 ate mx faca
           t3 := t1+t2
           escreva(t3)
           t1 := t2
           t2 := t3
      fimpara
fimprocedimento
Inicio
      escreval("--------------------------------")
      escreval("      F I B O N A C C I         ")
      escreval("--------------------------------")
      escreva("Digite quantos termos você deseja visualizar: ")
      leia(lim)
      maxFib(lim)


Fimalgoritmo