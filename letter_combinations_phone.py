# DFS
# March 4, 2021

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        
        def dfs(digits, map, result, string, index):
            if index == len(digits):
                result.append(string)
                return
            
            letters = map[int(digits[index])-1]
            for letter in letters:
                string += letter
                dfs(digits, map, result, string, index+1)
                string = string[:-1]

        if len(digits) > 0:
            map = ['', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
            dfs(digits, map, result, "", 0)
        return result