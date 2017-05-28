#!/bin/bash

# Name of new file
fileName="$1_with_table_of_contents.md"

# Too much things going on here :)

# /^#/ -> Select each line that starts with # character.
# header=$0 -> Assign $0 to **header** variable. In this case $0 is one line which comes from regex.
# lowerHeader=tolower(header) -> Convert every character in **header** to lower case letters and assign it to **lowerHeader** variable.
# gsub(/ /,"-",lowerHeader) -> Find and replace every space with hyphen (‐) in **lowerHeader**.
# print "* ["header"](#"lowerHeader")" -> Print the result as list format for markdown. 
contents="$(cat $1 | awk '/^#/ { header=$0; sub(/^[ \t#]+/, "",header); lowerHeader=tolower(header); gsub(/ /,"-",lowerHeader);  print "* ["header"](#"lowerHeader")" }')"

# Create new file with only table of contents.
echo -e "## Table of Contents\n\n$contents" > $fileName

# Add rest of the file to end of newly created file.
cat $1 >> $fileName
