class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp={}
        for i in nums:
            mp[i]=1+mp.get(i,0)
        arr=[]
        for i,j in mp.items():
            arr.append([j,i])
        arr.sort()
        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
