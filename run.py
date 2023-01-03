import pyfiglet 
import datetime
import re

red_color = '\033[91m'
green_color  = '\33[32m'

color_end = '\033[0m'


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
                print(red_color+"Name can only contain letter and spaces that are greater than three characters"+color_end)
                continue

            self.phone_number = input("Enter you phone number: ")
            if not self.phone_number.isnumeric():
                print(red_color+"phone number can only contain numbers"+color_end)
                continue
            if len(self.phone_number) < 10:
                print(red_color+"Phone number must contain atleast 10 numbers"+color_end)
                continue

            self.email = input("Enter your email")
            if not self.check_email(self.email):
                print(red_color+"Please enter valid email address"+color_end)
                continue
            
            self.check_in_date = input("enter your check in date in the format of dd/mm/yyyy : ")
            if not self.isvalidcheck_in_date(self.check_in_date):
                print(red_color+"Check in date is not valid or it is in the past, please try again"+color_end)
                continue
            
            self.check_out_date = input("enter your check out date in the format of dd/mm/yyyy : ")
            if not self.isvalidcheck_out_date(self.check_in_date, self.check_out_date):
                print(red_color+"The checkout date is not valid, please try again" + color_end) 
                continue
            else:
                print(green_color+"\n***** Customer Information added Sucessfully ***** \n"+color_end)
                print(green_color+ "Customer wishes to stay for " + str(self.no_of_days)+" days, please choose rooms next\n"+color_end)
                continue

            self.room_price = input("which room would you like to select")
            print("1 single room")
            print("2 ouble room")
            print("3 triple room")
            print("4 family room")
            if self.room_price == "1":
                self.room_price
            elif self.room_price =="2":
                print ("price = 100")
            elif self.room_price =="3":
                print ("price = 150")
            elif self.room_price =="4":
                print ("price = 200")

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

    def isvalidcheck_in_date(self, input_date) :
        valid_date = True
        try:
            day, month, year = input_date.split("/")
            check_in_date = datetime.datetime(int(year),int(month),int(day))
            present_date = datetime.datetime.now()
            if check_in_date.date() < present_date.date():
                valid_date = False
        except ValueError:
            valid_date = False
        finally:
            return valid_date

    def isvalidcheck_out_date(self,check_in_date,checkout_date):
        valid_date = True
        try:
            day1, month1, year1 = check_in_date.split("/")
            day2, month2, year2 = checkout_date.split("/")

            checkin_date1 = datetime.datetime(int(year1),int(month1),int(day1))
            checkout_date1 = datetime.datetime(int(year2),int(month2),int(day2))
            
            if checkin_date1.date() >= checkout_date1.date():
                print(red_color+"Check out date cannot be before check in date, please try again" +color_end)
                valid_date = False
            else:
                self.no_of_days = (checkout_date1.date() - checkin_date1.date()).days
        except ValueError:
            valid_date = False
        finally:
            return valid_date
    
    def check_email(self, email):
        valid_email = False
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(pattern,email):
            valid_email = True
            return valid_email
        else:
            return valid_email

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

