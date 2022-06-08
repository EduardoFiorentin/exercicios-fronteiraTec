try:
    #cria uma lista com todos os valores digitados
    array = list(map(int, input("Numeros: ").split()))
    #coloca a lista em ordem crescente
    array.sort() 

    menor_numero = array[0]
    ocorrencias = 0

    # verifica a quantidade de vezes que o menor número aparece
    for numero in array:
        if numero == menor_numero:
            ocorrencias += 1
        else:
            break

except: 
    print("ERRO! Verifique as informações e tente novamente.")

else:
    final = 'vez.' if ocorrencias == 1 else 'vezes.'

    print(f"O menor numero é {menor_numero} e ele aparece {ocorrencias} {final}")