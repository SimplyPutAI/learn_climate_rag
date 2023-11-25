# Version 3.10 is due to the error
# "cannot import name 'open_filename' from 'pdfminer.utils" for Python 3.11
FROM jupyter/minimal-notebook:python-3.10

# Install OS dependencies for supporting the PDF content extraction
USER root
RUN apt-get update && apt-get install -y libmagic-dev poppler-utils tesseract-ocr libgl1
