# Gerenciando dicionarios

def notas(*n, sit = False):
    n = {}

    n["Total"] = len(n)
    n["Maior"] = max(n)
    n["Menor"] = min(n)
    n["Media"] = sum(n) / len(n)

    if sit:
        if n["Media"] >= 7:
            n["Situacao"] = 'BOA'

        elif n["Media"] >= 5:
            n["Situacao"] = 'RAZOAVEL'

        else:
            n["Situacao"] = 'RUIM'

    return n

resposta = notas(5, 6, 8, 4, 9, sit = True)
print(resposta)