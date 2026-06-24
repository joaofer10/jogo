import random

# ==========================================
# CONFIGURAÇÕES DE DADOS (ESTADO DO JOGO)
# ==========================================

personagem = {
    "nome": "JT",
    "hp_max": 100,
    "hp_atual": 100,
    "inventario": [],  
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
    1: {
        "id": 1,
        "nome": "mulher (O Espírito Desolado)",
        "hp_max": 75,
        "hp_atual": 75,
        "habilidades": {
            1: {"ataque": "apunhalar", "dano": 12},
            2: {"ataque": "Ecos da Escuridão", "dano": 17},
            3: {"ataque": "Cansaço", "dano": 0}
        },
        "fraqueza": "contudente",
        "drop": None
    },
    2: {
        "id": 2,
        "nome": "amante (Espírito Furioso)",
        "hp_max": 55,  
        "hp_atual": 55,
        "habilidades": {
            1: {"ataque": "gancho", "dano": 20},
            2: {"ataque": "dilacerar", "dano": 25},
            3: {"ataque": "ansioso", "dano": 0} 
        },
        "fraqueza": "perfurante",
        "drop": "Chave do Porão"  
    },
    3: {
        "id": 3,
        "nome": "marido (O Monstro Final)",
        "hp_max": 150,
        "hp_atual": 150,
        "habilidades": {
            1: {"ataque": "cuspe de veneno", "dano": 22},
            2: {"ataque": "arranhão venenoso", "dano": 30},
        },
        "fraqueza": None,
        "drop": "Dossiê do Caso Encerrado"
    }
}

itens_investigacao = {
    "ato1": {
        1: {"nome": "faca ensanguentada", "lore": "Depois de revirar o sofá inteiro é possível encontrar uma faca com sangue seco, talvez tenha sido a arma do crime.", "importante": True, "visto": False},
        2: {"nome": "vinho na mesa", "lore": "As vítimas conheciam o assassino e estavam tomando o vinho junto com ele ou o assassino entrou e acabou encontrando ambos?", "importante": True, "visto": False},
        3: {"nome": "foto rasgada", "lore": "Uma foto de um casal, o rosto masculino da foto está rasgado.", "importante": False, "visto": False},
        4: {"nome": "papeis amassados", "lore": "Dou uma olhada na lata de lixo, e encontro alguns papéis amassados. Um sendo pedido de divórcio e outro sendo uma carta pelo que parece, nela tá escrito repetidas vezes ME DESCULPA.", "importante": True, "visto": False},
        5: {"nome": "anel de casamento", "lore": "Um anel de casamento... Isso é da vítima ou do assassino?", "importante": True, "visto": False},
        6: {"nome": "relogio quebrado", "lore": "O relógio está quebrado no chão, nele marca 22:53.", "importante": True, "visto": False}
    },
    "ato2": {
        1: {"nome": "quadro de casal destruído", "lore": "O quadro que decorava o corredor foi arrancado e jogado na parede. O vidro está estilhaçado e a foto do marido foi violentamente riscada com algo afiado.", "importante": True, "visto": False},
        2: {"nome": "bilhete amoroso rasgado", "lore": "Pedaços de papel no chão do corredor formam uma carta de amor secreta: 'Mal posso esperar para quando ele não estiver em casa...'", "importante": True, "visto": False},
        3: {"nome": "marcas de arrastamento", "lore": "Marcas escuras no piso do corredor indicam que um corpo pesado foi arrastado em direção à porta trancada do porão.", "importante": True, "visto": False},
        4: {"nome": "lamparina quebrada", "lore": "Uma fonte de luz despedaçada no chão. O óleo derramado ainda cheira forte, indicando um confronto físico recente e desesperado no corredor.", "importante": False, "visto": False}
    },
    "ato3": { 
        1: {
            "nome": "frasco de veneno de rato vazio", 
            "lore": "Um frasco de veneno jogado perto do altar. O Marido ingeriu o conteúdo em seus últimos momentos, tentando cometer suicídio para fugir da polícia após o duplo homicídio. O veneno agora corre em suas veias espirituais.", 
            "importante": True, 
            "visto": False
        },
        2: {
            "nome": "altar do ritual fracassado", 
            "lore": "Um cadáver mutilado serve de oferenda no centro de um círculo místico. Notas rabiscadas no chão mostram que o Marido tentou um ritual de ressurreição ou barganha que deu 'errado'... Em vez de salvação, sua alma foi distorcida pelo puro rancor.", 
            "importante": True, 
            "visto": False
        },
        3: {
            "nome": "cartas de desespero e rancor", 
            "lore": "Páginas manchadas de vômito e sangue revelam os últimos pensamentos dele: 'O ritual não funcionou, eles ainda estão mortos e eu estou queimando por dentro...'. O veneno o matou, mas o rancor o trouxe de volta como algo pior.", 
            "importante": True, 
            "visto": False
        }
    }
}

