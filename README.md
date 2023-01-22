# getLINKS
A Python3 tool to search links for different articles by providing a file with queries. The tool returns a list of links based on the number of links specified by the user.

## How To Install the Rquired libraries 

```
pip install -r /path/to/requirements.txt
```

## USAGE:
```
usage: getLINKS.py [-h] -f  -n  [-o] [-p] [-b]

Get all The Ans of Your Questions

options:
  -h, --help      show this help message and exit
  -f , --file     Path to the file containing Questions
  -n , --number   Number of Articles per Question
  -o , --output   outputname of the file
  -p, --pdf       Saved in Pdf format
  -b , --book     Generates a book by downloading the pages
```
Examples
To search for 5 links per query from a file called "questions.txt" and save the output to a file called "output.txt":

Copy code
```
getLINKS.py -f questions.txt -n 5 -o output.txt
```
To search for 5 links per query from a file called "questions.txt" and save the output in pdf format:

```
getLINKS.py -f questions.txt -n 5 -p
```

To search for 5 links per query from a file called "questions.txt" and download the pages to generate a book:
**Note**: To generater A book it would Require time and also Depends on the websites to scarp data so limit your no to just 2 or 3 

Copy code
```
getLINKS.py -f questions.txt -n 5 -p -b sample_book
```

### Requirements
Python3

```
beautifulsoup4==4.11.1
google==3.0.0
Markdown==3.4.1
pdfkit==1.0.0
PyPDF2==3.0.1
python-nmap==0.7.1
soupsieve==2.3.2.post1
```



```
Note
Always ensure to check the scope
```

## EXAMPLE FILE


```
Create a example.txt and add these lines to test 

top 10 books to learn java
top 2 books for learning python
road map for Front-end Web development
```


