class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        """
        Topological Sort - Kahn's Algorithm

        create adjacency list
        create indegrees

        come up with order through iterating through words

        find indegrees with 0 and then shrink
        """
        adjList = defaultdict(list)
        indegrees = {}

        for w in words:
            for c in w:
                indegrees[c] = 0
        
        for i in range(len(words) - 1):
            fword, sword = words[i], words[i + 1]

            if len(fword) > len(sword) and fword.startswith(sword):
                return ""

            for j in range(min(len(fword), len(sword))):
                f, s = fword[j], sword[j]

                if f != s:
                    if s not in adjList[f]:
                        adjList[f].append(s)
                        indegrees[s] += 1
                    break
            
        q = deque()
        for k, v in indegrees.items():
            if v == 0:
                q.append(k)

        res = ""
        while q:
            node = q.popleft()
            res += node

            for neigh in adjList[node]:
                indegrees[neigh] -= 1
                if indegrees[neigh] == 0:
                    q.append(neigh)
        return "" if len(indegrees) != len(res) else res

