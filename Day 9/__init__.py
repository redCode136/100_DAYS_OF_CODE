bids={}
auction_is_on=True

def find_highest_bidder(bids):
    highest_amount=int(0)
    bid_amount=0
    winner=""
    for bid in bids:
        bid_amount=bids.get(bid)
        print(bids.get(bid))
        if highest_amount<bid_amount:
            highest_amount=bid_amount
            winner=bid
    print(f"The winner is {winner} with a bid of ${highest_amount}")



while auction_is_on:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        auction_is_on = False
        find_highest_bidder(bids)