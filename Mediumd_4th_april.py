# //Problem statement -to find number which is having three divisor

#Given two positive integers L and R, return count of numbers having exactly 3 divisors from L to R inclusive.

#Trick-A number has exactly 3 divisors if and only if it is a square of a prime number. The three divisors are {1, p, p^2}, where p is a prime number.

# This is my own solution

class Solution:
    def count3DivNums(self, L, R):
        targeted=0
        for i in range(L,R+1):
            currentDivisor=1
            noOfDivisor=0
            while(i%currentDivisor==0 or currentDivisor<=i):
                if(i%currentDivisor==0):
                    noOfDivisor+=1
                currentDivisor+=1
            if(noOfDivisor==3):
                # print(i)
                targeted+=1
        # print(targeted)
        return targeted




class Solution:
    def count3DivNums(self, L, R):
        l=[True]*(R+1)
        l[0]=l[1]=False
        for i in range(2,int(R**0.5)+1):
            for j in range(i*i,R+1,i):
                l[j]=False
        primelist=[i for i in range(len(l)) if l[i]]
        count=0
        for i in primelist:
            i=i*i
            if (L<=i<=R):
                count+=1
        return count
                    

