Algoritmo "C�lculo IMC - completo"

Var
 d1,d2,d3,IMC: Real
 msg1: Caractere

Inicio
      escreva("Digite a sua massa em kg: ")
      leia(d1)
      escreva("Digita a sua altura em metros: ")
      leia(d2)
      d3 <- d2^2
      msg1 <- "O seu IMC � de: "
      IMC <- d1/d3
      escreval(msg1, IMC:4:2)
      se (IMC<17) entao
         escreva("Voc� est� muito abaixo do peso")
      senao
           se (IMC >= 17) e (IMC<18.5) entao
              escreva("Voc� est� abaixo do peso")
           senao
                se (IMC>=18.5) e (IMC<25) entao
                   escreva("Voc� est� no seu peso ideal")
                senao
                     se (IMC>=25) e (IMC<30) entao
                        escreva("Voc� est� com sobrepeso")
                     senao
                          se (IMC>=30) e (IMC<35) entao
                             escreva("Voc� est� com obesidade")
                          senao
                               se (IMC>=35) e (IMC<40) entao
                                  escreva("Voc� est� com obesidade severa")
                               senao
                                    escreva("Voc� est� com obesidade m�rbida")
                                    FimSe
                               FimSe
                          FimSe
                     FimSe
                FimSe
           FimSe



Fimalgoritmo