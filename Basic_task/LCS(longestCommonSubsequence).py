class Solution:
    def longestCommonSubsequence(self, word1: str, word2: str) -> int:
        dp = [0 for _ in range(len(word2)+1)]
        for i in range(len(word1)):
            new_dp = dp.copy()
            for j in range(len(word2)):
                if word1[i] != word2[j]:
                    new_dp[j + 1] = max(new_dp[j], dp[j+1])
                else:
                    new_dp[j + 1] = dp[j] + 1
            dp = new_dp
        return dp[-1]
