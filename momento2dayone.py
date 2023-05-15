#!/usr/bin/env python
# coding: utf-8

# Momento to Day One Migration Script

# Copyright © 2023, Douglas Bergère

# add libraries
import sys # environment variables
import os # for file input/output
import linecache
#import html2image

#import lxml.html # for parsing HTML
from datetime import datetime # for converting timestamp to formatted data
from datetime import date # for converting timestamp to formatted data
#import geopy # for converting geolocation data to location name
#import pypandoc # for converting body to markdown (requires Pandoc installation)
import subprocess # for scripting through command line
#import time # enable pauses for uplods
#import urllib # for dealing with html encoded string
#from html2image import Html2Image

def getJournalLines(journal, startline, endline):
    for lineno in range(startline, endline):
        line = line + linecache.getline(journal, lineno)
        linecache.clearcache()
    return line

def isDate(inString):
    jdate = date.today()
    try:
        jdate = datetime.strptime(inString, '%d %B %Y')
           
    except ValueError:
        return False
        
    return inString == datetime.strftime(jdate, '%-d %B %Y')

def isTime(inString):
    jdate = datetime.now()
    
    try:
        jdate = datetime.strptime(inString, '%I:%M %p')
           
    except ValueError:
        return False
    
    return inString == datetime.strftime(jdate, '%-I:%M %p')

class JournalDay:
  def __init__(self, jdate):
    self.jdate = jdate

class JournalEntry:
  def __init__(self, jdate):
    self.jdate = jdate

  def writeJournalEntry():
    print(self.jdate)

if len(sys.argv) > 1:
    basepath = sys.argv[1]
    print(f"Input file is: {basepath}")
else:
    print("No command line parameter was provided.")
    quit()

# set options
path = dict()
path['in'] = basepath # input folder with HTML files
path['out'] = '/Users/me/Recipes_md' # output folder to save MD files
path['exe'] = '/usr/local/bin/dayone2' # path of sh file for the Day One Command Line Interface
form = dict()
form['in'] = 'html' # input format
form['out'] = 'txt' # output format
options = dict()
options['write'] = True # convert Evernote notes to Markdown files
options['command'] = True # write Markdown files to Day One using the Command Line Interfac
options['journal'] = 'My-Evernote-Journal' # destination Day One journal 
options['pause'] = 20 # seconds to pause between uploads
options['limit'] = 30 # maximum allowed number of photos

journal = f"{basepath}/Export.txt"

row = 0
currentdate = date.today()
currentday = ""
lookingfortimestamp = False
daybegins = 1
journalDay = ""
journalEntry = ""
jIndex = {"r0":""}
previousLine = ""
previousBlank = True
line = ""

while True:
    print("{} ({}): {}".format(row, jIndex["r" + str(row)], line.strip()))
    previousLine = line.strip()
    row += 1
#    line = getline(journal, row) 
    line = linecache.getline(journal, row)
    
#    print("{}: {}".format(row, line.strip()))
    

    if not line:
        break
    
    if line.strip() == "":
        jIndex["r" + str(row)] = "Blank"
        previousBlank = True
        continue
           
# A line with just a date after a Blank indicates the beginning of a new day    
    if previousBlank and isDate(line.strip()):
        jIndex["r" + str(row)] = "Date"
        previousBlank = False
        continue

    if previousBlank and isTime(line.strip()):
        jIndex["r" + str(row)] = "Time"
        previousBlank = False
        continue


    if line.strip() == "=" * len(previousLine.strip()):
        jIndex["r" + str(row)] = "Hash"    
        previousBlank = False
        continue
        
    if line.startswith('Feed: '):
        jIndex["r" + str(row)] = "Feed"    
        previousBlank = False
        continue

    if line.startswith('URL: '):
        jIndex["r" + str(row)] = "URL"    
        previousBlank = False
        continue

    if line.startswith('Mentioned: '):
        jIndex["r" + str(row)] = "Mentioned"    
        previousBlank = False
        continue
    
    if line.startswith('Tags: '):
        jIndex["r" + str(row)] = "Tags"    
        previousBlank = False
        continue
        
    if line.startswith('At: '):
        jIndex["r" + str(row)] = "At"    
        previousBlank = False
        continue
        
    if line.startswith('Events: '):
        jIndex["r" + str(row)] = "Events"    
        previousBlank = False
        continue

    if line.startswith('Media: '):
        jIndex["r" + str(row)] = "Media"    
        previousBlank = False
        continue

    jIndex["r" + str(row)] = "Data"
    previousBlank = False
    

 #       row += 1
 #       if daybegins > 1:
 #           jIndex["d"+currentday.strftime("%Y%m%d")]["endRow"]=row-2
 #           print("{}: {}-{}".format(jIndex["d"+currentday.strftime("%Y%m%d")]['jdate'].strftime("%Y%m%d"), jIndex["d"+currentday.strftime("%Y%m%d")]["startRow"], jIndex["d"+currentday.strftime("%Y%m%d")]["endRow"]) )              
 #       daybegins = row + 1
 #       jIndex["d"+jdate.strftime("%Y%m%d")]={}
 #       jIndex["d"+jdate.strftime("%Y%m%d")]["startRow"]=daybegins
 #       jIndex["d"+jdate.strftime("%Y%m%d")]["jdate"]=jdate
 #       currentday=jdate
        
 #       lookingfortimestamp = True
        
         
#        writeJournalEntry(journalEntry)
#        journalEntry = ""


    
#    print("Line{}: {}".format(row, line.strip()))

    linecache.clearcache()
