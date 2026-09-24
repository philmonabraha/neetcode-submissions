class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def findKth(k):
            i = 0
            j = 0

            while True:

                # If nums1 is exhausted
                if i == len(nums1):
                    return nums2[j + k - 1]

                # If nums2 is exhausted
                if j == len(nums2):
                    return nums1[i + k - 1]

                # If we want the 1st smallest remaining element
                if k == 1:
                    return min(nums1[i], nums2[j])

                half = k // 2

                new_i = min(i + half, len(nums1)) - 1
                new_j = min(j + half, len(nums2)) - 1

                val1 = nums1[new_i]
                val2 = nums2[new_j]

                if val1 <= val2:
                    # Remove nums1[i : new_i + 1]
                    removed = new_i - i + 1
                    i = new_i + 1
                    k -= removed

                else:
                    # Remove nums2[j : new_j + 1]
                    removed = new_j - j + 1
                    j = new_j + 1
                    k -= removed

        total = len(nums1) + len(nums2)

        if total % 2 == 1:
            return float(findKth(total // 2 + 1))

        left = findKth(total // 2)
        right = findKth(total // 2 + 1)

        return (left + right) / 2