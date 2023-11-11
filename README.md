# PDF Merger

Stop paying for nothing. Don't worry anymore about cancelling free trials:

This Python script allows you to merge multiple PDF documents into a single PDF file.

## Prerequisites

- Python 3.x installed. If not, download and install it from [python.org](https://www.python.org/).
- You can use [Homebrew](https://brew.sh/) to install it (for macOS users):

```bash
brew install python
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/gonbaum/pdfmerger.git
cd pdfmerger
```

### 2. Create a Virtual Environment (Optional but Recommended)

### On Windows

```bash
python -m venv venv_pdf
```

### On Unix or MacOS

```bash
python3 -m venv venv_pdf
```

### 3. Activate the Virtual Environment

## On Unix or MacOS

```bash
source venv_pdf/bin/activate
```

### On Windows

```bash
venv_pdf\Scripts\activate
```

### 4. Install dependencies

pip install -r requirements.txt

## Usage

The documents to merge must be located inside the /documents folder. The order of merging is determined by sorting the list of .pdf files folder using the sort() method. By default, this will sort the files alphabetically. So you can name your files for example:

doc-1, doc-2, doc-3 ... , and so on acording to your desired order.

Then run:

```bash
python pdf_merger.py
```

The merged file will be outputed in the root directory with the name 'merged_documents.pdf'.

## License

This project is licensed under the MIT License
