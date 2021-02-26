# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1
# as one sorted array.The number of elements initialized in nums1 and nums2
# are m and n respectively. You may assume that nums1 has a size equal to
# m + n such that it has enough space to hold additional elements from nums2.

 
# Two different solutions here
# the second was how I initially solved it, the first is more succinct
# and uses less memory and is of O(m) insteand of O(m+n) time complexity

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        t = m + n - 1
        m -= 1
        n -= 1

        while n >= 0:

            if m >= 0 and nums1[m] > nums2[n]:
                nums1[t] = nums1[m]
                m -= 1
            else:
                nums1[t] = nums2[n]
                n -= 1
            t -= 1




def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_copy = nums1[:m][:] #O(m+n)
        i = len(nums1) - 1
        
        while len(nums1_copy) != 0 or len(nums2) != 0: #O(m+n)
            
            # case where both arrays still have values
            if len(nums1_copy) > 0 and len(nums2) > 0:
                if nums1_copy[-1] >= nums2[-1]:
                    nums1[i] = nums1_copy.pop(-1) # O(1)
                else:
                    nums1[i] = nums2.pop(-1) # O(1)

            # case where nums1 is empty but nums2 isnt
            elif len(nums1_copy) == 0 and len(nums2) > 0:
                nums1[i] = nums2.pop(-1) # O(1)
            
            # case where nums2 is empty but nums1 isnt
            elif len(nums1_copy) > 0 and len(nums2) == 0:
                nums1[i] = nums1_copy.pop(-1) # O(1)
            i -= 1
    
