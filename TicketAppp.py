tickets = 20
buyers = 0
#function and loop
while tickets > 1:
    print("Number of Tickets for Sale: ", tickets)

    #input
    howManyTickets = int(input("How many tickets do you want?  "))
    #if statement
    if (5 < howManyTickets > 0) & (tickets - howManyTickets) >= 0:
    #accumlator
        buyers += 1
        tickets -= howManyTickets
    if howManyTickets > 4:
        #output
        print("a maximum of 4 tickets can be sold at a time")
        print("All tickets sold; number of buyers: ", buyers)
else:
    #output
    print("I'm sorry I can't sell this amount of tickets")
    print("I only have ", tickets , "tickets left")



