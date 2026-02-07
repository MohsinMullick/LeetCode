class Solution(object):
    def distributeCandies(self, candies):
        unique_types = len(set(candies))
        max_sister_can_take = len(candies) // 2
        return min(unique_types, max_sister_can_take)

candies= [1,1,2,2,3,3]
obj=Solution()
array=obj.distributeCandies(candies)
print(array)