Raspberry Pi Cluster project
============================

This repository holds the code for [the tutorials](https://chewett.co.uk/blog/category/raspberry-pi-cluster/) for creating a Raspberry Pi Cluster in Python.

Here I go through the basics of creating a simple logger to a distributed task assigned system.

Each folder relates to a new topic of creating a Raspberry Pi Cluster.
If you are familiar with python the first few topics should be short topics to revise.
Later we will get onto more complicated topics such as reaching a consensus of who must "lead" the cluster.

Questions comments and suggestions can be raised the specific blog post or by using issues here.

## Current Examples

1. Logging Liveness [Full tutorial](https://chewett.co.uk/blog/741/raspberry-pi-cluster-node-01-logging-liveness/) - 
 To start with we are going to make a really simple file to start logging data.
 This will set up a python logger and log data to it every minute.

2. Packaging common functionality [Full tutorial](https://chewett.co.uk/blog/881/raspberry-pi-cluster-node-02-packaging-common-functionality/) -
 Here I introduce python packages and the reason why we use them.
I move some of the common functionality into a package so more easily use across scripts.

3. Basic node communication between two nodes [Full tutorial](https://chewett.co.uk/blog/901/raspberry-pi-cluster-node-03-basic-node-communication-two-nodes/) -
 Here I introduce sockets as a simple way of sending data between two concurrently running scripts.
 
 
## ToDo - List of things that will come in the future

* Config loading - Config parser
* Socket talking - Slave to master
* Socket talking - Master Broadcast
* Socket talking - Master informs slaves of data
* Config loading - JSON
* Daemon Process -