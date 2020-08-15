def resolve():
    '''
    code here
    '''
    X, K, D = [int(item) for item in input().split()]

    if K*D > abs(X):
        temp = K - X // D

        if temp % 2 == 1:
            print(D - X%D)
        else:
            print(X%D)
    else:
        print(abs(X) - K*D)


if __name__ == "__main__":
    resolve()
