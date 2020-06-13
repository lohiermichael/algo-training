from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        res = ""
        min_l = min([len(s) for s in strs])
        for i in range(min_l):
            for s in strs[1:]:
                if s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))
