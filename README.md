# Web Scraper
# Description
In this project I made a web scraper using python. The tools I used were python pandas, beautifulSoup and requests, so basically what this web scrapers does it that it extracts data from quotestoscrape(any any link you might want) using request and beautifulSoup and organises the data and saves it in a CSV file using pandas
# Requirements
To run this code you will need to have python installed and all other requirements listed in requirements.txt
# Installation Guide
To install requests, run in your terminal: pip install requests 
TO install pandas run in your terminal: pip install pandas
To install BeautifulSoup run in your terminal: pip install beautifulSoup4
# Usage
To run this script, first make sure you installed all the dependencies then go to your terminal and run: python scraper.py
You will see in your terminal 10 sorted out quotes with text, author and tags 
And if you look in your project folder you will see a file has been created called quotes.csv thats where all the stored data is.
# Example 
                                                text             author                                            tags
0  “The world as we have created it is a process ...    Albert Einstein        [change, deep-thoughts, thinking, world]
1  “It is our choices, Harry, that show what we t...       J.K. Rowling                            [abilities, choices]
2  “There are only two ways to live your life. On...    Albert Einstein  [inspirational, life, live, miracle, miracles]
3  “The person, be it gentleman or lady, who has ...        Jane Austen              [aliteracy, books, classic, humor]
4  “Imperfection is beauty, madness is genius and...     Marilyn Monroe                    [be-yourself, inspirational]
5  “Try not to become a man of success. Rather be...    Albert Einstein                     [adulthood, success, value]