Rasperry Pi Cluster project - 01 Logging Liveness
=================================================

In the first tutorial I talked about setting up a simple python script to log data to a file every 10 seconds.

This will form the basis of logging what each node in the cluster is doing. One of the requirements is
that the logger should work for multi-threaded processes. This is why I introduce the standard python
library "logging".

The full details for
[Tutorial 01 - Logging Liveness is available on my blog](https://chewett.co.uk/blog/741/raspberry-pi-cluster-node-01-logging-liveness/)