#!/usr/bin/python3
"""
Making Change
"""



def makeChange(coins, total):
   """
    Return the minimum number of coins needed to meet a given total
    Args:
        coins (list of ints): a list of coins of different values
        total (int): total value to be met
    Return:
        Number of coins or -1 if meeting the total is not possible
  """
  if total <= 0:
      return 0
  dp = [0] + [float('inf')] * total
  for coin in coins:
      for i in range(coin, total + 1):
          dp[i] = min(dp[i], dp[i - coin] + 1)
  return dp[total] if dp[total] != float('inf') else -1
