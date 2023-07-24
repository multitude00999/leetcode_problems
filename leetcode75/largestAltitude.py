class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        # initial condition
        max_altitude = 0
        running_sum = 0

        # obtain maximum altitude by maintaining running sum
        for i in gain:
            running_sum += i
            max_altitude = max(running_sum, max_altitude)
        
        return max_altitude