## Introduction

This project was created in order for hotels to easily calcualte and track the expenses hotel guests spend during their vists in hotels

### Target Audience

* Hotel management/ receptionist who handles the cost of staying in the hotel for guests

### User Stories

* As a User, I would like to be able to easily find various guest infomration with ease
* As a User, I would like to be able to differentiate the different costs for customers during their stay. Such as restaurant expenses and room expenses.
* As a User, I would like to be able to easily the determine the cost of the room the customers have used
* As a User, I would like to be able to view bookings with ease,
* Aa a User, I would like to be able to retrieve specific booking information with ease.
* As a User, I would like to be able to return to the main menu without having to restart the application.
* As a user, I would like to be able to generate a bill for customers to enable them to see the costs during their stay.

### Features Planned

* Simple, easy to use application with clear navigation.
* Ability to store customer information such as name, addresss, and dates of their vist
* Ability to calculate the price of the room during the customers stay.
* Ability to calculate restaurant expenses during the their stay.
* Ability to calculate the total price of stay.
* Generate a bill for guests

**Error Handling**

Error handling was implemented throughout the application with the use of try/except statements to handle exceptions raised for things like, None type values and Value errors.

### Features Left to Implement

As a future enhancement, I would like to add some functionanality to edit room bookings. I would also like to add a feature to retrieve a bill based on a customers name.

IMPLEMENTATION
* Bill Menu
    * When the application starts, you will get a welcome message with a main menu with the following options:
    * 1 - Enter customer information
    * 2 - Select the room
    * 3 - Calculate restaurant expenses
    * 4 - Generate bill
    * 5 - Retrieve room for bill
    * 6 - Remove bill for room
    * 7 - Enable the user to exit the application
    * The user must input a correct number corresponding to each menu or they will be alerted of an inccorect choice and the menu will be presented again.

    ![Hotel Menu](docs/screenshots/booking_menu.PNG)

 * Customer information Menu
    * When customer information menu has been selected, the following menu options appear:
    * Enter your customer name - This will enables users to input and store customers name.
    * Enter phone number - This will allow the users to input their and store customer phone numbers.
    * Enter your email - This will allow the users to enter and store their customer email.
    * Enter check in date - This option will enable users to enter customer check in date during their stay.
    * Enter check out date - This option will return the user to enter customer checkout date during their.
    * Total room price - This will be calculated and displayed to the user based on the number of days and type of room.

 * Selecting room Menu
    * Single room - 50 eur
    * Double room - 100 eur
    * Triple room - 150 eur
    * Family room - 200 eur

   Total room price
 * This will be displayed to the user once the user 
 as selected a room. It is calculted based on length of stay multiplied by the type of room.

 * Restaurant Menu
    * 1 Breakfast - 15 eur
    * 2 Lunch - 25 eur
    * 3 Dinner - 40 eur
    * 4 Beverages - 25 eur
    * 5 Exit
    Quantity
    * Once users select a meal, they will be asked to input the quanaity of meals purchased. 
    Total restaurant cost
     * This will be displayed to the user once the user has entered the number of meals they have had.

* Generate bill
   * This will generate the bill with the information for all of the customers expenses.
   * Users will then have an option to return to the main menu or leave the application.

   ## Technologies

* Python - Python was the main language used to build the application.
* [Pyfiglet](https://pypi.org/project/pyfiglet/0.7/) was used to create the design of the main menu 
* [LucidCharts](https://www.lucidchart.com/) was used to create the UML Case Diagram, Class Diagram and the Flowchart.
* [Google Drive](https://drive.google.com/) and [Google sheets API](https://developers.google.com/sheets/api) 
    was connected, so data can be collected and stored on Google spreadhseet.
* [Re](https://www.w3schools.com/python/python_regex.asp) was used to validate the input for customers email information.
* [Gspread] (https://docs.gspread.org/en/v5.7.0/) was used for Google Sheets.

 ## Testing






