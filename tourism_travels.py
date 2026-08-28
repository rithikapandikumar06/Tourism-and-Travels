print("**********WELCOME TO DREAM VACATION**********")

a = input("Enter N for national, I for International tour: ").lower()


# =========================================================
# NATIONAL TOUR
# =========================================================

def national():
    print("*****Travel details*****")

    des = input("Enter your destination: ")
    trans = input("Enter the transport you prefer to travel: ")
    pas = int(input("Enter the number of passengers: "))
    days = int(input("Enter the number of days: "))
    nights = int(input("Enter the number of nights: "))
    dep = input("Enter your departure date: ")
    ret = input("Enter your return date: ")

    print("*****Passenger details*****")

    for i in range(pas):
        print("## Details of passenger", i + 1, "##")

        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gen = input("Enter your gender: ")
        phno = input("Enter the phone no for contact: ")

        if len(phno) != 10:
            print("Please ensure that your phone number is 10 digits")
            break

        adno = input("Enter the adhar no: ")
        address = input("Enter your address: ")
        dob = input("Enter your date of birth: ")


# =========================================================
# INTERNATIONAL TOUR
# =========================================================

def International():
    print("*****Travel details*****")

    des = input("Enter your destination: ")
    trans = input("Enter the transport you prefer to travel: ")
    pas = int(input("Enter the number of passengers: "))
    days = int(input("Enter the number of days: "))
    nights = int(input("Enter the number of nights: "))
    dep = input("Enter your departure date: ")
    ret = input("Enter your return date: ")

    print("*****Passenger details*****")

    for i in range(pas):
        print("## Details of passenger", i + 1, "##")

        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gen = input("Enter your gender: ")
        phno = input("Enter the phone no for contact: ")

        if len(phno) != 10:
            print("Please ensure that your phone number is 10 digits")
            break

        adno = input("Enter the adhar no: ")
        address = input("Enter your address: ")
        dob = input("Enter your date of birth: ")
        passport = input("Enter your passport id: ")


# =========================================================
# ROOMS
# =========================================================

def rooms():
    print("*****Availability of rooms*****")

    typ = input(
        "Enter the type you prefer "
        "Deluxe/standard/villa/exclusive suits: "
    ).lower()

    num = int(input("Enter the no of rooms you prefer: "))
    night = int(input("Enter how much nights you would wish to stay: "))

    print("*****Type of room*****")

    if typ == "deluxe":
        print("##Deluxe##")
        price = 2500 * night
        return price

    elif typ == "standard":
        print("##Standard##")
        price = 1500 * night
        return price

    elif typ == "villa":
        print("##Villa##")
        price = 10000 * night
        return price

    elif typ == "exclusive suits":
        print("##Exclusive suits##")
        price = 5000 * night
        return price

    else:
        print("Room type not available")
        return 0


# =========================================================
# CARS
# =========================================================

def cars():
    print("*****CARS*****")

    n = int(input("Enter the no of seats you prefer: "))

    if n <= 4:
        car = input(
            "Enter the car you prefer to travel "
            "celerio/alto/maruti/mahindra/mercedes: "
        )

        distance = int(
            input("Enter the distance covered is 500-900km: ")
        )

        days = int(
            input("Enter the no of days you need the car: ")
        )

        if distance >= 500 and distance < 600:
            price = 6000 * days
            return price

        elif distance >= 600 and distance < 700:
            price = 7000 * days
            return price

        elif distance >= 700 and distance <= 800:
            price = 8000 * days
            return price

        elif distance >= 800 and distance <= 900:
            price = 9000 * days
            return price

        else:
            print("Distance should be between 500-900 km")
            return 0

    elif n <= 8 and n > 4:
        car = input(
            "Enter the car you prefer to travel "
            "toyota innova/mahindra scorpio/kia carnival/"
            "bmw/maruti suzuki: "
        )

        distance = int(
            input("Enter the distance covered is 500-900km: ")
        )

        days = int(
            input("Enter the no of days you need the car: ")
        )

        if distance >= 500 and distance < 600:
            price = 9000 * days
            return price

        elif distance >= 600 and distance <= 700:
            price = 10000 * days
            return price

        elif distance >= 700 and distance <= 800:
            price = 11000 * days
            return price

        elif distance >= 800 and distance <= 900:
            price = 12000 * days
            return price

        else:
            print("Distance should be between 500-900 km")
            return 0

    else:
        print("Car is not available")
        return 0


# =========================================================
# BUS
# =========================================================

