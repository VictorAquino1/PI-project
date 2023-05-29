import re
from better_profanity import profanity

# Constantes
TESTE = False

# caracteres usados em operadores
OPERADORES = "%*/+-!^="

# caracteres usados em números inteiros
DIGITOS = "0123456789"

# ponto decimal 
PONTO = "."

# todos os caracteres usados em números float
FLOATS = DIGITOS + PONTO

# caracteres usados em nomes de variáveis
LETRAS = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# abre e fecha parênteses
ABRE_FECHA_PARENTESES = "()"

# categorias
OPERADOR = 1  # para operadores aritméticos e atribuição
NUMERO = 2  # para números: todos são considerados floatw
VARIAVEL = 3  # para variáveis
PARENTESES = 4  # para '(' e ')

# Whitespace characters: space, newline, horizontal tab,
# vertical tab, form feed, carriage return
BRANCOS = [' ', '\n', '\t', '\v', '\f', '\r']

# caractere que indica comentário
COMENTARIO = "#"

# palavras negativas
PALAVRAS_NEGATIVAS = True
PALAVRAS_POSITIVAS = False




#------------------------------------------------------------
def tokeniza(frase):    
    if COMENTARIO in frase:
        frase = frase.split(COMENTARIO, 1)[0]

    tokens = []
    if profanity.contains_profanity(frase) == True:
        tokens.append([frase, PALAVRAS_NEGATIVAS])
    else:
        tokens.append([frase, PALAVRAS_POSITIVAS])

    return tokens