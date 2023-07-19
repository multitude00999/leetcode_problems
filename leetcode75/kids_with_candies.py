class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        max_candy = max(candies)
        lower_bound = max_candy - extraCandies
        bool_arr = [True]*(n)

        if lower_bound <= 0:
            return bool_arr
        else:
            for i in range(n):
                if candies[i] < lower_bound:
                    bool_arr[i] = False
            return bool_arr