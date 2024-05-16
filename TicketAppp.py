#function
def ticket_sales():

   tickets = 20

   ticketsleft = tickets

   buyers = 0

   while ticketsleft > 0:
    #output
       print(f"There are currently {ticketsleft} tickets remaining.")
    #input
       num_tickets = int(input("How many tickets would you like to purchase? "))
        #if statement
       if num_tickets < 1 or num_tickets > 4:
        #output
           print("Sorry, you cannot purchase that amount.")

       elif num_tickets > ticketsleft:

           print("Sorry, there are not enough tickets remaining.")

       else:

           ticketsleft -= num_tickets
        #accumulator
           buyers += 1

   print(f"The total number of buyers was {buyers}")

ticket_sales()

