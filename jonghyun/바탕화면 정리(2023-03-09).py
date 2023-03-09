def solution(wallpaper):

    x_min = 100
    y_min = 100
    x_max = -1
    y_max = -1

    for i in range(len(wallpaper)) :
        for j in range(len(wallpaper[i])) :
            if wallpaper[i][j] == '#' :
                x_min = min(x_min, i)
                y_min = min(y_min, j)
                x_max = max(x_max, i)
                y_max = max(y_max, j)

    answer = [x_min, y_min, x_max +1 , y_max +1]
    return answer


print(solution(	[".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))