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

## Tutorial 13 - Abstracting Slave Code

This tutorial focuses on abstracting the slave code to be more extensible.
I create a general purpose class which is used by each Slave Thread.
This will include the ability to customise the slave more generally
while maintaining a common core.

The next tutorial will focus on adding a simple webserver to the core of the code.

The full details for
[Tutorial 13 - Abstracting Slave Code](
https://chewett.co.uk/blog/2090/raspberry-pi-cluster-node-13-abstracting-slave-code/
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

