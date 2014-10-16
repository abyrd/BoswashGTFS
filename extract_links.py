#!/usr/bin/env python

# First, do: export PYTHONIOENCODING=utf-8

# extract the link text and URLs from an HTML page

from lxml.html import parse, tostring
#doc = parse('http://www.massdot.state.ma.us/developersdata.aspx')
doc = parse('http://www.cttransit.com/about/developers/gtfsdata/Main.asp')
# select the url in href for all a tags(links)
for anchor in doc.xpath('//a'):
    print "%s,%s" % (anchor.text, anchor.get('href'))


