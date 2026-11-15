class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i = 0 
        j = len(s)-1

        while i < j:
            print(f"i={i}, j={j}")
            while s[i].isalnum() == False and i < j:
                i += 1
            while s[j].isalnum() == False and j > i:
                j -= 1
            if (s[i].isalnum() == False and s[j].isalnum() == False) or s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True
            

        