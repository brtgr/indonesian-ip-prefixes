# Indonesian IP Address List
# Supported and tested on MikroTik RoS 6.x or latest
# Script created by Dewangga Alam <dewangga@beritagar.id>
# Last update: Mon May 22 00:00:01 2017 
# Processed 0 prefix(es) in 0.0 seconds

/ip firewall address-list
add list=prefixid address="1.2.3.4"
rem [find list="prefixid"]
add list=prefixid address="103.52.2.0/23"
add list=prefixid address="103.87.70.0/23"
