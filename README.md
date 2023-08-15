# Vital Metrics Extraction

## Prerequisites

Before you begin, ensure you have the following:

- Python latest version or v3 above
- Virtual Environment

### Installing Virtual Environment

#### Windows

1. Open Command Prompt or PowerShell
2. Run `python -m venv venv`
3. Run `venv\Scripts\activate`

#### MacOS and Linux

1. Open Terminal
2. Run `python -m venv venv`
3. Run `source venv/bin/activate`

## Setup

1. Activate virtual environment

- Run `source venv/bin/activate` on MacOS and Linux
- Run `venv\Scripts\activate` on Windows

2. Install dependencies in virtual environment

- Run `pip3 install -r requirements.txt` or `pip install -r requirements.txt`

3. Additional Setup for `pdf2image` Library

#### MacOS

- Run `brew install poppler`

#### Windows

1. Download the latest poppler package from [@oschwartz10612 version](https://github.com/oschwartz10612/poppler-windows/releases) which is the most up-to-date.
2. Move the extracted directory to the desired place on your system.
3. Add the `bin/` directory to your PATH.

### Using Python Extension in VS Code

1. Open VS Code
2. Install the Python extension
3. Open the project folder in VS Code
4. Select the virtual environment by clicking on the Python version in the bottom left corner of the VS Code window
