#User function Template for python3

class Solution:
    def dupLastIndex(self, arr):
        # Complete the function
        track=[-1,-1]
        dict={}
        for i,j in enumerate(arr):
            if j in dict:
                track[0]=i
                track[1]=j
            dict[j]=i
        return track
