# Dream Vacation - Tourism and Travels

## Project Description

Dream Vacation is a Python-based Tourism and Travels management project.

The project allows users to choose between national and international tours and provides different travel and accommodation options. It calculates the total transportation cost and room rent based on the user's selections.

The project also uses MySQL to store passenger details for national and international tours.

## Features

- National tour booking
- International tour booking
- Passenger details collection
- Room selection and room rent calculation
- Car rental options
- Bus travel options
- Train travel options
- Domestic flight options
- International flight options
- Economic and business class options
- AC and non-AC travel options
- Automatic transportation cost calculation
- Automatic room rent calculation
- Total travel cost calculation
- MySQL database connectivity
- Storage of passenger records in MySQL
- Display of stored passenger records

## Travel Options

### National Tours

For national tours, the project provides the following transportation options:

- Car
- Bus
- Train
- Flight

### International Tours

For international tours, the project provides flight options to:

- Singapore
- Paris
- London
- Dubai
- Bangkok

The user can select:

- Economic class
- Business class

## Room Options

The project provides the following room types:

- Standard
- Deluxe
- Villa
- Exclusive Suites

Room rent is calculated based on the number of nights.

## Car Options

The car section provides options based on the number of seats required.

The cost is calculated according to:

- Number of seats
- Distance
- Number of days

## Bus Options

The bus section allows the user to select:

- AC
- Non-AC

Available destinations include:

- Tiruchi
- Madurai
- Thanjavur
- Kanchipuram
- Thiruvannamalai

The bus cost is calculated based on the number of seats and destination.

## Train Options

The train section allows the user to select:

- AC
- Non-AC

Available destinations include:

- Mysore
- Delhi
- Tiruchi
- Madurai
- Dindugal

The train cost is calculated based on the number of seats and destination.

## Flight Options

The national flight section provides:

- Economic class
- Business class

Available destinations include:

- Goa
- Kerala
- Ooty
- Shimla
- Gangtok

## International Flight Options

International flights are available for:

- Singapore
- Paris
- London
- Dubai
- Bangkok

The user can select economic or business class.

## Database

The project uses MySQL for storing passenger information.

A database named:

`dream_vacation`

is created automatically if it does not already exist.

Two tables are used:

- `national`
- `international`

The tables store passenger and travel-related information such as:

- Passenger number
- Passenger name
- Age
- Gender
- Destination
- Departure date
- Return date
- Departure time
- Return time

## Technologies Used

- Python
- MySQL
- MySQL Connector
- SQL

## Python Concepts Used

This project demonstrates several Python programming concepts:

- Variables
- User input
- Functions
- Conditional statements
- `for` loops
- `while` loops
- `if`, `elif`, and `else`
- String methods
- Type conversion
- Return statements
- Exception handling
- Modular programming

## SQL Concepts Used

The project also demonstrates basic SQL operations:

- Creating a database
- Creating tables
- Inserting records
- Selecting records
- Fetching records
- Committing database transactions

## Requirements

Before running the project, install:

- Python
- MySQL Server
- MySQL Connector for Python

Install the MySQL connector using:

```bash
pip install mysql-connector-python
