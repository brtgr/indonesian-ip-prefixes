#!/usr/bin/python
# License: WTFPL - 2017
# Author: Dewangga Alam <dewanggaba@xtremenitro.org>
# Description:
# All prefixes came from our router direct peer with IIX
# and OpenIXP. For more information, please visit 
# http://sumberterbuka.beritagar.id

import fileinput
import time

now = time.strftime("%c")
start_time = time.clock()

lines = open('indonesia.txt', 'r').readlines()
lines_set = set(lines)
out  = open('id.rsc', 'w')

for line in lines_set:
    out.write(line)

for line in fileinput.input('id.rsc', inplace=1):
    print '{0}{1}{2}'.format('add list=prefixid address="', line.rstrip(), '"')

num_lines = sum(1 for line in open('id.rsc'))

with open('id.rsc', "r+") as f:
    first_line = f.readline()
    if first_line != "# Indonesian IP Address List\n":
        lines = f.readlines()
        f.seek(0)
        f.write("# Indonesian IP Address List\n")
        f.write("# Supported and tested on MikroTik RoS 6.x or latest\n")
        f.write("# Script created by Dewangga Alam <dewangga@beritagar.id>\n")
        f.write("# Last update: %s \n" % now)
        f.write("# Processed %d prefix(es) in %s seconds\n" % (num_lines, (time.clock() - start_time)))
        f.write("\n")
        f.write("/ip firewall address-list\n")
	f.write("add list=prefixid address=\"1.2.3.4\"\n")
	f.write("rem [find list=\"prefixid\"]\n")
	f.write("add list=prefixid address=\"103.52.2.0/23\"\n")
	f.write("add list=prefixid address=\"103.87.70.0/23\"\n")
        f.write(first_line)
        f.writelines(lines)    

