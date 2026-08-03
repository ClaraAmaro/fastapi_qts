from app.descontos.descontos import calcular_desconto

def test_retorna_zero_quando_valor_for_zero(): 
    assert calcular_desconto(0, True) == 0

def test_retorna_zero_quando_valor_for_negativo():
    assert calcular_desconto(-5, False) == 0

def test_aplica_desconto_para_cliente_vip():
    assert calcular_desconto(100, True) == 80

def test_aplica_desconto_cliente():
    assert calcular_desconto(100, False) == 90

def test_valor_decimal():
    assert round(calcular_desconto(0.01, False), 3) == 0.009

def test_valor_maior():
    assert calcular_desconto(200, True) == 160