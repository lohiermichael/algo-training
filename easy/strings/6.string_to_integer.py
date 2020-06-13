import re


class Solution:

    def myAtoi(self, str: str) -> int:
        # lstrip removes leading spaces of the string
        L = re.findall('^[+-]?\d+', str.lstrip())
        # Extract the integer from the list
        num = int(*L)
        return max(min(num, 2**31 - 1), -2**31)


if __name__ == "__main__":
    tests = ["42", "   -42", "4193 with words",
             "words and 987", "-91283472332", "3.14159", "  -0012a42"]
    for s in tests:
        print(Solution().myAtoi(s))
