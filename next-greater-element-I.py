class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        ans = dict()
        st = []
        for i in range(n2-1, -1, -1):
            while len(st)>0 and st[-1] <= nums2[i]:
                st.pop()
            if len(st) == 0: ans[nums2[i]] = -1
            else : ans[nums2[i]] = st[-1]
            st.append(nums2[i])
        res = [0] * n1
        for i in range(n1):
            res[i] = ans[nums1[i]]
        return res