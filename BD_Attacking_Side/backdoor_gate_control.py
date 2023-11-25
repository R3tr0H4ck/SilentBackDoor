"""
Author: R3tr0H4ck
Date: 25/11/2023
Purpose: Holds the main operation of the packet handling
"""
from scapy.all import *
import consts


class AttackerGateControl:
	"""
	make sure all the packets that comes in the given port holds the main operation 
	"""

	def __init__(self, packet_handler, listening_port=consts.LISTENING_PORT, accepted_flags=consts.RECIEVING_FLAG_VALUE):
		"""
		:param: packet_handler is a class that holds a function for handling the packets called handle_packet
		:param: listening_port is the port the attacker will listen to
		:param: accepted_flags is the value of the flags the packets should have
		"""
		self.packet_handler = packet_handler
		self.listening_port = listening_port
		self.accepted_flags = accepted_flags
		self.running = None


	def check_packet(self, packet):
		"""
		check if packet is suppose to be handled, in case it dose it will call the handle function
		:param: packet is the packet recieved from the sniffing
		"""
		if not TCP in packet:
			return
		if int(packet[TCP].flags) == self.accepted_flags:
			self.packet_handler.handle_packet(packet)


	def wait_for_packet(self):
		"""
		this funtion will sniff packets and will handle them if its suppose to
		"""
		while self.running:
			sniff(filter=f"port {self.listening_port}", prn=self.check_packet, count=1)


	def start_capturing_packet(self):
		"""Becuse the command sniff is a blocking command, the wait_for_packet will run as a thread this helps you close the program"""
		self.running = True

	def stop_capturing_packet(self):
		"""Becuse the command sniff is a blocking command, the wait_for_packet will run as a thread this helps you close the program"""
		self.running = False