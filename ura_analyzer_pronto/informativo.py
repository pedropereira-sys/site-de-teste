import random
from dicas import gerar_dicas  # Corrigida a importação
from datetime import datetime

agora = datetime.now()
hora_atual = agora.strftime("%H:%M")

def gerar_tom_aleatorio(dica_texto):
    tons = [
        "📈 *Dica prática:* ",
        "💡 *Sugestão estratégica:* ",
        "🤝 *Oportunidade de melhoria:* ",
        "⚠️ *Recomendação rápida:* ",
        "🏆 *Excelente Parceria:* ",
        "⚙️ *Ponto de atenção:*",
        "📝 *Insight de performance:* ",
        "⭐ *Ajuste sugerido:* ",
        "✨ *Destaque positivo:* ",
        "🔍 *Melhoria recomendada:* ",
        "👀 *Feedback construtivo:* ",
        "📌 *Observação importante:* ",
        "🧭 *Análise rápida:* ",
        "🔍 *Potencial de otimização:* ",
        "♟️ *Olhada estratégica:* ",
        "⚡ *Reconhecimento de resultado:* ",
        "🚀 *Direcionamento útil:* ",
        "🚀 *Boas práticas:* ",
        "✅ *Insight valioso:* ",
        "💎 *Ação recomendada:* "
    ]
    positivos = ["excelente", "ótimo", "bom", "parabéns", "ótimos", "excelência"]

    if any(p in dica_texto.lower() for p in positivos):
        tons = [t for t in tons if "Excelente" not in t and "🤝" not in t]

    return random.choice(tons)

def gerar_informativo(empresa, campanha_id, entregue, invalidas, total_disparos, cliques, total_respostas=0, status="Finalizado"):
    taxa_entrega = round((entregue / total_disparos) * 100, 2) if total_disparos > 0 else 0
    taxa_cliques = round((cliques / entregue) * 100, 2) if entregue > 0 else 0
    taxa_respostas = round((total_respostas / entregue) * 100, 2) if entregue > 0 else 0
    
    dica = gerar_dicas(taxa_cliques, taxa_entrega)
    tom = gerar_tom_aleatorio(dica)


    if invalidas < 1:
        texto = f"""
Bom dia!
📊 *Informativo de Desempenho do Disparo de SMS - {empresa}*

{tom}{dica}

> Relatório emitido às: {hora_atual}

📌 Campanha ID: *{campanha_id}*
📈 Status: {status}

✅ *Mensagens entregues:* {entregue:,} ({taxa_entrega}%)
🔗 *Cliques registrados:* {cliques:,} ({taxa_cliques}%)
💬 *SMS Respondidos:* {total_respostas:,} ({taxa_respostas}%)

Obrigado pela parceria e bons disparos! 🚀"""

    else:
        texto = f"""
Bom dia!
📊 *Informativo de Desempenho do Disparo de SMS - {empresa}*

{tom}{dica}

> Relatório emitido às: {hora_atual}

📌 Campanha ID: *{campanha_id}*
📈 Status: {status}

✅ *Mensagens entregues:* {entregue:,} ({taxa_entrega}%)
🔗 *Cliques registrados:* {cliques:,} ({taxa_cliques}%)
💬 *SMS Respondidos:* {total_respostas:,} ({taxa_respostas}%)
❌ *Mensagens Inválidas:* {invalidas}

Obrigado pela parceria e bons disparos! 🚀"""
    return texto.strip()

