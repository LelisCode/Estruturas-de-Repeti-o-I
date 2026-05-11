

# 1. Validador de Complexidade de Senha

# Garantir que uma senha tenha o comprimento mínimo e caracteres especiais.
# Regras:
# 1. Comprimento mínimo: 8 caracteres;
# 2. Um caracter maiúsculo;
# 3. Um caracter minúsculo;
# 4. Um caracter especial;
# 5. Um número;

# Lógica: Percorrer a string caractere por caractere para validar critérios.
# Resultado Esperado: "Senha forte" ou lista de requisitos ausentes.


import string

def processar_s(s):
    especiais = r"!@#$%^&*()-_=+[]{};:,.<>?/\\|"
    
    match s:
        #Lê a lista e confere se são 8 digitos
        case s if len(s) < 8:
            return "Erro: a senha deve ter pelo menos 8 caracteres."
        #Confere se a senha contem apenas números
        case s if s.isdigit():
            return "Erro: a senha contém apenas números."
        #Confere se existem apenas digitos maiúsculos    
        case s if s.isupper():
            return "Erro: a senha contém apenas letras maiúsculas."
         #Confere se existem apenas digitos minusculos
        case s if s.islower():
            return "Erro: a senha contém apenas letras minúsculas."
         #Confere se a senha tem pelo menos um caractere especial
        case s if not any(c in especiais for c in s): 
            return "Erro: a senha não contém nenhum caractere especial."
        #Caso a senha esteja correta  
        case _:
            return "Senha correta!"


s = input("Digite sua senha: ")
print(processar_s(s))
