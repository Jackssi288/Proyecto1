from proyecto1.app import sumar, validar_usuario

def test_sumar():
    assert sumar(2, 3) == 5

def test_validar_usuario_correcto():
    assert validar_usuario("admin", "1234") == True

def test_validar_usuario_incorrecto():
    assert validar_usuario("user", "4321") == False
