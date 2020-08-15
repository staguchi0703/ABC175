def resolve():
    '''
    code here
    '''
    N, K = [int(item) for item in input().split()]
    Ps = [int(item)-1 for item in input().split()]
    Cs = [int(item) for item in input().split()]

    loops = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        next_node = i
        loops[i][i] = 1
        while True:
            next_node = Ps[next_node]
            if loops[i][next_node] != 1:
                loops[i][next_node] = 1
            else:
                break

    prio_num = [0 for _ in range(N)]
    for i in range(N):
        prio_num[i] = sum(loops[i])

    # print(prio_num)
    res_list = [0 for _ in range(N)]
    for i in range(N):
        num = K % prio_num[i]
        if num == 0:
            num = K

        prio = prio_num[i]
        cnt = 0
        temp_num = 0
        prio_num1 = 0

        next_node = i
        temp_max = -10000000000000000
        while cnt < prio:
            next_node = Ps[next_node]
            prio_num1 += Cs[next_node]
            
            if cnt < num:
                temp_num += Cs[next_node]
                temp_max = max(temp_max, temp_num)
                # print(i, temp_num, temp_max)
            cnt += 1

        if prio_num1 > 0:
            res_list[i] = temp_max + prio_num1 * (K //prio)
        else:
            res_list[i] = temp_max

    # print(res_list)
    print(max(res_list))

if __name__ == "__main__":
    resolve()
