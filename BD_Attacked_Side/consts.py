"""
holds the consts for the backdoor
"""
############# THE BACKDOOR SETTINGS #############
LISTENING_PORT = 64321
SENDING_PORT = 42069
RECIEVING_FLAG_VALUE = 5 #This Gives The Value of FIN RST flags, and if you know the protocol TCP, they never apear together. (pretty good way to see its our program that contacts us)
SENDING_FLAG_VALUE = 19 # This Gives The Value of FIN SYN and ACK flags, and if you know the protocol TCP, they never apear together. (pretty good way to see its our program that contacts us)

#############   Response Settings   #############
ERR_MSG = b"ERR_FUNC_NOT_FOUND"