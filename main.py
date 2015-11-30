#!/usr/bin/env python


import sys, getopt

debug = 0




def help():
  print "%s : -dh" % sys.argv[0]
  print "     -d : Print debug messages"
  print "     -h : Print this help message"

def main(argv):

  try:
    opts, args = getopt.getopt(argv,"dh",[])
  except getopt.GetoptError:
    help()
    sys.exit(2)

  for opt,arg in opts:
    if opt in ( '-h'):
      help()
    elif opt in ( '-d'):
      global debug
      debug = 1
    else:
      help()
      sys.exit(2)


########################################
#

if __name__ == "__main__":

  main(sys.argv[1:])
