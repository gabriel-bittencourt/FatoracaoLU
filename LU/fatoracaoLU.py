from files import readFile, writeFile
from matriz import *

# Funcao que troca as linhas da matriz
def changeRows(matriz, i, j):
    # for k in range(len(matriz)):
    #     print(matriz[k])
    aux = matriz[i]
    matriz[i] = matriz[j]
    matriz[j] = aux
    # print("--------------")
    # for k in range(len(matriz)):
    #     print(matriz[k])
    # print("~~~~~~~~~~")
    return matriz


# Calcula o valor absoluto
def abs(x):
    if x < 0:
        return -x
    return x


def pivoting(matriz, i):
    N = len(matriz)  # Ordem da Matriz

    if(i != len(matriz)-1):
        den = matriz[i][i]

        for linha in range(i+1, N):
            num = matriz[linha][i]

            for coluna in range(i, N):
                matriz[linha][coluna] -= (num / den) * matriz[i][coluna]

            # Constrói a matriz L
            matriz[linha][i] = num / den


def gauss(matriz, B):
    N = len(matriz)  # Ordem da Matriz
    
    L = matrizIdentidade(N)

    for i in range(N):
        # O primeiro pivo selecionado é o elemento da diagonal
        pivo = matriz[i][i]

        for j in range(i + 1, N):

            # Se houver elementos na coluna que o valor absoluto é maior que o pivo
            # e é diferente de zero, este será o novo pivo
            if (abs(matriz[j][i]) > pivo and matriz[j][i] != 0):
                pivo = matriz[j][i]
                matriz = changeRows(matriz, i, j)
                B = changeRows(B, i, j)

        pivoting(matriz, i)

    # Atualiza as matrizes U e L
    for coluna in range(0, N):
        for linha in range(coluna+1, N):
            L[linha][coluna] = matriz[linha][coluna] # Matriz L
            matriz[linha][coluna] = 0                # Matriz U

    return matriz, L, B


matriz, rows, columns = readFile()

# Matriz lida do arquivo texto
print("\nMatriz A")
imprimeMatriz(matriz)

# Matriz identidade que 
B = matrizIdentidade(rows)

# Matrizes L, U e B após a fatoração LU da matriz A
U, L, B = gauss(matriz, B)

print("----------------------------\n")

print("Matriz L")
imprimeMatriz(U)

print("Matriz U")
imprimeMatriz(L) 

print("----------------------------")


"""
   Em um sistema:

   AX = B <==> LUX = B

   onde X é uma matriz de mesma ordem de A
   e B é uma matriz identidade de mesma ordem de A

   Então X é a inversa de A
"""

# Calcula a matriz inversa
B = matrizInversa(L, U, B)

print("Matriz Inversa de A")
imprimeMatriz(B)

# Escreve a matriz em um arquivo texto
writeFile(B)
