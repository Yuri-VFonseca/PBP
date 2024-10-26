'''3) Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. Você deve imprimir a lista antes e depois da deleção.

Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]
Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]'''
# Gerar lista aleatória com 20 elementos entre -10 e 10
import random

# Gerar lista aleatória com 20 elementos entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

# Variáveis para rastrear sequências de números negativos
negativos = []
inicio = -1
tamanho_max = 0

# Percorrer a lista para identificar sequências de números negativos
for i in range(len(lista)):
    if lista[i] < 0:
        if inicio == -1:  # Começou uma nova sequência
            inicio = i
        # Continuar contando negativos
    else:
        if inicio != -1:  # Uma sequência terminou
            tamanho = i - inicio
            negativos.append((inicio, i - 1, tamanho))  # Armazena o índice inicial, final e o tamanho
            if tamanho > tamanho_max:
                tamanho_max = tamanho
            inicio = -1  # Resetar

# Se a lista terminar com uma sequência negativa, precisamos adicioná-la
if inicio != -1:
    tamanho = len(lista) - inicio
    negativos.append((inicio, len(lista) - 1, tamanho))
    if tamanho > tamanho_max:
        tamanho_max = tamanho

# Criar uma lista com os intervalos a serem removidos
intervalos_remover = [negativo for negativo in negativos if negativo[2] == tamanho_max]

# Remover as sequências de tamanho máximo
for intervalo in sorted(intervalos_remover, key=lambda x: x[0], reverse=True):
    del lista[intervalo[0]:intervalo[1] + 1]

print("Editada:", lista)
