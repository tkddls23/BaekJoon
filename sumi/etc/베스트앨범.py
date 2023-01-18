def solution(genres, plays):
    dict = {}
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        dict[genre] = dict[genre] + [(play, i)] if genre in dict else [(play, i)]

    lengths = []
    for key in dict:
        sum_t = 0
        for x in dict[key]:
            sum_t += x[0]
        lengths.append((key, sum_t))

    lengths.sort(key=lambda x: x[1], reverse=True)

    answer = []
    # 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
    for key, l in lengths:
        cnt = 0
        current_list = dict[key]
        # 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
        current_list.sort(key=lambda x: x[1])
        # 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
        current_list.sort(key=lambda x: x[0], reverse=True)

        for play_cnt, idx in current_list:
            if cnt >= 2:  break;
            answer.append(idx)
            cnt += 1

    return answer