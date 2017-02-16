'''
Author: Veerendra. Kakumanu
Description: TCP status number(st) which we are in /proc/net/tcp

According to MAN Page:
/proc/net/tcp Holds a dump of the TCP socket table. Much of the information is not of use apart from debugging. 
The "sl" value is the kernel hash slot for the socket, the "local_address" is the local address and port number pair. 
The "rem_address" is the remote address and port number pair (if connected). 
"St" is the internal status of the socket. 
The "tx_queue" and "rx_queue" are the outgoing and incoming data queue in terms of kernel memory usage. 
The "tr", "tm->when", and "rexmits" fields hold internal information of the kernel socket state and are only useful for debugging. 
The "uid" field holds the effective UID of the creator of the socket. 
'''
states={
"01":"TCP_ESTABLISHED",
"02":"TCP_SYN_SENT",
"03":"TCP_SYN_RECV",
"04":"TCP_FIN_WAIT1",
"05":"TCP_FIN_WAIT2",
"06":"TCP_TIME_WAIT",
"07":"TCP_CLOSE",
"08":"TCP_CLOSE_WAIT",
"09":"TCP_LAST_ACK",
"0A":"TCP_LISTEN",
"0B":"TCP_CLOSING",
"0C":"TCP_MAX_STATES"
}
