

class VitalsPayload:

    def __init__(self, cpu_percentage, cpu_frequency, ram_free, swap_free, cpu_temperature=None):
        self.cpu_percentage = cpu_percentage
        self.cpu_frequency = cpu_frequency
        self.ram_free = ram_free
        self.swap_free = swap_free
        self.cpu_temperature = cpu_temperature

    def get_flat_payload(self):
        """ This will be called to get the data in a flat format to be used to send as a payload """
        base_object = {
            'cpu_percentage': self.cpu_percentage,
            'cpu_frequency': self.cpu_frequency,
            'ram_free': self.ram_free,
            'swap_free': self.swap_free,
        }

        # If there are more "optional" parts, these will be added if they exist
        if self.cpu_temperature:
            base_object['cpu_temperature'] = self.cpu_temperature

        return base_object

    @staticmethod
    def load_payload(payload):
        cpu_temperature = None
        if "cpu_temperature" in payload:
            cpu_temperature = payload['cpu_temperature']

        return VitalsPayload(payload['cpu_percentage'], payload['cpu_frequency'], payload['ram_free'], payload['swap_free'], cpu_temperature=cpu_temperature)

