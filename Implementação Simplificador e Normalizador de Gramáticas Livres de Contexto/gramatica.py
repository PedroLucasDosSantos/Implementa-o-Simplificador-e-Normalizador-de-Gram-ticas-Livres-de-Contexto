class Gramatica:
    def __init__(self):
        self.regras = {}
    
    def adicionar_regra(self, nao_terminal, producoes):
        if nao_terminal not in self.regras:
            self.regras[nao_terminal] = []
        self.regras[nao_terminal].extend(producoes)
    
    def __str__(self):
        result = ""
        for nao_terminal, producoes in self.regras.items():
            result += f"{nao_terminal} -> {' | '.join(producoes)}\n"
        return result
