numeros=[4526,2468,3687,846,228,9746,357,86422]

filtrados= list(filter(lambda x: x%2 ==0 ,numeros))
lista= list(map(lambda x: map(int, str(x)) ,filtrados))

print(filtrados)
print(lista)
