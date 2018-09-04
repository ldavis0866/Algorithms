#!/usr/bin/python

import argparse

# Brute force solution
# uses O(n**2) time


# def find_max_profit(prices):

#   profit = 0

#   # Go through every time
#   for outer_time in range(len(prices)):
#     # For every time, go trough other time
#     for inner_time in range(len(prices)):
#       # For each pair, find the earlier and later times
#       earlier_time = min(outer_time, inner_time)
#       later_time   = max(outer_time, inner_time)
#       print (earlier_time)
#       print (later_time)

#       # And use those to find the earlier and later prices
#       earlier_price = prices[earlier_time]
#       later_price   = prices[later_time]
#       print(earlier_price)
#       print(later_price)
#       # See what our profit would be if we bought at the
#       # earlier price and sold at the later price
#       potential_profit = later_price - earlier_price
#       print(potential_profit)
#       # Update max_profit if we can do better
#       profit = max(profit, potential_profit)
#       print(profit)

#   return profit


#Better solution

def find_max_profit(prices):
  profit = 0

  # Go through every price(with its index as the time)
  for earlier_time, earlier_price in enumerate(prices):
    print(earlier_time)
    print(earlier_price)
    # And go through all the LATER prices
    for later_time in range(earlier_time + 1, len(prices)):
      print(later_time)
      later_price = prices[later_time]
      print(later_price)
      # See what our profit would be if we bought at the
      # earlier price and sold at the later price
      potential_profit = later_price - earlier_price
      print(potential_profit)
      # Update profit if we can do better
      profit = max(profit, potential_profit)
      print(profit)
  return profit

print(find_max_profit([100, 90, 80, 50, 20, 10])) 





if __name__ == '__main__':
  # You can test your implementation by running 
  # `python stock_prices.py [prices]` where prices is comprised of
  # space-separated integer values
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))