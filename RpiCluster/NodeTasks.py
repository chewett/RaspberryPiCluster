import subprocess
import time


def reboot():
    subprocess.call(["sudo", "reboot"])


def shutdown():
    subprocess.call(["sudo", "shutdown", "-h"])


def update_node():
    node_update_log_1 = subprocess.check_output(["sudo", "apt-get", "update"])
    node_update_log_2 = subprocess.check_output(["sudo", "apt-get", "upgrade"])
    return [node_update_log_1, node_update_log_2]


def get_node_time():
    return time.time()


def get_node_codebase_revision():
    # Note: This is not nesscarily the revision of the code currently running
    current_rev = subprocess.check_output(["git", "rev-parse", "HEAD"])
    return current_rev.rstrip("\r\n")


def get_node_codebase_revision_time():
    node_rev = get_node_codebase_revision()
    rev_time = subprocess.check_output(["git", "show", "-s", "--format=%ct", node_rev])
    return int(rev_time.rstrip("\r\n"))


def update_node_codebase():
    update_log = subprocess.check_output(["git", "pull"])
    return update_log








