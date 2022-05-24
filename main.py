# -- coding: utf-8 --
#Inicio da Aplicação

#Pre declaracao de variaveis
respostaElevada = 9.9
respostaSim = 7
respostaNao = 0
loop = str("s")

#lista
questions = [
                "\n01 - Você tem febre? (N = Não, S = Sim igual ou maior que 37º, E = Elevada maior que 38º",
                "\n02 - Você tem tosse seca? (N = Não, S = Sim de forma moderada, E = Elevada persistente",
                "\n03 - Você tem cansaço? (N= Não, S= Sim de forma moderada, E= Elevada)",
                "\n04 - Você tem dores musculares? (N= Não, S= Sim de forma moderada, E= Elevada)",
                "\n05 - Você tem dor de garganta? (N= Não, S= Sim de forma moderada, E= Elevada)",
                "\n06 - Você teve diarréia? (N= Não, S= Sim de forma moderada, E= Elevada)",
                "\n07 - Você teve perda de paladar? (N= Não, S= Sim de forma moderada, E= Elevada)",
                "\n08 - Você teve dor de cabeça? (N= Não, S= Sim de forma moderada, E= Elevada)",
                "\n09 - Você teve perda de apetite? (N= Não, S= Sim de forma moderada, E= Elevada)",
                "\n10 - Você teve dificuldade de respirar ou falta de ar? (N= Não, S= Sim de forma moderada, E= Elevada)"
            ]

#Inicia o sistema 
while (loop != 'n'):

    #zera a probabilidade
    probabilidade = 0

    #Menu Inicial
    print("\n******* Triagem Covid-19 *******")
    nome = input("\nDigite seu nome: ")

    for i in questions:
        resposta = "x"
        while(resposta != 'n' and resposta !='s' and resposta !='e'):        
            print(i)
            resposta = input("\nDigite sua resposta (N, S ou E): ")
            if resposta == 'n':
                 probabilidade = probabilidade + respostaNao
            elif resposta == 's':
                 probabilidade = probabilidade + respostaSim
            elif resposta == 'e':
                 probabilidade = probabilidade + respostaElevada

    #Imprimir o resultado da probabilidade
    print("\nSua probabilidade de estar com COVID-19 é: ", round(probabilidade,2))

    if probabilidade > 60:
        print("\nAlerta sua probabilidade de estar infectado é muito alta, deve procurar consultar com um médico.")
    else:
        print("\nA probabilidade de estar infectado é baixa, mas não esqueça de tomar os devidos cuidados")

    #Solicita se o usuario quer refazer o teste
    print("\nDeseja refazer o teste? (S/N):")
    loop = str(input("\nDigite sua resposta (S ou N): "))