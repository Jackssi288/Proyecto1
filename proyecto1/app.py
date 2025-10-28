def validar_usuario(usuario: str, contraseña: str) -> bool:
    if not usuario or not contraseña:
        return False
    if usuario == "admin" and contraseña == "1234":
        return True
    return False

def sumar(a: int, b: int) -> int:
    return a + b
