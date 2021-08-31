import socket
from threading import Thread
import EcsLogDef    as eld
import ViaSub       as via
import GetSub       as get

class EcsLogClient:
    def __init__(self):
        print("Client start")
        self.Client_Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Client_Sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.Host = '192.168.0.193'
        
    def Connect(self):
        try:
            self.Client_Sock.connect((self.Host, 5025))
            
            eld.EcsC.CommSts = 1
            eld.EcsC.Used = 0

            thread_GetFrSvrData = Thread(target=self.GetFrSvrData)
            thread_GetFrSvrData.daemon = True
            thread_GetFrSvrData.start()

        except Exception as e:
            print('EcsLogClient.Connect : ',e)
            eld.EcsC.CtlPhase = 0
            eld.EcsC.CommSts = 0
            
    def Send(self,WData):
        WData = str(WData)
        WData = WData.encode(encoding='UTF-8')
        self.Client_Sock.sendall(WData)

    def DataRecver(self, Data, Path):
        Data = str(Data[1][0])
        Data = bytes(Data,encoding='utf8')
        with open(Path + '\\' + eld.EcsC.ChoiseCurrentItem, 'wb') as f: 
            try:
                while Data != b'bend': 
                    f.write(Data)
                    eld.EcsC.Data_Transfered += len(Data)
                    Data = self.Client_Sock.recv(4096)
            except Exception as e:
                print(e)

        print("Download Complete")
        eld.EcsC.RxEnd = 1
        print(eld.EcsC.Data_Transfered)
        eld.EcsC.Data_Transfered = 0

    def GetFrSvrData(self):
        try:
            while True:
                data = self.Client_Sock.recv(1024)
                data = data.decode()
                data = get.RDataSeparator(data)

                if data[0] == '10':
                    via.SetFrSvrMesLogList(data[1])
                    eld.EcsC.RxEnd = 1

                elif data[0] == '15':
                    self.DataRecver(data, eld.CLT_MES_LOG_PATH)

                elif data[0] == '20':
                    via.SetFrSvrCnvLogList(data[1])
                    eld.EcsC.RxEnd = 1

                elif data[0] == '25':
                    self.DataRecver(data, eld.CLT_CNV_LOG_PATH)

                elif data[0] == '30':
                    via.SetFrSvrBcrLogList(data[1])
                    eld.EcsC.RxEnd = 1

                elif data[0] == '35':
                    self.DataRecver(data, eld.CLT_BCR_LOG_PATH)

                elif data[0] == '40':
                    via.SetFrSvrBcrNoReadLogList(data[1])
                    eld.EcsC.RxEnd = 1

                elif data[0] == '45':
                    self.DataRecver(data, eld.CLT_BCR_NOREAD_PATH)

                elif data[0] == '50':
                    via.SetFrSvrStcLogList(data[1])
                    eld.EcsC.RxEnd = 1

                elif data[0] == '55':
                    self.DataRecver(data, eld.CLT_STC_LOG_PATH)

                elif data[0] == '60':
                    via.SetFrSvrJobLogList(data[1])
                    eld.EcsC.RxEnd = 1

                elif data[0] == '65':
                    self.DataRecver(data, eld.CLT_JOB_LOG_PATH)

        except Exception as ex:
            print('listen : ',ex)
            self.Client_Sock.close()
            eld.EcsC.CtlPhase = 100
            eld.EcsC.CommSts = 99
            
