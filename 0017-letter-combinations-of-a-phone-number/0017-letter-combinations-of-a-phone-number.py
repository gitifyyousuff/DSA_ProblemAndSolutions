class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        #hashmap with respective values hard coded
        phone_dict = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }
        
        #recursion call
        def backtrack(i,currentString):

            #base case
            if len(digits)==len(currentString):
                result.append(currentString)
                return
            #iterate each char in given digits
            for char in phone_dict[digits[i]]:
                backtrack(i+1,currentString+char)

        backtrack(0,"")
        return result