class Solution(object):
    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int
        """
        player1score = self.getScore(player1)
        player2score = self.getScore(player2)
        return 1 if player1score > player2score else 2 if player1score < player2score else 0

    def getScore(self, player):
        playerscore = 0
        for i in range(len(player)):
            if i >= 2 and (player[i-1] == 10 or player[i-2] == 10):
                playerscore += 2 * player[i]
            elif i == 1 and player[i-1] == 10:
                playerscore += 2 * player[i]
            else:
                playerscore += player[i]
        return playerscore

solution = Solution()

player1 = [2,3]
player2 = [4,1]
print(solution.isWinner(player1, player2))