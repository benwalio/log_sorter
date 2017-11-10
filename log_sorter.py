#!/usr/bin/env python
from datetime import datetime
import re
import getopt, sys

# CONSTANTS
verboseMode = False
versionNumber = "1.2a"
updatedOn = "11/11/2017"

inFileName = "file.txt"
outFileName = "outfile.txt"
additional_search = ""
additional_search_flag = False
read_file = []
sorted_outlog = []

def set_outfile(file_name):
   global outFileName
   outFileName = file_name
   print (("output file is - %s") % (outFileName))

def set_infile(file_name):
   global inFileName
   inFileName = file_name
   print (("input file is - %s") % (inFileName))

def set_additional_search_flag_true():
   global additional_search_flag
   additional_search_flag = True

def set_verbose_mode(toggle):
   global verboseMode
   if toggle:
      verboseMode = True
      print "Verbose mode - engaged"
   elif not toggle:
      print "Verbose mode - disengaged"
      verboseMode = False
   else:
      print "unable to set verbose mode to " + str(toggle) + "\nExiting..."
      quit_program()

def quit_program():
   sys.exit()

def print_help():
   print "  log_sorter.py  -  Version " + str(versionNumber)
   print "params"
   print "    -a       version number\n    -o var   output to var\n    -i var   input var\n    -v       toggle verbose mode number\n    -g       only process GETs\n    -p       only process PUSHs\n    -q       only process POSTs"
   print "slack @ben.wallace if you have a question on this"
   sys.exit()

def get_args():
   fullCmdArgs = sys.argv
   argList = fullCmdArgs[1:]
   global additional_search
   global additional_search_flag

   # define arguments
   #   a- version number
   #   o- ouput file, requires variable
   #   i- input file, requires variable
   #   v- version number
   #   g- GETs only
   #   p- PUSHs only
   #   q- POSTs only
   macArgs = "aho:i:vgpq"

   try:
       arguments, values = getopt.getopt(argList, macArgs)
   except getopt.error as err:
       # output error, and return with an error code
       print (str(err))
       quit_program()

# loads arguments
   for currentArgument, currentValue in arguments:
       if currentArgument in ("-h"):
           print_help()
       elif currentArgument in ("-v"):
           set_verbose_mode(True)
       elif currentArgument in ("-o"):
           set_outfile(currentValue)
       elif currentArgument in ("-a"):
           print (("version number is - %s") % (versionNumber))
       elif currentArgument in ("-g"):
           additional_search = "Started GET "
           set_additional_search_flag_true()
           print ("only processing for GETs")
       elif currentArgument in ("-p"):
          additional_search = "Started PUSH "
          set_additional_search_flag_true()
          print ("only processing for PUSHs")
       elif currentArgument in ("-q"):
          additional_search = "Started POST "
          set_additional_search_flag_true()
          print ("only processing for POSTs")
       elif currentArgument in ("-i"):
           set_infile(currentValue)

   if verboseMode:
     print "Finished processing command line args..."

def read_and_split_inFile(in_file):

   if verboseMode:
      print "Reading and splitting the infile..."

   test_file = open(in_file,"r")
   read_file = test_file.read()
   in_log = read_file.split("\n\n")
   return in_log

def parse_for_additional_search(in_file, search_string):

   if verboseMode:
      print "Begin searching and splitting for " + str(search_string) + "..."

   out_file = []
   search_format = re.compile(search_string)

   for i in range(len(in_file)):
      current_line = in_file[i]
      match = re.search(search_format, current_line)
      if match:
         out_file.append(in_file[i])



   return out_file


def sort_log_by_time(in_log, arg='desc'):

   if verboseMode:
       print "Begin sorting by time..."

   list_of_tuples = []

   datetime_format = re.compile("\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")

   for i in range(len(in_log)):
       current_line = in_log[i]
       match = re.search(datetime_format, current_line)
       if match:
           hold_tups = (match.group(),in_log[i])
           list_of_tuples.append(hold_tups)

   list_of_tuples.sort()
   return list_of_tuples

def write_file(out_log, out_file, args='append'):

   if verboseMode:
      print "Begin writing to the file output..."

   wf = open(out_file,"a")

   for i in out_log:
       wf.write(i[1] + "\n\n")


get_args()

read_file = read_and_split_inFile(inFileName)

if additional_search_flag:
   read_file = parse_for_additional_search(read_file, additional_search)

sorted_outlog = sort_log_by_time(read_file)

write_file(sorted_outlog, outFileName)
