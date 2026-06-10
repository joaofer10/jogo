import random

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

# Unificado conforme sua última versão de teste
bestiario = {
    "nome": "Vítima 1",
    "hp_max": 75,
    "hp_atual": 75,
    "habilidades": {
        1: {"ataque": "Apunhalar", "dano": 12},
        2: {"ataque": "Ecos da Escuridão", "dano": 17},
        3: {"ataque": "Cansaço", "dano": 0}
    },
    "fraqueza": "contudente"
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
# INTERFACE VISUAL (HUD)
# ==========================================

def exibir_barra_hp(nome, hp, hp_max):
    """Gera visualmente a barra de vida estilizada no console."""
    if hp < 0:
        hp = 0
    porcentagem = int((hp / hp_max) * 10)  # Calcula a proporção para 10 blocos
    barra = "█" * porcentagem + "░" * (10 - porcentagem)
    print(f"{nome}: [{barra}] {hp}/{hp_max}")


# ==========================================
# FUNÇÕES DO JOGO (SISTEMAS MODULARES)
# ==========================================

def mostrar_cutscene_inicial(nome_detetive):
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
    investigacao = 0
    pistas_importantes_encontradas = 0
    itens_do_ato = itens_investigacao[ato]

    while investigacao < 5:
        print(f'\n--- Progresso da Investigação: {investigacao}/5 itens vistos ---')
        print('Onde você deseja olhar agora?')
        
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
    print('\n' + '!' * 50)
    print('De repente, a porta da sala bate com força atrás de você!')
    print('A temperatura cai drasticamente e as luzes começam a piscar freneticamente.')
    print(f'O espírito da {bestiario["nome"]} se materializa diante dos seus olhos!')
    
    if pistas_encontradas >= 4:
        print("\n[BÔNUS DE LORE] Como você descobriu quase toda a história do crime,")
        print("você compreende a dor do espírito e não é pego de surpresa!")
    else:
        print("\n[ALERTA] Você não descobriu pistas cruciais sobre o crime.")
        print("O espírito avança furioso e descontrolado!")
    print('!' * 50 + '\n')

    input('[Aperte Enter para iniciar o COMBATE]')

    # Sincronizando variáveis locais com os dicionários globais
    nome_player = personagem["nome"]
    hp_player = personagem["hp_atual"]
    hp_max_player = personagem["hp_max"]
    
    inimigo_nome = bestiario["nome"]
    inimigo_hp = bestiario["hp_atual"]
    inimigo_hp_max = bestiario["hp_max"]

    while hp_player > 0 and inimigo_hp > 0:
        print(f'\n========================================')
        exibir_barra_hp(nome_player, hp_player, hp_max_player)
        exibir_barra_hp(inimigo_nome, inimigo_hp, inimigo_hp_max)
        print(f'Munição Pistola: {personagem["habilidades"]["pistola"]["mun_atual"]}/{personagem["habilidades"]["pistola"]["mun_max"]}')
        print('========================================')
        
        print("Comandos: [a] ATACAR | [d] DEFENDER | [f] FUGIR")
        comando = input("⬆️ Digite um dos comandos acima ⬆️: ").strip().lower()
        
        if comando in ["a", "atacar", "ataca"]:
            acao = "a"
        elif comando in ["d", "defender", "defende", "defesa"]:
            acao = "d"
        elif comando in ["f", "fuga", "fugir"]:
            acao = "f"
        else:
            print("\n[!] Comando inválido! Você hesitou e perdeu o foco.")
            acao = "invalido"

        match acao:
            case "a":
                print(f"\nOpções: [pistola] para disparo rápido | [cassetete] para golpes contundentes")
                escolha = input("Escolha sua habilidade R: ").strip().lower()
                
                dano_causado = 0
                ataque_valido = False

                match escolha:
                    case "pistola":
                        if personagem["habilidades"]["pistola"]["mun_atual"] > 0:
                            personagem["habilidades"]["pistola"]["mun_atual"] -= 1
                            dano_causado = personagem["habilidades"]["pistola"]["dano"]
                            ataque_valido = True
                            print("\n💥 BANG! Você disparou contra o espírito.")
                            
                            if bestiario["fraqueza"] == "perfurante":
                                dano_causado *= 2
                                print("🔥 GOLPE CRÍTICO! O dano perfurante perfura a névoa espiritual!")
                        else:
                            print("\n⚠️ CLIQUE! A pistola está sem munição!")
                            
                    case "cassetete":
                        dano_causado = personagem["habilidades"]["cassetete"]["dano"]
                        ataque_valido = True
                        print("\n💥 TROW! Você desferiu um golpe de cassetete.")
                        
                        if bestiario["fraqueza"] == "contudente":
                            dano_causado *= 2
                            print("🔥 GOLPE CRÍTICO! O impacto quebra a barreira de ectoplasma!")
                    case _:
                        print("\n[!] Arma inválida! Você atacou no vento.")

                if ataque_valido:
                    inimigo_hp -= dano_causado
                    print(f"Você causou {dano_causado} de dano ao espírito.")

                # Turno de Contra-Ataque do Espírito (se ele ainda estiver vivo)
                if inimigo_hp > 0:
                    r = random.randint(1, 3)
                    ataque_inimigo = bestiario["habilidades"][r]
                    hp_player -= ataque_inimigo["dano"]
                    print(f"\n👻 {inimigo_nome} revidou com [{ataque_inimigo['ataque']}] causando {ataque_inimigo['dano']} de dano!")
                
            case "d": 
                # Defesa: reduz o dano do ataque sorteado pela metade
                r = random.randint(1, 3)
                ataque_inimigo = bestiario["habilidades"][r]
                dano_reduzido = int(ataque_inimigo["dano"] * 0.5)
                hp_player -= dano_reduzido

                print(f"\n🛡️ Você se protegeu! [{ataque_inimigo['ataque']}] causaria {ataque_inimigo['dano']}, mas você sofreu apenas {dano_reduzido}!")

            case "f":
                # Fuga falha: toma o dano total do ataque sorteado
                r = random.randint(1, 3)
                ataque_inimigo = bestiario["habilidades"][r]
                hp_player -= ataque_inimigo["dano"]

                print(f"\n🏃‍♂️ Você tentou correr para a saída, mas as portas estão trancadas!")
                print(f"👻 O espírito te pegou pelas costas com [{ataque_inimigo['ataque']}] causando {ataque_inimigo['dano']} de dano!")
                print("Você falhou ao fugir!")

    # --- VERIFICAÇÃO DE FINAL DE COMBATE ---
    print('\n========================================')
    if hp_player <= 0:
        print("💀 Seu HP chegou a 0. A frieza da morte toma sua consciência...")
        print("=== GAME OVER ===")
    elif inimigo_hp <= 0:
        print(f"✨ O espírito da {inimigo_nome} solta um último suspiro e se dissipa no ar...")
        print("A sala volta a ficar silenciosa. O Ato 1 foi superado!")
        print("=== VITÓRIA ===")
    print('========================================')


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
    mostrar_cutscene_inicial(personagem["nome"])
    
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
            
            pistas_chave = iniciar_investigacao("ato1")
            iniciar_combate(pistas_chave)
            break
            
        elif escolha == 2:
            print('\nVocê decide que sua vida vale mais do que esse salário. Você dá meia volta e entra no carro.')
            print('=== FINAL 0: Prudência ou Covardia? ===')
            break

elif menu == 2:
    print('\nAinda em desenvolvimento (o desenvolvedor narigudo não veio).')
elif menu == 3:
    print('\nPorque tu entrou no meu jogo se tu ia sair?\nAinda sim, muito obrigado por ter perdido o seu tempo :)')