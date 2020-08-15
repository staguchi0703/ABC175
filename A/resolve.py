def resolve():
    '''
    code here
    '''
    S = input()

    res = 0
    temp = 0
    for item in S:
        if item == 'R':
            temp += 1
        else:
            temp = 0

        res = max(res, temp)

    print(res)


if __name__ == "__main__":
    resolve()