def Bus():
    print("*****BUSES*****")

    n = int(input("Enter the no of seats you prefer: "))

    typ = input(
        "Enter your preference ac/non-ac: "
    ).lower()

    places = input(
        "Enter the destination you prefer "
        "tiruchi/madurai/thanjavur/kanchipuram/thiruvannamalai: "
    ).lower()

    if typ == "ac":

        if places == "tiruchi":
            price = 1000 * n
            return price

        elif places == "madurai":
            price = 800 * n
            return price

        elif places == "thanjavur":
            price = 750 * n
            return price

        elif places == "kanchipuram":
            price = 500 * n
            return price

        elif places == "thiruvannamalai":
            price = 900 * n
            return price

        else:
            print("Destination not available")
            return 0

    elif typ == "non-ac":

        if places == "tiruchi":
            price = 900 * n
            return price

        elif places == "madurai":
            price = 700 * n
            return price

        elif places == "thanjavur":
            price = 650 * n
            return price

        elif places == "kanchipuram":
            price = 400 * n
            return price

        elif places == "thiruvannamalai":
            price = 800 * n
            return price

        else:
            print("Destination not available")
            return 0

    else:
        print("Please enter ac or non-ac")
        return 0


# =========================================================
# TRAIN
# =========================================================

def train():
    print("*****TRAINS*****")

    n = int(input("Enter the no of seats you prefer: "))

    typ = input(
        "Enter your preference ac/non-ac: "
    ).lower()

    places = input(
        "Enter the destination you prefer "
        "mysore/delhi/tiruchi/madurai/dindugal: "
    ).lower()

    if typ == "ac":

        if places == "mysore":
            price = 2500 * n
            return price

        elif places == "delhi":
            price = 4000 * n
            return price

        elif places == "tiruchi":
            price = 1500 * n
            return price

        elif places == "madurai":
            price = 1800 * n
            return price

        elif places == "dindugal":
            price = 1600 * n
            return price

        else:
            print("Destination not available")
            return 0

    elif typ == "non-ac":

        if places == "mysore":
            price = 2000 * n
            return price

        elif places == "delhi":
            price = 3500 * n
            return price

        elif places == "tiruchi":
            price = 1000 * n
            return price

        elif places == "madurai":
            price = 1300 * n
            return price

        elif places == "dindugal":
            price = 1100 * n
            return price

        else:
            print("Destination not available")
            return 0

    else:
        print("Please enter ac or non-ac")
        return 0


# =========================================================
# FLIGHT
# =========================================================

def flight():
    print("*****FLIGHTS*****")

    n = int(input("Enter the no of seats you prefer: "))

    typ = input(
        "Enter your preference economic/business: "
    ).lower()

    places = input(
        "Enter the destination you prefer "
        "goa/kerala/ooty/shimla/gangtok: "
    ).lower()

    if typ == "economic":

        if places == "goa":
            price = 7000 * n
            return price

        elif places == "kerala":
            price = 4000 * n
            return price

        elif places == "ooty":
            price = 3000 * n
            return price

        elif places == "shimla":
            price = 8000 * n
            return price

        elif places == "gangtok":
            price = 8000 * n
            return price

        else:
            print("Destination not available")
            return 0

    elif typ == "business":

        if places == "goa":
            price = 2 * 7000 * n
            return price

        elif places == "kerala":
            price = 2 * 4000 * n
            return price

        elif places == "ooty":
            price = 2 * 3000 * n
            return price

        elif places == "shimla":
            price = 2 * 8000 * n
            return price

        elif places == "gangtok":
            price = 2 * 8000 * n
            return price

        else:
            print("Destination not available")
            return 0

    else:
        print("Please enter economic or business")
        return 0


# =========================================================
# NATIONAL TRAVEL - MODE OF TRANSPORT
# =========================================================

def national_travels():

    print("*****Mode of transport*****")

    trans = input(
        "Enter the transport you prefer "
        "car/bus/train/flight: "
    ).lower()

    if trans == "car":
        x = cars()
        return x

    elif trans == "bus":
        x = Bus()
        return x

    elif trans == "train":
        x = train()
        return x

    elif trans == "flight":
        x = flight()
        return x

    else:
        print("Transport not available")
        return 0


# =========================================================
# INTERNATIONAL TRAVEL - FLIGHTS
# =========================================================

def international_travels():

    print("*****Availability of flights*****")

    coun = input(
        "Enter the destination you prefer "
        "Singapore/Paris/London/Dubai/Bangkok: "
    ).lower()

    n = int(input("Enter the no of tickets: "))

    typ = input(
        "Enter your preference economic/business: "
    ).lower()

    if typ == "economic":

        if coun == "singapore":
            price = 8500 * n
            return price

        elif coun == "paris":
            price = 23500 * n
            return price

        elif coun == "london":
            price = 21400 * n
            return price

        elif coun == "dubai":
            price = 12150 * n
            return price

        elif coun == "bangkok":
            price = 7500 * n
            return price

        else:
            print("Destination not available")
            return 0

    elif typ == "business":

        if coun == "singapore":
            price = 11500 * n
            return price

        elif coun == "paris":
            price = 26500 * n
            return price

        elif coun == "london":
            price = 25400 * n
            return price

        elif coun == "dubai":
            price = 16150 * n
            return price

        elif coun == "bangkok":
            price = 10500 * n
            return price

        else:
            print("Destination not available")
            return 0

    else:
        print("Please enter economic or business")
        return 0


