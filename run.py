#!/usr/bin/env python

import argparse
import sys


class ExtractPDFData:
  
  def __init__(self):
    pass


  def use_pdfplumber(self, pdf_file):
    import pdfplumber
    with pdfplumber.open(pdf_file) as pdf:
      page = pdf.pages[0]
      print(page.extract_text())
  

  def use_PyMuPDF(self, pdf_file):
    import fitz
    doc = fitz.open(pdf_file)
    for page in doc:
      text = page.get_text()
      print(text)


  def use_PyPDF2(self, pdf_file):
    from PyPDF2 import PdfReader 
    reader = PdfReader(pdf_file) 
    page = reader.pages[0] 
    text = page.extract_text() 
    print(text) 


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '-l',
    '--list-libraries', 
    help='List PDF libraries available to use.',
    action='store_true')
  parser.add_argument(
    '-L',
    '--library',
    help='Which library to use. (needs [-p,--pdf-file] parameter)'
  )
  parser.add_argument(
    '-p',
    '--pdf-file',
    help='Path to the PDF file. (needs [-L,--library] parameter)')

  args = vars(parser.parse_args())
  
  list_libraries = (args['list_libraries'] is True and (args['library'] is None and args['pdf_file'] is None))
  read_pdf_file = (args['list_libraries'] is False and (args['library'] is not None and args['pdf_file'] is not None))

  if list_libraries:
    x = ExtractPDFData()
    for method in dir(x):
      if method.startswith('use_'):
        print(f' - {method.replace('use_','')}')
  elif read_pdf_file:
    x = ExtractPDFData()
    x.use_pdfplumber(pdf_file=args['pdf_file'])
  else:
    parser.print_help()

  