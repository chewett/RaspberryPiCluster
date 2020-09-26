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

## Tutorial 1 - Logging Liveness - [Full tutorial](https://chewett.co.uk/blog/741/raspberry-pi-cluster-node-01-logging-liveness/) 
 
In the first tutorial I talked about setting up a simple python script to log data to a file every 10 seconds.

This will form the basis of logging what each node in the cluster is doing. One of the requirements is
that the logger should work for multi-threaded processes. This is why I introduce the standard python
library "logging".

The full details for
[Tutorial 01 - Logging Liveness is available on my blog](https://chewett.co.uk/blog/741/raspberry-pi-cluster-node-01-logging-liveness/)

## Licence

All code in this repository is licenced under a MIT licence.

The tutorials are copyright Christopher Hewett and should only be 
published on [http://chewett.co.uk/](http://chewett.co.uk/).
If you wish to use or republish these tutorials please contact me.

