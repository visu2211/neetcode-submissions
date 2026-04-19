class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = defaultdict(set)
        indegree = {}

        for word in words:
            for c in word:
                if c not in indegree:
                    indegree[c] = 0
        
        #Build adjacency list with relations

        #if odd numbered list, we 
        for i in range(len(words) - 1):
            fword = words[i]
            sword = words[i + 1]

            #compute relation between characters
            #if fword longer than sword and sword is a prefix return
            if len(fword) > len(sword) and fword.startswith(sword):
                return ""
            
            for j in range(min(len(fword), len(sword))):
                f, s = fword[j], sword[j]

                #create order relation between characters
                #adjList and indegree increment
                if f != s:
                    # if f in adjList[s]:
                    #     return ""
                    if s not in adjList[f]:
                        adjList[f].add(s)
                        indegree[s] += 1
                    break
            #Now adjlist and indegree arrays are built. Ready for Kahn's Algorithm

        #Kahn's Algorithm, find indegrees that are 0, and trim
        q = deque()

        for k, v in indegree.items():
            if v == 0:
                q.append(k)

        res = ""

        #if a cycle occurs, it will never enter the queue since its indegree will always be == 1 

        while q:
            char = q.popleft()
            res += char

            #reduce indegrees
            for neigh in adjList[char]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        return "" if len(indegree) > len(res) else res