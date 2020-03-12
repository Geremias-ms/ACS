# GEREMIAS MARTINS DOS SANTOS RA:1901844
# NATALIA


def salario_liquido(lista):
    if lista[2] == "DESENVOLVEDOR":
        if lista[3] >= 2000.00:
            sal = lista[3]
            desc = sal - (sal * 0.2)
            return desc
        else:
            sal = lista[3]
            desc = sal - (sal * 0.1)
            return desc
    elif lista[2] == "ANALISTA":
        if lista[3] >= 4000.00:
            sal = lista[3]
            desc = sal - (sal * 0.25)
            return desc
        else:
            sal = lista[3]
            desc = sal - (sal * 0.15)
            return desc
    elif lista[2] == 'GERENTE':
        if lista[3] >= 5500.00:
            sal = lista[3]
            desc = sal - (sal * 0.30)
            return desc
        else:
            sal = lista[3]
            desc = sal - (sal * 0.20)
            return desc
    else:
        raise TypeError
