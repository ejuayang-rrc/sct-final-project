# Intermediate Software Development Automated Teller Project

This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author

Elijah Juayang

## Assignment

Assignment 1: Using knowledge learned in Module 1 on Classes, Encapsulation, and Unit Test Planning. Will be developing classes to support a larger system.  
Assignment 2: Building off the Classes created in the previous assignment. Will be using knowledge learned from Module 2 on Abstraction, Inheritance, and Polymorphism.  
Assignment 3: Continuing from the previous assignment. Will be implementing design patterns to address and improve the scalability and maintainability of the current service charge calculation functionality.  
Assignment 4: This assignment incorporates a Graphical User Interface (GUI) to the banking system we're creating using PySide6, allowing users to view and manage client and bank account data through a lookup window. Our main task is to implement the Event Driven Programming Paradigm to the system as the windows and the design is already given.
Assignment 5: For this assignment, we are implementing a filtering algorithm to the application, wrapping up the project by generating help files for classes using class documentation, and packaging the project into an installer for distribution. All while using our knowledge in Algorithms, Help Files and Distribution.

## Encapsulation

I achieved Encapsulation in the BankAccount class by making its attributes private and only allowing access through methods.
In the BankAccount's class, the diagram specifies that its three attributes (`account_number`, `client_number`, and `balance`) must be private. Attributes were made private by prefixing an attribute name with double underscores before the name (`__`).
Since these attributes are private, the only way the attribute's values can be accessed is by using Accessors. Accessors are methods named after the attribute's name marked with the `@property` decorator. The only attribute that can be modified is the `balance` attribute. But since the `balance` attribute is private, it can only be changed using the `update_balance()` method, which is used within the `deposit()` and `withdraw()` methods.

## Polymorphism

This was achieved by making the `BankAccount` abstract, and creating subclasses from the `BankAccount` class. This makes it so that instances of the `BankAccount` class can only be called by it's subclasses which are more detailed/specific/specialized versions of the `BankAccount` class.  
These subclasses are the newly created `ChequingAccount`, `InvestmentAccount`, and `SavingsAccount`. As these subclasses are children of the `BankAccount` class, they inherit all methods and attributes from their parent class like the `bank_account.get_service_charges()` method.
With the `bank_account.get_service_charges()` method, each subclass has their own way of calculating the value for the service charge.

## Strategy Pattern

Ihe strategy pattern is used to create and manage different service charge strategies. These strategies are used for calculating the service charge of a client's bank account, and each subclass of ServiceChargeStrategy has a different way of calculating the service charge.

This replaces the existing calculations in the `get_service_charges` method in the BankAccount's subclasses with an abstract method for calculating service charge. This method can be freely changed or swapped with another service charge method based on the ServiceChargeStrategy subclass given, which is good for scalability.

## Observer Pattern

The observer pattern is used to notify clients of changes in their bank accounts.
BankAccounts being the subject that notifies the observer (the Client object).

If the bank account is at a low balance or they try to make a deposit that's above their account's limit, the bank account sends a notification to the client assigned. The client object will receive a message from the affected bank account(s), which will send a notification to the client's email.

## Event-Driven Programming Paradigm

Using PySide6, the Event-Driven Programming Paradigm was applied by creating a user interface that listens for user interactions, then executing functions based on those actions. Giving the user an interface to interact and manage data with.  

There are two windows in this program. The first window is used to display a client's bank account information. An event handler listens for the user clicking the `lookup_button` QPushButton widget. When that action happens, a slot function is run where the user's input is taken from the `client_number_edit` QLineEdit widget, then checks if the requested client exists. If that requested client exists, it goes through an array of bank accounts and displays each bank account under the requested client in the `account_table` QTableWidget below. When the user starts typing in the `client_number_edit` widget again, an event handler listens for that action and executes a slot function that clears the table of displayed records.  

If the user clicks a bank account's account number in the `account_table` QTableWidget, it opens a new window where the selected bank account can be managed. Using buttons and event listeners to give the user the option to deposit or withdraw from the bank account. The transaction amount is taken from the user's input in the `transaction_amount_edit` QLineEdit widget, and either does a deposit or withdrawal based on the button the user clicks. A Signal is then used to communicate to the other window to update the bank account details of the corresponding bank account.  

## Filtering

The application asked for a feature that goes through the displayed bank accounts, and returns a collected list of accounts based on the criteria the user entered.

As Python doesn't have a built-in filtering algorithm, if-else blocks and conditional statements were used to accomplish filtering for the application. First it takes values from the window *(the `filter_combo_box` and `filter_edit` elements)* for filter criteria.
Then using if-else blocks and conditional statements, it goes through each displayed account from the `account_table` element and checks if the displayed details match the filter criteria. Then displays filtered results by hiding the row of the account that doesn't meet the filter criteria.
