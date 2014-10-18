polygon file made with [http://www.keene.edu/campus/maps/tool/]

The NJ feeds are clickwrapped. Get them manually at [http://www.njtransit.com/developer]

The zip fie downloaded for SEPTA contains two other zipped feeds. You must unzip it or the feeds will be unusable.

to extract only the area of interest:
`osmconvert us-northeast-latest.osm.pbf -B=NY_MA_CT_RI_NJ_Phila.polygon -o=extract.osm.pbf`

or to convert on the fly while downloading:
`wget -q -O - http://download.geofabrik.de/north-america/us-northeast-latest.osm.pbf | osmconvert - -B=NY_MA_CT_RI_NJ_Phila.polygon -o=extract.osm.pbf`


