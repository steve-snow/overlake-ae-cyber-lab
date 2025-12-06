import sys

def readCmdLine():

  cmd_line = sys.argv

  if (len(cmd_line) > 1):
    print(f"Command line args: {cmd_line[1]}")
    try:
      return int(cmd_line[1])
    except ValueError:
      return 1

  return 1
