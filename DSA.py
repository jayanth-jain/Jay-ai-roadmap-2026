#Two sums
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums[j]:
                    return i,j
              



#Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        counts = {}
        for ch in s:
            count[ch] = count.get(ch,0)+1
        for th in t:
            counts[th] = counts.get(th,0) +1

        return(count == counts)             



