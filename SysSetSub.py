from socket import gethostname, gethostbyname
import EcsLogDef as eld

#print("host name : ", socket.gethostname())
#print("host ip (internal) : ", socket.gethostbyname(socket.gethostname()))
#print("host ip (external): ", socket.gethostbyname(socket.getfqdn()))


def SetMasterSlave(mmip):
    ip = gethostbyname(gethostname())
    if ip == mmip:
        eld.MASTER_SLAVE = 'M'
    else:
        eld.MASTER_SLAVE = 'C'

