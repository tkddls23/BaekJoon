def solution(numbers):
    doubleNums = set()
    
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers):
            if i == j:
                continue
            doubleNums.add(num1 + num2)

    return sorted(doubleNums)