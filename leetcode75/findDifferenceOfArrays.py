class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[]]*2

        # use set for finding elements that occured in one array but not in the other
        answer[0] = list(set(nums1) - set(nums2))
        answer[1] = list(set(nums2) - set(nums1))

        return answer