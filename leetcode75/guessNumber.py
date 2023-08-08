class Solution:
    def guessNumber(self, n: int) -> int:
        # set low and high
        low, high = 1, n

        # intial guess
        guessNumber = (low + high)//2

        # continue until correct guess
        while guess(guessNumber) != 0:
            # if guess is higher than the actual number
            if guess(guessNumber) == -1:
                high = guessNumber - 1
                guessNumber = (low + high)//2
            
            # if guess is lower than the actual number
            else:
                low = guessNumber + 1
                guessNumber = (low + high)//2
        return guessNumber