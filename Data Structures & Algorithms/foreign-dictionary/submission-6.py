class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        we need an order amongst letters
            topological sort --> kahn's algorithm
        """
        graph = defaultdict(list)
        indegree = {}
        
        for word in words:
            for c in word:
                if c not in indegree:
                    indegree[c] = 0

        for i in range(len(words) - 1):
            fword = words[i]
            sword = words[i + 1]

            if len(fword) > len(sword) and fword.startswith(sword):
                return ""

            for j in range(min(len(fword), len(sword))):
                f, s = fword[j], sword[j]

                if f != s:
                    if s not in graph[f]:
                        graph[f].append(s)
                        indegree[s] += 1
                    break

        q = deque()
        for k, v in indegree.items():
            if v == 0:
                q.append(k)

        res = ""

        while q:
            node = q.popleft()
            res += node
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        return res if len(res) == len(indegree) else ""