class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic = {"1" : 1, "2" : 2,  "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "0" : 0}
        n1 = n2 = 0
        c = 0
        for i in range(len(num1) -1, -1, -1):
            n1 += dic[num1[i]] * (10 ** c)
            c += 1
        c = 0
        for i in range(len(num2) -1, -1, -1):
            n2 += dic[num2[i]] * (10 ** c)
            c += 1
        mult = n1 * n2
        s = ""
        inv_map = {v: k for k, v in dic.items()}
        if (mult == 0):
            return "0"
        while mult > 0:
            s += inv_map[mult % 10]
            mult //= 10
        return s[::-1]