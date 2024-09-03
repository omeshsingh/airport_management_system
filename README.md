# airport_management_system
The provided script is a simple command-line interface (CLI) for an Airport Management System that allows users to add details, view details, and reserve seats in a MySQL database. The script includes several functions for handling database operations such as adding records to various tables (airports, airlines, airplanes, flights, passengers, reservations) and retrieving data from them. Below is an explanation of each section of the code along with a small correction and enhancement:

### 1. **Database Connection**
   ```python
   import mysql.connector

   # Connect to MySQL
   conn = mysql.connector.connect(
       host="127.0.0.1",
       user="root",
       password="password",
       database="mydatabase"
   )
   cursor = conn.cursor()
   ```
   - This part establishes a connection to a MySQL database. Ensure that the `host`, `user`, `password`, and `database` parameters match your local MySQL setup.

### 2. **Main Menu**
   ```python
   def display_menu():
       print("Airport Management System")
       print("1. Add Details")
       print("2. View Details")
       print("3. Reserve a seat")
       print("0. Exit")
   ```
   - Displays the main menu with options to add details, view details, reserve a seat, or exit the application.

### 3. **Sub-Menu for Adding Details**
   ```python
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
   ```
   - This sub-menu handles the addition of different entities (airports, airlines, airplanes, flights, passengers, reservations) to the database.

### 4. **Sub-Menu for Viewing Details**
   ```python
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
   ```
   - This sub-menu allows users to view details of different entities in the database.

### 5. **Functions for Adding Details**
   - The functions (`add_airport`, `add_airline`, `add_airplane`, `add_flight`, `add_passenger`, `add_reservation`) handle the insertion of records into the respective tables in the database.

### 6. **Functions for Viewing Details**
   - The functions (`view_airports`, `view_airlines`, `view_airplanes`, `view_flights`, `view_passengers`, `view_reservations`) retrieve and display records from the respective tables.

### 7. **Function for Reserving a Seat**
   ```python
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
   ```
   - This function allows users to reserve a seat on a flight. It first checks for available flights on the specified route and then allows the user to register a passenger and reserve a seat.

### 8. **Main Loop**
   ```python
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
   ```

### 9. **Closing the Cursor and Connection**
   ```python
   # Close the cursor and connection
   cursor.close()
   conn.close()
   ```
   - Ensures the cursor and database connection are properly closed after the program exits.

### Corrections/Enhancements:
- Ensure data integrity by checking if the `passenger_id` already exists before inserting a new passenger.
- Use `try-except` blocks to handle potential errors during database operations.
- Handle seat assignment more dynamically by automatically choosing the next available seat number.

If you need further customization or have any specific questions, feel free to ask!
