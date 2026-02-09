class Solution(object):
    def findRestaurant(self, list1, list2):
        index_map = {}
        for i in range(len(list1)):
            index_map[list1[i]] = i
        min_sum = float('inf')
        result = []
        for j in range(len(list2)):
            if list2[j] in index_map:
                total = j + index_map[list2[j]]

                if total < min_sum:
                    min_sum = total
                    result = [list2[j]]
                elif total == min_sum:
                    result.append(list2[j])
        return result

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
obj=Solution()
array=obj.findRestaurant(list1,list2)
print(array)