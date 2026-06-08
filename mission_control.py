# Mission Control AI
# Sistema de Monitoramento de Missão Espacial
# GS2026.1 - Pensamento Computacional e Automação com Python

# Dados da missão
NOME_MISSAO = "Aether"
NOME_EQUIPE  = "Stig4 Space"

# Matriz principal: cada linha é um ciclo [temperatura, comunicacao, bateria, oxigenio, estabilidade]
dados_missao = [
    [22, 95, 91, 98, 93],  # Ciclo 1 - Início da missão
    [26, 83, 76, 95, 88],  # Ciclo 2 - Estabilização
    [32, 67, 55, 90, 72],  # Ciclo 3 - Queda parcial de comunicação
    [37, 44, 35, 85, 52],  # Ciclo 4 - Alerta de energia
    [41, 25, 17, 76, 32],  # Ciclo 5 - Risco operacional máximo
    [35, 58, 28, 83, 48],  # Ciclo 6 - Tentativa de recuperação
    [30, 72, 43, 88, 65],  # Ciclo 7 - Recuperação em progresso
]

# Nome de cada área (mesma ordem das colunas da matriz)
areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional",
]

# Descrição narrativa de cada ciclo
nomes_ciclos = [
    "Início da missão",
    "Estabilização dos sistemas",
    "Queda parcial de comunicação",
    "Alerta de energia",
    "Risco operacional",
    "Tentativa de recuperação",
    "Recuperação em progresso",
]


# --- Funções de análise por área ---
# Cada função retorna uma tupla (classificacao, pontuacao, descricao)
# Pontuação: NORMAL=0, ATENÇÃO=1, CRÍTICO=2

def analisar_temperatura(valor):
    # < 18°C → ATENÇÃO | 18-30°C → NORMAL | 30-35°C → ATENÇÃO | > 35°C → CRÍTICO
    if valor < 18:
        return "ATENÇÃO", 1, "Temperatura abaixo do limite mínimo"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura estável"
    elif valor <= 35:
        return "ATENÇÃO", 1, "Temperatura elevada"
    else:
        return "CRÍTICO", 2, "Risco de superaquecimento"


def analisar_comunicacao(valor):
    # < 30% → CRÍTICO | 30-59% → ATENÇÃO | >= 60% → NORMAL
    if valor < 30:
        return "CRÍTICO", 2, "Comunicação com a base em nível crítico"
    elif valor < 60:
        return "ATENÇÃO", 1, "Comunicação instável"
    else:
        return "NORMAL", 0, "Comunicação estável"


def analisar_bateria(valor):
    # < 20% → CRÍTICO | 20-49% → ATENÇÃO | >= 50% → NORMAL
    if valor < 20:
        return "CRÍTICO", 2, "Bateria em nível crítico"
    elif valor < 50:
        return "ATENÇÃO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia estável"


def analisar_oxigenio(valor):
    # < 80% → CRÍTICO | 80-89% → ATENÇÃO | >= 90% → NORMAL
    if valor < 80:
        return "CRÍTICO", 2, "Oxigênio em nível crítico"
    elif valor < 90:
        return "ATENÇÃO", 1, "Oxigênio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigênio adequado"


def analisar_estabilidade(valor):
    # < 40% → CRÍTICO | 40-69% → ATENÇÃO | >= 70% → NORMAL
    if valor < 40:
        return "CRÍTICO", 2, "Estabilidade operacional crítica"
    elif valor < 70:
        return "ATENÇÃO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional adequada"


# --- Funções de classificação e análise ---

def classificar_ciclo(pontuacao):
    # 0-2 → ESTÁVEL | 3-5 → EM ATENÇÃO | 6-10 → CRÍTICA
    if pontuacao <= 2:
        return "MISSÃO ESTÁVEL"
    elif pontuacao <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"


