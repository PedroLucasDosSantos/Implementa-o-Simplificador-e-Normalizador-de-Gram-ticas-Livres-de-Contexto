def forma_normal_chomsky(gramatica):
    novas_regras = {}
    
    def terminal_para_nao_terminal(terminal):
        nao_terminal = terminal.upper()
        if nao_terminal not in novas_regras:
            novas_regras[nao_terminal] = [terminal]
        return nao_terminal
    
    for nao_terminal, producoes in gramatica.regras.items():
        novas_regras[nao_terminal] = []
        for producao in producoes:
            if len(producao) == 1:
                if producao.islower():
                    novas_regras[nao_terminal].append(producao)
                else:
                    novas_regras[nao_terminal].extend(gramatica.regras[producao])
            elif len(producao) == 2:
                novas_regras[nao_terminal].append(producao)
            else:
                while len(producao) > 2:
                    novas_producoes = []
                    i = 0
                    while i < len(producao) - 1:
                        if producao[i].islower():
                            nt = terminal_para_nao_terminal(producao[i])
                            novas_producoes.append(nt)
                        else:
                            novas_producoes.append(producao[i])
                        i += 1
                    novas_regras[nao_terminal].append(novas_producoes)
                    producao = novas_producoes[-1] + producao[-1]
    
    gramatica.regras = novas_regras
