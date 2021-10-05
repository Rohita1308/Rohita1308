import sys

def update_accounts(accounts, transaction):
  type = transaction[2]
  acc = transaction[3]
  ac2 = transaction[-2]
  amt = int(transaction[-1])

  if type == "open":
    accounts[acc] = amt
    return

  if type == "deposit":
    if acc in accounts:
        accounts[acc] = accounts[acc] + amt
    else:
        accounts[acc] = amt
    return

  if type == "withdraw":
    accounts[acc] = accounts[acc] - amt
    return

  if type == "transfer":
    accounts[acc] = accounts[acc] + amt
    accounts[ac2] = accounts[ac2] - amt

def main(argv):
  if len(argv) != 1:
    #raise AttributeError("Wrong number of command-line arguments.")
    print("Wrong number of command-line arguments.")

  accounts = {}
  with open(argv[0], "r") as f:
    for line in f:
      update_accounts(accounts, line.split())

  for key in accounts:
    print("balance of " + key + " is " + str(accounts[key]))

if __name__ == '__main__':
    main(sys.argv[1:])