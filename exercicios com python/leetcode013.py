equação = input("Digite uma equação: ")

def parenteses_validos(equação):
    pilha = []
    for i in equação:
        if i == "(" or i == "[" or i == "{":
            pilha.append(i)
        elif i == ")" or i == "]" or i == "}":
            if not pilha:
                return False
            if i == ")" and pilha[-1] == "(":
                pilha.pop()
            elif i == "]" and pilha[-1] == "[":
                pilha.pop()
            elif i == "}" and pilha[-1] == "{":
                pilha.pop()
            else:
                return False
    return not pilha

print(parenteses_validos(equação))