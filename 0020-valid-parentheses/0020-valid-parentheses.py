class Solution:
    def isValid(self, s: str) -> bool:
        Stack = []
        pairDict = { "}" : "{" , ")" : "(" , "]" : "[" }

        for c in s:
            if c in pairDict:
                if Stack and Stack[-1] == pairDict[c]:
                    Stack.pop()
                else: 
                    return False
            else:
                Stack.append(c)
        return True if not Stack else False
