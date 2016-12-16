# -*- coding: utf-8 -*-
import requests
import urllib
from bs4 import BeautifulSoup
import optparse
import sys


def scrapedorks(page,filename):

    print "[+]Scraping results from page: " +str(page)
    print "[+]Saving to file: " +filename

    url = 'https://cxsecurity.com/dorks/' + str(page)
        
    r = urllib.urlopen(url).read()
    
    soup = BeautifulSoup(r,'lxml')
    
    dorksraw = soup.find_all("font",{'color':'#FCFCFC'})    
                
    clean = bleach.clean(dorksraw, tags=[], strip=True)
    
    dorksclean = clean
    
    print dorksclean

    writefile = open(filename,'w')

    writefile.write(str(dorksclean))

def main():
   
    print ' by threebones \n https://github.com/threebarber\n'

    parser = optparse.OptionParser() #create parser object called "parser"

    parser.usage = "[+] Usage:   dorkdumper.py -p <page#> -f <filename.txt>" \
                   "\n[+] Example: dorkdumper.py -p 4 -f dorklist.txt      " #add usage for "parser" object as well as example

    parser.add_option(
            '-p','--page',dest='page',type='int',help='specify page number IE 5) #add page number option as -p' )

    parser.add_option(
            '-f','--file',dest='filename',default='list.txt',type='string',help='specify filename (add .txt to end)') #add filename option as -f

    (options, args) = parser.parse_args(sys.argv) #finalize parsing portion

    page = options.page
    filename = options.filename

    if (str(page)) == None != (filename == None):
        print parser.usage
        exit(0) #check to make sure required params were assigned a value - if not, exit
    scrapedorks(page,filename)

if __name__ == '__main__':
    main()


 
