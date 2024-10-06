# Cat Importer

This project provides a framework for importing cat data from various file formats including CSV, DOCX, and PDF. The imported data is parsed into `Cat` objects.

## Project Structure

- .gitignore 
- data/ 
    - cats.csv 
    - cats.docx 
    - cats.txt 
- ImportEngine/ 
    - Cat\.py 
    - CSVImporter\.py 
    - DocxImporter\.py 
    - Importer\.py 
    - ImportInterface\.py 
    - PDFImporter\.py 
- README\.md 
- requirements.txt 
- run\.py 
- tmp/

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/obinnaogbonnajoseph/cat-importer.git
    cd cat-importer
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the importer, execute the `run.py` script:

```sh
python run.py
```

This will parse the files located in the data/ directory and print the imported cat data.

## Importers
The project supports importing cat data from the following file formats:

- CSV: Implemented in [CSVImporter](https://github.com/obinnaogbonnajoseph/cat-importer/blob/4e250beb64aa4f292a127c6a52d53a1d1a73c301/ImportEngine/CSVImporter.py)
- DOCX: Implemented in [DocxImporter](https://github.com/obinnaogbonnajoseph/cat-importer/blob/4e250beb64aa4f292a127c6a52d53a1d1a73c301/ImportEngine/DocxImporter.py)
- PDF: Implemented in [PDFImporter](https://github.com/obinnaogbonnajoseph/cat-importer/blob/4e250beb64aa4f292a127c6a52d53a1d1a73c301/ImportEngine/PDFImporter.py). You will need to install the cli tool [xpdf](https://www.xpdfreader.com/about.html).

## Adding New Importers
To add support for a new file format, create a new importer class in the ImportEngine directory that inherits from [ImportInterface](https://github.com/obinnaogbonnajoseph/cat-importer/blob/4e250beb64aa4f292a127c6a52d53a1d1a73c301/ImportEngine/ImportInterface.py). Implement the parse method and add the new importer to the importers list in Importer.

## License
This project is licensed under the MIT License. See the LICENSE file for details.


Feel free to customize this file further based on your specific project details and requirements.