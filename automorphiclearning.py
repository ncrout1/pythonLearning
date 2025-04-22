class Solution:
	def is_AutomorphicNumber(self, n):
	    result=pow(n,2)
	    if(result%10==n%10):
	        return "Automorphic"
	    else:
	        return "Not Automorphic"
		# Code here
# Given a number N, check whether the number is Automorphic number or not.
# A number is called Automorphic number if and only if its square ends in  has the same last digit as the number itself.
