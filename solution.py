from socket import *
import os
import sys
import struct
import time
import select
import binascii
ICMP_ECHO_REQUEST = 8

def checksum(s):
    # In this function we make the checksum of our packet 
    s = bytearray(s)
    dsum = 0
    countTo = (len(s) // 2) * 2

    for count in range(0, countTo, 2):
        thisVal = s[count+1] * 256 + s[count]
        dsum = dsum + thisVal
        dsum = dsum & 0xffffffff

    if countTo < len(s):
        dsum = dsum + s[-1]
        dsum = dsum & 0xffffffff

    dsum = (dsum >> 16) + (dsum & 0xffff)
    dsum = dsum + (dsum >> 16)
    ans = ~dsum
    ans = ans & 0xffff
    ans = ans >> 8 | (ans << 8 & 0xff00)
    return ans

def receiveOnePing(mySocket, ID, timeout, destAddr):
    timeLeft = timeout
    while 1:
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []: # Timeout
            return "Request timed out."

        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)

        icmpHeader = recPacket[20:28]
        icmpType, code, mychecksum, packetID, sequence = struct.unpack("bbHHh", icmpHeader)
    
        if type != 8 and packetID == ID:
            bytesInDouble = struct.calcsize("d")
            timeSent = struct.unpack("d", recPacket[28:28 + bytesInDouble])[0]
            return timeReceived - timeSent

        timeLeft = timeLeft - howLongInSelect
        
        if timeLeft <= 0:
            return "Request timed out."

def sendOnePing(mySocket, destAddr, ID):
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)

    myChecksum = 0
    # Make a dummy header with a 0 checksum.
    # struct -- Interpret strings as packed binary data
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("d", time.time())
    # Calculating the checksum on the data and the dummy header.
    myChecksum = checksum(header + data)

    # Get the right checksum, and put in the header
    if sys.platform == 'darwin':
        myChecksum = htons(myChecksum) & 0xffff
    #Convert 16-bit integers from host to network byte order.
    else:
        myChecksum = htons(myChecksum)

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data
    mySocket.sendto(packet, (destAddr, 1)) # AF_INET address must be tuple, not str

def doOnePing(destAddr, timeout):         
    icmp = getprotobyname("icmp") 
    #Creating Socket 
    mySocket = socket(AF_INET, SOCK_DGRAM, icmp) 

    myID = os.getpid() & 0xFFFF  #Return the current process i     
    sendOnePing(mySocket, destAddr, myID) 
    delay = receiveOnePing(mySocket, myID, timeout, destAddr)          

    mySocket.close()         
    return delay  

def ping(host, timeout=1):
    dest = gethostbyname(host)
    print ("Pinging " + dest + " using Python:")
    print ("")
    #Send ping requests to a server separated one second
    while 1 :
        delay = doOnePing(dest, timeout)
        print (delay)
        time.sleep(1)# one second to wait for reply
    return delay

ping("127.0.0.1")
