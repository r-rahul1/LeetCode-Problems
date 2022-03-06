class Solution:
    def countOrders(self, n: int) -> int:
        @functools.cache
        def totalWays(unpicked, undelivered):
            if not unpicked and not undelivered:
                return 1

            if (unpicked < 0 or undelivered < 0 or undelivered < unpicked):
                return 0

            ans = unpicked * totalWays(unpicked - 1, undelivered)
            ans %= MOD

            ans += (undelivered - unpicked) * totalWays(unpicked, undelivered - 1)
            ans %= MOD

            return ans
        
        MOD = 1_000_000_007
        return totalWays(n, n)