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

## Tutorial 11 - 11 Automatic Slave Reconnection

This tutorial focuses on changing the slave so that it will automatically reconnect to the master if the connection is lost.

With this addition the slave will automatically reconnect to the master no matter how many times it has been restarted. This moves the cluster one step forward towards a system which will automatically repair if there is an issue.

The next tutorial will focus on looking at how we can make the cluster code run on boot using rc.local.

The full details for [Tutorial 11 - Automatic Slave Reconnection is available on my blog](

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

