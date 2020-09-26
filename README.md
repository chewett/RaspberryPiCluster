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

## Tutorial 2 -  Packaging common functionality - [Full tutorial](https://chewett.co.uk/blog/881/raspberry-pi-cluster-node-02-packaging-common-functionality/) 

This second post builds on the first by packaging up the logging code we created last time.

As I am planning on running the cluster with a number of scripts for the server and client I need
to be able to share the code. This will remove duplication and means we have standard ways of
doing common operations. We will start by creating the common package structure to hold our code.

The full details for
[Tutorial 02 - Packaging common functionality is available on my blog](https://chewett.co.uk/blog/881/raspberry-pi-cluster-node-02-packaging-common-functionality/)


## Licence

All code in this repository is licenced under a MIT licence.

The tutorials are copyright Christopher Hewett and should only be 
published on [http://chewett.co.uk/](http://chewett.co.uk/).
If you wish to use or republish these tutorials please contact me.

