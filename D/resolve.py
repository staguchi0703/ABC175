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
        cnt = 1
        looped_flag = True
        while Ps[next_node] != i:
            cnt += 1
            if cnt > K:
                looped_flag = False
            else:
                temp_num += Cs[next_node]
                temp_res = max(temp_res, temp_num)
            next_node = Ps[next_node]

        if looped_flag:
            cycle = K // cnt
            tail = K % cnt
            cnt2 = 0
            next_node = i
            while cnt2 <= tail:
                cnt2 += 1
                next_node = Ps[next_node]
                temp_num += Cs[next_node]
                temp_res = max(temp_res, temp_num)
            if temp_num > 0:
                if tail != 0:
                    ans = max(ans, temp_res + cycle*temp_num)
                else:
                    ans = max(ans, temp_res + (cycle-1)*temp_num)
            else:
                ans = max(ans, temp_res)
            
        else:
            ans = max(ans, temp_res)

    print(ans)


if __name__ == "__main__":
    resolve()
