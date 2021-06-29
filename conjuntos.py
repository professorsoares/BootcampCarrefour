

# Trabalhando com Listas



# Trabalhando com Tuplas



# Organizando conjuntos e subconjuntos de elementos em Python

conjunto  = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))

conjunto_interseccao =  conjunto.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_interseccao))

conjunto3 = {6, 2, 2, 1, 4, 5}
print(conjunto3)
conjunto3.discard(5)
print(conjunto3)

tp_teste = tuple(conjunto)
print(tp_teste)


ls_teste = list(conjunto)
print(ls_teste)

teste = set(ls_teste)
print(type(teste))

#Quando quisermos ordenar uma lista, basta transformá-la em um set(conjunto) e depois retornar para lista, caso tenha necessidade.
