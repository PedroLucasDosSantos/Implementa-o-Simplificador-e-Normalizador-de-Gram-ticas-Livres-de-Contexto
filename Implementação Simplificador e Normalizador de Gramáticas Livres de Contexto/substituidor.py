def substituir_producoes_unitarias(gramatica):
    while True:
        substituicoes = []
        for nao_terminal, producoes in gramatica.regras.items():
            for producao in producoes:
                if len(producao) == 1 and producao.isupper():
                    substituicoes.append((nao_terminal, producao))
        if not substituicoes:
            break
        for (nt, prod) in substituicoes:
            gramatica.regras[nt].remove(prod)
            gramatica.regras[nt].extend(gramatica.regras[prod])
