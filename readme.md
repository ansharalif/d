# Data Scraper for SSCASN

This Python script scrapes job vacancy data from the SSCASN website, saving the results in a CSV file. The script extracts specific details such as institution name, job formation, job title, work unit, number of vacancies, and salary range.

## Requirements

To run this script, you'll need:

- Python 3.x
- Required Python packages (install them using `pip` if necessary):
  - `requests`
  - `csv`
  - `time`

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/rfaturriza/get-data-cpns-to-csv-2024
cd get-data-cpns-to-csv-2024
```

### 2. Install Dependencies

Ensure you have Python 3.x installed. Then, install any required packages:

```bash
pip install requests
```

### 3. Run the Script

Execute the script by running the following command in your terminal:

```bash
python main.py
```

### 4. Output

The script will generate a CSV file named `data-{timestamp}.csv`, where `{timestamp}` is the current Unix timestamp. The CSV file will contain the following columns:

- **Nama Instansi**: The name of the institution.
- **Formasi**: The job formation name.
- **Jabatan**: The job title.
- **Unit Kerja**: The work unit.
- **Jumlah Kebutuhan**: The number of vacancies.
- **Gaji Min**: The minimum salary.
- **Gaji Max**: The maximum salary.
- **Link**: A link to more details about the job vacancy.

### 5. Customization

If you need to change the search parameters, you can modify the following variables in the script:

- `kode_pendidikan`: The education code.
- `kode_pengadaan`: The procurement code.

You can also adjust the loop's range to specify the number of pages to scrape.

### 6. Done

After the script completes execution, you'll see a `Done` message in the terminal, indicating that the data has been successfully scraped and saved.

## Contact

For any questions or feedback, please contact rfaturriza.dev@gmail.com.
