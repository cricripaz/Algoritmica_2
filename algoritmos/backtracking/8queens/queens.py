


def esValido(tablero, i, j):
    return (tablero[i][0] != tablero[j][0]) and (abs(tablero[0][i] - tablero[0][j]) == abs(i - j))
#           <- y ->                                       diagonales

def solve8queen(total, tablero):
    if (total == 8):
        return print(tablero)

    for i in range(len(tablero[0])):
        for j in range(len(tablero)):
            if (tablero[i][j] == 0):
                tablero[i][j] = 1
                if (esValido(tablero, i, j)):
                    solve8queen(total + 1, tablero)
                else:
                    tablero[i][j] = 0


def showMatriz(matriz):
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()


if __name__ == '__main__':

    n = 8

    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(n):
            matriz[i].append(0)

    showMatriz(matriz)


    solve8queen(0, matriz)
