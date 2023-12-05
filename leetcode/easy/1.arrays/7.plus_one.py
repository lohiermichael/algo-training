from typing import List

# [1, 2, 3]


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Initialize the carry to 1 as it the element that we want to add
        carry = 1
        res = digits.copy()
        for i, x in enumerate(list(reversed(digits))):
            j = len(digits) - 1 - i
            res[j] = (x + carry) % 10
            carry = (x + carry) // 10
            if carry == 0:
                break
        # Add the final carry if equal to 1 as a new element of the list
        if carry == 1:
            res.insert(0, 1)
        return res


if __name__ == "__main__":
    example = [9, 9, 9]
    print(Solution().plusOne(example))
