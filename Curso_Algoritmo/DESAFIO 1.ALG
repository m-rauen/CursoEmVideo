Algoritmo "Desafio 1"

Var
tcm, tcd, tca, r1, r2, tap: real
msg1, msg2, msg3:caractere
Inicio
msg1 <- "Diga h� quantos anos voc� fuma:"
escreval(msg1)
leia(r1)
msg2 <- "Diga quantos cigarros voc� fuma por dia:"
escreval(msg2)
leia(r2)
tcm <- r2 * 10
tcd <- tcm * 365
tca <- tcd * 0.000694444
tap <- tca * r1
escreva("Em 1 ano voc� perdeu: ")
escreva(int(tca))
escreval(" dias de vida")
escreva("No tempo que voc� fuma, voc� perdeu j�: ")
escreva(int(tap))
escreva(" dias de vida")
Fimalgoritmo