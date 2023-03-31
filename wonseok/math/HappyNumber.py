# happy number
class Solution:
    def isHappy(self, n: int) -> bool:
        def happyCycle(s, memory):
            result = 0
            list_s = list(map(int,str(s)))
            for i in list_s:
                result += i**2
            if result == 1:
                return True
            elif result in memory:
                return False
            else:
                memory.add(result)
                return happyCycle(result, memory)

        memory = set()
        return happyCycle(n, memory)