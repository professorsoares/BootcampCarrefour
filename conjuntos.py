

# Trabalhando com Listas

#!/usr/bin/env python
# coding: utf-8

lista = [1,3,7,5]
lista_animal = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante', 'lobo', 'arara']

print(lista_animal)
print(lista_animal.pop(2))
print(lista_animal)


print("-----------------------------------------")

# Lista pode alterar um vvalor:
#
# print(lista_animal)
lista_animal[0] = "macaco"


print("\nDesOrdenado:")
print(lista_animal)

print("\nOrdenado:")
lista_animal.sort()
print(lista_animal)

print("\nOrdenado inversamente:")
lista_animal.reverse()
print(lista_animal)
print("-----------------------------------------")

# Trabalhando com Tuplas



# Organizando conjuntos e subconjuntos de elementos em Python

conjunto  = {1,2,3,4,5,1}
conjunto2 = {5,6,7,8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))

conjunto_interseccao =  conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))


print("-----------------------------------------")
print("\nDiferença:")
conjunto_diferenca = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
conjunto_diff_simetrica2 = conjunto2.symmetric_difference(conjunto)
print('Diferença Simetrica: {}'.format(conjunto_diff_simetrica))

conjunto_interseccao =  conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subset de B: {}'.format(conjunto_interseccao))
conjunto_superset = conjunto_a.issubset(conjunto_b)
print('B é superconjunto de A: {}'.format(conjunto_superset))

conjunto3 = {6, 2, 2, 1, 4, 5}
print(conjunto3)
conjunto3.discard(5)    #remover
print(conjunto3)

tp_teste = tuple(conjunto)      # converte a lista em Tupla
print(tp_teste)


ls_teste = list(conjunto)
print(ls_teste)

teste = set(ls_teste)
print(type(teste))

#Quando quisermos ordenar uma lista, basta transformá-la em um set(conjunto) e depois retornar para lista, caso tenha necessidade.

