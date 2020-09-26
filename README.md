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

## Tutorial 3 - Basic node communication between two nodes

In this tutorial we build a very basic one way communication method to send data from the slave to a master.

The basis of any cluster is being able to collaborate and communicate between nodes. This initial implementation
of this will create a connection between a master and slave node and send data from slave to master.
The master will print out any messages recieved from the slave. The slave will send a message every 10 seconds
with a message.

The full details for
[Tutorial 03 - Basic node communication between two nodes is available on my blog](https://chewett.co.uk/blog/901/raspberry-pi-cluster-node-03-basic-node-communication-two-nodes/)

## Licence

All code in this repository is licenced under a MIT licence.

The tutorials are copyright Christopher Hewett and should only be 
published on [http://chewett.co.uk/](http://chewett.co.uk/).
If you wish to use or republish these tutorials please contact me.

