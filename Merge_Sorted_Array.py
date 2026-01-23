"""
You are given two integer arrays nums1 and nums2,
 sorted in non-decreasing order, and two integers m and n,
  representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be
stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
 where the first m elements denote the elements that should be merged,
 and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""
class Solution(object):#create class
    def merge(self,nums1,m,nums2,n):#create function
        i=m-1#nums1 last valid index or element
        j=n-1#nums2 last valid index or element
        k=m+n-1#nums1 last index

        while i>=0 and j>=0:#jsut check condition 0 and until two array valid elements
            if nums1[i]>nums2[j]:#jsut for big element because we check last to first element
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1

        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1

