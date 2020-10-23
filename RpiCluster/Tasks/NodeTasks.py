import subprocess
import time


def reboot():
    """When called the node will be rebooted"""
    subprocess.call(["sudo", "reboot"])


def shutdown():
    """When called the node will be shut down, make sure you can turn it back on if needed!"""
    subprocess.call(["sudo", "shutdown", "-h"])


def update_node():
    """When called the node will run apt update followed by apt upgrade"""
    node_update_log_1 = subprocess.check_output(["sudo", "apt", "update"])
    node_update_log_2 = subprocess.check_output(["sudo", "apt", "upgrade", "-y"])
    return [node_update_log_1, node_update_log_2]


def get_node_time():
    """Returns the current node time which may be useful for times when the Pi clock might be out of sync"""
    return time.time()


def get_node_codebase_revision():
    """Gets the revision of the codebase currently on the filesystem

        TODO: Improve this so we store the revision "on load" rather than hoping its the same
    """
    # Note: This is not necessarily the revision of the code currently running
    current_rev = subprocess.check_output(["git", "rev-parse", "HEAD"])
    return current_rev.rstrip("\r\n")


def get_node_codebase_revision_time():
    """Gets the time of the revision of the codebase currently on the filesystem

        TODO: Improve this so we store the revision "on load" rather than hoping its the same
    """
    node_rev = get_node_codebase_revision()
    rev_time = subprocess.check_output(["git", "show", "-s", "--format=%ct", node_rev])
    return int(rev_time.rstrip("\r\n"))


def update_node_codebase():
    """Updates the codebase using git pull, note if any local changes are present this might fail horribly """
    update_log = subprocess.check_output(["git", "pull"])
    return update_log








