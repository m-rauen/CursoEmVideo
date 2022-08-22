Algoritmo "semnome"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 09/06/2021
Var
msg,r:caractere
b,v:inteiro

procedimento gerador(ms:caractere)
var
C:inteiro
inicio
      C <- 1
      se (b=1) entao
         escreval("+-------================-------+")
         para C := 1 ate v faca
               escreval("          ",ms,"!!!          ")
         fimpara
         escreval("+-------================-------+")
      senao
           se (b=2) entao
              escreval("~~~~~~~~~~~~~:::::::~~~~~~~~~~~~")
              para C := 1 ate v faca
                   escreval("          ",ms,"!!!          ")
              fimpara
              escreval("~~~~~~~~~~~~~:::::::~~~~~~~~~~~~")
           senao
                escreval("<<<<<<<<<<<<<------->>>>>>>>>>>>")
                para C := 1 ate v faca
                     escreval("          ",ms,"!!!          ")
                fimpara
                escreval("<<<<<<<<<<<<<------->>>>>>>>>>>>")
           fimse
      fimse
fimprocedimento

Inicio
      escreva("- É sua primeira vez programando? (S/N): ")
      leia(r)
      se (r="S") entao
         escreva("- Qual mensagem você quer que seja exibida: ")
         leia(msg)
         escreva("- Quantas vezes deseja repetir a mensagem exibida: ")
         leia(v)
         escreval("- Selecione o tipo de borda desejado (1,2 ou 3): ")
         escreval("Borda 1: +-------================-------+")
         escreval("Borda 2: ~~~~~~~~~~~~~:::::::~~~~~~~~~~~~")
         escreval("Borda 3: <<<<<<<<<<<<<------->>>>>>>>>>>>")
         leia(b)
         gerador(msg)
      senao
           escreva("Então seja bem vindo novamente!")
      fimse




Fimalgoritmo