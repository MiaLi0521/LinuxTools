#!/usr/bin/python
"""
1. Specify one or more files, support Linux wildcards, and replace the line breaks under win with Linux line breaks;
2. Replace the win line breaks of all files in the specified directory with Linux line breaks;

eg:
   ./wl_tool.py raid.py ui-zh-cn.json CPU/
   ./wl_tool.py raid.py ui-*.json CPU/ 
"""
import os
import sys


def main(argv=None):
    for f in argv:
        if f.endswith(os.sep):
            if os.system("sed -i 's/\r//g' {}*".format(f)) == 0:
                print "files in {} dir, change linux line break ok!".format(f)
            else:
                print "files in {} dir, change linux line break failed!".format(f)
        else:
            if os.system("sed -i 's/\r//g' {}".format(f)) == 0:
                print "file {} change linux line break ok!".format(f)
            else:
                print "file {} change linux line break failed!".format(f)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt as e:
        sys.exit(0)
    except Exception as e:
        print e
        sys.exit(1)
