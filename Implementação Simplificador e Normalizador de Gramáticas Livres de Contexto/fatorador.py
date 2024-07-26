def fatoracao_esquerda(gramatica):
    novas_regras = {}
    
    for nao_terminal, producoes in gramatica.regras.items():
        prefixo_comum = None
        for producao in producoes:
            if prefixo_comum is None:
                prefixo_comum = producao[0]
            elif producao[0] != prefixo_comum:
                prefixo_comum = None
                break
        if prefixo_comum:
            novo_nao_terminal = nao_terminal + "'"
            novas_regras[nao_terminal] = [prefixo_comum + novo_nao_terminal]
            novas_regras[novo_nao_terminal] = [producao[1:] for producao in producoes]
        else:
            novas_regras[nao_terminal] = producoes
    
    gramatica.regras = novas_regras
