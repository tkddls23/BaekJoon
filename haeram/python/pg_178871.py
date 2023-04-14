def solution(players, callings):
    name_rank = {}
    rank_name = {}
    
    for i in range(len(players)):
        name_rank[players[i]] = i
        rank_name[i] = players[i]
        
    for call in callings:
        cur_rank = name_rank[call]
        
        prev_name = rank_name[cur_rank-1] # 나보다 하나 앞에 있는 애 이름
        
        name_rank[call] = cur_rank - 1 # 지금 불린 애는 하나 앞으로
        name_rank[prev_name] = cur_rank # 앞에 있던 애는 하나 뒤로
        
        rank_name[cur_rank-1] = call
        rank_name[cur_rank] = prev_name
        
    return list(rank_name.values())
        
        
    