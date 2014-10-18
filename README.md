Polygon file made with [this polygon tool](http://www.keene.edu/campus/maps/tool/).

The NJ feeds are clickwrapped. Create an account and get them [here](http://www.njtransit.com/developer).

The SEPTA feeds are also semi-clickwrapped. Get them [here](http://www2.septa.org/developer/).
The zip from SEPTA contains two other zipped feeds. You must unzip it or the feed will be unusable.

To extract only the area needed from the Geofabrik US Northeast extract:
`osmconvert us-northeast-latest.osm.pbf -B=NY_MA_CT_RI_NJ_Phila.polygon -o=extract.osm.pbf`

Or to convert on the fly while downloading:
`wget -q -O - http://download.geofabrik.de/north-america/us-northeast-latest.osm.pbf | osmconvert - -B=NY_MA_CT_RI_NJ_Phila.polygon -o=extract.osm.pbf`


