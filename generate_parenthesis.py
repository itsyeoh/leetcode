# DFS
# March 4, 2021

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def dfs(result, left, right, string):
            if left == right == 0:
                result.append(string)
                return
            
            if left > 0:
                dfs(result, left-1, right, string+"(")
            if left < right:
                dfs(result, left, right-1, string+")")
            
        if n > 0:
            dfs(result, n, n, "")
        return result