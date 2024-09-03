import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="mydatabase"
)
cursor = conn.cursor()

def display_menu():
    print("Airport Management System")
    print("1. Add Details")
    print("2. View Details")
    print("3. Reserve a seat")
    print("0. Exit")

def display_menu1():

    while True:
        print("Add Details:")
        print("1. Add Airport")
        print("2. Add Airline")
        print("3. Add Airplane")
        print("4. Add Flight")
        print("5. Add Passenger")
        print("6. Add Reservation")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "0":
            break
        elif choice == "1":
            add_airport()
        elif choice == "2":
            add_airline()
        elif choice == "3":
            add_airplane()
        elif choice == "4":
            add_flight()
        elif choice == "5":
            add_passenger()
        elif choice == "6":
            add_reservation()
        else:
            print("Invalid choice. Please try again.")

def display_menu2():

    while True:
        print("View Details:")
        print("1. View Airports")
        print("2. View Airlines")
        print("3. View Airplanes")
        print("4. View Flights")
        print("5. View Passengers")
        print("6. View Reservations")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "0":
            break
        elif choice == "1":
            view_airports()
        elif choice == "2":
            view_airlines()
        elif choice == "3":
            view_airplanes()
        elif choice == "4":
            view_flights()
        elif choice == "5":
            view_passengers()
        elif choice == "6":
            view_reservations()
        else:
            print("Invalid choice. Please try again.")

def add_airport():
    airport_code = input("Enter airport code: ")
    airport_name = input("Enter airport name: ")
    city = input("Enter city: ")
    country = input("Enter country: ")
    query = "INSERT INTO airports (airport_code, airport_name, city, country) VALUES (%s, %s, %s, %s)"
    values = (airport_code, airport_name, city, country)
    cursor.execute(query, values)
    conn.commit()
    print("Airport added successfully")

def add_airline():
    airline_id = input("Enter airline id: ")
    airline_name = input("Enter airline name: ")
    country = input("Enter country: ")
    query = "INSERT INTO airlines (airline_id, airline_name, country) VALUES (%s, %s, %s)"
    values = (airline_id, airline_name, country)
    cursor.execute(query, values)
    conn.commit()
    print("Airline added successfully")

def add_airplane():
    airplane_id = input("Enter airplane id: ")
    airplane_model = input("Enter airplane model: ")
    capacity = int(input("Enter capacity: "))
    query = "INSERT INTO airplanes (airplane_id, airplane_model, capacity) VALUES (%s, %s, %s)"
    values = (airplane_id, airplane_model, capacity)
    cursor.execute(query, values)
    conn.commit()
    print("Airplane added successfully")

def add_flight():
    flight_number = int(input("Enter flight number: "))
    airline_id = int(input("Enter airline ID: "))
    airplane_id = int(input("Enter airplane ID: "))
    departure_airport_code = input("Enter departure airport code: ")
    arrival_airport_code = input("Enter arrival airport code: ")
    departure_time = input("Enter departure time (YYYY-MM-DD HH:MM:SS): ")
    arrival_time = input("Enter arrival time (YYYY-MM-DD HH:MM:SS): ")
    available_seats = int(input("Enter available seats: "))
    fare = float(input("Enter fare: "))
    query = "INSERT INTO flights (flight_number, airline_id, airplane_id, departure_airport_code, arrival_airport_code, departure_time, arrival_time, available_seats, fare) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (flight_number, airline_id, airplane_id, departure_airport_code, arrival_airport_code, departure_time, arrival_time, available_seats, fare)
    cursor.execute(query, values)
    conn.commit()
    print("Flight added successfully")

