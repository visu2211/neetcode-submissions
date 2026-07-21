class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        n airports (0, n - 1)
        flights are edges airports are vertices

        no duplicate flights
        no circular flights

        k is max number of layovers (does not include src and dst)

        return cheapest price or -1 if impossible

        impossible if there is no path from src to dst

        dijkstras algorithm

            starting at source
            we add all the neighbors on and choose the cheapest neighbor

        dont have to overcomplicate visited since if we can assume that if a node has been visited, its cheapest path has already been considered

        I overgeneralized Dijkstra's assumption that the first (cheapest) visit to a node is always optimal
        , but this problem forces me to consider both the cost and the number of stops used, 
        so the same node may need to be explored multiple times with different stop counts.


        Bellman Ford
            start at source node
            do a BFS

            we use a backup array so we can see the difference it takes for a single iteration

            in the for loop, you build it level by level so i represents which node you are at and you are building shortest paths from there
            every iteration we extend one edge from the src, this cuts off any legs with too many layovers
        """
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:
                #no direct edge to this destination yet
                if prices[s] == float("inf"):
                    continue
                #if we found a new shortest path to the new destination
                tmpPrices[d] = min(prices[s] + p, tmpPrices[d])
            prices = tmpPrices
        return prices[dst] if prices[dst] != float("inf") else -1




            
                
            

