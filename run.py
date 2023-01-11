import pyfiglet
import datetime
import re
from google.oauth2.service_account import Credentials
import gspread

red_color = "\033[91m"
green_color = "\33[32m"
yellow_color = "\33[33m"

color_end = "\033[0m"

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hotel_billing")

MAIN_MENU = """
Welcome to the hotel please select from the options below
    1 Enter customer information
    2 Select the room
    3 Calculate restaurant expenses
    4 Generate bill
    5 Exit
"""
ROOM_MENU = """
 **Please select from the following available rooms**
    1 : Single Room--> 50  EUR
    2 : Double Room--> 100 EUR
    3 : Triple Room--> 150 EUR
    4 : Family Room--> 200 EUR
"""

RESTAURANT_MENU = """
 ** Please select from the Menu**
    1 : Breakfast --> 15 EUR
    2 : Lunch --> 25 EUR
    3 : Dinner --> 40 EUR
    4 : Desert --> 10 EUR
    5 : Beverages --> 5 EUR
    6 : Exit
"""


class hotel_bill_management:
    def __init__(
        self,
        name="",
        phone_number="",
        email="",
        customer_info_added=False,
        room_info_added=False,
        restaurant_price=0,
        check_in_date="",
        check_out_date="",
        no_of_days=0,
        room_price=0,
        selected_room="",
    ):
        print(pyfiglet.figlet_format("Leung hotel"))
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.room_info_added = room_info_added
        self.customer_info_added = customer_info_added
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.no_of_days = no_of_days
        self.room_price = room_price
        self.selected_room = selected_room
        self.restaurant_price = restaurant_price

    """
    Display customer information options. Take user input
    and call next functions. If invalid input, show
    error and ask for input again.
    """
    def customer_information(self):
        while True:
            self.name = input("Enter your name: ")
            customer_name = self.name
            if not (
                customer_name.replace(
                    " ",
                    "").isalpha() and len(customer_name) > 3):
                print(
                    red_color +
                    "Name can only contain letter and spaces" +
                    " that are greater than three characters" +
                    color_end)
                continue
            else:
                break

        while True:
            self.phone_number = input("Enter you phone number: ")
            if not self.phone_number.isnumeric():
                print(
                    red_color +
                    "Phone number can only contain numbers" +
                    color_end)
                continue
            elif len(self.phone_number) < 10:
                print(
                    red_color
                    + "Phone number must contain atleast 10 numbers"
                    + color_end
                )
                continue
            else:
                break

        while True:
            self.email = input("Enter your email: ")
            if not self.check_email(self.email):
                print(
                    red_color +
                    "Please enter valid email address" +
                    color_end)
                continue
            else:
                break

        while True:
            self.check_in_date = input(
                "Enter your check in date in the format of dd/mm/yyyy : "
            )
            if not self.isvalidcheck_in_date(self.check_in_date):
                print(
                    red_color
                    + "Check in date is not valid "
                    + "or it is in the past, please try again"
                    + color_end
                )
                continue
            else:
                break

        while True:
            self.check_out_date = input(
                "Enter your check out date in the format of dd/mm/yyyy : "
            )
            if not self.isvalidcheck_out_date(
                    self.check_in_date,
                    self.check_out_date):
                print(
                    red_color
                    + "The checkout date is not valid, please try again"
                    + color_end
                )
                continue
            else:
                print(
                    green_color
                    + "\n***** Customer Information added Sucessfully ***** \n"
                    + color_end
                )
                print(
                    green_color
                    + "Customer wishes to stay for "
                    + str(self.no_of_days)
                    + " days, please choose rooms next\n"
                    + color_end
                )
                self.customer_info_added = True
                break

     """
    Display Room price menu options. Take user input
    and call next functions. 
    """
    def calculate_room_price(self):
        if self.customer_info_added:
            while True:
                print(ROOM_MENU)
                choice = input("Please enter yout choice number: ")
                if choice == "1":
                    self.selected_room = "Single Room--> 50 EUR"
                    self.room_price = self.no_of_days * 50
                elif choice == "2":
                    self.selected_room = "Double Room--> 100 EUR"
                    self.room_price = self.no_of_days * 100
                elif choice == "3":
                    self.selected_room = "Triple Room--> 150 EUR"
                    self.room_price = self.no_of_days * 150
                elif choice == "4":
                    self.selected_room = "Family Room--> 200 EUR"
                    self.room_price = self.no_of_days * 200
                else:
                    print(
                        red_color +
                        "Please select the correct option" +
                        color_end)
                    continue
                print(
                    green_color
                    + "**** Total room price for "
                    + str(self.no_of_days)
                    + " days is "
                    + str(self.room_price)
                    + "EUR ****"
                    + color_end
                )
                print(
                    green_color
                    + "Please continue to restaurant expenses if any"
                    + color_end
                    + "\n"
                )
                self.room_info_added = True
                break
        else:
            print(
                red_color +
                "You need to add customer " +
                "information before" +
                " selecting a room" +
                color_end)

     """
    Display Calculate restaurant options. Take user input
    and call next functions. If invalid input, show
    error and ask for input again.
    """
    def calculate_restaurant_expenses(self):
        if not self.customer_info_added:
            print(red_color + "You are missing customer information")
        elif not self.room_info_added:
            print("You are missing room details")
        else:
            while True:
                print(RESTAURANT_MENU)
                choice = input("Please select an option: ")
                if choice == "1":
                    qnty = int(input("Please enter the amount of quantity: "))
                    self.restaurant_price = self.restaurant_price + 15 * qnty
                elif choice == "2":
                    quantity = int(
                        input("Please enter the amount of quantity: "))
                    self.restaurant_price = (self.restaurant_price +
                                             25 * quantity)
                elif choice == "3":
                    qnty = int(
                        input("Please enter the amount of quantity: "))
                    self.restaurant_price = self.restaurant_price + 40 * qnty
                elif choice == "4":
                    qnty = int(
                        input("Please enter the amount of quantity: "))
                    self.restaurant_price = self.restaurant_price + 10 * qnty
                elif choice == "5":
                    qnty = int(
                        input("Please enter the amount of quantity: "))
                    self.restaurant_price = self.restaurant_price + 5 * qnty
                elif choice == "6":
                    break
                else:
                    print(
                        red_color +
                        "Please enter the correct choice" +
                        color_end)
            print(
                green_color
                + "**** Total restaurant cost = "
                + str(self.restaurant_price)
                + " Eur ****"
                + color_end
            )
    """
    Display Bill. Give user option
    to close application or move
    to next customer.
    """
    def generate_and_retrieve_bill(self):
        print(self.room_price)
        if not self.customer_info_added:
            print(
                red_color +
                "You are missing customer information" +
                color_end)
        elif not self.room_info_added:
            print(red_color + "You are missing room details" + color_end)
        elif self.restaurant_price == 0:
            print(red_color + "No restaurant expenses" + color_end)
            print("Would you like to add restuarant expenses?")
            print("1: add Restaurant expenses to bill")
            print("2: continue to generate bill without restaurant expenses")
            choice = input("Please enter your choice: \n")
            if choice == "1":
                self.calculate_restaurant_expenses()
            elif choice == "2":
                print(
                    yellow_color
                    + "******************* LEUNGHOTEL BILL *******************"
                    + color_end
                )
                print(yellow_color + "CUSTOMER INFORMATION" + color_end)
                print(yellow_color + "    Name: " + self.name + color_end)
                print(
                    yellow_color
                    + "    Phone number: "
                    + str(self.phone_number)
                    + color_end
                )
                print(
                    yellow_color +
                    "    Email: " +
                    self.email +
                    color_end +
                    "\n")
                print(yellow_color + "ROOM EXPENSES: " + color_end)
                print(
                    yellow_color
                    + "    Selected room: "
                    + self.selected_room
                    + color_end
                )
                print(
                    yellow_color
                    + "    Check in date: "
                    + self.check_in_date
                    + color_end
                )
                print(
                    yellow_color
                    + "    Check out date: "
                    + self.check_out_date
                    + color_end
                )
                print(
                    yellow_color
                    + "    Number of days: "
                    + str(self.no_of_days)
                    + color_end
                )
                print(yellow_color + "    Total Room Price: " 
                      + str(self.room_price)
                      + " EUR")
                vat_price = (self.room_price * 10) / 100
                print(yellow_color + "OTHER EXPENSES: " + color_end)
                print(
                    yellow_color
                    + "    Cost of VAT: "
                    + str(vat_price)
                    + " EUR\n"
                    + color_end
                )
                total_price = vat_price + self.room_price
                print(
                    yellow_color
                    + "Total Price : "
                    + str(total_price)
                    + " EUR"
                    + color_end
                )
                print(
                    yellow_color +
                    "********************END OF BILL*********" +
                    "**********************\n" +
                    color_end)
                self.update_spreadsheet(vat_price, total_price)
                while True:
                    print("Do you wish to continue with the next customer?")
                    print("1: Continue to main menu")
                    print("2: Exit")
                    customer_choice = input("Enter your choice: \n")
                    if customer_choice == "1":
                        self.remove_bill_for_room()
                        break
                    elif customer_choice == "2":
                        quit()
                    else:
                        print(
                            red_color +
                            "Please enter the correct choice" +
                            color_end)
                        continue
        else:
            print(
                yellow_color
                + "******************* LEUNGHOTEL BILL *******************"
                + color_end
            )
            print(yellow_color + "CUSTOMER INFORMATION" + color_end)
            print(yellow_color + "    Name: " + self.name + color_end)
            print(yellow_color + "    Phone number: " +
                  str(self.phone_number) + color_end)
            print(yellow_color + "    Email: " + self.email + color_end + "\n")
            print(yellow_color + "ROOM EXPENSES: " + color_end)
            print(
                yellow_color +
                "    Selected room: " +
                self.selected_room +
                color_end)
            print(
                yellow_color +
                "    Check in date: " +
                self.check_in_date +
                color_end)
            print(
                yellow_color +
                "    Check out date: " +
                self.check_out_date +
                color_end)
            print(yellow_color + "    Number of days: " +
                  str(self.no_of_days) + color_end)
            print(yellow_color + "    Selected room: " + self.selected_room)
            print(yellow_color + "    Total Room Price: " 
                  + str(self.room_price)
                  + " EUR")
            print(yellow_color + "RESTAURANT EXPENSES: " + color_end)
            print(
                yellow_color
                + "    Total restauarant expenses: "
                + str(self.restaurant_price)
                + " EUR"
                + color_end
            )
            print(yellow_color + "OTHER EXPENSES: " + color_end)
            vat_price = ((self.room_price + self.restaurant_price) * 10) / 100
            print(
                yellow_color +
                "    Cost of VAT: " +
                str(vat_price) +
                " EUR" +
                color_end)
            total_price = vat_price + self.room_price + self.restaurant_price
            print(
                yellow_color +
                "Total price : " +
                str(total_price) +
                " EUR" +
                color_end)
            print(
                yellow_color +
                "********************END OF BILL***" +
                "****************************\n" +
                color_end)
            self.update_spreadsheet(vat_price, total_price)
            while True:
                print("Do you wish to continue with the next customer?")
                print("1: Continue to main menu")
                print("2: Exit")
                customer_choice = input("Enter your choice: \n")
                if customer_choice == "1":
                    self.remove_bill_for_room()
                    break
                elif customer_choice == "2":
                    quit()
                else:
                    print(
                        red_color +
                        "Please enter the correct choice" +
                        color_end)
                    continue

    def remove_bill_for_room(self):
        self.room_price = 0
        self.restaurant_price = 0
        self.customer_info_added = False
        main()

    def isvalidcheck_in_date(self, input_date):
        valid_date = True
        try:
            day, month, year = input_date.split("/")
            check_in_date = datetime.datetime(int(year), int(month), int(day))
            present_date = datetime.datetime.now()
            if check_in_date.date() < present_date.date():
                valid_date = False
        except ValueError:
            valid_date = False
        finally:
            return valid_date

    def isvalidcheck_out_date(self, check_in_date, checkout_date):
        valid_date = True
        try:
            day1, month1, year1 = check_in_date.split("/")
            day2, month2, year2 = checkout_date.split("/")

            checkin_date1 = datetime.datetime(
                int(year1), int(month1), int(day1))
            checkout_date1 = datetime.datetime(
                int(year2), int(month2), int(day2))

            if checkin_date1.date() >= checkout_date1.date():
                print(
                    red_color +
                    "Check out date cannot be before check in" +
                    " date, please try again" +
                    color_end)
                valid_date = False
            else:
                self.no_of_days = (
                    checkout_date1.date() -
                    checkin_date1.date()).days
        except ValueError:
            valid_date = False
        finally:
            return valid_date

    def check_email(self, email):
        valid_email = False
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if re.match(pattern, email):
            valid_email = True
            return valid_email
        else:
            return valid_email

    def update_spreadsheet(self, vat, total_price):
        spread_sheet = SHEET.worksheet("billing information")
        spread_sheet.append_row(
            [
                self.name,
                self.phone_number,
                self.email,
                self.check_in_date,
                self.check_out_date,
                self.no_of_days,
                self.selected_room,
                self.room_price,
                self.restaurant_price,
                vat,
                total_price,
            ]
        )


def main():
    hotel = hotel_bill_management()
    while True:

        print(MAIN_MENU)
        choice = input("Please enter your choice\n")
        if choice == "1":
            hotel.customer_information()
        elif choice == "2":
            hotel.calculate_room_price()
        elif choice == "3":
            hotel.calculate_restaurant_expenses()
        elif choice == "4":
            hotel.generate_and_retrieve_bill()
        elif choice == "5":
            quit()
        else:
            print("Please enter the correct choice\n")


if __name__ == "__main__":
    main()
