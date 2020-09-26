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

## Tutorial 8 - Slave Helper Functions

This tutorial focuses on creating a number of slave helper functions
 to begin the process of fully automating the slaves.
 
A few simple commands such as shutting down a node and rebooting
 it along with updating the operating system are added ready for
 implementation.

The next tutorial will focus on converting the master script
 to accept any number of slave nodes.

The full details for
[Tutorial 08 - Slave Helper Functions is available on my blog](
https://chewett.co.uk/blog/1839/raspberry-pi-cluster-node-08-slave-helper-functions/
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

