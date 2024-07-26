def remover_producoes_vazias(gramatica):
    producoes_vazias = set()
    
    for nao_terminal, producoes in gramatica.regras.items():
        for producao in producoes:
            if producao == "":
                producoes_vazias.add(nao_terminal)
    
    while True:
        novos_vazios = set()
        for nao_terminal, producoes in gramatica.regras.items():
            if nao_terminal not in producoes_vazias:
                for producao in producoes:
                    if all(simbolo in producoes_vazias for simbolo in producao):
                        novos_vazios.add(nao_terminal)
        if not novos_vazios:
            break
        producoes_vazias.update(novos_vazios)
    
    novas_regras = {}
    for nao_terminal, producoes in gramatica.regras.items():
        novas_regras[nao_terminal] = []
        for producao in producoes:
            sub_producoes = [""]
            for simbolo in producao:
                if simbolo in producoes_vazias:
                    sub_producoes = [sub + simbolo for sub in sub_producoes] + sub_producoes
                else:
                    sub_producoes = [sub + simbolo for sub in sub_producoes]
            novas_regras[nao_terminal].extend(filter(lambda p: p != "", sub_producoes))
    
    gramatica.regras = novas_regras
