class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {"]": "[", ")": "(", "}": "{"}
        string = []

        for char in s:
            if char in hashmap:
                if not string or hashmap[char] != string[-1]:
                    return False
                string.remove(hashmap[char])
            else: 
                string.append(char)
    
        return not string
