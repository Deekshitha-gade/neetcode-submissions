class Solution:
    def isPalindrome(self, s: str) -> bool:
        new=""
        for i in s:
            if i.isalnum():
                new+=i.lower()
        p=new
        if new==p[::-1]:
            return True
        else:
            return False
        