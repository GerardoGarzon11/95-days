# queries-on-a-permutation-with-key

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [x for x in range(1, m+1)]
        results = []
        
        for query in queries:
            results.append(P.index(query))
            P.insert(0, P.pop(P.index(query)))
            
        return results
