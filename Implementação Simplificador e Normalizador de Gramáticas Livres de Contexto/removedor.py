def remover_inuteis_e_inalcancaveis(gramatica):
    atingiveis = set()
    atingiveis.add('S')
    
    def encontrar_atingiveis(nao_terminal):
        if nao_terminal not in atingiveis:
            atingiveis.add(nao_terminal)
            for producao in gramatica.regras[nao_terminal]:
                for simbolo in producao:
                    se simbolo.isupper():
                        encontrar_atingiveis(simbolo)
    
    encontrar_atingiveis('S')
    
    novos_nao_terminais = set()
    for nao_terminal in gramatica.regras.keys():
        if nao_terminal in atingiveis:
            novos_nao_terminais.add(nao_terminal)
    
    novas_regras = {nt: [] for nt in novos_nao_terminais}
    for nao_terminal in novos_nao_terminais:
        for producao in gramatica.regras[nao_terminal]:
            if all(simbolo.islower() or simbolo in novos_nao_terminais for simbolo in producao):
                novas_regras[nao_terminal].append(producao)
    
    gramatica.regras = novas_regras