def gerar_informativo_ura(campanha_id, nome_campanha, usuario_email, status_campanha, 
                          taxa_conversao, porcentagem_andamento, quantidade_leads, 
                          total_falta_ligar, total_convertido, total_convertido_dia, total_atendidos, total_nao_atendidos):
    """
    Gera informativo no formato específico para campanhas de URA
    """
    
    # Cálculo da taxa de atendimento
    taxa_atendimento = 0
    if total_atendidos and total_nao_atendidos and (total_atendidos + total_nao_atendidos) > 0:
        taxa_atendimento = (total_atendidos / (total_atendidos + total_nao_atendidos) * 100)
    
    # Lógica para campanhas com mais de 100% de andamento
    campanha_esgotada = porcentagem_andamento > 100
    leads_restantes_reais = max(0, total_falta_ligar) if total_falta_ligar else 0
    
    # Calcular tentativas totais (considerando que podem ter ligado mais vezes que o total de leads)
    tentativas_totais = (total_atendidos or 0) + (total_nao_atendidos or 0)
    retrabalho = tentativas_totais > quantidade_leads if quantidade_leads > 0 else False
    
    # Determinar o tom da mensagem baseado no desempenho
    if porcentagem_andamento > 1000:
        situacao = random.choice([
            "🚨 *LISTAGEM ESGOTADA - ALTA REPETIÇÃO*",
            "🛑 *BASE TOTALMENTE ESGOTADA*",
            "🚫 *LISTAGEM SEM EFETIVIDADE*",
            "⚠️ *RETRABALHO EXCESSIVO DETECTADO*"
        ])
        if retrabalho:
            recomendacao = random.choice([
                f"🔄 Foram realizadas *{tentativas_totais:,} tentativas* em *{quantidade_leads:,} leads* (*{(tentativas_totais/quantidade_leads*100) if quantidade_leads > 0 else 0:.1f}x repetição*). É indispensável *substituir a listagem* imediatamente.",
                "📛 A campanha entrou em repetição massiva — o mesmo lead já recebeu diversas ligações. Troque a base agora para não perder eficiência!",
                "⚠️ Listagem em esgotamento total, com volume elevado de retrabalho. Recomendamos uma nova base o quanto antes!"
            ])
        else:
            recomendacao = random.choice([
                "🚨 Listagem completamente esgotada! A URA já ligou múltiplas vezes para os mesmos leads. Recomendamos a troca URGENTE da base!",
                "📉 Base esgotada, sem novos contatos disponíveis. É o momento ideal para atualizar a listagem e retomar a performance.",
                "🧭 Todas as oportunidades dessa listagem já foram exploradas. Substitua por uma nova para continuar performando."
            ])

    elif porcentagem_andamento > 500:
        situacao = random.choice([
            "⚠️ *LISTAGEM ESGOTADA - MUITAS REPETIÇÕES*",
            "📉 *LISTAGEM COM ALTA TAXA DE RECONTATO*",
            "🔁 *BASE SATURADA - REPETIÇÃO ELEVADA*"
        ])
        if retrabalho:
            recomendacao = random.choice([
                f"🔄 Já foram feitas *{tentativas_totais:,} tentativas* para *{quantidade_leads:,} leads* (*{(tentativas_totais/quantidade_leads*100) if quantidade_leads > 0 else 0:.1f}% de repetição*). A base está saturada — troque para manter resultados consistentes.",
                "⚙️ A campanha está rodando sobre contatos repetidos. Avalie inserir novos leads para evitar queda de performance.",
                "🔁 Repetição em excesso detectada. Uma nova listagem deve ser priorizada para preservar a taxa de conversão."
            ])
        else:
            recomendacao = random.choice([
                f"📉 Base com muitos recontatos:{tentativas_totais:,}. É o momento de atualizar a listagem para não comprometer o desempenho.",
                "⚡ A performance pode cair — a URA está insistindo nos mesmos números. Nova base recomendada.",
                "🧩 O volume de repetição está alto, o que indica esgotamento da lista. Atualize a base para continuar eficiente."
            ])

    elif porcentagem_andamento > 300:
        situacao = random.choice([
            "🔁 *LISTAGEM EM REPETIÇÃO*",
            "⚠️ *MUITAS TENTATIVAS REPETIDAS*",
            "📞 *BASE COM RECONTATO FREQUENTE*"
        ])
        recomendacao = random.choice([
            "A campanha apresenta alta taxa de repetição. Recomendamos preparar uma nova base antes de esgotar a atual.",
            "Os mesmos contatos estão sendo abordados repetidamente. Uma listagem nova ajudará a manter o desempenho.",
            "⚙️ Alta taxa de retrabalho identificada — substitua parte dos leads para continuar performando bem."
        ])

    elif porcentagem_andamento > 200:
        situacao = random.choice([
            "📉 *LISTAGEM PRÓXIMA DO ESGOTAMENTO*",
            "📊 *BASE SE APROXIMANDO DO LIMITE*",
            "⚡ *LISTAGEM EM FASE FINAL DE APROVEITAMENTO*"
        ])
        recomendacao = random.choice([
            "A listagem está próxima do esgotamento. Programe a substituição para não afetar a conversão.",
            "⚡ Já ultrapassou 200% de andamento — a base está se esgotando. Planeje a troca em breve.",
            "A campanha segue ativa, mas a repetição começa a aumentar. Atualizar a base em breve é recomendado."
        ])

    elif porcentagem_andamento > 100:
        situacao = random.choice([
            "🔄 *LISTAGEM EM RETRABALHO*",
            "📈 *CAMPANHA RODANDO EM RECONTATO*"
        ])
        recomendacao = random.choice([
            "📊 A campanha já completou 100% e está em fase de retrabalho. A performance pode cair — avalie nova listagem!",
            "⚙️ Em fase de repetição. Se a conversão estiver estável, mantenha por pouco tempo; caso contrário, troque a base.",
            "🔁 A campanha entrou em retrabalho. Uma nova listagem pode elevar as taxas de resposta novamente."
        ])

    elif porcentagem_andamento > 50:
        situacao = random.choice([
            "🟢 *LISTAGEM EM ANDAMENTO*",
            "📞 *BASE EM BOA UTILIZAÇÃO*",
            "📊 *CAMPANHA AINDA COM BOM POTENCIAL*"
        ])
        recomendacao = random.choice([
            "🚀 Campanha em ritmo saudável! Continue acompanhando o desempenho e prepare a próxima base antecipadamente.",
            "Tudo dentro do esperado — mantenha o acompanhamento e programe a substituição quando chegar a 100%.",
            "💡 Taxa de discagem estável. Aproveite o bom momento para otimizar mensagens ou ajustar o fluxo de URA."
        ])

    else:
        situacao = random.choice([
            "🟢 *LISTAGEM NOVA - EM INÍCIO DE EXECUÇÃO*",
            "📈 *CAMPANHA EM FASE INICIAL*",
            "✨ *BASE RECÉM-IMPORTADA*"
        ])
        recomendacao = random.choice([
            "A listagem está começando a rodar. Acompanhe as primeiras conversões e avalie a qualidade dos contatos.",
            "🚀 Início de campanha! Monitore o andamento para identificar rapidamente padrões de desempenho.",
            "Campanha inicializada com sucesso. Acompanhe os primeiros resultados e ajuste se necessário."
        ])


    # Formatar números
    porcentagem_andamento_str = f"{porcentagem_andamento:,.2f}%" if porcentagem_andamento else "0%"
    taxa_conversao_str = f"{taxa_conversao:.2f}%"
    taxa_atendimento_str = f"{taxa_atendimento:.2f}%"

    # Texto base com informações da campanha
    texto = f"""🎯 Campanha da *URA {campanha_id}* - {nome_campanha}
📧 Responsável: {usuario_email}

> Relatório emitido às: {hora_atual}

📞 *Atendimento:* *{taxa_atendimento_str}*
✅ *Conversão:* *{taxa_conversao_str}*
📊 *Andamento:* *{porcentagem_andamento_str}*

{situacao}

{recomendacao}

📈 *DETALHES DA CAMPANHA:*
• Total de Leads: *{quantidade_leads:,}*
• Leads Restantes: *{leads_restantes_reais:,}*
• Total Convertidos: *{total_convertido:,}*
• Quantidade de Convertidos Hoje: *{total_convertido_dia}*"""

    # Adicionar alerta específico para retrabalho
    if retrabalho and tentativas_totais > 0 and quantidade_leads > 0:
        taxa_repeticao = (tentativas_totais / quantidade_leads * 100)
        texto += f"\n• Taxa de Repetição: *{taxa_repeticao:.1f}%*"
        
        if taxa_repeticao > 200:
            texto += f"\n\n 🚨 *ALERTA:* A URA já ligou em média *{tentativas_totais/quantidade_leads:.1f}x* para cada lead!"
        elif taxa_repeticao > 150:
            texto += f"\n\n ⚠️ *AVISO:* Múltiplas tentativas nos mesmos leads podem reduzir a eficácia!"

    texto += "\n\n💡 *Dica Estratégica:* Base esgotada impacta performance - considere nova listagem!" if campanha_esgotada else "\n\n💡 *Dica Estratégica:* Mantenha o monitoramento constante!"
    texto += "\n\n🤝 Ficamos à disposição para auxiliar em caso de dúvidas!"

    return texto