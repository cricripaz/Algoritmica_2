

length = [1,3,5,7]
prices = [20,15,30,50]


dp = [int] * 100000

def solve_dp(size_barra):
    gananciaMaxima = [int]
    if(size_barra == 0):
        return 0

    if(dp[size_barra] == -1):
        gananciaMaxima = -1

        for i in 4 :
            if(size_barra >= length[i]):
                gananciaMaxima =  max(gananciaMaxima , prices[i] + solve_dp(size_barra - length[i]))

    dp[size_barra] = gananciaMaxima

    return dp[size_barra]



if __name__ == '__main__':
    print("rod cutting")


    print(solve_dp(6))
