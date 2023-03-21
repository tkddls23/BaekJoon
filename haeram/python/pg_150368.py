from itertools import product

def solution(users, emoticons):
    ans = [0, 0]
    cand = list(product([10, 20, 30, 40], repeat=len(emoticons)))

    print(cand)
    
    for discount in cand:
        cur_emo = []
        income = 0
        gain = 0
        
        for i in range(len(emoticons)):
            cur_emo.append([discount[i], int(emoticons[i] * (100-discount[i])*0.01)])
            
            for user in users: # 유저 별 탐색
                user_buy = 0
                gain_flag = 0
                for emo in cur_emo: # 유저 별, 이모티콘 순회
                    if(emo[0] >= user[0]):
                        user_buy += emo[1]
                    
                    if(user_buy > user[1]):
                        gain_flag += 1
                        break
                        
                # 이 유저는 이모티콘 플러스인가 아니면 구매했는가
                if(gain_flag):
                    gain += 1
                else:
                    income += user_buy
            
        if(gain > ans[0]):
            ans = [gain, income]
        elif(gain == ans[0], income > ans[1]):
            ans = [gain, income]
        
        
    print(ans)

solution([[40, 10000], [25, 10000]], [7000, 9000])