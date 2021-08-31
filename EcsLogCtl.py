import EcsLogDef    as eld
import Client       as clt
import Server       as svr
import ViaSub       as via
import GetSub       as get

from os import path as ospath
from time import sleep
from threading import Thread

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *  

class EcsLogCtl(QObject):
    SetLogListSignal            = pyqtSignal()
    SetLogTableSignal           = pyqtSignal()
    SetLoadProgSignal           = pyqtSignal()

    def __init__(self):
        super().__init__()

        
        if via.GetMasterSlave() == 'M':
            self.EcsLogServer           = svr.EcsLogServer()
            self.EcsLogServer.Run()
        else:
            self.EcsLogClient           = clt.EcsLogClient()
            #self.EcsLogClient.Connect()
    
    def Run(self):
        thread_server = Thread(target=self.ClientControlPhase)
        thread_server.daemon = True
        thread_server.start()

    ###############################################################
    ##                      ClientControlPhase                   ##
    ###############################################################
    def ClientControlPhase(self):
        while True:
            sleep(0.01)

            #############################################################
            ##                       10 MES                            ## 
            ##                       20 CNV                            ##
            ##                       30 BCR                            ##
            ##                       40 BCR NOREAD                     ##
            ##                       50 STC                            ##
            ##                       60 JOBLOG                         ##
            #############################################################

            if eld.EcsC.CtlPhase == 0:
                if eld.EcsC.CommSts == 0:
                    try:
                        self.EcsLogClient.Connect()
                    except Exception as e:
                        print(e)
            
            elif eld.EcsC.CtlPhase == 10:
                if eld.EcsC.CommSts != 0: 
                    self.EcsLogClient.Send('10')
                    eld.EcsC.CtlPhase = 11
                else:
                    eld.EcsC.CtlPhase = 0
            elif eld.EcsC.CtlPhase == 11:
                if eld.EcsC.RxEnd != 1 : continue
                self.SetLogListSignal.emit()
                eld.EcsC.RxEnd = 0

            elif eld.EcsC.CtlPhase == 15:
                if self.FileExistsChecker(eld.CLT_MES_LOG_PATH, eld.EcsC.ChoiseCurrentItem):
                    self.ReqSender(eld.EcsC.CtlPhase, eld.EcsC.ChoiseCurrentItem)
                    eld.EcsC.CtlPhase = 16
                else:
                    eld.EcsC.RxEnd = 1
                    eld.EcsC.CtlPhase = 16
            
            elif eld.EcsC.CtlPhase == 16:
                if eld.EcsC.RxEnd != 1 : continue
                self.SetLogTableSignal.emit()
                self.SetLogListSignal.emit()
                eld.EcsC.RxEnd = 0

            elif eld.EcsC.CtlPhase == 20:
                self.EcsLogClient.Send('20')
                eld.EcsC.CtlPhase = 21
            
            elif eld.EcsC.CtlPhase == 21:
                if eld.EcsC.RxEnd != 1 : continue
                self.SetLogListSignal.emit()
                eld.EcsC.RxEnd = 0

            elif eld.EcsC.CtlPhase == 25:
                if self.FileExistsChecker(eld.CLT_CNV_LOG_PATH, eld.EcsC.ChoiseCurrentItem):
                    self.ReqSender(eld.EcsC.CtlPhase, eld.EcsC.ChoiseCurrentItem)
                    eld.EcsC.CtlPhase = 26
                else:
                    eld.EcsC.RxEnd = 1
                    eld.EcsC.CtlPhase = 26
            
            elif eld.EcsC.CtlPhase == 26:
                if eld.EcsC.RxEnd != 1 : continue
                self.SetLogTableSignal.emit()
                self.SetLogListSignal.emit()
                eld.EcsC.RxEnd = 0
                    
            elif eld.EcsC.CtlPhase == 30:
                self.EcsLogClient.Send('30')
                eld.EcsC.CtlPhase = 31
            
            elif eld.EcsC.CtlPhase == 31:
                if eld.EcsC.RxEnd != 1 : continue
                self.SetLogListSignal.emit()
                eld.EcsC.RxEnd = 0

            elif eld.EcsC.CtlPhase == 35:
                if self.FileExistsChecker(eld.CLT_BCR_LOG_PATH, eld.EcsC.ChoiseCurrentItem):
                    self.ReqSender(eld.EcsC.CtlPhase, eld.EcsC.ChoiseCurrentItem)
                    eld.EcsC.CtlPhase = 36
                else:
                    eld.EcsC.RxEnd = 1
                    eld.EcsC.CtlPhase = 36
            
            elif eld.EcsC.CtlPhase == 36:
                if eld.EcsC.RxEnd != 1 : continue
                self.SetLogTableSignal.emit()
                self.SetLogListSignal.emit()
                eld.EcsC.RxEnd = 0

            elif eld.EcsC.CtlPhase == 40:
                self.EcsLogClient.Send('40')
                eld.EcsC.CtlPhase = 41

            elif eld.EcsC.CtlPhase == 41:
                if eld.EcsC.RxEnd != 1 : continue
                self.SetLogListSignal.emit()
                eld.EcsC.RxEnd = 0

            elif eld.EcsC.CtlPhase == 45:
                if self.FileExistsChecker(eld.CLT_BCR_NOREAD_PATH, eld.EcsC.ChoiseCurrentItem):
                    self.ReqSender(eld.EcsC.CtlPhase, eld.EcsC.ChoiseCurrentItem)
                    eld.EcsC.CtlPhase = 46
                else:
                    eld.EcsC.RxEnd = 1
                    eld.EcsC.CtlPhase = 46
            
            elif eld.EcsC.CtlPhase == 46:
                if eld.EcsC.RxEnd != 1 : continue
                self.SetLogTableSignal.emit()
                self.SetLogListSignal.emit()
                eld.EcsC.RxEnd = 0

            elif eld.EcsC.CtlPhase == 50:
                self.EcsLogClient.Send('50')
                eld.EcsC.CtlPhase = 51

            elif eld.EcsC.CtlPhase == 51:
                if eld.EcsC.RxEnd != 1 : continue
                self.SetLogListSignal.emit()
                eld.EcsC.RxEnd = 0

            elif eld.EcsC.CtlPhase == 55:
                if self.FileExistsChecker(eld.CLT_STC_LOG_PATH, eld.EcsC.ChoiseCurrentItem):
                    self.ReqSender(eld.EcsC.CtlPhase, eld.EcsC.ChoiseCurrentItem)
                    eld.EcsC.CtlPhase = 56
                else:
                    eld.EcsC.RxEnd = 1
                    eld.EcsC.CtlPhase = 56
            
            elif eld.EcsC.CtlPhase == 56:
                if eld.EcsC.RxEnd != 1 : continue
                self.SetLogTableSignal.emit()
                self.SetLogListSignal.emit()
                eld.EcsC.RxEnd = 0

            elif eld.EcsC.CtlPhase == 60:
                self.EcsLogClient.Send('60')
                eld.EcsC.CtlPhase = 61

            elif eld.EcsC.CtlPhase == 61:
                if eld.EcsC.RxEnd != 1 : continue
                self.SetLogListSignal.emit()
                eld.EcsC.RxEnd = 0

            elif eld.EcsC.CtlPhase == 65:
                if self.FileExistsChecker(eld.CLT_JOB_LOG_PATH, eld.EcsC.ChoiseCurrentItem):
                    self.ReqSender(eld.EcsC.CtlPhase, eld.EcsC.ChoiseCurrentItem)
                    eld.EcsC.CtlPhase = 66
                else:
                    eld.EcsC.RxEnd = 1
                    eld.EcsC.CtlPhase = 66
            
            elif eld.EcsC.CtlPhase == 66:
                if eld.EcsC.RxEnd != 1 : continue
                self.SetLogTableSignal.emit()
                self.SetLogListSignal.emit()
                eld.EcsC.RxEnd = 0

            elif eld.EcsC.CtlPhase == 99:
                pass
            
            elif eld.EcsC.CtlPhase == 100:
                self.EcsLogClient           = clt.EcsLogClient()
                eld.EcsC.CtlPhase = 0
                eld.EcsC.CommSts = 0

    ###############################################################
    ##                      FileExistsChecker                    ##
    ###############################################################
    def FileExistsChecker(self, path, CurrentItem):
        if not ospath.exists(ospath.join(path,CurrentItem)):
            return True
        else:
            return False
    
    ###############################################################
    ##                      FileExistsChecker                    ##
    ###############################################################
    def ReqSender(self, Code, CurrentItem):
        SendData = get.WDataSeparator(str(Code),CurrentItem)
        self.EcsLogClient.Send(SendData)