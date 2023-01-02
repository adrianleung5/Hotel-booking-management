import pyfiglet 

class hotel_bill_management:
    def customer_information (self):
        name = input("Name")
        Address = input("address")
        check_in_date = input("check in ")
        check_out_date =  input("check out")
    def calculate_room_price (self): 
        pass
    def calculate_restaurant_expenses (self):
        pass
    def calculate_total (self):
        pass
    def generate_bill (self):
        pass
    def retrieve_bill_for_room (self):
        pass
    def remove_bill_for_room (self):
        pass


def main ():
    hotel = hotel_bill_management()
    while True:
        print(pyfiglet.figlet_format("leung hotel"))
        print("Welcome to the hotel please select from the options below\n")
        print("1 enter customer information\n")
        print("2 calculate the room price\n")
        print("3 calculate restaurant expenses\n")
        print("4 calculate total\n") 
        print("5 generete bill\n")
        print("6 retrieve bill for room\n")
        print("7 remove bill for room\n")
        print("8 exit\n")
        choice = input("please enter your choice\n")
        if choice == "1":
            hotel.customer_information()
        elif choice == "2":
            hotel.calculate_room_price()
        elif choice == "3":
            hotel.calculate_room_price()
        elif choice == "4":
            hotel.calculate_total()
        elif choice == "5":
            hotel.generate_bill()
        elif choice == "6":
            hotel.retrieve_bill_for_room()
        elif choice == "7":
            hotel.remove_bill_for_room()
        elif choice == "8":
            quit ()
        else:
            print("please enter the correct choice\n")


main()

