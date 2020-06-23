class Solution:
    def countAndSay(self, n: int) -> str:
        def next_step(s: str):
            element = s[0]
            i = 1
            count = 1
            res = ""
            while i < len(s):
                if s[i] == element:
                    count += 1
                else:
                    res = res + str(count) + element
                    element = s[i]
                    count = 1
                i += 1

            res = res + str(count) + element
            return res

        def loop(n):
            if n == 1:
                return "1"
            else:
                return next_step(loop(n-1))

        return loop(n)


if __name__ == "__main__":
    n = 4
    print(Solution().countAndSay(4))
