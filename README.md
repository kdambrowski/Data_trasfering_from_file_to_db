# Data Processing and Database Insertion Application

## Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Demo](#demo)
- [Project Status](#project-status)
- [Acknowledgements](#acknowledgements)

## Overview
The Data Processing and Database Insertion Application is a Python-based tool designed to simplify the transformation and insertion of data from various sources into a SQLite database. It provides functionalities for data preparation, including renaming columns, reordering data, and exporting cleaned data to a CSV file. Additionally, the application allows users to insert the prepared data into a specified SQLite database table.

## Technologies Used
- Python - version 3.7
- SQLite3 - version 3.35
- pandas - version 1.3.3
- re (Regular Expressions) - built-in
- os - built-in

## Features
- Data reading from CSV and Excel files.
- Data preparation, including column renaming and reordering.
- Data export to a CSV file.
- Data insertion into a SQLite database table.

## Setup
To run the project, you need Python 3.7 or later installed. Additionally, ensure you have the required libraries by running:

```bash
 pip install -r requirements.txt
```

Clone the repository and make adjustments to the `Settings.py` file as needed. Then, you can run the application using Python by terminal
```bash
python3 Demo.py
```

## Usage
1. Clone the repository to your local machine.

2. Install the required libraries as mentioned in the "Setup" section.

3. Customize the settings in the provided Python scripts according to your needs.
4. Run the project by command python
```bash
python3 Demo.py
```
5. Fill the required information in the popped terminal requests
6. Check created file

## Demo
[![ Data Processing and Database Insertion Application](https://img.youtube.com/vi/pdDQjnz_rcU/0.jpg)](https://www.youtube.com/watch?v=pdDQjnz_rcU)
 
## Project Status
The project is complete.

## Acknowledgements
- This project was inspired by the need for efficient data processing.
- Thanks to the pandas and SQLite3 communities for their invaluable contributions to data processing and database management in Python.
