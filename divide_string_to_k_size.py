class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        rem=len(s)%k
        l=[]
       
        c=""
        for i in range(0,len(s)):
            c+=s[i]
            if(len(c)==k):
                l.append(c)
                c=""
        
        if(rem):
            for i in range(0,k-rem):
                c+=fill
                if(len(c)==k):
                    l.append(c)
                    c=""
                
        return l
            
         
       
            
            
        
