# Railway Ticket project.... steps required 
''' step 1 - Create account(username & password) after login into ur account
Enter ur train details(train number) and choose how many tickets do u want. Then give ur personal 
infromation(name,age,destination) after ur ticket booking is succesfully completed'''

import random 

# We define a train 'class' which contains 4 parameters
class Train:
    def __init__(self, train_num, source, destination, seats):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.seats = seats

    def info(self):
        print(f"Train Number : {self.train_num}")
        print(f"Source : {self.source}")
        print(f"Destination : {self.destination}")
        print(f"Available Seats : {self.seats}")
        print()

    def book_tickets(self, num_tickets):
        if num_tickets > self.seats:
            return None

        pnr_no = []
        for _ in range(num_tickets):
            pnr_no.append(random.randint(10000, 99999))

        self.seats -= num_tickets
        return pnr_no


class Passenger:
    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def info(self):
        print(f"Passenger Name : {self.name}")
        print(f"Passenger Age : {self.age}")
        print(f"Passenger Gender : {self.gender}")
        print(f"Passenger Phone : {self.phone}")


class Ticket:
    def __init__(self, train, source, destination, passengers, pnr):
        self.train = train
        self.source = source
        self.destination = destination
        self.passengers = passengers
        self.pnr = pnr

    def info(self):
        print(f"Train Number : {self.train.train_num}")
        print(f"Source : {self.source}")
        print(f"Destination : {self.destination}")
        print(f"PNR : {self.pnr}")

        for passenger in self.passengers:
            passenger.info()
            print()


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_pass(self, password):
        return self.password == password


accounts = [
    Account("user1", "password1"),
    Account("user2", "password2")
]

logged_in_account = None

while True:
    print("\n1. Create an account\n2. Login\n")
    choice = input("Enter a choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        accounts.append(Account(username, password))
        print("Account created successfully")

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")

        for account in accounts:
            if account.username == username and account.check_pass(password):
                logged_in_account = account
                break

        if logged_in_account is None:
            print("Invalid details.")
        else:
            print(f"\nLogged in as {logged_in_account.username}\n")
            break

    else:
        print("Invalid choice...")


if logged_in_account is not None:
    trains = [
        Train("12345", "Nellore", "Secendrabad", 32),
        Train("12346", "Nellore", "Hyd", 56),
        Train("12355", "Goa", "Kadapa", 21),
        Train("12456", "Hyd", "Mumbai", 100),
        Train("22222", "Naidupetaa", "Secendrabad", 32)
    ]

    print("----- Available Train Details -----\n")
    for train in trains:
        train.info()

    # Get valid train number and ticket count
    while True:
        try:
            train_num = input("Enter Train Number: ")
            num_tickets = int(input("Enter Number of Tickets: "))

            if num_tickets <= 0:
                raise ValueError("Number of tickets should be greater than 0")

            selected_train = None
            for t in trains:
                if t.train_num == train_num:
                    selected_train = t
                    break

            if selected_train is None:
                raise ValueError("Invalid Train Number.")

            if num_tickets > selected_train.seats:
                raise ValueError("Selected more tickets than available seats")

            break

        except ValueError as e:
            print(f"Invalid input: {e}")

    passengers = []

    for i in range(num_tickets):
        print(f"\nEnter details for passenger {i + 1}:")

        while True:
            try:
                name = input("Name: ").strip()
                if not name:
                    raise ValueError("Name cannot be empty.")

                age = int(input("Age: "))
                if age <= 0 or age > 120:
                    raise ValueError("Invalid age")

                gender = input("Gender: ")
                phone = input("Phone Number: ")

                if len(phone) != 10 or not phone.isdigit():
                    raise ValueError("Invalid phone number.")

                passenger = Passenger(name, age, gender, phone)
                passengers.append(passenger)
                break

            except ValueError as e:
                print(f"Invalid input: {e}")

    pnr = selected_train.book_tickets(num_tickets)

    if pnr is None:
        print("Tickets not available..")
    else:
        print("\n---------- Booking Successful ----------\n")
        print("Ticket details:\n")

        for i in range(num_tickets):
            ticket = Ticket(
                selected_train,
                selected_train.source,
                selected_train.destination,
                [passengers[i]],
                pnr[i]
            )
            ticket.info()

        print("\n-------- Thank you --------")
        print("-------- Safe Journey --------")
