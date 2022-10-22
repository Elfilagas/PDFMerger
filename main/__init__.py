import PyPDF2
import os


def merge():
    merger = PyPDF2.PdfFileMerger()
    for file in os.listdir(os.curdir):
        if file.endswith(".pdf"):
            merger.append(file)
        merger.write("combined.pdf")


def main():
    merge()


if __name__ == '__main__':
    main()