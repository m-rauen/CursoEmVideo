Algoritmo "Bháskara Completo"

Var
msg1, msg2, msg3, msg4, msg5, msg6, msg7: caractere
n1, n2, n3, d, r1, r2: real
D1, D2, D3: logico
Inicio
msg1 <- "por favor, informe o valor de A: "
escreval(msg1)
leia(n1)
msg2 <- "por favor, informe o valor de B: "
escreval(msg2)
leia(n2)
msg3 <- "por favor, informe o valor de C: "
escreval(msg3)
leia(n3)
d <- (n2^2) - 4 * n1 * n3
msg4 <- "o valor do seu delta é de: "
escreval(msg4 , d)
escreval("Existem raízes para o seu valor de delta?")
escreval("Sim!")
msg5 <- "As raízes para o seu delta são reais e distintas?"
D1 <- d <> 0  e d > 0
escreval(msg5 , D1)
msg6 <- "As raízes para o seu delta são reais e iguais?"
D2 <- d > 0 e d = 0
escreval(msg6, D2)
r1 <- ((-n2) + raizq(n2^2 - 4 * n1 * n3)) / 2 * n1
r2 <- ((-n2) - raizq(n2^2 - 4 * n1 * n3)) / 2 * n1
msg5 <- "o valor da primeira raiz é: "
msg6 <- "o valor da segunda raiz é: "
escreval(msg5, r1)
escreva(msg6, r2)
Fimalgoritmo