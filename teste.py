def amigo(arr):
    return [animal for animal in arr if isinstance(animal,list)]

print(amigo([1,'a',2,4,False,56,7,True]))