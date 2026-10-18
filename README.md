# ValuePlus Customer & Fleet Manager

A beginner-friendly Python command-line application for managing customer records, fleet information, and vehicle leasing quotations.

## About the Project

The **ValuePlus Customer & Fleet Manager** is an independent portfolio project inspired by common workflows in vehicle leasing and fleet management.

The goal is to build a simple application that helps organize customer information, track vehicle availability, search for suitable vehicles, and calculate estimated leasing costs.

This project is also part of my journey in developing practical Python programming skills by turning business requirements into a working application.

*This is an independent learning project. It is not official Value Plus software and is not affiliated with Value Plus KSA.*

## Features — Version 1

The first version is planned to include:

- **Customer Management:** Add, view, and search customer records.
- **Fleet Management:** Add, view, and search vehicle records.
- **Vehicle Availability:** Filter vehicles by city, category, and availability status.
- **Quotation Management:** Create and view leasing quotations linked to customers and vehicles.
- **Cost Calculation:** Calculate estimated monthly and total contract costs.
- **Data Storage:** Save and load records using JSON files.
- **Input Validation:** Handle invalid entries and missing records gracefully.

Features will be marked as completed as they are implemented and tested.

## Technologies

- **Python** — application logic and business rules.
- **JSON** — local data storage.
- **Git and GitHub** — version control and project documentation.
- **Terminal / Command Line** — user interaction.

## Project Structure

```text
valueplus-customer-fleet-manager/
├── main.py
├── customers.py
├── fleet.py
├── quotations.py
├── storage.py
├── data/
│   ├── customers.json
│   ├── vehicles.json
│   └── quotations.json
├── README.md
└── .gitignore
```

The `data/` directory and JSON files will be created as the storage functionality is implemented.

- `main.py` — runs the application and displays the main menu.
- `customers.py` — handles customer-related operations.
- `fleet.py` — handles vehicle records and availability searches.
- `quotations.py` — creates quotations and calculates estimated costs.
- `storage.py` — manages loading and saving JSON data.
- `data/` — stores customer, vehicle, and quotation records locally.

## How to Run

**Prerequisites:** Python 3 installed on your computer.

1. Clone this repository:

   ```bash
   git clone https://github.com/esmaahmet25/valueplus-customer-fleet-manager.git
   ```

2. Open the project directory:

   ```bash
   cd valueplus-customer-fleet-manager
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Example Workflow

A typical workflow is intended to look like this:

1. Add a customer who needs leased vehicles.
2. Add vehicle records to the fleet.
3. Search for vehicles matching the customer's requirements.
4. Create a quotation using the selected customer and vehicle.
5. Calculate the estimated monthly cost and total contract value.
6. Save the records for future use.

## Learning Objectives

Through this project, I aim to practice:

- Functions, loops, conditionals, and dictionaries.
- Lists and structured data management.
- Input validation and error handling.
- Splitting a program into multiple Python modules.
- Reading and writing JSON files.
- Testing, debugging, and maintaining code.
- Using Git and GitHub to document development progress.

## Future Improvements

Possible future versions may include:

- A database using SQLite or PostgreSQL.
- Automated customer follow-up reminders.
- More detailed fleet and quotation reports.
- A web interface using Flask or FastAPI.
- API integrations and AI-powered customer support.

These are future ideas, not features currently included in Version 1.

## Project Status

**Version 1 — In Development**

The project is being built incrementally, starting with core customer, fleet, and quotation functionality before adding persistent JSON storage.

## Disclaimer

This project uses fictional sample data and illustrative prices for educational purposes. It does not use Value Plus KSA's internal data, systems, or actual pricing.

## Author

Developed as part of my journey in Python programming, software development, and AI automation.
