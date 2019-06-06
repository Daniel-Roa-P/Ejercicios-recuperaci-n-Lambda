numeros=[[4,52,6],[2,4,6,8],[36,87],[8,46],[22,8],[97,46],[3,5,7],[8,64,22]]

lambda x,y: x if (x > y) else y

mayores = list(map(lambda x: reduce(lambda x,y: x if (x > y) else y, x) ,numeros))

print(mayores)
