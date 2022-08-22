Algoritmo "PA_funções"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/06/2021
Var
in,fim,ss:inteiro

funcao supersomador(a,b:inteiro):inteiro
var
som,c:inteiro
inicio
      se (a>b) entao
         para c := a ate b passo -1 faca
              escreva(c," ")
              som <- som+c
              retorne som
         fimpara
      senao
           se (b>a) entao
              para c := a ate b faca
                   escreva(c," ")
                   som <- som+c
                   retorne som
              fimpara
           fimse
      fimse
fimfuncao


Inicio
      escreva("Digite o algarismo inicial da progressão: ")
      leia(in)
      escreva("Digite o algarismo final da progressão: ")
      leia(fim)
      ss <- supersomador(in,fim)
      escreval(" - Acabou a P.A.!!")
      escreva("O resultado da progressão aritmética é: ",ss)


Fimalgoritmo