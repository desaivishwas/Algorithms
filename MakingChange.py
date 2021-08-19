class MakingChange:
    def minimumCoins(self, money, coins):
        """
        Bottom Up approach to find min number of coins
        """
        k = [money + 1] * (money + 1)
        # Making change for 0 will always be 0 coins
        k[0] = 0

        # outer for loop to find min coin from 1 to n (i.e money)
        for i in range(1, money + 1):
            # inner for loop to solve for each coin given
            for j in range(0, len(coins)):
                if coins[j] <= i:
                    k[i] = min(k[i], k[i - coins[j]] + 1)

                # returns -1 if no combination of coins exist
        return -1 if k[money] > money else k[money]
