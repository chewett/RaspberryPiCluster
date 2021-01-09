

class NodeConfig:
    ''' Static class used to hold generic information about the node's Config'''

    node_type = None

    @staticmethod
    def load(config_data):
        NodeConfig.node_type = config_data.get("node_config", "node_type")


