class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        """
        words are sorted in lexicographic order according to alien dictionary
        we want to come up with an order amongst letters given different words

        creating a directed graph
        smaller letters point to larger letters
        we keep track of the indegrees to show how many letters must be processed first before processing that letter

        create an adjacency list
        create an indegrees list
        """
        indegree = {}
        adjList = defaultdict(set)

        for w in words:
            for l in w:
                indegree[l] = 0

        
        for i in range(1, len(words)):
            a, b = words[i - 1], words[i]
            if len(a) > len(b) and a.startswith(b):
                    return ""

            for i in range(min(len(a), len(b))):
                l1, l2 = a[i], b[i]
                
                if l1 != l2:
                    if l2 not in adjList[l1]:
                        adjList[l1].add(l2)
                        indegree[l2] += 1
                    break
        
        queue = deque()
        for k, v in indegree.items():
            if v == 0:
                queue.append(k)

        res = ""
        print(queue)
        while queue:
            node = queue.popleft()
            res += node

            for neigh in adjList[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        #impossible if there is a cycle in the graph --> items are still in the queue
        return "" if len(indegree) != len(res) else res
