def resolve():
    '''
    code here
    '''
    N = int(input())
    Ls = [int(item) for item in input().split()]
    Ls.sort()
    res = 0
    if N >= 3:
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    if Ls[i] + Ls[j] > Ls[k] and Ls[i] != Ls[j] and Ls[j] != Ls[k] and Ls[k] != Ls[i] :
                        res += 1
    print(res)

if __name__ == "__main__":
    resolve()
