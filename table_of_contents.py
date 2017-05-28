#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, getopt

def create_content_from_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        # Filter lines by getting only starts with # character and remove # character with the space after it.
        contents = [line.replace("#", "")[1:-1] for line in lines if line[0]=='#']
    return contents

def get_text_from_file(filename):
    with open(filename) as f:
        text = f.read()
    return text

def create_new_file(newfilename, content):
    with open(newfilename, 'w+') as f:
        f.write(content)

def help():
    print 'table_of_contents.py -i <inputfile> -o <outputfile>'

def main(argv):
    inputfile = ''
    outputfile = ''
    
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            help()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    # If these variables are empty show help.
    if inputfile == '' or outputfile == '':
        help()
        sys.exit()
    
    # Get arrays of headers from file.
    headers = create_content_from_file(inputfile)
    # Title for Table of Contents which will come to first line.
    table_of_contents = "# Table of Contents\n\n"
    
    # Create table_of_contents the result as list format for markdown.
    for header in headers:
        table_of_contents += "* ["+header+"](#"+header.lower().replace(' ','-')+")\n"
    
    # Create a new file which has Table of Contents at the beginning and the same content with the input file.
    create_new_file(outputfile, table_of_contents+get_text_from_file(inputfile))

if __name__ == "__main__":
    main(sys.argv[1:])

