#User function Template for python3
import math
class Solution:
    def isDeficient (self, x):
        sum=0
        for i in range(1,int(math.sqrt(x))+1):
            if(x%i==0):
                if(x/i==i):
                    sum+=i
                else :
                    sum+=i+x/i
        if(2*x>sum):
            return "YES"
        else:
            return "NO"
                    
        
        # code here 
