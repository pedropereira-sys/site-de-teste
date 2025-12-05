import random
def gerar_dicas(taxa_cliques, taxa_entrega):
    """
    Retorna uma lista de dicas personalizadas conforme cliques e entrega.
    Textos curtos, institucionais e com foco em performance de campanhas SMS.
    """
    # === ENTREGA ABAIXO DE 50% ===
    if taxa_entrega < 50:
        return random.choice([
            f"A entrega ficou abaixo de 50%. Ou seja: {taxa_entrega}%. Recomendamos revisar a base para identificar possíveis caracteres inválidos ou números preenchidos incorretamente.",
            f"A taxa de entrega ficou menor que 50%. Resultado atual: {taxa_entrega}%. Sugimos verificar se há números incompletos ou mal formatados.",
            f"Entrega abaixo de 50%. Valor identificado: {taxa_entrega}%. Revise a base para encontrar dígitos faltantes ou caracteres não permitidos.",
            f"A campanha teve menos de 50% de entrega. Indicador: {taxa_entrega}%. Oriente-se revisando a base em busca de inconsistências.",
            f"A entrega caiu para baixo de 50%. Dado atual: {taxa_entrega}%. Recomendamos validar formatação e possíveis erros nos números.",
            f"Menos de 50% de entrega detectados. Taxa registrada: {taxa_entrega}%. Verifique se existem contatos inválidos na base.",
            f"A performance de entrega ficou baixa. Atualmente: {taxa_entrega}. Sugerimos revisar números incompletos ou com caracteres inválidos.",
            f"Entrega insuficiente, abaixo de 50%. Resultado: {taxa_entrega}%. Recomendamos uma checagem completa da base.",
            f"A taxa de entrega está baixa (<50%). Atual: {taxa_entrega}%. Revise possíveis erros de preenchimento nos contatos.",
            f"Baixa entrega registrada, inferior a 50%. Valor: {taxa_entrega}%. Verifique formatação e consistência dos números.",
            f"O desempenho de entrega ficou abaixo de 50%. Índice: {taxa_entrega}%. Recomendamos validar toda a base.",
            f"A entrega não atingiu 50%. Nível atual: {taxa_entrega}%. Pode haver caracteres inválidos ou números incompletos.",
            f"Entregas abaixo de 50%. Total: {taxa_entrega}%. Sugerimos checar erros de digitação nos contatos.",
            f"A taxa registrada está abaixo de 50%. Dados: {taxa_entrega}%. Revise a base para corrigir possíveis inconsistências.",
            f"Menor que 50% de entrega. Resultado: {taxa_entrega}%. Indicamos verificar formato e integridade dos números.",
            f"A campanha teve entrega reduzida (<50%). Indicador: {taxa_entrega}%. Recomendamos revisar formatações e caracteres inválidos.",
            f"A entrega ficou em um nível baixo, inferior a 50%. Atual: {taxa_entrega}%. Faça uma revisão da base para identificar erros.",
            f"Taxa de entrega menor que 50%. Registro: {taxa_entrega}%. Verifique se existem contatos mal preenchidos.",
            f"A entrega não passou dos 50%. Valor encontrado: {taxa_entrega}%. Uma revisão da base pode solucionar inconsistências.",
            f"Taxa abaixo de 50%. Resultado: {taxa_entrega}%. Sugerimos validar dígitos faltando ou símbolos incorretos na base."
        ])

    # === ENTREGA ABAIXO DE 80% ===
    elif taxa_entrega < 80:
        return random.choice([
            f"Percebemos uma entrega abaixo do esperado. Taxa atual: {taxa_entrega}%. Verifique se os números da base estão atualizados.",
            f"Sua taxa de entrega está baixa. Resultado: {taxa_entrega}%. Recomendamos revisar a qualidade e atualidade dos contatos.",
            f"Poucas mensagens entregues. Entrega registrada: {taxa_entrega}. É importante validar os números antes do próximo disparo.",
            f"A base pode conter números inativos ou incorretos. Entrega atual: {taxa_entrega}%. Atualize os contatos para aumentar o desempenho.",
            f"A performance da entrega ficou abaixo da média. Taxa: {taxa_entrega}%. Revise o DDD e a origem dos leads.",
            f"O volume de entregas está abaixo do ideal. Entrega registrada: {taxa_entrega}%. Vale checar se a operadora está limitando o envio.",
            f"A baixa entrega pode indicar uma base antiga. Nível atual: {taxa_entrega}%. Tente segmentar por data de aquisição dos leads.",
            f"Entrega abaixo da média. Resultado: {taxa_entrega}%. Considere remover contatos com rejeições recorrentes.",
            f"Entrega abaixo do ideal. Taxa: {taxa_entrega}%. Recomendamos revisar possíveis bloqueios ou filtros nas operadoras.",
            f"A taxa de entrega ficou reduzida. Entrega atual: {taxa_entrega}%. Vale validar se os números seguem o padrão correto (DDD + número).",
            f"Baixo índice de entrega. Taxa registrada: {taxa_entrega}%. Tente realizar uma limpeza na base para eliminar contatos inativos.",
            f"O resultado indica falhas na base. Entrega identificada: {taxa_entrega}%. Atualizar os cadastros pode melhorar o desempenho.",
            f"Entregas inconsistentes. Taxa registrada: {taxa_entrega}%. An%alise se há duplicidades ou números inválidos na lista.",
            f"Desempenho de entrega abaixo da média. Taxa: {taxa_entrega}%. Segmentar por região pode ajudar a identificar o problema.",
            f"Parte das mensagens não foi entregue. Entrega atual: {taxa_entrega}%. Reavalie o formato do envio e a origem dos leads.",
            f"A campanha encontrou dificuldades de entrega. Resultado: {taxa_entrega}%. Teste outro remetente ou ajuste o horário de disparo.",
            f"Poucas mensagens entregues. Taxa: {taxa_entrega}%. Um filtro de qualidade na base pode aumentar a entrega significativamente.",
            f"O volume de entrega ficou aquém do esperado. Entrega atual: {taxa_entrega}%. Avalie o tempo de inatividade da base.",
            f"A base parece desatualizada. Taxa: {taxa_entrega}%. Uma verificação com dados recentes pode melhorar os resultados.",
            f"Entregas abaixo do normal. Nível: {taxa_entrega}%. Verifique se há números corporativos ou fixos na lista.",
            f"A campanha apresentou falhas de envio. Resultado: {taxa_entrega}%. Ajustar o formato do arquivo de base pode resolver.",
            f"Parte dos contatos não recebeu a mensagem. Entrega registrada: {taxa_entrega}%. Tente dividir a base em lotes menores para testar.",
            f"Taxa de entrega reduzida. Indicador: {taxa_entrega}%. Considere eliminar números com rejeições consecutivas nos últimos envios.",
        ])

    # === QUANTIDADE DE CLIQUES ZERADA ===
    if taxa_cliques == 0:
        return random.choice([
            "A campanha não registrou cliques. Vale revisar o CTA ou testar uma abordagem mais direta.",
            "Não houve cliques na ação. Recomenda-se ajustar o posicionamento ou destaque do link.",
            "A campanha teve zero cliques, indicando que o link pode não ter chamado atenção suficiente.",
            "Apesar da entrega, nenhum clique foi registrado. Tente reforçar o benefício principal no texto.",
            "O engajamento foi nulo. Ajustar o CTA pode ajudar a gerar ação do público.",
            "A mensagem chegou à base, mas não houve cliques. Uma reformulação do convite ao acesso pode melhorar.",
            "Zero cliques registrados. Considere simplificar o texto ou destacar melhor a chamada para ação.",
            "Não houve interação com o link. Teste uma frase de incentivo mais clara.",
            "Zero cliques podem indicar que o link não estava visível o suficiente. Avalie alterar sua posição.",
            "Nenhum clique foi captado. Inserir o link mais cedo no texto pode trazer mais atenção.",
            "A campanha teve entrega, mas zero cliques. Reforce o motivo pelo qual o usuário deve acessar.",
            "Não houve cliques. Vale testar um CTA mais convidativo ou direto.",
            "A base recebeu a mensagem, porém sem interação. Tente usar um benefício explícito antes do link.",
            "Zero cliques sinalizam baixa atração. Uma mensagem mais curta pode aumentar o foco no link.",
            "Não houve interação com o link enviado. Ajustar o estilo de escrita pode melhorar a conversão.",
            "O resultado foi de zero cliques. Adicionar uma pergunta que gere curiosidade pode ajudar.",
            "A campanha não obteve cliques. Vale testar um formato mais objetivo e orientado à ação.",
            "Sem cliques registrados. Revise o CTA e considere reforçar o valor do clique para o usuário.",
            "Através dos dados, identificamos zero cliques. Reposicionar o link pode melhorar o desempenho."
        ])
    
    # === QUANTIDADE DE CLIQUES EXTREMAMENTE BAIXA ===
    elif taxa_cliques < 1:
        return random.choice([
            "A entrega foi boa, mas a taxa de cliques ficou muito baixa. Vale testar um CTA mais direto no início da mensagem.",
            "Mesmo com uma entrega sólida, os cliques foram mínimos. Experimente destacar o benefício principal logo na abertura.",
            "A taxa de cliques ficou muito abaixo do esperado. Talvez um link mais visível ou isolado ajude.",
            "A mensagem chegou ao público, porém quase ninguém clicou. Tente reforçar o motivo para acessar o link.",
            "Entrega ok, mas o clique foi muito baixo. Teste uma frase mais chamativa antes do link.",
            "A taxa de cliques foi muito baixa. Considere reposicionar o link para uma área mais evidente do texto.",
            "Pouquíssimos cliques. Um CTA mais forte ou uma promessa clara pode aumentar a ação do leitor.",
            "Apesar da boa distribuição, o engajamento foi mínimo. Tente usar verbos de ação para incentivar o clique.",
            "A taxa de cliques ficou bem abaixo da média. Inserir um benefício direto ligado ao link pode ajudar.",
            "O público recebeu, mas quase não interagiu. Experimente reduzir o texto e focar no convite ao clique.",
            "A entrega funcionou, mas a ação não aconteceu. Reforce o porquê vale a pena clicar.",
            "Clique extremamente baixo. Uma reformulação do CTA pode deixar o objetivo mais claro.",
            "O clique foi quase inexistente. Teste uma abordagem mais curiosa, como perguntas ou teasers.",
            "Houve entrega, mas não houve cliques suficientes. Talvez o link esteja muito escondido no texto.",
            "O conteúdo chegou, mas não converteu. Reforce o valor imediato do clique com uma frase curta e objetiva.",
            "A taxa de cliques foi muito baixa. Inserir o link no início pode aumentar a atenção.",
            "A mensagem foi vista, mas o clique não aconteceu. Destaque o benefício antes do CTA.",
            "Engajamento quase nulo. Teste um CTA mais chamativo ou uma estrutura de mensagem mais direta.",
            "A taxa de cliques ficou muito baixa. Tente usar formatações como negrito para destacar o link ou o call to action.",
        ])

    # === BOA ENTREGA, POUCOS CLOQUES ===
    elif 1 <= taxa_cliques < 3:  
        return random.choice([
            "Boa entrega, mas poucos cliques. Tente destacar mais o link na mensagem.",
            "A entrega foi ótima, porém o engajamento foi baixo. Reforce o valor do clique no texto.",
            "Mensagens estão chegando, mas o interesse foi baixo. Teste diferentes CTAs ou benefícios.",
            "A base recebeu bem a mensagem, mas houve pouca interação. Experimente um link mais visível.",
            "Entregas consistentes, mas cliques baixos. Um CTA mais direto pode ajudar (ex: *Acesse agora!*).",
            "A mensagem pode estar pouco atrativa. Tente um texto mais curto e com foco no benefício.",
            "A entrega foi alta, mas o clique ficou baixo. Reforce urgência ou exclusividade no texto.",
            "Poucos cliques podem indicar que o link está muito no fim da mensagem. Reposicione-o.",
            "Entrega excelente! Mas os cliques ficaram abaixo do esperado. Tente usar um CTA mais convidativo.",
            "A campanha chegou bem aos contatos, mas gerou pouco interesse. Inclua uma frase que desperte curiosidade.",
            "Boa performance de envio, porém baixa interação. Teste formatos mais curtos e diretos.",
            "Entregas altas, mas pouca ação. Inserir um benefício logo no início pode ajudar.",
            "A mensagem foi entregue, mas não motivou o clique. Reforce o motivo para acessar o link.",
            "O público recebeu bem, mas não clicou. Tente destacar o link com formatação ou nova posição.",
            "Mensagem clara, porém pouco envolvente. Inclua uma chamada que desperte desejo ou curiosidade.",
            "Entregas sólidas, mas conversão baixa. Reforce o benefício real que o clique oferece.",
            "Boa taxa de entrega, mas engajamento modesto. Teste novos horários ou públicos da base.",
            "A campanha chegou bem, mas faltou impacto. Adicione um gatilho como “Descubra agora” ou “Veja como”.",
            "O conteúdo foi entregue, mas o CTA pode estar fraco. Deixe claro o que o usuário ganha ao clicar.",
            "A base recebeu a mensagem, mas houve pouca ação. Reforce o valor da oferta logo nas primeiras linhas.",
            "O público visualizou, mas não interagiu. Tente reformular o título para gerar mais curiosidade.",
        ])

    # === DESEMPENHO MEDIANO ===
    elif 3 <= taxa_cliques < 5:
        return random.choice([
            "A campanha de SMS está dentro da média. Um CTA mais direto pode elevar a taxa de cliques.",
            "O desempenho foi razoável. Pequenos ajustes no início do texto podem melhorar o interesse.",
            "Bom resultado! Considere testar horários diferentes de disparo.",
            "Campanha sólida, com engajamento dentro do esperado. Teste variações de título para avançar.",
            "O conteúdo performou bem. Pequenas alterações de palavras-chave podem otimizar o resultado.",
            "A taxa de cliques está na média do segmento. Mantenha o estilo e teste dias alternados.",
            "O resultado está regular. Inserir uma pergunta no início da mensagem pode chamar mais atenção.",
            "Campanha equilibrada! Um toque mais emocional no texto pode aumentar o interesse.",
            "O conteúdo está claro, mas o CTA pode ser mais convidativo para gerar ação.",
            "Desempenho consistente. Vale testar uma variação de tom — mais direto ou mais conversacional.",
            "Campanha estável. Ajustar o início da mensagem pode gerar maior curiosidade.",
            "Resultados dentro do esperado. Experimente alterar a posição do link no texto.",
            "Taxa de cliques regular. Um título mais chamativo pode melhorar o desempenho.",
            "O texto está funcional, mas pode ganhar impacto com um verbo de ação logo no começo.",
            "O engajamento ficou mediano. Tente simplificar a mensagem para torná-la mais fluida.",
            "Desempenho ok! Testar novos horários de disparo pode trazer insights interessantes.",
            "Campanha dentro da média. Um tom mais próximo e natural pode aumentar as respostas.",
            "Engajamento estável. Reavaliar o público-alvo pode ajudar a melhorar a conversão.",
            "O conteúdo é bom, mas talvez falte uma chamada mais clara para o próximo passo.",
            "O formato funcionou bem. Testar versões mais curtas pode otimizar os cliques.",
            "Campanha razoável. Inserir uma frase de curiosidade antes do CTA pode gerar mais atenção.",
        ])

    # === DESEMPENHO BOM ===
    elif 5 <= taxa_cliques < 7:  
        return random.choice([
            "A campanha apresentou um bom desempenho, mantendo estabilidade nos principais indicadores.",
            "O resultado foi bom e mostrou que a estratégia adotada está funcionando de forma consistente.",
            "O desempenho foi bom, com números equilibrados e dentro do esperado.",
            "A performance foi boa e demonstrou que o público recebeu bem a mensagem.",
            "A campanha teve um bom retorno e manteve regularidade nas interações.",
            "O desempenho se manteve bom, indicando que o formato está adequado ao público.",
            "A ação apresentou um bom comportamento geral, sem grandes oscilações.",
            "O resultado foi bom e reflete uma boa aceitação da comunicação enviada.",
            "A campanha teve um bom funcionamento, com métricas dentro do padrão.",
            "Desempenho bom, demonstrando estabilidade no envio e engajamento.",
            "A ação teve um desempenho bom, com indicadores coerentes ao esperado.",
            "O resultado se manteve bom, sugerindo que a abordagem está adequada.",
            "A campanha registrou um bom desempenho, mostrando alinhamento com a base.",
            "O desempenho foi bom e reforça que a estratégia está no caminho certo.",
            "A performance ficou em um nível bom, demonstrando equilíbrio nos dados.",
            "A campanha apresentou um bom rendimento, com boa recepção do público.",
            "O desempenho geral foi bom, mantendo a consistência dos resultados.",
            "A ação alcançou um nível bom de performance, sem quedas significativas.",
            "O comportamento da campanha foi bom, mantendo sinais positivos nos indicadores.",
            "O resultado ficou em um patamar bom, com boa estabilidade no engajamento.",
        ])

    # === DESEMPENHO ALTO ===
    elif 7 <= taxa_cliques < 9:  
        return random.choice([
            "A campanha apresentou um desempenho alto, mostrando boa resposta do público.",
            "Os indicadores ficaram em nível alto, demonstrando boa efetividade da estratégia.",
            "O engajamento atingiu um patamar alto, reforçando a qualidade da comunicação.",
            "A performance se manteve alta, indicando boa aceitação da mensagem.",
            "A ação teve um retorno alto, com boa consistência nos resultados.",
            "O desempenho geral ficou alto, sugerindo alinhamento com o perfil da base.",
            "A taxa de interação alcançou um nível alto, validando a abordagem utilizada.",
            "Os dados mostram um engajamento alto, refletindo boa conexão com o público.",
            "A campanha registrou entrega e resposta em níveis altos e estáveis.",
            "A ação apresentou métricas em patamar alto, mantendo regularidade.",
            "O desempenho ficou alto, indicando que o formato escolhido funcionou bem.",
            "A performance se manteve em nível alto, sem variações negativas relevantes.",
            "A campanha alcançou um engajamento alto, sugerindo boa construção do texto.",
            "O retorno foi alto, mostrando eficiência no envio e adesão do público.",
            "A taxa de resposta subiu para um nível alto, reforçando o bom direcionamento.",
            "Os números ficaram altos, com boa estabilidade entre envio e interação.",
            "A ação atingiu um desempenho alto, demonstrando que a estratégia está funcionando.",
            "A campanha obteve um nível alto de engajamento, com boa participação dos contatos.",
            "A performance se manteve alta, sinalizando que a mensagem foi adequada ao público.",
            "O comportamento geral da campanha ficou alto, reforçando a eficiência do disparo."
        ])

    # === DESEMPENHO MUITO ALTO ===
    elif 9 <= taxa_cliques < 11:  
        return random.choice([
            "A campanha atingiu um desempenho muito alto, mostrando forte resposta do público.",
            "Os indicadores ficaram em nível muito alto, evidenciando grande eficiência na abordagem.",
            "O engajamento alcançou patamar muito alto, reforçando a boa aceitação da mensagem.",
            "A performance registrou um nível muito alto, demonstrando excelente adesão dos contatos.",
            "A entrega e o retorno ficaram em níveis muito altos, mostrando alinhamento com a estratégia.",
            "A ação obteve um desempenho muito alto, com dados acima do comportamento habitual da base.",
            "A taxa de interação chegou a um nível muito alto, validando plenamente o formato utilizado.",
            "O engajamento manteve-se muito alto, indicando boa conexão com o público.",
            "A campanha apresentou métricas em patamar muito alto, sem quedas relevantes.",
            "O desempenho geral foi muito alto, refletindo grande aderência da audiência.",
            "Os resultados alcançaram um nível muito alto, destacando a eficiência da comunicação.",
            "O engajamento ficou muito alto, reforçando que o conteúdo chamou bastante atenção.",
            "A ação manteve uma performance muito alta, com retorno expressivo da base.",
            "As taxas de resposta atingiram níveis muito altos, evidenciando grande interesse.",
            "Os indicadores tiveram um salto para um nível muito alto, mostrando evolução clara.",
            "A campanha atingiu níveis muito altos de interação, acima do usual para essa base.",
            "O desempenho ficou muito alto, consolidando uma boa estratégia de comunicação.",
            "A ação apresentou constância em um patamar muito alto de resultados.",
            "A performance foi mantida em nível muito alto, com participação ampla dos contatos.",
            "O comportamento geral da campanha manteve-se muito alto, demonstrando forte engajamento.",
        ])

    # === DESEMPENHO MAXIMO ===
    else:
        return random.choice([
            "Excelente! Sua campanha de SMS obteve ótima taxa de cliques. Continue com essa linha de comunicação.",
            "Parabéns! O texto está engajando bem, mantenha o estilo e teste novos horários.",
            "Ótimos números! Essa estrutura de mensagem está performando muito bem.",
            "Campanha com excelente engajamento! Replicar esse formato pode gerar bons resultados novamente.",
            "Excelente taxa de cliques! A comunicação foi clara e assertiva.",
            "Resultados acima da média! Mantenha o formato e valide a frequência de disparos.",
            "Campanha de alta performance! Avalie repetir o mesmo modelo em novas bases.",
            "Engajamento excepcional. Continue com o mesmo padrão de clareza e CTA objetivo.",
            "Mensagem bem recebida! A taxa de resposta indica que o público está engajado.",
            "Excelente desempenho! Continue explorando esse tipo de abordagem.",
            "Resultado expressivo! Essa comunicação gerou ótimo retorno.",
            "Campanha de destaque! O conteúdo despertou alto interesse no público.",
            "Boa escolha de texto! A linguagem está contribuindo para ótimos índices de cliques.",
            "Desempenho consistente! Esse modelo está entregando bons resultados.",
            "Campanha eficiente! Reutilizar essa estrutura pode manter o bom engajamento.",
            "Excelente estratégia! A clareza e o tom estão alinhados com o público.",
            "Alta taxa de interação! Continue testando variações para potencializar ainda mais.",
            "Parabéns pelo resultado! O formato aplicado está rendendo muito bem.",
            "Texto assertivo e eficaz! A mensagem foi direta e despertou interesse.",
            "Boa leitura de público! A comunicação está adequada ao perfil da base.",
            "Campanha bem construída! O equilíbrio entre informação e CTA foi ideal.",
            "Excelente abordagem! O público reagiu positivamente ao formato da mensagem.",
            "Top performance! Essa linha de comunicação está superando expectativas.",
        ])