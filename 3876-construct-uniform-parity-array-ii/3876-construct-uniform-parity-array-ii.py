class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        min_even = float('inf')
        # 

        possible_odd = True

        for x in nums1:
            if x % 2 == 1:
                
                continue

            if min_odd >= x:
                possible_odd = False
                break

        if possible_odd:
            return True

        possible_even = True

        for x in nums1:
            if x % 2 == 0:
                continue

            if min_odd >= x:
                possible_even = False
                break

        return possible_even
