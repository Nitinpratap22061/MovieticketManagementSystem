class Multiplex:
    def __init__(self,noHalls,Address,totalProfit):
        self.halls=noHalls
        self.address=Address
        self.profit=totalProfit
class Hall(Multiplex):
    def __init__(self,movieName,totalTicket,listAvalSeat,ticketPrice):
        self.moviename=movieName
        self.totalticket=totalTicket
        self.seataval=listAvalSeat
        self.ticketprice=ticketPrice
        self.l=[]
    
    def calTicketPrice(self,movieName,Nooftickets):
        if(movieName==self.moviename):
            print(f"ticket price {Nooftickets*self.ticketprice}") 
        else:
            print(f"{movieName} is not available in hall")
    
    def checkSeat(self,movieName,Nooftickets):
        if(movieName==self.moviename):
            if(Nooftickets<=len(self.seataval)):
                print(f"{Nooftickets} are present")
            else:
                print(f"{Nooftickets} not present")
        else:
            print(f"{movieName} is not in hall")

    def getSeatNo(self):
        print(f"list of available seat number:-{self.seataval}")

    def bookTicket(self,movieName,Nooftickets):
        if(len(self.seataval)==0):
            print("seat not available")
        else:
            if(movieName==self.moviename):
                i=1
                while i<=Nooftickets:
                    p=self.seataval.pop()
                    self.l.append(p)
                    i=i+1
                print(f"{Nooftickets} tickets booked for {movieName} with seatnumbers{self.l}")    
            else:
               print(f"{movieName} is not in hall")

    def cancelticket(self,seatNumber):
        if seatNumber in self.l:
            self.l.remove(seatNumber)
            self.seataval.append(seatNumber)
            print(f"{seatNumber} Cancelled successfully\n")
        else:
            print(f"{seatNumber} seat was not booked")

Multiplex=Multiplex(2,"buddha park",400)
hall=Hall("king",9,[3,4,5,6,7,8,9,1,2],150)

while True:
    print("1.Calculate ticket price")
    print("2.check seat avaiblity")
    print("3.get available seat no")
    print("4 book ticket")
    print("5 cancel ticket")
    ch=int(input ("enter your choice"))
    if(ch==1):
        moviename=input("enter movie name")
        nooftickets=int(input("enter no of tickets"))
        hall.calTicketPrice(moviename,nooftickets)
    elif(ch==2):
          moviename=input("enter movie name")
          nooftickets=int(input("enter no of tickets"))
          hall.checkSeat(moviename,nooftickets)
    elif (ch==3):
        hall.getSeatNo()
    elif (ch==4):
          moviename=input("enter movie name")
          nooftickets=int(input("enter no of tickets"))
          
          hall.bookTicket(moviename,nooftickets)
    elif(ch==5):
        seatNo=input(int("enter seat number to be canceled"))
        hall.cancelticket(seatNo)
    else:
        print("please select a valid option")
    print("press q to quit and c to continue")
    user_choice2=input()
    if user_choice2=="q":
            exit()
    if user_choice2=="c":
            continue