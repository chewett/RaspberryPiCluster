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

## Tutorial 4 - Configuration Files with ConfigParser

Here I am using moving some of the configuration data from being hardcoded into the scripts into configuration files.

As I deploy the scripts to the nodes I don't want to have to change the scripts for each node.
Instead I am going to use configuration files to store data specific to the node such as the name of the node.
By using a specific configuration parsing module we can easily keep track of variables that are required
to be stored.

The full details for
[Tutorial 04 - Configuration Files with ConfigParser is available on my blog](https://chewett.co.uk/blog/1001/raspberry-pi-cluster-node-04-configuration-files-configparser/)

## Licence

All code in this repository is licenced under a MIT licence.

The tutorials are copyright Christopher Hewett and should only be 
published on [http://chewett.co.uk/](http://chewett.co.uk/).
If you wish to use or republish these tutorials please contact me.

