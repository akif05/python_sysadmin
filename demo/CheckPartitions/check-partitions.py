from optparse import OptionParser
import time
from check_partition_func import *

parser = OptionParser()
parser .add_option("-t", "--threshold",
                   dest="threshold",
                   type="int",
                   default=90,
                   help="Set threshold in (%). Must be a number.")

parser .add_option("-s", "--single",
                   action="store_true",
                   dest="singleshot",
                   default=False,
                   help="Just check once, don't loop")

parser.add_option("-m", "--maillbox",
                  dest="maillbox",
                  help="mail report to this mailbox")
# parser return tuple of two value 'options and args'

(options, partition_list) = parser.parse_args()
print ("singleshot is %r" % options.singleshot)
print ("mailbox is %s" % options.maillbox)
print ("threshold is %d" % options.threshold)
print ("partition list is %s" % str(partition_list))

# if -s option is given execute only once and exit else repeate every 10 seconds
while True:
    check_once(options, partition_list)
    if options.singleshot:
        sys.exit(0)
    time.sleep(10)
