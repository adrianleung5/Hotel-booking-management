import pyfiglet 

class hotel_bill_management:
    def __init__(self, name = "", phone_number= "", email = "", check_in_date = "", check_out_date = "", no_of_days = 0 , room_price = 0, selected_room = ""):
        print(pyfiglet.figlet_format("leung hotel"))
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.no_of_days = no_of_days
        self.room_price = room_price
        self.selected_room = selected_room 

    def customer_information (self):
        while True:
            self.name = input("Enter your name: ")
            customer_name = self.name 
            if not (customer_name.replace(" ", "").isalpha() and len(customer_name) > 3) :
                print("Name can only contain letter and spaces that are greater than three characters")
                continue

            self.phone_number = input("Enter you phone number: ")
            if not self.phone_number.isnumeric():
                print("phone number can only contain numbers")
            if len(self.phone_number) >= 10:
                print("Phone number must contain atleast 8 numbers")
            break






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
      
        print("Welcome to the hotel please select from the options below")
        print("1 enter customer information")
        print("2 calculate the room price")
        print("3 calculate restaurant expenses")
        print("4 calculate total") 
        print("5 generete bill")
        print("6 retrieve bill for room")
        print("7 remove bill for room")
        print("8 exit")
        choice = input("please enter your choice\n")
        if choice == "1":
            hotel.customer_information()
        elif choice == "2":
            hotel.calculate_room_price()
        elif choice == "3":
            hotel.calculate_restaurant_expenses()
        elif choice == "4":
            hotel.calculate_total()
        elif choice == "5":
            hotel.generate_bill()
        elif choice == "6":
            hotel.retrieve_bill_for_room()
        elif choice == "7":
            hotel.remove_bill_for_room()
        elif choice == "8":
            quit()
        else:
            print("please enter the correct choice\n")


main()