# ==========================================
# INTERFACE VISUAL (HUD)
# ==========================================

def exibir_barra_hp(nome, hp, hp_max):
    if hp < 0: hp = 0
    porcentagem = int((hp / hp_max) * 10)  
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
        
        # Define o limite dinamicamente por ato
        limite = 3 if ato in ["ato2", "ato3"] else 5

        while investigacao < limite:
            print(f'\n--- Progresso da Investigação: {investigacao}/{limite} itens vistos ---')
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

def combate(dados_monstro):
    nome_player = personagem["nome"]
    pistola = personagem["habilidades"]["pistola"]
    cassetete = personagem["habilidades"]["cassetete"]
    
    print(f"\n💥 O combate contra {dados_monstro['nome'].upper()} começou!")
    
    while personagem["hp_atual"] > 0 and dados_monstro["hp_atual"] > 0: 
        print("\n" + "="*40)
        exibir_barra_hp(nome_player, personagem["hp_atual"], personagem["hp_max"])
        exibir_barra_hp(dados_monstro["nome"], dados_monstro["hp_atual"], dados_monstro["hp_max"])
        print(f"Munição da Pistola: {pistola['mun_atual']}/{pistola['mun_max']}")
        print("="*40)
        
        print("Comandos: [a] ATACAR | [d] DEFENDER | [f] FUGIR")
        comando = input("⬆️ Digite um dos comandos acima: ").strip().lower()
        
        if comando in ["a", "atacar", "ataca"]:
            acao = "a"
        elif comando in ["d", "defender", "defesa"]:
            acao = "d"
        elif comando in ["f", "fuga", "fugir"]:
            acao = "f"
        else:
            acao = "invalido"

        match acao:
            case "a":
                print(f"\nOpções: [pistola] (Dano: {pistola['dano']}) | [cassetete] (Dano: {cassetete['dano']})")
                escolha = input("Escolha sua habilidade: ").strip().lower()
                
                dano_causado = 0
                ataque_valido = False
                
                if escolha == "pistola":
                    if  pistola["mun_atual"] > 0:
                        pistola["mun_atual"] -= 1 
                        dano_causado = pistola["dano"]
                        ataque_valido = True
                        print("\n💥 BANG! Você disparou contra o espírito.")
                        if dados_monstro.get("fraqueza") == "perfurante":
                            dano_causado *= 2
                            print("🔥 CRÍTICO! O dano perfurante perfura a névoa!")
                    else:
                        print("\n⚠️ CLIQUE! A pistola está sem munição!")
                        
                elif escolha == "cassetete":
                    dano_causado = cassetete["dano"]
                    ataque_valido = True
                    print("\n🏏 TROW! Você desferiu um golpe físico.")
                    if dados_monstro.get("fraqueza") == "contudente":
                        dano_causado *= 2
                        print("🔥 CRÍTICO! O impacto esmaga a barreira ectoplásmica!")
                else:
                    print("\n[!] Comando inválido! Você atacou o vento.")
                
                if ataque_valido:
                    dados_monstro["hp_atual"] -= dano_causado
                
                if dados_monstro["hp_atual"] > 0:
                    qtd_habilidades = len(dados_monstro["habilidades"])
                    r = random.randint(1, qtd_habilidades)
                    ataque_inimigo = dados_monstro["habilidades"][r]
                    personagem["hp_atual"] -= ataque_inimigo["dano"]
                    print(f"👻 {dados_monstro['nome']} contra-atacou com [{ataque_inimigo['ataque']}] causando {ataque_inimigo['dano']} de dano!")

            case "d": 
                qtd_habilidades = len(dados_monstro["habilidades"])
                r = random.randint(1, qtd_habilidades)
                ataque_inimigo = dados_monstro["habilidades"][r]
                dano_reduzido = int(ataque_inimigo["dano"] * 0.5)
                personagem["hp_atual"] -= dano_reduzido
                
                print(f"\n🛡️ Você se protegeu! O inimigo usou [{ataque_inimigo['ataque']}].")
                print(f"Em vez de {ataque_inimigo['dano']}, você sofreu apenas {dano_reduzido} de dano.")

            case "f":
                qtd_habilidades = len(dados_monstro["habilidades"])
                r = random.randint(1, qtd_habilidades)
                ataque_inimigo = dados_monstro["habilidades"][r]
                personagem["hp_atual"] -= ataque_inimigo["dano"]
                print(f"\n🏃‍♂️ Você falhou ao fugir! As portas estão seladas!")
                print(f"👻 O espírito te atingiu pelas costas com [{ataque_inimigo['ataque']}] causando {ataque_inimigo['dano']} de dano.")
            
            case _:
                print("\n[!] Você hesitou e perdeu o turno!")

        if dados_monstro["id"] == 3 and dados_monstro["hp_atual"] <= dados_monstro["hp_max"] * 0.5 and dados_monstro["hp_atual"] > 0:
            print("\n🚨 O MARIDO ENTRA EM FÚRIA! Seus ataques parecem mais rápidos!")

    if personagem["hp_atual"] <= 0:
        print("\n💀 FIM DE JOGO. A escuridão te consumiu...")
        return False
    else:
        print(f"\n✨ Você derrotou {dados_monstro['nome']}!")
        if dados_monstro["drop"]:
            item_dropado = dados_monstro["drop"]
            personagem["inventario"].append(item_dropado)
            print(f"🔑 [DROP DE ITEM] O espírito se desfez e deixou cair: {item_dropado.upper()}!")
            print(f"Inventário Atual: {personagem['inventario']}")
        return True

