# ==========================================
# CONFIGURAÇÕES DE DADOS (ESTADO DO JOGO)
# ==========================================

personagem = {
    "nome": "JT",
    "hp_max": 100,
    "hp_atual": 100,
    "habilidades": {
        "cassetete": {
            "dano": 10,
            "tipo": "contudente",
        },  
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
        "nome": "vitima 1",
        "hp_max": 75,
        "hp_atual": 75,
        "habilidades": {
            "facada": {
                "dano": 10,
                "tipo": "cortante"
            },
            "grito ensurdecedor": {
                "dano": 25,
                "tipo": "trovejante"
            },
            "ataque inutil": {
                "descricao": "O espírito vacila no tempo, flutuando sem reação por um instante.",
            },
        },
        "resistencias": {
            "cortante": True
        },
    }
}

itens_investigacao = {
    "ato1": {
        1: {
            "nome": "faca ensanguentada",
            "lore": "Depois de revirar o sofá inteiro é possível encontrar uma faca com sangue seco, talvez tenha sido a arma do crime.",
            "importante": True,
            "visto": False,
        },
        2: {
            "nome": "vinho na mesa",
            "lore": "As vítimas conheciam o assassino e estavam tomando o vinho junto com ele ou o assassino entrou e acabou encontrando ambos?",
            "importante": True,
            "visto": False,
        },
        3: {
            "nome": "foto rasgada",
            "lore": "Uma foto de um casal, o rosto masculino da foto está rasgado.",
            "importante": False,
            "visto": False,
        },
        4: {
            "nome": "papeis amassados",
            "lore": "Dou uma olhada na lata de lixo, e encontro alguns papéis amassados. Um sendo pedido de divórcio e outro sendo uma carta pelo que parece, nela tá escrito repetidas vezes ME DESCULPA.",
            "importante": True,
            "visto": False,
        },
        5: {
            "nome": "anel de casamento",
            "lore": "Um anel de casamento... Isso é da vítima ou do assassino?",
            "importante": True,
            "visto": False,
        },
        6: {
            "nome": "relogio quebrado",
            "lore": "O relógio está quebrado no chão, nele marca 22:53.",
            "importante": True,
            "visto": False,
        },
    }
}


# ==========================================
# FUNÇÕES DO JOGO (SISTEMAS MODULARES)
# ==========================================

def mostrar_cutscene_inicial(nome_detetive):
    """Gerencia a introdução e o diálogo com Rubert."""
    print('\n--- CUTSCENE ---')
    print(f'Você é {nome_detetive}, um detetive especializado em investigar assassinatos.')
    print('Você chegou em casa cansado depois de analisar diferentes relatórios de mortes estranhas.')
    print('Antes que possa descansar, você recebe uma ligação dizendo que na rua XXXXXXXXX\nna casa de número XXX foram encontrados dois corpos.')
    print('----')
    print('Chegando no local, o policial Rubert, seu colega, te espera...')
    print('----')
    input('Digite qualquer tecla para continuar... ')

    print('\nATO 0: INÍCIO')
    print('----')
    print('(Com um cigarro na boca e cara de cansado, Rubert diz)')
    print(f'Rubert: - Boa noite, {nome_detetive}, como você está?')
    print('\nOpções de resposta:\n1 - Boa noite Rubert, estou bem e você?\n2 - Vamos cortar as apresentações, cadê os outros?\n3 - Que desperdício de palavras.')
    
    try:
        escolha = int(input(f'R: '))
    except ValueError:
        escolha = 1

    print('----')
    if escolha == 1:
        print('Rubert: - Na medida do possível sim.')
    elif escolha == 2:
        print('Rubert: - Como sempre, priorizando a eficiência...')
    else:
        print('Rubert: - Você sabe que ser assim não te deixa mais maneiro, né?\nIsso parece fala de protagonista de filmes ou jogos de policiais, é vergonhoso.')
    
    print('(Ele apaga o cigarro depois de ter dado uma tragada)')
    input('Digite qualquer tecla para continuar... ')
    print('----')

    print('Rubert: - Bom, os outros estão procurando o suspeito pelas redondezas.')
    print('(Ele tira do bolso uma chave)')
    print('Rubert: - Eu tentei dar uma vasculhada no lugar, mas sendo sincero não consigo ficar muito tempo nessa casa.')
    print('(Ele joga a chave na sua direção e você pega)')
    input('Digite qualquer tecla para continuar... ')
    print('Rubert: - Não sei para você, mas eu me sinto estranho quando participo de investigações assim.\nTalvez eu tenha um estômago fraco.')
    print('(Ele começa a se afastar e vai embora)')
    input('Digite qualquer tecla para continuar... ')


