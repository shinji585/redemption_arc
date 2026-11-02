from dataclasses import dataclass


@dataclass()
class Solution:
    def intersection(self, num1: list[int], num2: list[int]) -> list[int]:
        return list(frozenset(num1).intersection(num2))


solution = Solution()

print(solution.intersection(num1=[1, 2, 3, 4], num2=[6, 7, 2, 3]))
