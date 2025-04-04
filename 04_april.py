class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        s=list(s)
        for i in range(len(s)//2):
            temp=s[i]
            s[i]=s[len(s)-1-i]
            s[len(s)-1-i]=temp
        s=''.join(s)    
        return s
