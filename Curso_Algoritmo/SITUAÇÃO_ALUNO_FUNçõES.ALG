Algoritmo "SITUA��O_ALUNO_fun��es"
// 
//  
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 14/06/2021
Var
p1,p2,p3,x:real
sit:caractere

funcao media(a,b,c:real):real
var
med:real
inicio
      med <- (a+b+c)/3
      retorne med
fimfuncao

funcao situacao(x:real):caractere
inicio
      se (x>=6) entao
         retorne "APROVADO"
      senao
           se (x<6) e (x>=3.5) entao
              retorne "EM RECUPERA��O"
           senao
                retorne "REPROVADO"
           fimse
      fimse
fimfuncao
Inicio
      escreva("Digite a nota da sua P1: ")
      leia(p1)
      escreva("Digite a nota da sua P2: ")
      leia(p2)
      escreva("Digite a nota da sua P3: ")
      leia(p3)
      x <- media(p1,p2,p3)
      sit <- situacao(x)
      escreval("A m�dia das suas notas foi de: ",x:4:2)
      escreval("A sua situa��o final foi: ",sit)


Fimalgoritmo