def manifestacao_sobrenatural(pistas, ato):
    
    # Define o total de pistas possíveis baseado no ato
    total_pistas = 3 if ato in ["ato2", "ato3"] else 5
    
    print("\n🔮 [SINTONIA SOBRENATURAL]")
    print("Ao desvendar os segredos do ambiente, uma energia gélida ecoa pela sala...")
    
    # CASO 1: Investigação Perfeita (100% das pistas importantes encontradas)
    if pistas == total_pistas:
        print("\n👁️ LAMPEJO DE LUCIDEZ: Sua mente se conecta perfeitamente ao passado!")
        print("Uma névoa densa espanta o cansaço do seu corpo e materializa o impossível:")
        print("-> [RESTAURAÇÃO]: Seu HP foi completamente regenerado pelo vigor espiritual!")
        print("-> [MATERIALIZAÇÃO]: Duas balas de éter surgem no tambor da sua pistola! (+2 Munição)")
        
        personagem["hp_atual"] = personagem["hp_max"]
        personagem["habilidades"]["pistola"]["mun_atual"] = min(
            personagem["habilidades"]["pistola"]["mun_atual"] + 2, 
            personagem["habilidades"]["pistola"]["mun_max"]
        )

    # CASO 2: Investigação Parcial (Achou pelo menos metade das pistas importantes)
    elif pistas >= (total_pistas / 2):
        print("\n👻 ECO DOS MORTOS: O ambiente sussurra fragmentos da verdade.")
        print("A compreensão parcial dos fatos estabiliza sua sanidade e fecha suas feridas leves.")
        print("-> [CONFORTO MÓRBIDO]: Você absorve a energia do local, recuperando 30 de HP.")
        
        personagem["hp_atual"] = min(personagem["hp_atual"] + 30, personagem["hp_max"])
        
    # CASO 3: Investigação Ruim (Ignorou as pistas)
    else:
        print("\n🖤 O HORROR TE SUFOCA: Você ignorou os detalhes cruciais do ambiente...")
        print("A ignorância deixa sua mente exposta ao medo. O ar parece mais pesado e hostil.")
        print("-> [SUSSURROS ANGOSTIANTES]: Nada acontece. Um calafrio corta sua espinha.")
        
    input('\n[Aperte Enter para encarar o espírito...]')

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
        
        # --- EXECUÇÃO DO ATO 1 ---
        pistas_ato1 = iniciar_investigacao("ato1")
        
        # <<< MUDANÇA AQUI: Inserir a manifestação antes do combate >>>
        manifestacao_sobrenatural(pistas_ato1, "ato1")
        
        vitoria_ato1 = combate(bestiario[1])
        
        if not vitoria_ato1:
            break

        # --- TRANSIÇÃO PARA O ATO 2 ---
        print('\n' + '='*60)
        print('           ATO 2: PUNHOS FECHADOS')
        print('='*60)
        print('O silêncio retorna à sala de estar, mas a atmosfera fica ainda mais pesada.')
        print('Ao avançar pelo corredor estreito que conecta a casa, o ar gela instantaneamente.')
        print('No chão, outra demarcação de cadáver em giz revela que a violência continuou aqui.')
        print('Você limpa o suor do rosto, saca sua arma e se prepara para o pior... ')
        input('\n[Investigar corredor...]')
        
        # --- EXECUÇÃO DO ATO 2 ---
        pistas_ato2 = iniciar_investigacao("ato2")
        
        # <<< MUDANÇA AQUI: Inserir a manifestação antes do combate >>>
        manifestacao_sobrenatural(pistas_ato2, "ato2")
        
        vitoria_ato2 = combate(bestiario[2])
        
        if not vitoria_ato2:
            break
        # --- TRANSIÇÃO PARA O ATO 3 (O PORÃO) ---
        print('\nVocê ouve um estalo vindo de uma porta pesada no fim do corredor...')
        print('É a entrada do porão. Está trancada por correntes pesadas.')
        
        # Verifica se o jogador derrotou o amante e pegou a chave
        if "Chave do Porão" in personagem["inventario"]:
            print("\n[!] Você usa a CHAVE DO PORÃO deixada pelo espírito do Amante.")
            print("As correntes caem com um estrondo metálico. O cheiro de podridão e produtos químicos invade suas narinas.")
            input('\n[Girar a maçaneta e descer os degraus...]')
        else:
            print("\nA porta está trancada magneticamente por forças ocultas e você não tem a chave. Fim da linha.")
            break
            
        print('\n' + '='*60)
        print('           ATO 3: O RITUAL DA AGONIA (O PORÃO)')
        print('='*60)
        print('O porão é escuro, úmido e imundo. Paredes descascadas revelam símbolos profanos.')
        print('Ao fundo, você consegue ver o horror em seu estado mais puro.')
        print('Antes de confrontar o mal definitivo, você precisa entender o tamanho da loucura desse homem...')
        input('\n[Investigar o porão...]')
        
        # --- EXECUÇÃO DO ATO 3 ---
        pistas_ato3 = iniciar_investigacao("ato3")
        
        # Manifestação sobrenatural antes do chefe final
        manifestacao_sobrenatural(pistas_ato3, "ato3")
        
        # Luta final contra o Marido (ID 3)
        # Resetando a fúria para garantir que a mecânica funcione
        furia_ativada = False 
        vitoria_final = combate(bestiario[3])
        
        if vitoria_final:
            print('\n' + '='*60)
            print('🎉 PARABÉNS! VOCÊ SOLUCIONOU O CASO!')
            print('='*60)
            print(f'Com o Marido purificado, o Dossiê final foi recuperado.')
            print('JT caminha para fora da casa enquanto as primeiras luzes da manhã surgem.')
            print('O terror acabou... por enquanto.')
        
        break # Fim do Loop do jogo principal

elif menu == 2:
    print('\nAinda em desenvolvimento (o desenvolvedor narigudo não veio).')
elif menu == 3:
    print('\nPorque tu entrou no meu jogo se tu ia sair?\nAinda sim, muito obrigado por ter perdido o seu tempo :)')