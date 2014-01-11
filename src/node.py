from sim import Sim

class Node(object):
    def __init__(self):
        self.links = []
        self.protocols = {}
        self.forwarding_table = {}

    ## Links ## 

    def add_link(self,link):
        self.links.append(link)

    def delete_link(self,link):
        if link not in self.links:
            return
        self.links.remove(link)

    ## Protocols ## 

    def add_protocol(self,protocol,handler):
        self.protocols[protocol] = handler

    def delete_protocol(self,protocol):
        if protocol not in self.protocols:
            return
        del self.protocols[protocol]

    ## Forwarding table ##

    def add_forwarding_entry(self,address,link):
        self.forwarding_table[address] = link

    def delete_forwarding_entry(self,address,link):
        if address not in self.forwarding_table:
            return
        del self.forwarding_table[address]

    ## Handling packets ##

    def handle_packet(self,packet):
        # check if the packet is for me
        for link in self.links:
            if link.address == packet.destination_address:
                self.receive_packet(packet)

        # forward the packet
        self.forward_packet(packet)

    def receive_packet(self,packet):
        if packet.protocol not in self.protocols:
            return
        self.protocols[packet.protocol].handle_packet(packet)

    def forward_packet(self,packet):
        if packet.destination_address not in self.forwarding_table:
            return
        self.forwarding_table[packet.destination_address].handle_packet(packet)