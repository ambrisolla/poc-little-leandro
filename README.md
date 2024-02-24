## Create Virtual Environment
```bash
$ pip -m venv venv
$ source venv/bin/activate
```

## Install libraries

```bash
$ pip install -r requirements.txt
```

## Usage

List available libraries to convert PDF's:
```bash
[brisa@brisa-machine] $ ./run.py -l
 - PyMuPDF
 - PyPDF2
 - pdfplumber
```

To extract data we need to pass the following parameters:  
  - ```-p [pdf_file_path]```: Specify the path to the PDF file;
  - ```-L [python_library]```: The library to use for the data conversion;