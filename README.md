# We-Care-Hospital-Administration

## Overview
We-Care-Hospital-Administration is a Hospital Database Management System (DBMS) designed to streamline and optimize the administrative functions within a healthcare environment. It aims to simplify the management of critical hospital operations such as patient data, billing, room allocations, prescriptions, and staff management through an easy-to-use graphical user interface (GUI). The system integrates seamlessly with a MySQL database for data storage and retrieval, ensuring efficient and accurate handling of hospital operations.

## Features
The hospital management system provides the following functionalities:

### 1. **User Authentication**
- Secure login mechanism to authenticate various users such as doctors, nurses, administrative staff, and other personnel.
- Role-based access control to ensure appropriate data privacy and security, allowing different levels of access based on user roles.

### 2. **Patient Management**
- Register new patients and store their medical history, treatment details, and personal information.
- Schedule appointments and update patient records.
- Efficient retrieval of patient data as needed.

### 3. **Room Management**
- Allocate hospital rooms to patients based on availability.
- Track room occupancy and manage patient transfers between rooms as required.

### 4. **Staff Management**
- Manage staff records, including doctors, nurses, and support staff.
- Track staff work schedules, shifts, and departmental assignments.

### 5. **Billing and Payment**
- Generate and manage patient bills, including room rates, treatment fees, and medicine costs.
- Track payments and generate bill reports for accounting purposes.

### 6. **Database Connectivity**
- MySQL database integration for storing and retrieving critical information, including patient records, billing data, room allocations, and staff details.
- Secure and efficient database operations to ensure data integrity and consistency.

## Technology Stack
- **Backend:** Python
- **Frontend:** Python (Tkinter for GUI)
- **Database:** MySQL
- **GUI Framework:** Tkinter

## Installation
To install and run the We-Care-Hospital-Administration system, follow these steps:

1. Clone the repository.
```bash
git clone https://github.com/KrishnenduMR/We-Care-Hospital-Administration.git
cd We-Care-Hospital-Administration/src
```
2. Install the required dependencies from the `requirements.txt` file.
```bash
pip install -r requirements.txt
```
3. Set up the MySQL database by creating a database and configuring the connection details in the `config.py` file. Run the provided SQL script to create the necessary tables.
4. Run the application by executing `python login.py`.

## Usage
- Launch the application to access the login screen.
- After logging in, use the various modules (Patient Management, Room Management, Staff Management, Billing, etc.) to manage hospital operations.

## License
This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
