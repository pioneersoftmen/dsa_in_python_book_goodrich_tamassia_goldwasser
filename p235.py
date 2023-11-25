import time 

class Packet:
    def __init__(self, data):
        self.data = data

class Alice:
    def __init__(self):
        self.packets = []

    def create_packet(self, data):
        packet = Packet(data)
        self.packets.append(packet)

class Internet:
    def __init__(self, alice, bob):
        self.alice = alice
        self.bob = bob

    def deliver_packets(self):
        while True:
            if self.alice.packets:
                packet = self.alice.packets.pop(0)
                self.bob.receive_packet(packet)
                print(f"Packet delivered to Bob:{packet.data}")
            time.sleep(1)

class Bob:
    def __init__(self):
        self.received_packets = []

    def receive_packet(self, packet):
        self.received_packets.append(packet)
        print(f"Bob received packet:{packet.data}")

    def check_packets(self):
        while True:
            if self.received_packets:
                packet = self.received_packets.pop(0)
                print(f'Bob read packet:{packet.data}')
            time.sleep(1)

alice = Alice()
bob = Bob()
internet = Internet(alice, bob)

alice.create_packet("Packet 1")
alice.create_packet("Packet 2")
alice.create_packet("Packet 3")

internet.deliver_packets()
bob.check_packets()
            

