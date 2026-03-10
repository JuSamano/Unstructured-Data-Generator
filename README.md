# Unstructured Data Generator

This Python script generates semi-structured data in JSON, XML, and CSV formats. It creates 1000-2000 records of person data with fields like name, age, city, phone, and optionally email. The CSV format also includes a randomly assigned occupation.

## Features

- Generates random person data with semi-structured fields
- Outputs data in three formats: JSON, XML, and CSV
- Saves files to a DATA directory with unique filenames including date and ID
- Each run creates new files with unique identifiers

## Requirements

- Python 3.x
- Standard library modules (no external dependencies)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JuSamano/Unstructured-Data-Generator.git
   cd Unstructured-Data-Generator
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

## Usage

Run the script:
```bash
python generate_data.py
```

The script will generate and save three files:
- `Data_json_YYYY-MM-DD_XXXXXXX.json`
- `Data_xml_YYYY-MM-DD_XXXXXXX.xml`
- `Data_csv_YYYY-MM-DD_XXXXXXX.csv`

Where `YYYY-MM-DD` is today's date and `XXXXXXX` is a unique 8-character ID.

## Output

- **JSON**: Array of person objects
- **XML**: Root element "people" with "person" child elements
- **CSV**: Tabular data with headers: name, age, city, email, phone, occupation

The files are saved in a `DATA` directory created in the same folder as the script.