import ac02

try:
    lista = ["Marcílio dos Santos", "marcilio@email.com", "DESENVOLVEDOR", 5000.00]
    test = ac02.salario_liquido(lista)
    assert test == 4000.00
    print("Correto")
except AssertionError:
    print("Erro")
    print("Retorno: ", test)
    print("Esperado: ", 4000.00)
    
try:
    lista = ["Marinalva Aparecida", "marizinha@email.com", "DESENVOLVEDOR", 1500.00]
    test = ac02.salario_liquido(lista)
    assert test == 1350.00
    print("Correto")
except AssertionError:
    print("Erro")
    print("Retorno: ", test)
    print("Esperado: ", 1350.00)
    
