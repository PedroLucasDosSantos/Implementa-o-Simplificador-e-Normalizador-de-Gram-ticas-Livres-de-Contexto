def remocao_recursao_esquerda(gramatica):
    novas_regras = {}
    
    for nao_terminal, producoes in gramatica.regras.items():
        recursivas = [p for p in producoes if p.startswith(nao_terminal)]
        nao_recursivas = [p for p in producoes if not p.startswith(nao_terminal)]
        
        if recursivas:
            novo_nao_terminal = nao_terminal + "'"
            novas_regras[nao_terminal] = [p + novo_nao_terminal for p in nao_recursivas]
            novas_regras[novo_nao_terminal] = [p[len(nao_terminal):] + novo_nao_terminal for p in recursivas] + [""]
        else:
            novas_regras[nao_terminal] = producoes
    
    gramatica.regras = novas_regras
