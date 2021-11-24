from math import sqrt

def euclidiana(base,user1,user2): #faz o calculo de aproximidade dos usuários
    dados = {}

    for item in base[user1]:
        if item in base[user2]:
            dados[item] = 1

    if len(dados) == 0:
        return 0

    soma = sum ([pow(base[user1][item] - base[user2][item],2)
                    for item in base[user1] if item in base[user2]
                ])
    return 1/(1+sqrt(soma))

def getSimilares(base,user): #retorna a similaridade de um usuários com todos os outros usuários
    similaridade = [(euclidiana(base,user, outro), outro)
                    for outro in base if outro != user]
    similaridade.sort()
    similaridade.reverse()
    return similaridade[0:30]


def calculaItensSimilares(base):
    result = {}
    for item in base:
        notas = getSimilares(base,item)
        result[item] = notas
    return result


def getRecomendacoesUsuario(base,user):
    totais = {}
    somasimilaridade = {}

    for outro in base: #percorre usuários
        if outro == user:
            continue

        similaridade = euclidiana(base,user,outro)

        if similaridade <= 0:
            continue

        for item in base[outro]: #percorre bebidas avaliadas pelo usuário
            if item not in base[user]: #verifica os bebidas que não estão avaliados pelo usuario
                totais.setdefault(item,0)
                totais[item] += base[outro][item] * similaridade
                somasimilaridade.setdefault(item,0)
                somasimilaridade[item] += similaridade

    rankings = [(total/somasimilaridade[item],item) for item , total in totais.items()]
    rankings.sort()
    rankings.reverse()
    return rankings[0:30]