class Solution:
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}

        def solve(n):
            if n in memo:
                return memo[n]

            memo[n] = solve(n - 1) + solve(n - 2)
            return memo[n]

        return solve(n)

s = 10
print(Solution().fib(s))