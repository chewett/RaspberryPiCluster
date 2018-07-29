Raspberry Pi Cluster project
============================

This repository holds the code for [the tutorials](https://chewett.co.uk/blog/category/raspberry-pi-cluster/) for creating a Raspberry Pi Cluster in Python.

Here I go through the basics of creating a simple logger to a distributed task assigned system.

Each folder relates to a new topic of creating a Raspberry Pi Cluster.
If you are familiar with python the first few topics should be short topics to revise.
Later we will get onto more complicated topics such as reaching a consensus of who must "lead" the cluster.

Questions comments and suggestions can be raised the specific blog post or by using issues here.

## Current Examples

1. **Logging Liveness [Full tutorial](https://chewett.co.uk/blog/741/raspberry-pi-cluster-node-01-logging-liveness/)** - 
 To start with we are going to make a really simple file to start logging data.
 This will set up a python logger and log data to it every minute.

2. **Packaging common functionality [Full tutorial](https://chewett.co.uk/blog/881/raspberry-pi-cluster-node-02-packaging-common-functionality/)** -
 Here I introduce python packages and the reason why we use them.
I move some of the common functionality into a package so more easily use across scripts.

3. **Basic node communication between two nodes [Full tutorial](https://chewett.co.uk/blog/901/raspberry-pi-cluster-node-03-basic-node-communication-two-nodes/)** -
 Here I introduce sockets as a simple way of sending data between two concurrently running scripts.

4. **Configuration files [Full tutorial](https://chewett.co.uk/blog/1001/raspberry-pi-cluster-node-04-configuration-files-configparser/)** - 
 Here I introduce configuration files and why we use them.
 I change the previous script to use configuration files.
 
5. **Sending data with JSON [Full tutorial](https://chewett.co.uk/blog/1072/raspberry-pi-cluster-node-05-talking-to-nodes-with-json/)** -
 Here I improve I the cluster sends data around by creating a JSON
 based message format. The implementation is abstracted into a module
 to allow easy modification without changing scripts that use it.

6. **Sending Slave Details to the Master [Full tutorial](https://chewett.co.uk/blog/)** -
 This tutorial focuses on modifying the original data sending functions
to use a more generic format. This will allow the master to read what messages are being received and
determine what action it needs to take for each message type.

 
 
## ToDo - List of things that will come in the future

* Socket talking - Slave to master
* Socket talking - Master Broadcast
* Socket talking - Master informs slaves of data
* Socket talking - Replay attacks
* Socket talking - Encryption
* Config loading - JSON
* Daemon Process -