def gerar_recomendacao(resultados_ciclo):
    # Gera recomendações para cada área em CRÍTICO
    # resultados_ciclo = lista com o retorno de cada função analisar_*
    recomendacoes = []

    if resultados_ciclo[0][0] == "CRÍTICO":
        recomendacoes.append("Verificar controle térmico da missão.")
    if resultados_ciclo[1][0] == "CRÍTICO":
        recomendacoes.append("Tentar restabelecer contato com a base.")
    if resultados_ciclo[2][0] == "CRÍTICO":
        recomendacoes.append("Ativar modo de economia de energia.")
    if resultados_ciclo[3][0] == "CRÍTICO":
        recomendacoes.append("Acionar protocolo de suporte à vida.")
    if resultados_ciclo[4][0] == "CRÍTICO":
        recomendacoes.append("Reduzir operações não essenciais.")

    # Com 3 ou mais críticos, adiciona alerta geral
    criticos = sum(1 for r in resultados_ciclo if r[0] == "CRÍTICO")
    if criticos >= 3:
        recomendacoes.append("Ativar modo de segurança máxima e priorizar suporte à vida.")

    # Sem críticos, verifica atenções
    if not recomendacoes:
        atencoes = sum(1 for r in resultados_ciclo if r[0] == "ATENÇÃO")
        if atencoes > 0:
            recomendacoes.append("Monitorar sistemas em atenção e preparar plano de contingência.")
        else:
            recomendacoes.append("Manter operação normal e continuar monitoramento.")

    return " | ".join(recomendacoes)


def analisar_tendencia(riscos_por_ciclo):
    # Compara o risco do primeiro ciclo com o do último
    risco_inicial = riscos_por_ciclo[0]
    risco_final = riscos_por_ciclo[-1]

    if risco_final > risco_inicial:
        return "A missão apresentou tendência de piora."
    elif risco_final < risco_inicial:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."


def identificar_area_mais_afetada(pontuacao_acumulada):
    # Retorna a área com maior pontuação acumulada ao longo de todos os ciclos
    indice_max = 0
    for i in range(1, len(pontuacao_acumulada)):
        if pontuacao_acumulada[i] > pontuacao_acumulada[indice_max]:
            indice_max = i
    return areas_monitoradas[indice_max]


# --- Análise dos ciclos ---

def analisar_ciclos():
    # Percorre todos os ciclos, exibe os resultados e retorna os dados consolidados
    sep = "=" * 60
    div = "-" * 60

    print(sep)
    print("MISSION CONTROL AI")
    print(sep)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Ciclos analisados: {len(dados_missao)}")
    print(sep)

    riscos_por_ciclo = []              # Armazena a pontuação de risco de cada ciclo
    pontuacao_acumulada = [0] * 5      # Soma os pontos de risco por área
    ciclo_mais_critico = 0             # Guarda o número do ciclo mais crítico
    maior_risco = -1                   # Maior pontuação de risco encontrada
    qtd_ciclos_criticos = 0            # Contador de ciclos classificados como críticos
    totais = [0] * 5                   # Soma dos valores de cada indicador para cálculo das médias

    rotulos = ["Temperatura", "Comunicação", "Bateria", "Oxigênio", "Estabilidade"]
    unidades = ["°C", "%", "%", "%", "%"]  # Unidade de medida de cada indicador

    for i in range(len(dados_missao)):
        ciclo = dados_missao[i]
        numero = i + 1

        print(f"\nCICLO {numero} — {nomes_ciclos[i]}")
        print(div)

        resultados = [
            analisar_temperatura(ciclo[0]),
            analisar_comunicacao(ciclo[1]),
            analisar_bateria(ciclo[2]),
            analisar_oxigenio(ciclo[3]),
            analisar_estabilidade(ciclo[4]),
        ]  # Resultado da análise de cada área do ciclo

        pontuacao_ciclo = 0  # Acumula a pontuação total de risco do ciclo

        for j in range(5):
            valor = ciclo[j]
            classif = resultados[j][0]
            pontos = resultados[j][1]
            descricao = resultados[j][2]

            print(f"  {rotulos[j]}: {valor}{unidades[j]} | {classif} | {descricao}")

            pontuacao_ciclo += pontos
            pontuacao_acumulada[j] += pontos
            totais[j] += valor

        classificacao = classificar_ciclo(pontuacao_ciclo)
        recomendacao = gerar_recomendacao(resultados)

        print(f"\n  Pontuação de risco: {pontuacao_ciclo}")
        print(f"  Classificação: {classificacao}")
        print(f"  Recomendação: {recomendacao}")

        riscos_por_ciclo.append(pontuacao_ciclo)  # Registra o risco do ciclo para análises futuras

        if pontuacao_ciclo > maior_risco:
            maior_risco = pontuacao_ciclo
            ciclo_mais_critico = numero  # Atualiza o ciclo mais crítico encontrado

        if classificacao == "MISSÃO CRÍTICA":
            qtd_ciclos_criticos += 1

    return {
        "riscos_por_ciclo": riscos_por_ciclo,
        "pontuacao_acumulada": pontuacao_acumulada,
        "ciclo_mais_critico": ciclo_mais_critico,
        "maior_risco": maior_risco,
        "qtd_ciclos_criticos": qtd_ciclos_criticos,
        "totais": totais,
    }


