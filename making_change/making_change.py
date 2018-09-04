#!/usr/bin/python

import sys




def making_change(amount, denominations):
  ways_of_doing_n_cents = [0] * (amount + 1)
  print(ways_of_doing_n_cents)

  ways_of_doing_n_cents[0] = 1

  for coin in denominations:
    print(coin)

    for higher_amount in range(coin, amount + 1):
      print(higher_amount)

      higher_amount_remainder = higher_amount - coin
      print(higher_amount_remainder)

      ways_of_doing_n_cents[higher_amount] += ( ways_of_doing_n_cents[higher_amount_remainder])
      print(ways_of_doing_n_cents[higher_amount])

  return ways_of_doing_n_cents[amount]



print(making_change(10, [1,5,10,25,50]))


if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")