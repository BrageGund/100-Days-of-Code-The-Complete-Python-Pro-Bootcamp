import art
print(art.logo)

dictionary = {}
continuation = True
######################################################################
def find_highest_bidder(Bidding_dictionary):
    highest_bidder = 0
    for bidder in Bidding_dictionary:
        bid_amount = Bidding_dictionary[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a highest bid of {bid_amount}$")

######################################################################
while continuation == True:

    # TODO-1: Ask the user for input
    name = input("What's your name?: ")
    bid = input("What's your bid?: ")

    dictionary[name] = int(bid)

    # TODO-2: Save data into dictionary {name: price}
    print(dictionary)

    switch = input("Are there any other bidders? type 'Yes' if yes or 'No' if no: ").lower()

    # TODO-3: Whether if new bids need to be added
    # TODO-4: Compare bids in dictionary
    if switch == "yes":
        print("\n"*20)
    elif switch == "no":
        continuation = False
        Highest_Bidder = max(dictionary, key = dictionary.get)
        Highest_Bid = dictionary[Highest_Bidder]
        print(f"The winner is {Highest_Bidder} with a highest bid of {Highest_Bid}$")

    else:
        print("Invalid")
    #
    # if switch == "no":
    #     find_highest_bidder(dictionary)
    #     continuation = False
    # else:
    #     print(30*"\n")




