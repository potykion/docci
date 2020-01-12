.. docci documentation master file, created by
   sphinx-quickstart on Sun Jan 12 01:19:54 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

docci
==========================================

**docci** is a package which provides various document management utils to simplify work with files in python-applications (mostly web-applications)

.. contents:: :local:


Features
*********

- **File abstraction via FileAttachment class** which consists of file name and bytes-content and provides following features:

  - **base64-string creation** for file transference in json-apis
  - **Content-Disposition header generation** for file name identity in web apps
  - **file name manipulation** like extension extraction, mime-type detection
  - **file save on disk** - useful when have binary from web and you need to explore it as file on disk

- **Specific file utilities** based on FileAttachment manipulation:

  - **directories exploring** - list directory files as list of FileAttachment's
  - **zip-file exploring** - list zip file contents as list of FileAttachment's
  - **zip-file creation** - create zip-archive from list of FileAttachment's
  - **openpyxl-based xlsx utils** like converting xlsx to FileAttachment, xlsx creation from dicts

Usage
*******

Firstly, you need to create FileAttachment:

.. code-block:: python

 # Creation from pdf
 import pdfkit
 from docci.file import FileAttachment

 pdf_data: bytes = pdfkit.from_file("sample.pdf", output_path=False)
 file = FileAttachment("sample.pdf", pdf_data)

 # Creation from xlsx
 from openpyxl import load_workbook
 from docci.file import FileAttachment
 from docci.xlsx import xlsx_to_bytes

 xlsx = load_workbook("sample.xlsx")
 xlsx_data = xlsx_to_bytes(xlsx)
 file = FileAttachment("sample.xlsx", xlsx_data)

 # Creation from file on disk
 from docci.file import FileAttachment

 file = FileAttachment.load("path/to/file")

 # Creation from base64 str
 from docci.file import FileAttachment

 file = FileAttachment.load_from_base64("base64-string")

Now you can use the FileAttachment features:

.. code-block:: python

 # To get base64 file representation
 file.content_base64

 # To generate Content-Disposition header with file name
 file.content_disposition

 # To get file extension
 file.extension

 # To get file mimetype
 file.mimetype

 # To save file to disk
 file.save("path/to/file")

Specific file utilities are just functions:

.. code-block:: python

 # To get directory files
 from docci.file import list_dir_files

 files = list_dir_files("path/to/dir")

 # To list zip files
 from docci.zip import list_zip_files

 files = list_zip_files("path/to/zip")

 # To create zip-archive
 from docci.zip import zip_files

 zip_file = zip_files("sample.zip", [file])

 # To convert xlsx to FileAttachment
 from openpyxl import load_workbook
 from docci.xlsx import xlsx_to_file

 xlsx_file = xlsx_to_file(load_workbook("path/to/xlsx"))

 # To create xlsx from dicts
 from docci.xlsx import dicts_to_xlsx

 xlsx = dicts_to_xlsx([
   {"col1": 1, "col2": 2},
   {"col1": 3, "col2": 4}
 ])

More features can be found in api reference below

API reference
*************

docci.file
----------

.. automodule:: docci.file
   :members:

docci.xlsx
----------

.. automodule:: docci.xlsx
   :members:

docci.zip
----------

.. automodule:: docci.zip
   :members:


