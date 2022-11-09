PalindromeList = []

while True:
    word = input()
    if word != "0":
        PalindromeList.append(word)
    else:
        break
for i in PalindromeList:
    if i == i[::-1]:
        print("yes")
    else:
        print("no")