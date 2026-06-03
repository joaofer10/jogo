personagem = {
    "nome": "JT",
    "hp_max": 100,
    "hp_atual": 100,

    "habilidades": {
        "cassetete": {
            "dano": 10,
            "tipo": "contudente",
        },  # <-- Adicionada a vírgula aqui
        "pistola": {
            "dano": 25,
            "mun_max": 12,
            "mun_atual": 12,
            "tipo": "perfurante",
        },
    },
}

bestiario = {
    "bot1": {
        "nome": "vítima 1",
        "hp_max": 75,
        "hp_atual": 75,
        "habilidades": {


        },
    }
}

print('Jogo teste\n')
print('Menu\n1-novo jogo \n2-carregar save \n3-sair')
menu = int(input('digite o numero da sua escolha\nR: '))


if menu == 1:
    nome = personagem["nome"]
    hp_max = personagem["hp_max"]
    hp_atual = personagem["hp_atual"]

    # while true:
    print('cutscene:')
    print(f'Você é {nome}, um detetive especializado em investigar assassinatos')
    print('Você chegou em casa cansado depois de anali diferentes relatorios de mortes estranhas ')
    print('antes que possa descansar, você recebe uma ligação dizendo que na rua XXXXXXXXX\nna casa de numero XXX foi encontrado dois corpos')
    print('----')
    print('chegando no local, ao chegar no local Rubert, um colega policial te espera, Rubert...')
    print('----')
    proximo_dialogo = input('digite () para continuar\nR: ')

    print('ato 0: inicio')
    print('----')
    print('(com um cigarro na boca e cara de cansado, Rubert diz)')
    print(f'Rubert: -boa noite, {nome}, como você está?')
    print(f'opções de respota:\n1-Boa noite Rubert, estou bem e você?\n2-vamos cortar as apresentações, cade os outros?\n3-que desperdicio de palavras')
    escolha = int(input(f'R: '))
    print('----')

    if escolha == 1:
        print('na medida do possivel sim')
        print('(ele apaga o cigarro depois de ter dado uma tragada)')
        proximo_dialogo = input('digite (p) para continuar\nR: ')
    elif escolha == 2:
        print('como sempre, priorizando a eficiencia')
        print('(ele apaga o cigarro depois de ter dado uma tragada)')
        proximo_dialogo = input('digite (p) para continuar\nR: ')
    elif escolha == 3:
        print('você sabe que ser assim não te deixa mais maneiro né?')
        print('isso parece fala de protagosnista de filmes ou jogos de policiais, é vergonhoso')
        print('(ele apaga o cigarro depois de ter dado uma tragada)')
        proximo_dialogo = input('digite (p) para continuar\nR: ')
    print('----')

    print('Bom os outros estão procurando o suspeito pelas redondezas')
    print('(ele tira do bolso uma chave)')
    print('eu tentei dar uma vasculhada no lugar,\nmas sendo sincero não consigo ficar muito tempo nessa casa')
    print('(ele joga a chave na sua direção e você pega)')
    proximo_dialogo = input('digite (p) para continuar\nR: ')
    print('não sei para você mas eu me sinto estranho quando participo de investigações assim')
    print('talvez eu tenha um estomago fraco')
    print('(ele começa a se afastar e ir )')
    proximo_dialogo = input('digite (p) para continuar\nR: ')

    while True:
        print('----')
        print('Você olha para a casa, ela é uma casa comum de dois andares,\nvocê consegue ver algumas luzes acesas pela janela')
        print('a cada segundo que você passa olhando essa casa mais estranha ela parece')
        print('como se um ar de decadencia e morte fosse algo presente nela')
        print(f'opções de escolha:\n1-estou pensando demais, vamos terminar logo isso...\n2-isso não vai dar bom...')
        escolha = int(input(f'R: '))

        if escolha == 1:
            print('você pega a chave da casa e entra')
            print('você passa pelos corredores até que você chega na sala de estar')
            print('logo é possivel perceber uma taça de vinho e suas taças em uma mesinha')
            print('mas o que mais chama atenção é a demarcação de um cadaver no chão e sangue')
            print('"lá vamos nos..."')
            investigação = 0

            while True:
                if investigação < 5:
                    print('ok onde devo olhar agora?')
                    print('')

                elif investigação == 5:
                    while hp_atual > 0:
                        print('combate')


                    






            

        elif escolha == 2:
            print('final 0')

        break


elif menu == 2:
    print('ainda em desenvolvimento(o desenvolvedor narigudo não veio)')
elif menu == 3:
    print('porque tu entrou no meu jogo se tu ia sair?\nainda sim, muito obrigado por ter perdido o seu tempo :)')
