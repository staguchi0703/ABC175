def resolve():
    '''
    code here
    '''
    N, K = [int(item) for item in input().split()]
    Ps = [int(item)-1 for item in input().split()]
    Cs = [int(item) for item in input().split()]

    ans = -100**5
    for i in range(N):
        next_node = i
        temp_num = 0
        temp_res = -100**5
        cnt = 0
        looped_flag = True
        while Ps[next_node] != i:
            if cnt >= K:
                looped_flag = False
                break
            next_node = Ps[next_node]
            temp_num += Cs[next_node]
            ans = max(ans, temp_num)
            cnt += 1

        if temp_num > 0 and looped_flag:
            ans += (K // cnt) * temp_num

        ans = max(ans, )




if __name__ == "__main__":
    resolve()
