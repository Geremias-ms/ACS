# GEREMIAS MARTINS DOS SANTOS RA:1901844
# NATALIA DE JESUS DOS SANTOS RA:1901922

import ac02

try:
    lista = ["Marcílio Santos", "marcilio@email.com", "DESENVOLVEDOR", 5000.00]
    test = ac02.salario_liquido(lista)
    assert test == 4000.00
    print("Teste 1 Desenvolvedor: Correto")
except AssertionError:
    print("Teste 1 Desenvolvedor: Erro")
    print("Retorno: ", test)
    print("Esperado: ", 4000.00)

try:
    lista = ["Marcia Souza", "marizinha@email.com", "DESENVOLVEDOR", 1500.00]
    test = ac02.salario_liquido(lista)
    assert test == 1350.00
    print("Teste 2 Desenvolvedor: Correto")
except AssertionError:
    print("Teste 2 Desenvolvedor: Erro")
    print("Retorno: ", test)
    print("Esperado: ", 1350.00)

try:
    lista = ["Marcílio Santos", "marcilio@email.com", "ANALISTA", 4200.00]
    test = ac02.salario_liquido(lista)
    assert test == 3150.00
    print("Teste 1 Analista: Correto")
except AssertionError:
    print("Teste 1 Analista: Erro")
    print("Retorno: ", test)
    print("Esperado: ", 3150.00)

try:
    lista = ["Marcia Souza", "marizinha@email.com", "ANALISTA", 3000.00]
    test = (ac02.salario_liquido(lista))
    assert test == 2550.00
    print("Teste 2 Analista: Correto")
except AssertionError:
    print("Teste 2 Analista: Erro")
    print("Retorno: ", test)
    print("Esperado: ", 2550.00)

try:
    lista = ["Marcia Souza", "marizinha@email.com", "GERENTE", 8000.00]
    test = (ac02.salario_liquido(lista))
    assert test == 5600.00
    print("Teste 1 Gerente: Correto")
except AssertionError:
    print("Teste 1 Gerente: Erro")
    print("Retorno: ", test)
    print("Esperado: ", 5600.00)

try:
    lista = ["Marcílio Santos", "marcilio@email.com", "GERENTE", 5100.00]
    test = ac02.salario_liquido(lista)
    assert test == 4080.00
    print("Teste 2 Gerente: Correto")
except AssertionError:
    print("Teste 2 Gerente: Erro")
    print("Retorno: ", test)
    print("Esperado: ", 4080.00)

try:
    lista = ["Marcílio Santos", "marcilio@email.com", "Analista", 5100.00]
    test = ac02.salario_liquido(lista)
    assert test == 4080.00
    print("Teste: Correto")
except AssertionError:
    print("Teste: Erro")
    print("Retorno: ", test)
    print("Esperado: ", 4080.00)
