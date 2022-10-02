num_list = []
num_dic = {}
x = 0
while num_list != [0,0,0] :
    num_list = list(map(int, input().split()))

    if num_list != [0,0,0]: 
        num_dic[x] = num_list 
        x += 1


for i in range(len(num_dic)):
    heru = max(num_dic[i])
    num_dic[i].remove(heru)
    ausar = num_dic[i].pop()
    auset = num_dic[i].pop()

    if (ausar**2 + auset**2) == heru**2 :
        print("right")
    else:
        print("wrong")