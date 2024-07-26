def forma_normal_greibach(gramatica):
    def primeiras_regras(nao_terminal):
        return [producao[0] for producao in gramatica.regras[nao_terminal] if producao[0].islower()]
    
    novas_regras = {}
    
    for nao_terminal, producoes in gramatica.regras.items():
        novas_regras[nao_terminal] = []
        for producao in producoes:
            if producao[0].islower():
                novas_regras[nao_terminal].append(producao)
            else:
                novas_producoes = []
                for primeiro in primeiras_regras(producao[0]):
                    novas_producoes.append(primeiro + producao[1:])
                novas_regras[nao_terminal].extend(novas_producoes)
    
    gramatica.regras = novas_regras
