class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(start, curr):
            if start == len(s):
                res.append(curr[:])
                return
            for end in range(start + 1, len(s) + 1):
                if s[start: end] == s[start: end][::-1]:
                    curr.append(s[start: end])
                    dfs(end, curr)
                    curr.pop()
        
        dfs(0, [])
        return res

        """
        check if first substring partition is a palindrome, if it is, we move forward, if not repartition


        """
