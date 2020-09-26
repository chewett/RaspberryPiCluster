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

## Tutorial 5 - Talking to nodes with JSON

In this tutorial I am using JSON to send messages between the nodes in a machine
readable format.

To make it easy to extend across various scripts I am packaging the functionality
in a DataPackager module. This will allow me to modify how the cluster talks
in the future as the implementation will be abstracted into this module.

The full details for
[Tutorial 05 - Talking to nodes with JSON is available on my blog](
https://chewett.co.uk/blog/1072/raspberry-pi-cluster-node-05-talking-to-nodes-with-json/)

## Licence

All code in this repository is licenced under a MIT licence.

The tutorials are copyright Christopher Hewett and should only be 
published on [http://chewett.co.uk/](http://chewett.co.uk/).
If you wish to use or republish these tutorials please contact me.

