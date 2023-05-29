
import tokeniza as tk

import operadores as op
from googletrans import Translator

PROMPT = "expressão >>> "
QUIT   = ''

def translate_text(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src='pt', dest='en')
    return translation.text

def translate_textPT(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src='en', dest='pt')
    return translation.text

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            frases = arquivo.readlines()
        return frases
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {str(e)}")
        return []


nome_arquivo = 'frases.txt' 

frases = ler_arquivo("frases.txt")

if frases:
    frases_array = [frase.strip() for frase in frases]
    print(f"Frases lidas do arquivo '{nome_arquivo}':")
    print(frases_array)
else:
    print("Não foram encontradas frases no arquivo.")


def main():

    for frase in frases_array:
        frase = translate_text(frase)
        lista_tokens = tk.tokeniza(frase)
        for token in lista_tokens:
            item, tipo = token
            if tipo == tk.PALAVRAS_NEGATIVAS:
                item = translate_textPT(item)
                descricao = "'%s' : Frase negativa" %item
            else:
                item = translate_textPT(item)
                descricao = "'%s' : Palavras positivas" %item
            print(descricao)       

main()