# --- Relatório final ---

def gerar_relatorio_final(dados):
    # Exibe o resumo completo da missão com médias, tendência e área mais afetada
    sep = "=" * 60

    riscos = dados["riscos_por_ciclo"]
    pontuacao_acum = dados["pontuacao_acumulada"]
    ciclo_critico = dados["ciclo_mais_critico"]
    maior_risco = dados["maior_risco"]
    qtd_criticos = dados["qtd_ciclos_criticos"]
    totais = dados["totais"]
    n = len(dados_missao)

    media_temp = totais[0] / n
    media_com = totais[1] / n
    media_bat = totais[2] / n
    media_oxi = totais[3] / n
    media_est = totais[4] / n
    risco_medio = sum(riscos) / n  # Calcula o risco médio da missão

    tendencia = analisar_tendencia(riscos)  # Avalia a evolução do risco ao longo da missão
    area_afetada = identificar_area_mais_afetada(pontuacao_acum)  # Identifica a área com maior impacto
    classificacao_final = classificar_ciclo(round(risco_medio))  # Define a classificação geral da missão

    # Relatório final
    print("\n" + sep)
    print("RELATÓRIO FINAL DA MISSÃO")
    print(sep)

    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Ciclos analisados: {n}")

    print(f"\nMédia de temperatura: {media_temp:.2f} °C")
    print(f"Média de comunicação: {media_com:.2f}%")
    print(f"Média de bateria: {media_bat:.2f}%")
    print(f"Média de oxigênio: {media_oxi:.2f}%")
    print(f"Média de estabilidade: {media_est:.2f}%")

    print(f"\nCiclo mais crítico: Ciclo {ciclo_critico}")
    print(f"Maior pontuação de risco: {maior_risco}")
    print(f"Risco médio da missão: {risco_medio:.2f}")
    print(f"Ciclos críticos: {qtd_criticos}")

    print(f"\nTendência da missão:")
    print(f"  {tendencia}")

    print(f"\nPontuação acumulada por área:")
    for i in range(len(areas_monitoradas)):
        print(f"  {areas_monitoradas[i]}: {pontuacao_acum[i]} pontos")

    print(f"\nÁrea mais afetada: {area_afetada}")
    print(f"\nClassificação final: {classificacao_final}")

    print("\nConclusão:")
    if classificacao_final == "MISSÃO CRÍTICA":
        print("  A missão enfrentou condições extremamente adversas.")
        print("  Múltiplos sistemas atingiram nível crítico. Acionar todos os protocolos de emergência.")
    elif classificacao_final == "MISSÃO EM ATENÇÃO":
        print("  A missão apresentou instabilidade relevante durante a operação.")
        print("  Ainda existem sistemas em atenção. Manter o plano de contingência ativo.")
    else:
        print("  A missão transcorreu dentro dos parâmetros aceitáveis.")
        print("  Manter monitoramento contínuo para garantir a segurança.")

    print("\n" + sep)
    print("  Fim do relatório — Mission Control AI")
    print(sep)


# --- Execução ---

if __name__ == "__main__":
    # Executa a análise completa da missão
    dados_consolidados = analisar_ciclos()

    # Gera o relatório final com os dados consolidados
    gerar_relatorio_final(dados_consolidados)

