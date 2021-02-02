# https://leetcode.com/problems/coin-change/
# leetcode 322
import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # initialization
        n = len(coins) # number of coins we can use
        m = amount # total amount we need to get
        f = [sys.maxsize]*(m+1)
        f[0] = 0 # initialize for f[0]

        # calculate f[1], f[2]...-> f[27]
        for i in range(1, amount+1):
            # choose from n coins to
            '''
            eg coins = {2,5,7} amount = 27
            f[27] =  min{f[27-2], f[27-5],f[27-7]}+1
            f[i] = min{f[i- coins[0]], f[i-coins[1]],f[i-coins[2]]} +1
            need to check boundary: i>coins[j]  f[-1] can't exists
            and if f[i-coins[j] == sys.maxsize means can't get to f[i-coins[j]]
            '''
            for j in range(n):
                if i>=coins[j] and f[i-coins[j]]!=sys.maxsize:
                    f[i] = min(f[i],f[i-coins[j]]+1)

        if f[m] == sys.maxsize:
            f[m] = -1
        else:
            return f[m]

s1 = Solution
number = s1.coinChange(s1,[5,2,1],11)
print(number)




