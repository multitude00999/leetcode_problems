class Solution: 
    def predictPartyVictory(self, senate: str) -> str:

        # base case
        n = len(senate)
        if n < 2:
            if senate[0] == 'R':
                return "Radiant"
            else:
                return "Dire"

        # maintain two queues, senate_q for senates waiting for their chance, curr for senates that have come before senates in senate_q and are waiting for banning the opposition's voting right
        senate_q = list(senate)
        curr = []

        # break when either no one is waiting or there areonly members of one group
        while len(senate_q) and ["R"]*len(senate_q) != senate_q or ["D"]*len(senate_q) != senate_q:
            # if currently there is no one waiting to excercise their rights, append
            if len(curr) == 0:
                curr.append(senate_q.pop(0))
            
            # if there is someone waiting and he finds the opposition member
            elif curr[0] != senate_q[0]:

                # remove that senate from voting
                senate_q.pop(0)

                # add the senate that just used their right at the end of queue, this senate will wait until next round
                senate_q.append(curr[0])
                curr.pop(0)
            
            # else if the senate are from the same group they'll wait in curr
            else:
                curr.append(senate_q[0])
                senate_q.pop(0)

        # check if there are only "R"s or "D"s
        if len(senate_q):
            if senate_q[0] == 'R':
                return "Radiant"
            else:
                return "Dire"
        
        elif len(curr):
            if curr[0] =='R':
                return "Radiant"
            else:
                return "Dire"