class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1 and n not in visited:
            visited.add(n)
            temp = n
            new_value = 0
            while temp:
                new_value += (temp % 10) ** 2
                temp //= 10
            n = new_value
        return n == 1