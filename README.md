# CSV to MySQL Data Transfer

- [CSV to MySQL Data Transfer](#csv-to-mysql-data-transfer)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Known Issues](#known-issues)
  - [Contributing](#contributing)
  - [License](#license)
  - [Additional Information](#additional-information)

This program allows you to transfer data from a CSV file to a MySQL database table. It validates the data in the CSV file and inserts it into the specified table in the MySQL database.

## Installation

Before running the program, ensure that Python is installed on your system. You also need to install the required dependencies. Run the following command to install the dependencies:
```
pip install -r requirements.txt
```

## Usage

1. Ensure that the metadata in the metadata folder is according to the database schema.
2. Run the script by executing the following command:
```
python main.py --type <product type/table name> --file <path to csv>
```


## Known Issues

One important thing to note is that you should keep the metadata in the CSV file updated according to the database schema. Any discrepancies between the metadata and the database schema may result in errors or incorrect data insertion.

## Contributing

Contributions to this project are currently not accepted. However, if you have suggestions or bug reports, please feel free to open an issue in the GitHub repository.

## License

This project is currently not licensed.

## Additional Information

There is currently no additional information or documentation available for this project.
