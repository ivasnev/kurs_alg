class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1)):
            dp[i + 1][0] = i + 1
        for j in range(len(word2)):
            dp[0][j + 1] = j + 1
        print(" ", " ", " ".join(list(word2)))
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i][j])
            print(word1[i-1], " ".join([str(x) for x in dp[i]]))
        print(word1[-1], " ".join([str(x) for x in dp[-1]]))
        return dp[-1][-1]

    def minDistanceLowMemory(self, word1: str, word2: str) -> int:
        dp = [0] + list(range(1, len(word2) + 1))
        for i in range(len(word1)):
            new_dp = dp.copy()
            new_dp[0] = i + 1
            for j in range(len(word2)):
                if word1[i] != word2[j]:
                    new_dp[j + 1] = 1 + min(new_dp[j], dp[j + 1], dp[j])
                else:
                    new_dp[j + 1] = dp[j]
            dp = new_dp
        return dp[-1]


s = Solution()
res = s.minDistance("horse", "ros")
