# Work Tools Projects Repository

This repository contains a collection of various projects that I have developed and utilized as work tools. Each of these projects serve a unique purpose to help automate or streamline different tasks. Below you can find detailed information about each tool.

## Table of Contents

- [extractPPTImages.py](#extractPPTImages.py)
- [readTextFromImages.py](#readTextFromImages.py)
- [convertXSLMtoCSV.py](#convertXSLMtoCSV.py)
- [LoginAvosParameterized.py](#LoginAvosParameterized.py)
- [AVOSQuery.ahk](#AVOSQuery.ahk)
- [Paint.ahk](#Paint.ahk)

## extractPPTImages.py 
**extractPPTImages.py** is a Python script that uses the `pptx` and `PIL` libraries to extract text and images from a PowerPoint file. It stores all the images into a target directory with self-describing filenames for easy identification and future use.

### How to Use

1. Ensure you have Python installed on your machine, along with the `pptx` and `PIL` libraries. You can install these libraries using pip:

    ```bash
    pip install python-pptx Pillow
    ```

2. Run the script in your terminal, specifying the source PowerPoint file and target directory as arguments:

    ```bash
    python extractPPTImages.py source.pptx target_directory
    ```

## readTextFromImages.py
**readTextFromImages.py** is a Python script that utilizes an Optical Character Recognition (OCR) library to parse the text from images located in a source directory. It then outputs the text from those images to a target text file.

### How to Use

1. Ensure you have Python and an OCR library (like pytesseract) installed on your machine. You can install pytesseract using pip:

    ```bash
    pip install pytesseract
    ```

2. Run the script in your terminal, specifying the source directory and the target text file:

    ```bash
    python readTextFromImages.py source_directory output.txt
    ```

---

## convertXSLMtoCSV.py

**convertXSLMtoCSV.py** is a Python script that utilizes the `pandas` and `openpyxl` libraries to convert Macro Enabled Excel workbooks (XLSM) to CSV format. It takes the workbook path and sheet name as parameters.

### How to Use

1. Ensure you have Python, along with the `pandas` and `openpyxl` libraries installed. Install these libraries using pip:

    ```bash
    pip install pandas openpyxl
    ```

2. Run the script in your terminal, specifying the workbook path and sheet name as arguments:

    ```bash
    python convertXSLMtoCSV.py workbook.xlsm Sheet1
    ```

## LoginAvosParameterized.py

**LoginAvosParameterized.py** is a Python script that utilizes the `selenium` library to navigate to an AVOS Console, login, and setup a search query. It takes the AVOS URL, username, and password as parameters. 

### How to Use

1. Ensure you have Python and the `selenium` library installed. Install selenium using pip:

    ```bash
    pip install selenium
    ```

2. Run the script in your terminal, specifying the AVOS URL, username, and password as arguments:

    ```bash
    python LoginAvosParameterized.py http://avos-url.com username password
    ```

## AVOSQuery.ahk

**AVOSQuery.ahk** is an AutoHotkey script that wraps the **LoginAvosParameterized.py** script for easy running. To use this script, simply press `ctrl+6`.

## Paint.ahk

**Paint.ahk** is an AutoHotkey script that automatically saves the last image from the Windows clipboard, crops the image, and saves it. To use this script, simply press `ctrl+2`.

---

Feel free to explore these tools and adapt them to suit your needs. If you encounter any issues or have any suggestions for improvement, please open an issue or submit a pull request.
