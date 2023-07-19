class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l1 = len(flowerbed)

        # edge cases
        if n == 0:
            return True
        if n > l1//2 + 1:
            return False
        if l1 == 1:
            if flowerbed[0] == 0:
                return True
            else:
                return False

        # count maximum number of plants that can be planted
        cnt = 0
        if l1 > 1 and flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            cnt+=1
        for i in range(1, l1-1):
            if flowerbed[i] + flowerbed[i-1] + flowerbed[i+1] == 0:
                flowerbed[i] = 1
                cnt+=1
        if l1 > 1 and flowerbed[-1] + flowerbed[-2] == 0:
            cnt+=1

        # check if the required plants is less than equal to max number of plants
        if cnt >= n:
            return True
        return False
            
