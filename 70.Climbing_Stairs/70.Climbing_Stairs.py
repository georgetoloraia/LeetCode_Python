class Solution(object):
    def climbStairs(self, n):
        if n <= 1:
            return 1

        alg = [0] * (n + 1)
        alg[0] = 1
        alg[1] = 1

        for i in range(2, n + 1):
            alg[i] = alg[i - 1] + alg[i - 2]

        return alg[n]