# =========================================================
# MYSQL CONNECTION
# =========================================================

import mysql.connector as mc


try:

    con = mc.connect(
        host="localhost",
        user="root",
        password="prince",
        port=3307
    )

    if con.is_connected():
        print("Connected to mysql")

        c = con.cursor()

        # -------------------------------------------------
        # NATIONAL TOUR
        # -------------------------------------------------

        if a == "n":

            national()

            p = national_travels()
            print("Your total transport cost is", p)

            q = rooms()
            print("Your total room rent is", q)

            print("*****TOTAL*****")
            print("Your total cost is", p + q)

            # Create database
            c.execute(
                "CREATE DATABASE IF NOT EXISTS dream_vacation"
            )

            c.execute("USE dream_vacation")

            print("Created database successfully")

            # Create national table
            createq = """
            CREATE TABLE IF NOT EXISTS national(
                psgno INT(11),
                name VARCHAR(25),
                age INT(3),
                gender CHAR(1),
                destination VARCHAR(20),
                departuredate DATE,
                returndate DATE,
                departuretime VARCHAR(10),
                returntime VARCHAR(10)
            )
            """

            c.execute(createq)

            print("Table national created successfully")

            # Insert records
            while True:

                psgno = int(
                    input("Enter the passenger no: ")
                )

                name = input(
                    "Enter the passenger's name: "
                )

                age = int(
                    input("Enter the passenger's age: ")
                )

                destination = input(
                    "Enter the passenger's destination: "
                )

                gender = input(
                    "Enter the passenger's gender: "
                )

                departuredate = input(
                    "Enter the departure date: "
                )

                returndate = input(
                    "Enter the return date: "
                )

                departuretime = input(
                    "Enter the departure time: "
                )

                returntime = input(
                    "Enter the return time: "
                )

                sql = """
                INSERT INTO national
                (
                    psgno,
                    name,
                    age,
                    gender,
                    destination,
                    departuredate,
                    returndate,
                    departuretime,
                    returntime
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """

                values = (
                    psgno,
                    name,
                    age,
                    gender,
                    destination,
                    departuredate,
                    returndate,
                    departuretime,
                    returntime
                )

                c.execute(sql, values)

                con.commit()

                ch = input(
                    "Do you want to continue(y/n)? "
                ).lower()

                if ch == "n":
                    break

            print(
                "Added records into national table successfully"
            )

            c.execute("SELECT * FROM national")

            data = c.fetchall()

            for i in data:
                print(i)

            print(
                "Total number of rows:",
                c.rowcount
            )


        # -------------------------------------------------
        # INTERNATIONAL TOUR
        # -------------------------------------------------

        elif a == "i":

            International()

            p = international_travels()
            print("Your total transport cost is", p)

            q = rooms()
            print("Your total room rent is", q)

            print("*****TOTAL*****")
            print("Your total cost is", p + q)

            # Create database
            c.execute(
                "CREATE DATABASE IF NOT EXISTS dream_vacation"
            )

            c.execute("USE dream_vacation")

            print("Created database successfully")

            # Create international table
            createq = """
            CREATE TABLE IF NOT EXISTS international(
                psgno INT(11),
                name VARCHAR(25),
                age INT(3),
                gender CHAR(1),
                destination VARCHAR(20),
                departuredate DATE,
                returndate DATE,
                departuretime VARCHAR(10),
                returntime VARCHAR(10)
            )
            """

            c.execute(createq)

            print(
                "Table international created successfully"
            )

            # Insert records
            while True:

                psgno = int(
                    input("Enter the passenger no: ")
                )

                name = input(
                    "Enter the passenger's name: "
                )

                age = int(
                    input("Enter the passenger's age: ")
                )

                destination = input(
                    "Enter the passenger's destination: "
                )

                gender = input(
                    "Enter the passenger's gender: "
                )

                departuredate = input(
                    "Enter the departure date: "
                )

                returndate = input(
                    "Enter the return date: "
                )

                departuretime = input(
                    "Enter the departure time: "
                )

                returntime = input(
                    "Enter the return time: "
                )

                sql = """
                INSERT INTO international
                (
                    psgno,
                    name,
                    age,
                    gender,
                    destination,
                    departuredate,
                    returndate,
                    departuretime,
                    returntime
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """

                values = (
                    psgno,
                    name,
                    age,
                    gender,
                    destination,
                    departuredate,
                    returndate,
                    departuretime,
                    returntime
                )

                c.execute(sql, values)

                con.commit()

                ch = input(
                    "Do you want to continue(y/n)? "
                ).lower()

                if ch == "n":
                    break

            print(
                "Added records into international table successfully"
            )

            c.execute("SELECT * FROM international")

            data = c.fetchall()

            for i in data:
                print(i)

            print(
                "Total number of rows:",
                c.rowcount
            )

        else:
            print(
                "Please enter N for National or I for International"
            )

        c.close()
        con.close()

    else:
        print("Unable to connect to mysql")


except mc.Error as e:
    print("MySQL Error:", e)
