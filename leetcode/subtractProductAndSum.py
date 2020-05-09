class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_, prod = 0, 1
        while n > 0:
            sum_ += n % 10
            prod *= n % 10
            n = n // 10
        return prod - sum_