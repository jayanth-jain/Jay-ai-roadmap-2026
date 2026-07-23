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


#1480. Running Sum of 1d Array


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        count = []
        total = 0

        for i in range(len(nums)):
            total = total + nums[i]
            count.append(total)
        return count    
    

 #724. Find Pivot Index

   class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - left - nums[i]
            if left == right:
                return i
            left = left + nums[i]
        return -1       


is_palindrome

    class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_str=""
        for i in range(len(s)):
            if s[i].isalnum():
                my_str+=s[i].lower()


        left = 0
        right = len(my_str) -1
        is_pal=True
        while (left < right):
            if my_str[left] == my_str[right]:
                left+=1
                right-=1
            else:
                is_pal =False
                break
                
        return is_pal          


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        main_price = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if main_price > prices[i]:
                main_price = prices[i]
        today_profit = prices[i] - main_price
        if today_profit > max_profit:
            max_profit = today_profit

        print(max_profit)