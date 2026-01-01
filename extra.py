class Solution(object):#create a class, named Solution and default object
    def findMedianSortedArrays(self,nums1,nums2):#methon or function create
        #function name
        #self reference to the instance of the class when we call class.method
        #nums1=input parameters
        #num2=input parameters
        merged_array=nums1+nums2#this line joins nums1 and nums2 into one list
        merged_array.sort()#because the problem requires the array to be sorted
        m=len(merged_array)#check the list elements because we need midpoint
        #Now we are check midpoint value use loop condition
        if (m%2==1):#check the odd numbers and m==1 its true otherwise false because we need midpoint
            #so this line checks whether the length merged_array is odd.
            return merged_array[m//2]#find the middle index integer division
        #or return the index at the division
        else:
            mid_value1=merged_array[m//2-1]#merged_array all elements present so
            #subratct 1 means middle index -1
            #m=6-1=5
            mid_value2=merged_array[m//2]#this line only for even numbers
            return (mid_value1+mid_value2)/2.00#left value and right value
solve=Solution()#This line creates an instance of the solution class
median=solve.findMedianSortedArrays([1,3],[2])#This calls the method
print(median)