def add_passenger():
    passenger_id = input("Enter passenger id: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    phone_number = input("Enter phone number: ")
    query = "INSERT INTO passengers (passenger_id, first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s, %s)"
    values = (passenger_id, first_name, last_name, email, phone_number)
    cursor.execute(query, values)
    conn.commit()
    print("Passenger added successfully")

def add_reservation():
    reservation_id = int(input("Enter reservation id: "))
    flight_number = int(input("Enter flight number: "))
    passenger_id = int(input("Enter passenger ID: "))
    reservation_date = input("Enter reservation date (YYYY-MM-DD HH:MM:SS): ")
    seat_number = int(input("Enter seat number: "))
    query = "INSERT INTO reservations (reservation_id, flight_number, passenger_id, reservation_date, seat_number) VALUES (%s, %s, %s, %s, %s)"
    values = (reservation_id, flight_number, passenger_id, reservation_date, seat_number)
    cursor.execute(query, values)
    conn.commit()
    print("Reservation added successfully")

def view_airports():
    cursor.execute("SELECT * FROM airports")
    airports = cursor.fetchall()
    print("Airports:")
    for airport in airports:
        print(airport)

def view_airlines():
    cursor.execute("SELECT * FROM airlines")
    airlines = cursor.fetchall()
    print("Airlines:")
    for airline in airlines:
        print(airline)

def view_airplanes():
    cursor.execute("SELECT * FROM airplanes")
    airplanes = cursor.fetchall()
    print("Airplanes:")
    for airplane in airplanes:
        print(airplane)

def view_flights():
    cursor.execute("SELECT * FROM flights")
    flights = cursor.fetchall()
    print("Flights:")
    for flight in flights:
        print(flight)

def view_passengers():
    cursor.execute("SELECT * FROM passengers")
    passengers = cursor.fetchall()
    print("Passengers:")
    for passenger in passengers:
        print(passenger)

def view_reservations():
    cursor.execute("SELECT * FROM reservations")
    reservations = cursor.fetchall()
    print("Reservations:")
    for reservation in reservations:
        print(reservation)

def reserve_seat():
    # Input departure and arrival airports
    departure_airport_code = input("Enter departure airport code: ")
    arrival_airport_code = input("Enter arrival airport code: ")

    # Check if there are flights available for the given route
    cursor.execute("SELECT * FROM flights WHERE departure_airport_code = %s AND arrival_airport_code = %s", (departure_airport_code, arrival_airport_code))
    flights = cursor.fetchall()

    if not flights:
        print("No flights available for the given route.")
        return

    # Display available flights
    print()
    print("Available flights for the given route:")
    for flight in flights:
        print(f"Flight Number: {flight[0]}, Departure Time: {flight[5]}, Arrival Time: {flight[6]}, Available Seats: {flight[7]}, Fare: {flight[8]}")
    print()

    # Extract selected flight number from the first flight in the list
    selected_flight_number = flights[0][0]

    # Check if the selected flight has available seats
    selected_flight = [flight for flight in flights if flight[0] == selected_flight_number][0]
    if selected_flight[7] <= 0:
        print("No available seats on the selected flight.")
        return

    # Input passenger details
    passenger_id = input("Enter passenger id: ")
    passenger_first_name = input("Enter passenger first name: ")
    passenger_last_name = input("Enter passenger last name: ")
    passenger_email = input("Enter passenger email: ")
    passenger_phone_number = input("Enter passenger phone number: ")
    query = "INSERT INTO passengers (passenger_id, first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s, %s)"
    values = (passenger_id, passenger_first_name, passenger_last_name, passenger_email, passenger_phone_number)
    cursor.execute(query, values)
    conn.commit()
    print("Passenger registered successfully")
    print()

    # Reserve a seat
    reservation_id = input("Enter reservation id: ")
    seat_number = int(input("Enter seat number: "))
    reservation_date = input("Enter reservation date and time (YYYY-MM-DD HH:MM:SS): ")

    # Insert reservation into database
    query = "INSERT INTO reservations (reservation_id, flight_number, passenger_id, reservation_date, seat_number) VALUES (%s, %s, %s, %s, %s)"
    values = (reservation_id, selected_flight_number, passenger_id, reservation_date, seat_number)
    cursor.execute(query, values)
    conn.commit()

    # Update available seats
    cursor.execute("UPDATE flights SET available_seats = available_seats - 1 WHERE flight_number = %s", (selected_flight_number,))
    conn.commit()

    print("Seat reserved successfully.")




while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "0":
        break
    elif choice == "1":
        display_menu1()
    elif choice == "2":
        display_menu2()
    elif choice == "3":
        reserve_seat()
    else:
        print("Invalid choice. Please try again.")


# Close the cursor and connection
cursor.close()
conn.close()
