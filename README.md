# Vital Metrics Extraction

## Prerequisites

- Python (latest version)
- Virtual environment

## Setup

### 1. Create virtual environment

Git bash  
python -m venv venv  
source venv/bin/activate

On Windows, use:
bash  
venv\\Scripts\\activate

### 2. Install dependencies in virtual environment

- pip install -r requirements.txt

### 3. Additional Setup for `pdf2image` Library

#### MacOS

- brew install poppler

#### Windows

- Download the latest poppler package from [@oschwartz10612 version](https://github.com/oschwartz10612/poppler-windows/releases) which is the most up-to-date.
- Move the extracted directory to the desired place on your system.
- Add the `bin/` directory to your PATH.
