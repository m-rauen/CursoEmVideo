Algoritmo "DESAFIO_Fibonacci"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 07/06/2021
Var
C,T1,T2,T3:inteiro


Inicio
      T1 <- 0
      T2 <- 1
      escreva(T1)
      escreva(T2)
      para C := 3 ate 10 faca
           T3 <- T1+T2
           escreva(T3)
           T1 := T2
           T2 := T3
      fimpara


Fimalgoritmo