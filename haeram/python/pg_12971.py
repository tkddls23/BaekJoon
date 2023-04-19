def solution(sticker):
    length = len(sticker)
    
    if length == 1:
        return sticker[0]
    if length == 2:
        return max(sticker[0], sticker[1])
    
    ans = 0
        
    dp = [0]*length
    # 첫 번째를 선택하는 경우 : 1, length-1번 선택 불가능
    dp[0] = sticker[0]
    dp[1] = dp[0]
    for i in range(2, length-1):
        dp[i] = max(dp[i-2]+sticker[i], dp[i-1]) # 지금껄 고른거랑, 이전껄 선택한 것 중에서 비교
        
    ans = max(dp[length-3], dp[length-2])
    # print(dp)
    
    # 1번째를 선택하는 경우 : 0번째 선택 불가능
    dp = [0]*length
    dp[1] = sticker[1]
    for i in range(2, length):
        dp[i] = max(dp[i-2]+sticker[i], dp[i-1])
        
    ans = max(ans, dp[length-2], dp[length-1])
        
    return ans