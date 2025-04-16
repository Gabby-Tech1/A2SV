def maxCoins(piles):
    """
    Given an array of integers representing piles of coins, this function calculates the maximum number of coins
    a player can collect by selecting the largest pile and then the second largest pile, and so on.
    
    :param piles: List[int] - List of integers representing piles of coins.
    :return: int - Maximum number of coins that can be collected.
    """
    piles.sort()
    
    total_coins = 0
    
    for i in range(len(piles) // 3, len(piles), 2):
        total_coins += piles[i]
    
    return total_coins