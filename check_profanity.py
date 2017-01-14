#!/usr/bin/python
import urllib

def check_text(contents) :
        result = urllib.urlopen(r"http://www.wdyl.com/profanity?q="+contents)
        output = result.read()
        print(output)
        result.close()

def red_file() :
	s1 = open("/home/lakshita/Desktop/file1.txt","r")
	contents = s1.read()
	check_text(contents)
	s1.close()

red_file()
