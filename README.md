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

## Tutorial 7 - Sending data to the Slave

This tutorial focuses on improving the slave by being able to request
data from the master.

This will be further worked on in future tutorials to keep a state of the
cluster in each slave node.

In the next post I will look at adding a few more payloads to let the master
control the slave further. These will form the basis of the master requesting
the slave to perform computation.

The full details for
[Tutorial 07 - Sending data to the Slave is available on my blog](
https://chewett.co.uk/blog/1781/raspberry-pi-cluster-node-07-sending-data-to-the-slave/
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

