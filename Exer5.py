## Conta letras maiúsculas e minúsculas

# Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.

def char(text):
    dic = {"Uppercase": 0, "Lowercase": 0}
    for check in text:
        if check.isupper():
            dic["Uppercase"] += 1
        else:
            dic["Lowercase"] += 1
    print("Texto original", text)
    print("Letras maiusculas", dic["Uppercase"])
    print("Letras minusculas", dic["Lowercase"])

char("Eu sou um Deus e vou Mostrar minha Verdadeira Personalidade")




## Lista números pares e ímpares de uma lista

# Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.

def list(count):
    pair = []
    impar = []
    for number in count:
        if number % 2 == 0:
            pair.append(number)
        else:
            impar.append(number)
    return pair, impar

print(list([3, 5, 2, 6, 1, 4, 3, 8, 10, 15, 20]))
    

