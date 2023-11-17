# QTI Assessment - Data Engineer Position

## Overview
This repository contains the assessment for the Data Engineer position at PT. Quantus Telematika Indonesia. The project involves building a database schema for a specific form, generating dummy data, and running queries to analyze the data.

## Project Structure
- `schema.png`: Visual representation of the database schema.
- `main.ipynb`: Jupyter notebook with the initial project code.
- `tugas.pdf`: PDF file containing the form and the tasks

## Database Schema
The database schema is designed to track assets, employees, companies, supervisors, asset loss reports, and loss events. The schema is visualized below:
(![Schema](https://i.imgur.com/hukgzgp.png)).

## Features
- Data generation for companies, employees, supervisors, assets, asset loss reports, and loss events.
- Queries to determine:
  - The most frequently lost item type in each city and its count.
  - The supervisor with the highest number of lost items reported by their staff in each company.

## Installation and Usage
1. Clone the repository.
2. Install required Python packages: `Faker`, `pymysql`, `pandas`.
3. Set up a MySQL database and update the database connection details in `main.ipynb`.
4. Run `main.ipynb` to generate data and perform the analysis.

## Technologies
- Python
- MySQL
- Pandas for data analysis
- Faker for generating dummy data
- PyMySQL for database interaction

## Author

`Rahmadiyan Muhammad`

- Porto: [https://rian.social
- Medium: [https://medium.com/@rianying
- Linkedin: [https://www.linkedin.com/in/rahmadiyanmuhammad/
