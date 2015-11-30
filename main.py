#!/usr/bin/env python


import sys, getopt

debug = 0
verbose = 0
norun = 0


########################################




########################################
#
# Display help

def help():
  print "%s : -dh" % sys.argv[0]
  print "     -d, --debug : Print debug messages."
  print "     -h, --help  : Print this help message."
  print "     -n, --norun : Run script but do not actually modify anything."
  print "     -h, --verbose : Print verbose messages."


########################################
#
# Main function. Parse argument, get needed information, then do the work.

def main(argv):


  # Get and parse run-time arguments

  try:
    opts, args = getopt.getopt(sys.argv[1:], "dhnv", ["debug","help","norun","verbose"])
  except getopt.GetoptError:
    help()
    sys.exit(2)

  for opt,arg in opts:
    if opt in ( '-h','--help'):
      help()
    elif opt in ( '-d', '--debug'):
      global debug
      debug = 1
    elif opt in ( '-n', '--norun'):
      global norun
      norun = 1
    elif opt in ( '-v', '--verbose'):
      global verbose
      verbose = 1
    else:
      help()
      sys.exit(2)


  # Now do work




########################################
#
# If called as a script then do work. Else allow script to be imported so functions and classes can be used in other scripts.

if __name__ == "__main__":

  main(sys.argv[1:])


