listas=[[1,2,3,0,4,-8],[4,50,678,75644321,80000],[7,8,9,10]]

elevar = lambda x,y: x if (x<(y**5)) else 0

menores = list(map(lambda x: filter(elevar, x,x[0]),listas))

print(menores)
