from os import path as ospath
from time import sleep
import socket
from datetime import datetime
from threading import Thread
import ViaSub   as via
import GetSub   as get
import EcsLogDef as eld



class EcsLogServer():
    def __init__(self):
        Thread.__init__(self)

        # Server Init #
        self.Host = via.GetMasterIp()
        self.Port = 5025
        self.Server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.Server_socket.bind((self.Host, self.Port))
        self.Server_socket.listen(5)
        self.Max_bytes = 1024  
    ###############################################################
    ##                          Run                              ##
    ###############################################################
    def Run(self):
        thread_server = Thread(target=self.Server)
        thread_server.daemon = True
        thread_server.start()

    ###############################################################
    ##                          Server                           ##
    ###############################################################
    def Server(self):
        try:
            self.Accept()
        except Exception as e:
            print("Server Except : ",e)

    ###############################################################
    ##                          Accept                           ##
    ###############################################################
    def Accept(self):
        while (True):
            print("Accept start")

            Client_socket, Addr = self.Server_socket.accept()
            
            print('Accept', Addr)
            recv_thread = Thread(target=self.Binder, args=(Client_socket, Addr))
            recv_thread.daemon = True
            recv_thread.start()

    ###############################################################
    ##                          Binder                           ##
    ###############################################################
    def Binder(self, Client_socket, Addr):
        while (True):
            try:
                Rdata = Client_socket.recv(self.Max_bytes)
                if Rdata:
                    Rbuff = Rdata.decode()
                    Rbuff = get.RDataSeparator(Rbuff)

                    if len(Rbuff)   <=  2:
                        self.RcvLogList(Client_socket,Rbuff)

                    elif len(Rbuff) >   2:
                        self.RcvLogData(Client_socket,Rbuff,Rbuff[1])
                        sleep(0.1)
                        self.Send(Client_socket,str('bend'))

                    print("Binder : Read",Rbuff[0], Addr, datetime.now())

            except Exception as e:
                print("Binder Except : ",e)
                Client_socket.close()
                break

    ###############################################################
    ##                          Send                             ##
    ###############################################################               
    def Send(self,Client_Socket, WData):
        WData = bytes(WData, encoding='utf8')
        Client_Socket.sendall(WData)

    ###############################################################
    ##                          RcvLogList                       ##
    ###############################################################     
    def RcvLogList(self,Client_socket,Code):
        if Code[0] == '10':
            SendData = get.WDataSeparator(Code,via.GetMesLogList())
            self.Send(Client_socket,str(SendData))
            print("Binder : Send : ", SendData)

        elif Code[0] == '20':
            SendData = get.WDataSeparator(Code,via.GetCnvLogList())
            self.Send(Client_socket,str(SendData))
            print("Binder : Send : ", SendData)
        
        elif Code[0] == '30':
            SendData = get.WDataSeparator(Code,via.GetBcrLogList())
            self.Send(Client_socket,str(SendData))
            print("Binder : Send : ", SendData)
            
        elif Code[0] == '40':
            SendData = get.WDataSeparator(Code,via.GetBcrNoReadLogList())
            self.Send(Client_socket,str(SendData))
            print("Binder : Send : ", SendData)
            
        elif Code[0] == '50':
            SendData = get.WDataSeparator(Code,via.GetStcLogList())
            self.Send(Client_socket,str(SendData))
            print("Binder : Send : ", SendData)
            
        elif Code[0] == '60':
            SendData = get.WDataSeparator(Code,via.GetJobLogList())
            self.Send(Client_socket,str(SendData))
            print("Binder : Send : ", SendData)

    ###############################################################
    ##                          RcvLogData                       ##
    ############################################################### 
    def RcvLogData(self,Client_socket,Code,CurrFileName):
        if Code[0]  == '15':
            self.DataTransfer(Client_socket, Code, CurrFileName, eld.MES_LOG_PATH)

        elif Code[0] == '25':
            self.DataTransfer(Client_socket, Code, CurrFileName, eld.CNV_LOG_PATH)
        
        elif Code[0] == '35':
            self.DataTransfer(Client_socket, Code, CurrFileName, eld.BCR_LOG_PATH)

        elif Code[0] == '45':
            self.DataTransfer(Client_socket, Code, CurrFileName, eld.BCR_NOREAD_PATH)

        elif Code[0] == '55':
            self.DataTransfer(Client_socket, Code, CurrFileName, eld.STC_LOG_PATH)
            
        elif Code[0] == '65':
            self.DataTransfer(Client_socket, Code, CurrFileName, eld.JOB_LOG_PATH)
            
    ############################################################### 
    ##                          DataTransfer                     ##
    ############################################################### 
    def DataTransfer(self, Client_socket, Code, CurrFileName, Path):
        if self.CheckFileList(CurrFileName,Path) == True:
            MesLogFilePath = Path + '\\' + CurrFileName[0]
            with open('{0}'.format(MesLogFilePath),'r') as FileData :
                ReadData = FileData.readlines()
            
            with open('{0}'.format(MesLogFilePath),'r') as FileData :
                try:
                    SendData = get.WDataSeparator(Code, ReadData[0])
                    Flush = FileData.readline()
 
                    while SendData:
                         self.Send(Client_socket,str(SendData))
                         SendData = FileData.readline()
                except Exception as e:
                    print('RcvLogData->file open :  ', e)
            print("Binder : Sended!! ")
            
        else:
            print('check Name')
        
    def CheckFileList(self,CurrFileName,Path):
        try:
            if ospath.exists(ospath.join(Path,CurrFileName[0])):
                return True
            else:
                return False
        except Exception as e:
            print('CheckFileList : ',e)