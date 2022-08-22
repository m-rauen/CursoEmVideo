Algoritmo "Desafio 1"

Var
tcm, tcd, tca, r1, r2, tap: real
msg1, msg2, msg3:caractere
Inicio
msg1 <- "Diga há quantos anos você fuma:"
escreval(msg1)
leia(r1)
msg2 <- "Diga quantos cigarros você fuma por dia:"
escreval(msg2)
leia(r2)
tcm <- r2 * 10
tcd <- tcm * 365
tca <- tcd * 0.000694444
tap <- tca * r1
escreva("Em 1 ano você perdeu: ")
escreva(int(tca))
escreval(" dias de vida")
escreva("No tempo que você fuma, você perdeu já: ")
escreva(int(tap))
escreva(" dias de vida")
Fimalgoritmo