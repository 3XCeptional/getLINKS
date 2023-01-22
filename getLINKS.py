#!/usr/bin/env python
import os
import sys
import argparse
from googlesearch import search
import markdown
import pdfkit
from PyPDF2 import PdfMerger, PdfFileReader, PdfFileWriter
import random

parser = argparse.ArgumentParser(
    description="Get all The Ans of Your Questions")
parser.add_argument("-f", "--file", type=str, metavar="",
                    required=True, help="Path to the file containing Questions")
parser.add_argument("-n", "--number", type=int, metavar="",
                    required=True, help='Number of Articles per Question')
parser.add_argument("-o", "--output", required=False, type=str,
                    metavar="", help="outputname of the file ")

parser.add_argument("-p", "--pdf", required=False,
                    action="store_true", help='Saved in Pdf format')

parser.add_argument("-b", "--book", type=str, metavar="",
                    required=False, help="Generates a book by downloading the pages")


args = parser.parse_args()




def getQuery(file):
    """Returns Formated Queries"""
    with open(file, 'r') as f:
        data = f.readlines()
        queries = [x.removesuffix('\n') for x in data if x != '\n']
        queries.sort()
    return queries


def writeQuery(queries, outputfile):
    with open(outputfile, 'w') as f:
        f.write(f"# {args.file}\n")
        for count, query in enumerate(queries):
            ## Random Pause 
            randPause = random.randint(0, 3)
            title = f"\n## {count + 1}) {query}\n"
            print("Getting Links for :", title ,"\nPaused For",str(randPause)," seconds")
            f.write(title)
            urls = search(query, tld="co.in", num=10,
                          stop=args.number, pause=randPause) # You Can Change pause 
            res = []
            [res.append(x) for x in urls if x not in res]  
            for url in res:
                links = f" - {url}\n"
                f.write(links)


def convertToPDF(filename):
    if args.pdf:
        with open(filename, 'r') as f:
            text = f.read()
            html = markdown.markdown(text)

        with open(f"{filename}.html", 'w') as f:
            f.write(html)

        pdfkit.from_file(f"{filename}.html", f"{filename}.pdf")
        print("PDF With Links Generated, Done!")


def mergePDF(list_ofpdfs):
    bookname = f"{args.book}.pdf"
    merger = PdfMerger()
    for pdf in list_ofpdfs:
        merger.append(pdf)
    merger.write(bookname)
    merger.close()
    for i in list_ofpdfs:
        os.remove(i)


def deleteBlankPages(listofbooks):
    changed_books = []
    for i in listofbooks:
        with open(i, 'rb') as f1:
            ReadPDF = PdfFileReader(f1)
            pages = ReadPDF.numPages
            output = PdfFileWriter()
            f2 = open(f"new_{i}", "wb")
            new_book = f"new_{i}"
            changed_books.append(new_book)
            for j in range(pages):
                pageObj = ReadPDF.getPage(j)
                text = pageObj.extractText()
                if (len(text) > 0):
                    output.addPage(pageObj)
            output.write(f2)
            f2.close()
    print(changed_books)
    return changed_books


def generateBook(filename):
    if args.book:
        index_page = f"{filename}.pdf"
        downloaded_books = [index_page,]
        with open(filename, 'r') as f:
            data = f.readlines()
            urls = [x.removesuffix('\n').removeprefix(' - ')
                    for x in data if 'https' in x]
        for count, url in enumerate(urls):
            current_book = f"Book{count}.pdf"
            pdfkit.from_url(url, current_book, verbose=True)

            downloaded_books.append(current_book)

        new_books = deleteBlankPages(downloaded_books)
        mergePDF(new_books)
        for i in downloaded_books:
            os.remove(i)


def main():
    # q = getQuery('test.txt')
    # o = "op.md"
    # writeQuery(q, o)
    FILENAME = args.file

    if args.output:
        OUTPUTFILE = args.output
    else:
        OUTPUTFILE = f"Output_{FILENAME}.md"


    queries = getQuery(FILENAME)
    writeQuery(queries, OUTPUTFILE)
    convertToPDF(OUTPUTFILE)
    generateBook(OUTPUTFILE)

if __name__ == "__main__":
    main()