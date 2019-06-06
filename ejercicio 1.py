listas=[[1,2,3,4],[4,5,6,7],[7,8,9,10]]

elementos = list(map(lambda x: x[0] ,listas)+ map(lambda x: x[3] ,listas))

print(elementos)


