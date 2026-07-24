class Solution(object):
    def uniqueXorTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        vals = set(nums)

        # Step 1: all achievable pair-xors (a^b), repetition allowed
        pair_xor = set()
        for a in vals:
            for b in vals:
                pair_xor.add(a ^ b)

        # Step 2: combine with a third value to get all triplet-xors
        triplet_xor = set()
        for p in pair_xor:
            for c in vals:
                triplet_xor.add(p ^ c)

        return len(triplet_xor)