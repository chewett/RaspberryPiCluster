Raspberry Pi Cluster project
============================

This repository holds the code for [the tutorials](https://chewett.co.uk/blog/category/raspberry-pi-cluster/) for creating a Raspberry Pi Cluster in Python.

Here I go through the basics of creating a simple logger to a distributed task assigment system.

Each tutorial will have a github release and tagged version. These can be found
[on github](https://github.com/chewett/RaspberryPiCluster/releases).
This will make it easy to download the code for each tutorial.

The first few topics will start simple and continue to improve.
Later we will get onto more complicated topics such as reaching a consensus of who must "lead" the cluster.

Questions comments and suggestions can be raised the specific blog post or by using issues here.

## Tutorial 18 - Raspberry Pi Temp Monitoring

In this tutorial I collect the CPU temperature of the Raspberry Pi and report it
as part of the node vitals.

This again is logged in the InfluxDB data store for review.

The full details for
[Tutorial 18 - Raspberry Pi Temp Monitoring](
https://chewett.co.uk/blog/
)

## Requirements

This code should run on anything with Python 3 installed but is developed
to run on as Raspberry Pi.

Python modules required:
* All Base modules
* psutil
* bottle
* configparser
* influxdb
* RaspberryPiVcgencmd (installable via pip)

Additional services required:
* An InfluxDb database

## Licence

All code in this repository is licenced under a MIT licence.

The tutorials are copyright Christopher Hewett and should only be 
published on [http://chewett.co.uk/](http://chewett.co.uk/).
If you wish to use or republish these tutorials please contact me.

