listas=[[1,2,3,4],[4,5,6,7],[7,8,9,10]]

primeros = list(map(lambda x: x[0] ,listas))
ultimos = list(map(lambda x: x[3] ,listas))

print(primeros)
print(ultimos)

