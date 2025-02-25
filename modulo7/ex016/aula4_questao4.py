'''Escreva um programa em Python para executar o jogo, de acordo com as definições:

Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;

Permita que o jogador insira letras para adivinhar a palavra;

Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;

Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;

Limite o número de tentativas para 6 (as partes do enforcado).'''
#bibliotecas 
import random
#funcoes
def verificar_tentativa(letra, tentativas):
    if letra.lower() not in tentativas: 
            tentativas.append(letra.lower())
            return True
    return False
#listas e variaveis
tentativas = []
erros = 0
#abertura arquivos de texto
with open("gabarito_forca.txt","r", encoding="utf-8") as arquivo: 
    palavras = arquivo.read().splitlines()
with open("gabarito_enforcado.txt", "r", encoding="utf-8") as file: 
    enforcado = file.read().split("\n\n\n")
#palavra aleatoria
if palavras: 
     print(enforcado[0])
     palavra = random.choice(palavras).lower()
     oculta = list("_" * len(palavra))
     print("\n" + " ".join(oculta))
#laço
while True: 
     entrada = input("\nDigite uma letra: ").lower()
     if len(entrada) != 1 or not entrada.isalpha(): 
          print("Digite apenas uma letra válida")
          continue
     if entrada in tentativas: 
          print("Você já tentou essa letra, escolha outra")
          continue
     if verificar_tentativa(entrada, tentativas): 
      if entrada in palavra: 
        for i in range(len(palavra)): 
            if palavra[i] == entrada: 
                oculta[i] = entrada
        print(" ".join(oculta))
        
        # Verificação de vitória
        if "_" not in oculta: 
            print("Parabéns! Você acertou a palavra!")
            break
      else:
        erros += 1
        print(f"Letra errada! Você tem {6 - erros} tentativas restantes")
        print(enforcado[min(erros, 6)])  # Exibe a parte do desenho correspondente
        if erros == 6: 
            print("Você perdeu! A palavra era:", palavra)
            break
#aumentei muito a lista do gabarito pois acabei jogando o jogo de verdade