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

6. **Sending Slave Details to the Master [Full tutorial](https://chewett.co.uk/blog/1098/raspberry-pi-cluster-node-06-sending-slave-details-to-the-master/)** -
 This tutorial focuses on modifying the original data sending functions
to use a more generic format. This will allow the master to read what messages are being received and
determine what action it needs to take for each message type.

7. **Sending data to the Slave [Full tutorial](https://chewett.co.uk/blog/1781/raspberry-pi-cluster-node-07-sending-data-to-the-slave/)** -
 This tutorial focuses on improving the slave by being able to request
data from the master.
 
8. **Slave Helper Functions [Full tutorial](https://chewett.co.uk/blog/1839/raspberry-pi-cluster-node-08-slave-helper-functions/)** -
 This tutorial focuses on creating a number of slave helper functions
to begin the process of fully automating the slaves.
 


 
## ToDo - List of things that will come in the future

* Socket talking - Master Broadcast
* Socket talking - Replay attacks
* Socket talking - Encryption
* Config loading - JSON
* Daemon Process -
* Master running simple webserver to offer files
* Slave /Master version/updates
* Multiple Slaves
* Periodic updates of the system
* Storing state of the cluster node
* Report Health metrics back (uptime, updates pending, time correctness, disk space)
* Rejoining the cluster after a master restart
* Smart slave restart
* Restarting slave once rebooted
* Keeping track of the running code revision
* Why keeping track of the time is important
* Slave git stash, pull, stash pop, resolving. 

