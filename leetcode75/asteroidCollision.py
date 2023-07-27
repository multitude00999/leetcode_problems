class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        if n <2:
            return asteroids
        # maintain of stack of surviving asteroids
        survivors = []
        for i in range(n):
            takeAsteroidI = True

            # check if the top of stack and asteroids[i] can coliide
            while len(survivors) and survivors[-1] > 0 and asteroids[i] < 0:

                # check for chain of collisions
                if abs(survivors[-1]) < abs(asteroids[i]):
                    survivors.pop()
                    continue
                
                # in other case there are no collisions further with asetroid[]i]and hence break the chain
                elif abs(survivors[-1]) == abs(asteroids[i]):
                    survivors.pop()
                    takeAsteroidI = False
                    break
                else:
                    takeAsteroidI = False
                    break
            # append to stack if no collision
            if takeAsteroidI and (len(survivors) == 0 or survivors[-1] < 0 or asteroids[i] > 0):
                survivors.append(asteroids[i])
        return survivors