def iniciar_investigacao(ato):
    """Gerencia o loop de busca de pistas e retorna a quantidade de pistas importantes vistas."""
    investigacao = 0
    pistas_importantes_encontradas = 0
    itens_do_ato = itens_investigacao[ato]

    while investigacao < 5:
        print(f'\n--- Progresso da Investigação: {investigacao}/5 itens vistos ---')
        print('Onde você deseja olhar agora?')
        
        # Mostra o menu de pistas dinâmico
        for id_item, info in itens_do_ato.items():
            if not info["visto"]:
                print(f"{id_item} - Analisar {info['nome']}")
            else:
                print(f"[{id_item} - {info['nome']} (Já investigado)]")

        try:
            escolha_item = int(input('\nR: '))
            
            if escolha_item in itens_do_ato:
                if not itens_do_ato[escolha_item]["visto"]:
                    itens_do_ato[escolha_item]["visto"] = True
                    investigacao += 1
                    
                    print("\n========================================")
                    print(f"🔎 {itens_do_ato[escolha_item]['nome'].upper()}:")
                    print(itens_do_ato[escolha_item]["lore"])
                    print("========================================")
                    
                    if itens_do_ato[escolha_item]["importante"]:
                        pistas_importantes_encontradas += 1
                        
                    input('\n[Aperte Enter para continuar]')
                else:
                    print('\n[!] Você já revirou esse lugar. Escolha outro ponto de interesse!')
            else:
                print('\n[!] Esse ponto não parece relevante. Escolha um número da lista.')
                
        except ValueError:
            print('\n[!] Digite apenas o número correspondente ao item.')
            
    return pistas_importantes_encontradas


def iniciar_combate(pistas_encontradas):
    """Gerencia a batalha por turnos entre o detetive e o espírito."""
    print('\n' + '!' * 50)
    print('De repente, a porta da sala bate com força atrás de você!')
    print('A temperatura cai drasticamente e as luzes começam a piscar freneticamente.')
    print('O espírito da Vítima 1 se materializa diante dos seus olhos!')
    
    # Exemplo de utilidade para o seu sistema de "itens importantes"
    if pistas_encontradas >= 4:
        print("\n[BÔNUS DE LORE] Como você descobriu quase toda a história do crime,")
        print("você compreende a dor do espírito e não é pego de surpresa!")
    else:
        print("\n[ALERTA] Você não descobriu pistas cruciais sobre o crime.")
        print("O espírito avança furioso e descontrolado!")
    print('!' * 50 + '\n')

    input('[Aperte Enter para iniciar o COMBATE]')

    # Variáveis locais para controlar a vida durante a batalha
    hp_player = personagem["hp_atual"]
    inimigo_hp = bestiario["bot1"]["hp_atual"]
    inimigo_nome = bestiario["bot1"]["nome"]

    while hp_player > 0 and inimigo_hp > 0:
        print(f'\n=== TURNO DE COMBATE ===')
        print(f'Detetive {personagem["nome"]} | HP: {hp_player}/{personagem["hp_max"]}')
        print(f'{inimigo_nome} | HP: {inimigo_hp}/{bestiario["bot1"]["hp_max"]}')
        print('------------------------')
        print('Escolha sua ação:')
        print('1 - Atacar com Cassetete (Dano: 10 | Tipo: Contundente)')
        print(f'2 - Atirar com Pistola (Dano: 25 | Mun: {personagem["habilidades"]["pistola"]["mun_atual"]}/{personagem["habilidades"]["pistola"]["mun_max"]})')
        
        # O Combate acontecerá aqui! Por enquanto, um break para o código rodar sem travar.
        print("\n[Sistema de combate pronto para ser programado no próximo passo!]")
        break


# ==========================================
# FLUXO PRINCIPAL DO PROGRAMA
# ==========================================

print('Jogo Teste\n')
print('Menu\n1 - Novo Jogo \n2 - Carregar Save \n3 - Sair')

try:
    menu = int(input('Digite o número da sua escolha\nR: '))
except ValueError:
    menu = 3

if menu == 1:
    # 1. Executa a Introdução
    mostrar_cutscene_inicial(personagem["nome"])
    
    # 2. Entrada na Casa (Loop de Decisão de Entrada)
    while True:
        print('\n----')
        print('Você olha para a casa. Ela é uma casa comum de dois andares,\nvocê consegue ver algumas luzes acesas pela janela.')
        print('A cada segundo que você passa olhando essa casa, mais estranha ela parece,')
        print('como se um ar de decadência e morte estivesse presente nela.')
        print(f'\nOpções de escolha:\n1 - Estou pensando demais, vamos terminar logo isso...\n2 - Isso não vai dar bom... (Desistir)')
        
        try:
            escolha = int(input(f'R: '))
        except ValueError:
            escolha = 1

        if escolha == 1:
            print('\nVocê pega a chave da casa e entra.')
            print('Você passa pelos corredores até que chega na sala de estar.')
            print('Logo é possível perceber uma taça de vinho e suas taças em uma mesinha,')
            print('mas o que mais chama atenção é a demarcação de um cadáver no chão e sangue.')
            print('"Lá vamos nós..."')
            
            # 3. Chama o sistema modular de investigação
            pistas_chave = iniciar_investigacao("ato1")
            
            # 4. Vai direto para o combate ao terminar de coletar 5 pistas
            iniciar_combate(pistas_chave)
            break
            
        elif escolha == 2:
            print('\nVocê decide que sua vida vale mais do que esse salário. Você dá meia volta e entra no carro.')
            print('=== FINAL 0: Prudência ou Covardia? ===')
            break

elif menu == 2:
    print('\nAinda em desenvolvimento (o desenvolvedor narigudo não veio).')
elif menu == 3:
    print('\nPor que tu entrou no meu jogo se tu ia sair?\nAinda assim, muito obrigado por ter perdido o seu tempo :)')