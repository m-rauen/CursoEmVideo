Algoritmo "DESAFIO_Jokenpo_new"

Var
J1,J2,J3,J4,J5,J6,J7,J8: Caractere
Jogador1, Jogador2,RR1,RR_1,RR2,RR_2,RR3,RR_3,RR4,RR_4: Inteiro

Inicio
      escreval("------------------")
      escreval("JOGO DE JOKENPO")
      escreval("------------------")
      escreval("O jogo � baseado em 3 rodadas, MD3!.")
      escreval("As jogadas acess�veis s�o: Pedra (PE), Papel(PA), Tesoura(TS).")
      escreval("PRIMEIRA RODADA:")
      escreva("- Jogador1, fa�a sua jogada: ")
      leia(J1)
      escreva("- Jogador2, fa�a sua jogada: ")
      leia(J2)
      escreval("------------------------------")
      escreval("RESULTADO DA PRIMEIRA RODADA:")
      se (J1=J2) entao
         RR1 <- 0
         RR_1 <- 0
         Jogador1 <- RR1
         Jogador2 <- RR_1
         escreval("Essa rodada foi um empate!")
      senao
           se (J1="PE") e (J2="TS") entao
              RR1 <- 1
              RR_1 <- 0
              Jogador1 <- RR1
              Jogador2 <- RR_1
              escreval("Jogador1 ganhou essa rodada!")
              escreval("Placar atual:")
              escreval("Jogador1: ", Jogador1)
              escreval("Jogador2: ", Jogador2)
           senao
                se (J1="TS") e (J2="PE") entao
                RR1 <- 0
                RR_1 <- 1
                Jogador1 <- RR1
                Jogador2 <- RR_1
                escreval("Jogador2 ganhou essa rodada!")
                escreval("Placar atual:")
                escreval("Jogador1: ", Jogador1)
                escreval("Jogador2: ", Jogador2)
                senao
                     se (J1="PE") e (J2="PA") entao
                        RR1 <- 0
                        RR_1 <- 1
                        Jogador1 <- RR1
                        Jogador2 <- RR_1
                        escreval("Jogador2 ganhou essa rodada!")
                        escreval("Placar atual:")
                        escreval("Jogador1: ", Jogador1)
                        escreval("Jogador2: ", Jogador2)
                     senao
                          se (J1="PA") e (J2="PE") entao
                          RR1 <- 1
                          RR_1 <- 0
                          Jogador1 <- RR1
                          Jogador2 <- RR_1
                          escreval("Jogador1 ganhou essa rodada!")
                          escreval("Placar atual:")
                          escreval("Jogador1: ", Jogador1)
                          escreval("Jogador2: ", Jogador2)
                          senao
                               se (J1="PA") e (J2="TS") entao
                                  RR1 <- 0
                                  RR_1 <- 1
                                  Jogador1 <- RR1
                                  Jogador2 <- RR_1
                                  escreval("Jogador2 ganhou essa rodada!")
                                  escreval("Placar atual:")
                                  escreval("Jogador1: ", Jogador1)
                                  escreval("Jogador2: ", Jogador2)
                               senao
                                    se (J1="TS") e (J2="PA") entao
                                    RR1 <- 1
                                    RR_1 <- 0
                                    Jogador1 <- RR1
                                    Jogador2 <- RR_1
                                    escreval("Jogador1 ganhou essa rodada!")
                                    escreval("Placar atual:")
                                    escreval("Jogador1: ", Jogador1)
                                    escreval("Jogador2: ", Jogador2)
                                    fimse
                               fimse
                          fimse
                     fimse
                fimse
           fimse
      fimse
      escreval("------------------------------")
      escreval("SEGUNDA RODADA:")
      escreva("- Jogador1, fa�a sua jogada: ")
      leia(J3)
      escreva("- Jogador2, fa�a sua jogada: ")
      leia(J4)
      escreval("------------------------------")
      escreval("RESULTADO DA SEGUNDA RODADA:")
      se (J3=J4) entao
         RR2 <- RR1
         RR_2 <- RR_1
         Jogador1 <- RR2
         Jogador2 <- RR_2
         escreval("Essa rodada foi um empate!")
      senao
           se (J3="PE") e (J4="TS") entao
              RR2 <- (RR1)+1
              RR_2 <- RR_1
              Jogador1 <- RR2
              Jogador2 <- RR_2 <- RR_1
              escreval ("Jogador1 ganhou essa rodada!")
              escreval("Placar atual:")
              escreval("Jogador1: ", Jogador1)
              escreval("Jogador2: ", Jogador2)
           senao
                se (J3="TS") e (J4="PE") entao
                   RR2 <- RR1
                   RR_2 <- (RR_1)+1
                   Jogador1 <- RR2
                   Jogador2 <- RR_2
                   escreval ("Jogador2 ganhou essa rodada!")
                   escreval("Placar atual:")
                   escreval("Jogador1: ", Jogador1)
                   escreval("Jogador2: ", Jogador2)
                senao
                     se (J3="PE") e (J4="PA") entao
                        RR2 <- RR1
                        RR_2 <- (RR_1)+1
                        Jogador1 <- RR2
                        Jogador2 <- RR_2
                        escreval ("Jogador2 ganhou essa rodada!")
                        escreval("Placar atual:")
                        escreval("Jogador1: ", Jogador1)
                        escreval("Jogador2: ", Jogador2)
                     senao
                          se (J3="PA") e (J4="PE") entao
                              RR2 <- (RR1)+1
                              RR_2 <- RR_1
                              Jogador1 <- RR2
                              Jogador2 <- RR_2
                              escreval ("Jogador1 ganhou essa rodada!")
                              escreval("Placar atual:")
                              escreval("Jogador1: ", Jogador1)
                              escreval("Jogador2: ", Jogador2)
                          senao
                               se (J3="PA") e (J4="TS") entao
                                   RR2 <- RR1
                                   RR_2 <- (RR_1)+1
                                   Jogador1 <- RR2
                                   Jogador2 <- RR_2
                                   escreval ("Jogador2 ganhou essa rodada!")
                                   escreval("Placar atual:")
                                   escreval("Jogador1: ", Jogador1)
                                   escreval("Jogador2: ", Jogador2)
                               senao
                                    se (J3="TS") e (J4="PA") entao
                                       RR2 <- (RR1)+1
                                       RR_2 <- RR_1
                                       Jogador1 <- RR2
                                       Jogador2 <- RR_2 <- RR_1
                                       escreval ("Jogador1 ganhou essa rodada!")
                                       escreval("Placar atual:")
                                       escreval("Jogador1: ", Jogador1)
                                       escreval("Jogador2: ", Jogador2)
                                       fimse
                                     fimse
                                fimse
                           fimse
                      fimse
                 fimse
            fimse
            se ((RR2)=2) e ((RR_2)=0) entao
               escreval("Parab�ns, Jogador1! Voc� ganhou!!")
               escreval("------------------------------------")
            senao
                 se ((RR_2)=2) e ((RR2)=0) entao
                    escreval("Parab�ns, Jogador2! Voc� ganhou!!")
                    escreval("-----------------------------------")
                 senao
                      escreval("------------------------------")
                      escreval("TERCEIRA RODADA:")
                      escreva("- Jogador1, fa�a sua jogada: ")
                      leia(J5)
                      escreva("- Jogador2, fa�a sua jogada: ")
                      leia(J6)
                      escreval("------------------------------")
                      escreval("RESULTADO DA TERCEIRA RODADA:")
                      se (J5=J6) entao
                         RR3 <- RR2
                         RR_3 <- RR_2
                         Jogador1 <- RR3
                         Jogador2 <- RR_3
                         escreval("Essa rodada foi um empate!")
                         escreval("Placar Final:")
                         escreval("Jogador1: ", RR3)
                         escreval("Jogador2: ", RR_3)
                      senao
                           se (J5="PE") e (J6="TS") entao
                              RR3 <- (RR2)+1
                              RR_3 <- RR_2
                              Jogador1 <- RR3
                              Jogador2 <- RR_3
                              escreval("Placar final:")
                              escreval("Jogador1: ", Jogador1)
                              escreval("Jogador2: ", Jogador2)
                           senao
                                se (J5="TS") e (J6="PE") entao
                                   RR3 <- RR2
                                   RR_3 <- (RR_2)+1
                                   Jogador1 <- RR3
                                   Jogador2 <- RR_3
                                   escreval("Placar final:")
                                   escreval("Jogador1: ", Jogador1)
                                   escreval("Jogador2: ", Jogador2)
                                senao
                                     se (J5="PE") e (J6="PA") entao
                                        RR3 <- RR2
                                        RR_3 <- (RR_2)+1
                                        Jogador1 <- RR3
                                        Jogador2 <- RR_3
                                        escreval("Placar final:")
                                        escreval("Jogador1: ", Jogador1)
                                        escreval("Jogador2: ", Jogador2)
                                     senao
                                          se (J5="PA") e (J6="PE") entao
                                             RR3 <- (RR2)+1
                                             RR_3 <- RR_2
                                             Jogador1 <- RR3
                                             Jogador2 <- RR_3
                                             escreval("Placar final:")
                                             escreval("Jogador1: ", Jogador1)
                                             escreval("Jogador2: ", Jogador2)
                                          senao
                                               se (J5="PA") e (J6="TS") entao
                                                  RR3 <- RR2
                                                  RR_3 <- (RR_2)+1
                                                  Jogador1 <- RR3
                                                  Jogador2 <- RR_3
                                                  escreval("Placar final:")
                                                  escreval("Jogador1: ", Jogador1)
                                                  escreval("Jogador2: ", Jogador2)
                                               senao
                                                    se (J5="TS") e (J6="PA") entao
                                                       RR3 <- (RR2)+1
                                                       RR_3 <- RR_2
                                                       Jogador1 <- RR3
                                                       Jogador2 <- RR_3
                                                       escreval("Placar final:")
                                                       escreval("Jogador1: ", Jogador1)
                                                       escreval("Jogador2: ", Jogador2)
                                                       fimse
                                                    fimse
                                               fimse
                                          fimse
                                     fimse
                                fimse
                           fimse
                 fimse
            fimse
            se ((RR3)=2) e ((RR_3)=1) entao
               escreva("Parab�ns Jogador1, voc� venceu!!")
            senao
                 se ((RR3)=1) e ((RR_3)=2) entao
                    escreva("Parab�ns Jogador2, voc� venceu!!")
                 senao
                      se ((RR3)=0) e ((RR_3)=0) entao
                         escreva("Voc�s empataram nas 3 rodas, portanto, empate geral!!")
                      senao
                           se ((RR3)=1) e ((RR_3)=1) entao
                              escreval("Voc�s empataram em 1 a 1, portanto, rodada decisiva:")
                              escreval("--------------------------------------")
                              escreval("RODADA DECISIVA")
                              escreval("--------------------------------------")
                              escreva("- Jogador1, fa�a sua jogada: ")
                              leia(J7)
                              escreva("- Jogador2, fa�a sua jogada: ")
                              leia(J8)
                              escreval("------------------------------")
                              escreval("RESULTADO DA RODADA DECISIVA:")
                              se (J7=J8) entao
                                 RR4 <- RR3
                                 RR_4 <- RR_3
                                 Jogador1 <- RR4
                                 Jogador2 <- RR_4
                                 escreval("Essa rodada foi um empate!")
                                 escreval("Placar Final:")
                                 escreval("Jogador1: ", RR4)
                                 escreval("Jogador2: ", RR_4)
                                 escreval("EMPATE GERAL!")
                              senao
                                   se (J7="PE") e (J8="TS") entao
                                      RR4 <- (RR3)+1
                                      RR_4 <- RR_3
                                      Jogador1 <- RR4
                                      Jogador2 <- RR_4
                                      escreval("Placar final:")
                                      escreval("Jogador1: ", Jogador1)
                                      escreval("Jogador2: ", Jogador2)
                                   senao
                                        se (J7="TS") e (J8="PE") entao
                                           RR4 <- RR3
                                           RR_4 <- (RR_3)+1
                                           Jogador1 <- RR4
                                           Jogador2 <- RR_4
                                           escreval("Placar final:")
                                           escreval("Jogador1: ", Jogador1)
                                           escreval("Jogador2: ", Jogador2)
                                        senao
                                             se (J7="PE") e (J8="PA") entao
                                                RR4 <- RR3
                                                RR_4 <- (RR_3)+1
                                                Jogador1 <- RR4
                                                Jogador2 <- RR_4
                                                escreval("Placar final:")
                                                escreval("Jogador1: ", Jogador1)
                                                escreval("Jogador2: ", Jogador2)
                                             senao
                                                  se (J7="PA") e (J8="PE") entao
                                                     RR4 <- (RR3)+1
                                                     RR_4 <- RR_3
                                                     Jogador1 <- RR4
                                                     Jogador2 <- RR_4
                                                     escreval("Placar final:")
                                                     escreval("Jogador1: ", Jogador1)
                                                     escreval("Jogador2: ", Jogador2)
                                                  senao
                                                       se (J7="PA") e (J8="TS") entao
                                                          RR4 <- RR3
                                                          RR_4 <- (RR_3)+1
                                                          Jogador1 <- RR4
                                                          Jogador2 <- RR_4
                                                          escreval("Placar final:")
                                                          escreval("Jogador1: ", Jogador1)
                                                          escreval("Jogador2: ", Jogador2)
                                                       senao
                                                            se (J7="TS") e (J8="PA") entao
                                                               RR4 <- (RR3)+1
                                                               RR_4 <- RR_3
                                                               Jogador1 <- RR4
                                                               Jogador2 <- RR_4
                                                               escreval("Placar final:")
                                                               escreval("Jogador1: ", Jogador1)
                                                               escreval("Jogador2: ", Jogador2)
                                                               fimse
                                                            fimse
                                                       fimse
                                                  fimse
                                             fimse
                                        fimse
                                   fimse
                           fimse
                      fimse
                 fimse
            fimse














FimAlgoritmo