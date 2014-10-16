# Get NJ Transit Bus and Rail the hard way, from www.njtransit.com/developer

from urllib2 import urlopen
import datetime
import csv

def CommentStripper (iterator):
    for line in iterator:
        if line.startswith('#'):
            continue
        if not line.strip ():
            continue
        yield line

def slugify(name):
	return "-".join( [x.lower() for x in name.split()] )

def main():
	fp = CommentStripper(open("feeds.csv"))
	rd = csv.reader(fp)
	for name,url in rd:
		print name

		datestr = datetime.datetime.now().strftime("%Y%m%d")
		filename = "%s-%s.zip"%(slugify(name), datestr)
		fpout = open( filename, "w" )
		urlfp = urlopen( url )
		fpout.write( urlfp.read() )
		fpout.close()

if __name__=="__main__":
	main()
