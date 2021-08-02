def generateC(X, Y, m, n):
    C = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C


def printC(C):
    for i in C:
        print('\t'.join(map(str, i)))

def backtrack(C, X, Y, i, j):
    #print(C)
    if i == 0 or j == 0:
        return ""
    if X[i-1] == Y[j-1]:
        return backtrack(C,X,Y,i-1,j-1) + X[i-1]
    if C[i][j-1] > C[i-1][j]:
        return backtrack(C,X,Y,i, j-1)
    return backtrack(C, X, Y, i-1, j)





if __name__ == "__main__":
    # Cited and Test case retreived from Geeks For Geeks
    # https://www.geeksforgeeks.org/printing-longest-common-subsequence/
    string1 = "AGGTAB"
    string2 = "GXTXAYB"

    m = len(string1)
    n = len(string2)
    C = generateC(string1, string2, m, n)

    strs = backtrack(C, string1, string2, m, n)

    print("The Longest Common Subsequence is: " + strs)


    string1 = "Minneapolis"
    string2 = "Minnesota"

    m = len(string1)
    n = len(string2)
    C = generateC(string1, string2, m, n)

    strs = backtrack(C, string1, string2, m, n)

    print("The Longest Common Subsequence is: " + strs)

