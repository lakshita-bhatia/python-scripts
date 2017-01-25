#!/usr/bin/python

import os,sys
import string

# get filenname
ifpdf=1
filename_inp = sys.argv[1]

if filename_inp[-4:]=='.dat' or filename_inp[-4:]=='.txt':
    ifpdf=0

if filename_inp[-4:]=='.pdf' or filename_inp[-4:]=='.dat' or filename_inp[-4:]=='.txt':
    filename = filename_inp[:-4]
    if os.path.isfile(str(filename_inp)):
        if ifpdf:
            print 'converting pdf to ascii...'
            os.popen('pdftotext ' + str(filename) + '.pdf ' + str(filename) + '.txt')
        print 'start converting ascii to wav...'
        os.popen('cat ' + str(filename) + '.txt\
               |sed \'s/[^a-zA-Z .,!?]//g\'|text2wave -o ' + str(filename) + '.wav')
        print 'converting to mp3...'
        os.popen('lame -f ' + str(filename) + '.wav ' + str(filename) + '.mp3')
        os.popen('rm -f ' + str(filename) + '.wav')
        print 'finished. don\'t forget to delete txt file if you don\'t need it'
    else:
        print '*** file does not exist ***'
else:
    print '*** please give extension of your file (.dat, .txt or .pdf)'
    print '*** or your file called: ' + str(filename_inp) + '\n*** does not exist'
   

# that's it. have fun!!! :)
