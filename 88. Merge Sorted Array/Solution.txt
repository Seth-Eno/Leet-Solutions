class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Don't return anything, modify nums1 in-place instead.
        """
        #join arrays
        for i in range(n):
            nums1.pop()
        for i in range(n):
            nums1.append(nums2[i])
            m += 1

        #bubble sort joined array
        for j in range(m):
            for i in range(m):
                start = i
                if ((start+1) < m):
                    while (nums1[start] > nums1[start+1]):
                        temp = nums1[start+1]
                        nums1[start+1] = nums1[start]
                        nums1[start] = temp
                        start +=1
                        if (start+1) >= m:
                            break
