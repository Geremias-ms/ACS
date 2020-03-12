#Essa função recebe como entrada uma lista contendo nome, email, cargo
# e salário-base e retorna como resultado o 
# salário líquido desse funcionário.

#Observe abaixo um exemplo para a lista de entrada da função:
#["Marcílio dos Santos", "marcilio@email.com", "DESENVOLVEDOR", 5000.00]
#De acordo com seu cargo, a regra para cálculo do salário líquido é diferente:
#Se o cargo for DESENVOLVEDOR, o funcionário terá desconto de 20% caso o salário seja maior ou igual que 2.000,00, ou apenas 10% caso o salário seja menor que isso.
#Se o cargo for ANALISTA, o funcionário terá desconto de 25% caso o salário seja maior ou igual que 4.000,00, ou apenas 15% caso o salário seja menor que isso.
#Se o cargo for GERENTE, o funcionário terá desconto de 30% caso o salário seja maior ou  igual que 5.500,00, ou apenas 20% caso o salário seja menor que isso.  
#Se o cargo for diferente dos citados acima, a função deve gerar uma exceção do tipo TypeError
#A função deve apenas gerar a exceção (raise TypeError), não é necessário fazer o tratamento da exceção (try/except).

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
        return raise TypeError
        

