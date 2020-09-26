Raspberry Pi Cluster project
============================

This repository holds the code for [the tutorials](https://chewett.co.uk/blog/category/raspberry-pi-cluster/) for creating a Raspberry Pi Cluster in Python.

Here I go through the basics of creating a simple logger to a distributed task assigned system.

Each tutorial will have a github release and tagged version. These can be found
[on github](https://github.com/chewett/RaspberryPiCluster/releases).
This will make it easy to download the code for each tutorial.

The first few topics will start simple and continue to improve.
Later we will get onto more complicated topics such as reaching a consensus of who must "lead" the cluster.

Questions comments and suggestions can be raised the specific blog post or by using issues here.

## Tutorial 6 - Sending Slave Details to the Master

This tutorial focuses on modifying the original data sending functions
to use a more generic format.

This will allow the master to read what messages are being received and
determine what action it needs to take for each message type.

Once this is done there will be a versatile system for receiving messages
from a node and processing them.

In the future tutorials I will look into creating a two-way dialogue between
the master and slave.

The full details for
[Tutorial 06 - Sending Slave Details to the Master is available on my blog](
https://chewett.co.uk/blog/1098/raspberry-pi-cluster-node-06-sending-slave-details-to-the-master/
)

## Requirements

This code should run on anything with Python 2 installed but is developed
to run on as Raspberry Pi.

Python modules required:
* All Base modules
* psutil

## Licence

All code in this repository is licenced under a MIT licence.

The tutorials are copyright Christopher Hewett and should only be 
published on [http://chewett.co.uk/](http://chewett.co.uk/).
If you wish to use or republish these tutorials please contact me.

