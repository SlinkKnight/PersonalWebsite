import os
import time

pontuacao = 0
question = 0


def getquestions(qst, pontuacao):

    if qst == 0:
        os.system("cls")

        print("O pensamento iluminista é 'dividido' em 3 partes fundamentais, sendo elas... \n\n \n1- capitalismo, a importância de meios monetários e sociais      \n2- razão, pensamento lógico e social,     \n3- razão, liberdade e o avanço da sociedade")
        r1 = input("\n >>> ") 

        if r1 == "3":
            pontuacao = +1
            qst =+ 1
            print("parabêns você acertou, proxima pergunta!")
            time.sleep(2)
        else:
            print(f"\ninfelizmente sua resposta esta incorreta, sua pontuação é de {pontuacao} pontos")
            time.sleep(10)
    if qst == 1:
       os.system("cls")
        
       print("uma das maiores contribuição do iluminismo foi os três poderes, que são... \n\n \n1- executivo, legislativo e judiciário      \n2- clero, burguesia e nobreza     \n3- mãe, pai e filho")
       r1 = input("\n >>> ") 

       if r1 == "1":
            pontuacao = +1
            qst =+ 1
            print("parabêns você acertou, proxima pergunta!")
            time.sleep(2)
       else:
            print(f"\ninfelizmente sua resposta esta incorreta, sua pontuação é de {pontuacao} pontos")
            time.sleep(10) 
    if qst == 2:
        os.system("cls")

        print("o iluminismo surgiu no... na... \n\n \n1- século 18, noruega      \n2- século 20, frança     \n3- século 18 frança")
        r1 = input("\n >>> ") 

        if r1 == "3":
            pontuacao = +1
            qst =+ 1
            print("parabêns você acertou, proxima pergunta!")
            time.sleep(2)
        else:
            print(f"\ninfelizmente sua resposta esta incorreta, sua pontuação é de {pontuacao} pontos")
            time.sleep(10)
    if qst == 3:


        os.system("cls")

        print("os pensadores iluministas buscavam... \n\n \n1- defender o uso da razão e fé para entender e solucionar os problemas da sociedade      \n2- filosofar sobre como a sociedade era ruim,     \n3- entender os meios religiosos, pois queriam virar padres")
        r1 = input("\n >>> ") 

        if r1 == "1":
            pontuacao = +1
            qst =+ 1
            print("parabêns você acertou, proxima pergunta!")
            time.sleep(2)
        else:
            print(f"\ninfelizmente sua resposta esta incorreta, sua pontuação é de {pontuacao} pontos")
            time.sleep(10)
    if qst == 4:
        os.system("cls")

        print("sobre jonh locke é correto afirmar que... \n\n \n1- conhecimento era proveniencia das expêriencias das pessoas      \n2- nasceu em 1500,     \n3- provou que a gravidade era apenas uma mecânica do universo")
        r1 = input("\n >>> ") 

        if r1 == "1":
            pontuacao = +1
            qst =+ 1
            print("parabêns você acertou, proxima pergunta!")
            time.sleep(2)
        else:
            print(f"\ninfelizmente sua resposta esta incorreta, sua pontuação é de {pontuacao} pontos")
            time.sleep(10)
    if qst == 5:
        os.system("cls")

        print("eles... \n\n \n1- gostavam do sistema da época      \n2- criticavam o sistema da época,     \n3- não conheciam muito bem o sistema absolutista, portanto, não davam opinião sobre o mesmo")
        r1 = input("\n >>> ") 

        if r1 == "3":
            pontuacao = +1
            print(f"parabêns você acertou a ultima questão!, sua pontuação foi de {pontuacao}!")
            time.sleep(100000000)
        else:
            print(f"\ninfelizmente sua resposta esta incorreta, sua pontuação é de {pontuacao} pontos")
            time.sleep(10)

os.system('title quiz sobre o iluminismo')
os.system('color 3')

print("\n\n\n\n\n\n\n\n\n\n                                                     quiz de história")
print("\n\n\n                   1. começar                                                             2. sair")

r = input("\n\n\n >> ")

if r == "1":
        time.sleep(0.5)
        getquestions(question, pontuacao)
else:
    os.system("exit")
