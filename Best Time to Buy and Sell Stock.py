class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')#price did not 0
        max_profit = 0#assume 0

        for price in prices:#all prices into the price
            if price < min_price:#check
                min_price = price
            else:
                profit = price - min_price#profit calculation
                max_profit = max(max_profit, profit)#use max function for max profit

        return max_profit
prices=[1,2,3,4,5,6,7]
obj=Solution()
array=obj.maxProfit(prices)
print(array)
