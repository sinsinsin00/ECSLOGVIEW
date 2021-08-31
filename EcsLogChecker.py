from os import path as ospath
import sys
import MesLogSub        as mls
import CnvLogSub        as cls
import BarLogSub        as bls
import BarNoReadSub     as bns
import StcLogSub        as sls
import JobLogSub        as jls

import ViaSub           as via
import EcsLogDef        as eld
import EcsLogSub        as els
import EcsLogCtl        as elc
import SysSetSub        as sss

from PyQt5 import uic
from PyQt5 import QtCore 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

sss.SetMasterSlave(eld.MASTER_COMPUTER_IP)

if via.GetMasterSlave() == 'M':
    form_class = uic.loadUiType("EcsLogChecker_Svr.ui")[0]
else:
    form_class = uic.loadUiType("EcsLogChecker_Clt.ui")[0]

class MessWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    ###############################################################
    ##              MainWindow Var Init                          ##
    ###############################################################
        self.ReadRange          = 10
        self.SearchItem         = 0
        self.CurrSearchItem     = 0
        self.SearchMaxCount     = 0
        self.CurrSearchCount    = 0

    ###############################################################
    ##              Program   Start Init                         ##
    ###############################################################
        els.InitialRoutine()
        self.EcsLogCtl      = elc.EcsLogCtl()
        self.GetMesLog      = mls.GetMesLog()
        self.GetCnvLog      = cls.GetCnvLog()
        self.GetBarLog      = bls.GetBarLog()
        self.GetBarNoRead   = bns.GetBarNoRead()
        self.GetStcLog      = sls.GetStcLog()
        self.GetJobLog      = jls.GetJobLog()
        
        if via.GetMasterSlave() == 'M':
            self.setWindowTitle(eld.RCP_TITLE_M)

            
        else:
            self.setWindowTitle(eld.RCP_TITLE_C)
            self.EcsLogCtl.Run()


    ###############################################################
    ##              Other   Set Signal Connect                   ##
    ###############################################################
        #self.EcsLogCtl.SetLoadProgSignal.connect()
        self.EcsLogCtl.SetLogTableSignal.connect(self.WriteFrSvrLog)
        self.EcsLogCtl.SetLogListSignal.connect(self.WriteFrSvrLogList)

    ###############################################################
    ##              MainWindow   Set Signal Connect              ##
    ###############################################################
        self.Btn_BcrLog.clicked.connect(                    self.Btn_Bcr_Log_Clicked                        )
        self.Btn_CnvLog.clicked.connect(                    self.Btn_Cnv_Log_Clicked                        )
        self.Btn_JobLog.clicked.connect(                    self.Btn_Job_Log_Clicked                        )
        self.Btn_MesLog.clicked.connect(                    self.Btn_Mes_Log_Clicked                        )
        self.Btn_StcLog.clicked.connect(                    self.Btn_Stc_Log_Clicked                        )
        self.Btn_BcrNoReadLog.clicked.connect(              self.Btn_Bcr_No_Read_Log_Clicked                )

        self.BtnFind.clicked.connect(                       self.BtnFindclicked                             )
        self.BtnCurrRowSel.clicked.connect(                 self.BtnCurrRowSelclicked                       )

        self.comboBox.currentIndexChanged.connect(          self.comboBoxTextChanged1                       )
        self.comboBox_2.currentIndexChanged.connect(        self.comboBox_2TextChanged1                     )
        self.listWidget.itemDoubleClicked.connect(          self.ListWidgetDoubleClicked                    )

    ###############################################################
    ##                      Write File List                      ##
    ###############################################################
    ###############################################################
    ##                       10 MES                              ## 
    ##                       20 CNV                              ##
    ##                       30 BCR                              ##
    ##                       40 BCR NOREAD                       ##
    ##                       50 STC                              ##
    ##                       60 JOBLOG                           ##
    ###############################################################
    def WriteFrSvrLogList(self):
        if eld.EcsC.CurrScr == 10:
            FrSvrLogData = via.GetFrSvrMesLogFileList()

        elif eld.EcsC.CurrScr == 20:
            FrSvrLogData = via.GetFrSvrCnvLogFileList()

        elif eld.EcsC.CurrScr == 30:
            FrSvrLogData = via.GetFrSvrBcrLogFileList()

        elif eld.EcsC.CurrScr == 40:
            FrSvrLogData = via.GetFrSvrBcrNoReadLogFileList()

        elif eld.EcsC.CurrScr == 50:
            FrSvrLogData = via.GetFrSvrStcLogFileList()

        elif eld.EcsC.CurrScr == 60:
            FrSvrLogData = via.GetFrSvrJobLogFileList()

        list = [row_element for row in FrSvrLogData for row_element in row]
        self.listWidget.clear()
        self.listWidget.addItems(list)

        for i, filename in enumerate(list):
            if eld.EcsC.CurrScr == 10:
                if not ospath.exists(ospath.join(eld.CLT_MES_LOG_PATH,filename)):
                    self.listWidget.item(i).setForeground(QtCore.Qt.red)

            elif eld.EcsC.CurrScr == 20:
                if not ospath.exists(ospath.join(eld.CLT_CNV_LOG_PATH,filename)):
                    self.listWidget.item(i).setForeground(QtCore.Qt.red)

            elif eld.EcsC.CurrScr == 30:
                if not ospath.exists(ospath.join(eld.CLT_BCR_LOG_PATH,filename)):
                    self.listWidget.item(i).setForeground(QtCore.Qt.red)

            elif eld.EcsC.CurrScr == 40:
                if not ospath.exists(ospath.join(eld.CLT_BCR_NOREAD_PATH,filename)):
                    self.listWidget.item(i).setForeground(QtCore.Qt.red)

            elif eld.EcsC.CurrScr == 50:
                if not ospath.exists(ospath.join(eld.CLT_STC_LOG_PATH,filename)):
                    self.listWidget.item(i).setForeground(QtCore.Qt.red)

            elif eld.EcsC.CurrScr == 60:
                if not ospath.exists(ospath.join(eld.CLT_JOB_LOG_PATH,filename)):
                    self.listWidget.item(i).setForeground(QtCore.Qt.red)

        via.Clear()
 

    ###############################################################
    ##                      Write Log                            ##
    ###############################################################
    ###############################################################
    ##                       16 MES                              ## 
    ##                       26 CNV                              ##
    ##                       36 BCR                              ##
    ##                       46 BCR NOREAD                       ##
    ##                       56 STC                              ##
    ##                       66 JOBLOG                           ##
    ###############################################################
    def WriteFrSvrLog(self):
        if eld.EcsC.CtlPhase == 16:
            log = self.GetMesLog.Get_Clt_Mes_Log(eld.EcsC.ChoiseCurrentItem,self.ReadRange)

        elif eld.EcsC.CtlPhase == 26:
            log = self.GetCnvLog.Get_Clt_Cnv_Log(eld.EcsC.ChoiseCurrentItem,self.ReadRange)

        elif eld.EcsC.CtlPhase == 36:
            log = self.GetBarLog.Get_Clt_Bar_Log(eld.EcsC.ChoiseCurrentItem,self.ReadRange)

        elif eld.EcsC.CtlPhase == 46:
            log = self.GetBarNoRead.Get_Clt_Bar_No_Read(eld.EcsC.ChoiseCurrentItem,self.ReadRange)

        elif eld.EcsC.CtlPhase == 56:
            log = self.GetStcLog.Get_Clt_Stc_Log(eld.EcsC.ChoiseCurrentItem,self.ReadRange)

        elif eld.EcsC.CtlPhase == 66:
            log = self.GetJobLog.Get_Clt_Job_Log(eld.EcsC.ChoiseCurrentItem,self.ReadRange)

        via.Clear()
        self.TableHeader = list(log)
        self.tableWidget.setRowCount(len(log.index))
        self.SetTable(log)
        

    ###############################################################
    ##                ListWidget Double Click                    ##
    ###############################################################
    def ListWidgetDoubleClicked(self):
        self.ClearSearchData()
        if via.GetMasterSlave() == 'M':
            self.SrvLogLoad()
        else:
            self.CltLogLoad()

    def SrvLogLoad(self):
        if eld.EcsC.CurrScr == 10:
            log = self.GetMesLog.Get_Svr_Mes_Log(self.listWidget.currentItem().text(),self.ReadRange)

        elif eld.EcsC.CurrScr == 20:
            log = self.GetCnvLog.Get_Svr_Cnv_Log(self.listWidget.currentItem().text(),self.ReadRange)  

        elif eld.EcsC.CurrScr == 30:
            log = self.GetBarLog.Get_Svr_Bar_Log(self.listWidget.currentItem().text(),self.ReadRange) 

        elif eld.EcsC.CurrScr == 40:
            log = self.GetBarNoRead.Get_Svr_Bar_No_Read(self.listWidget.currentItem().text(),self.ReadRange) 
            
        elif eld.EcsC.CurrScr == 50:
            log = self.GetStcLog.Get_Svr_Stc_Log(self.listWidget.currentItem().text(),self.ReadRange) 
            
        elif eld.EcsC.CurrScr == 60:
            log = self.GetJobLog.Get_Svr_Job_Log(self.listWidget.currentItem().text(),self.ReadRange) 
            
    
        self.TableHeader = list(log)
        self.tableWidget.setRowCount(len(log.index))
        self.SetTable(log)

    def CltLogLoad(self):
        self.labelDownload.setText(self.listWidget.currentItem().text() +"<strong>" + "  Loading" + "</strong>" )
        eld.EcsC.ChoiseCurrentItem = self.listWidget.currentItem().text()
        if eld.EcsC.CurrScr == 10:
            eld.EcsC.CtlPhase = 15
            eld.EcsC.Used = 1
        elif eld.EcsC.CurrScr == 20:
            eld.EcsC.CtlPhase = 25
            eld.EcsC.Used = 1
        elif eld.EcsC.CurrScr == 30:
            eld.EcsC.CtlPhase = 35
            eld.EcsC.Used = 1
        elif eld.EcsC.CurrScr == 40:
            eld.EcsC.CtlPhase = 45
            eld.EcsC.Used = 1
        elif eld.EcsC.CurrScr == 50:
            eld.EcsC.CtlPhase = 55
            eld.EcsC.Used = 1
        elif eld.EcsC.CurrScr == 60:
            eld.EcsC.CtlPhase = 65
            eld.EcsC.Used = 1

    def SetTable(self,log):
        try:
            self.tableWidget.setColumnCount(len(log.columns))
            LogDataValues = log.values
            TableSetItem = self.tableWidget.setItem
            IndexLen = len(log.index)
            ColunmLen = len(log.columns)
            HeaderLen = len(self.TableHeader)

            for i in range(IndexLen):
                for j in range(ColunmLen):
                    TableSetItem(i,j,QTableWidgetItem(str(LogDataValues[i][j])))
                    #QApplication.processEvents()

            for i in range(HeaderLen):
                self.tableWidget.setHorizontalHeaderItem(i,QTableWidgetItem(str(self.TableHeader[i])))

            self.tableWidget.resizeColumnsToContents()

            self.TableHeader = []
            LogDataValues = []

        except Exception as e:
            print("SetTable : ",e)

    
    ###############################################################
    ##                Search ComboBox List                       ##
    ###############################################################
    def comboBoxTextChanged1(self):
        self.textEditFind.setPlainText(self.comboBox.currentText())
        self.Search(self.comboBox.currentText())

    def comboBox_2TextChanged1(self):
        self.ReadRange = self.comboBox_2.currentText()
        self.ReadRange = self.ReadRange.replace("%","")

    def Search(self, s):
        if self.SearchItem != self.tableWidget.findItems(str(s),Qt.MatchContains): 
            self.SearchItem = self.tableWidget.findItems(str(s),Qt.MatchContains)
            self.SearchMaxCount = (len(self.SearchItem))
        if self.SearchItem:  # we have found something
            if self.SearchItem == self.CurrSearchItem:
                if self.CurrSearchCount != self.SearchMaxCount:
                    item = self.SearchItem[self.CurrSearchCount]  
                    self.tableWidget.setCurrentItem(item)
                    self.CurrSearchCount = self.CurrSearchCount + 1 
                    self.LSearchNo.setText(str(self.SearchMaxCount))
                    self.LCurrNo.setText(str(self.CurrSearchCount)) 
                else:
                    self.ClearSearchData()
                    QMessageBox.about(self, "Search", "   더 이상 찾을 수가 없어요!.    ")
                    
            else:
                if self.CurrSearchCount > 0:
                    self.CurrSearchCount = 0
                item = self.SearchItem[0]  
                self.tableWidget.setCurrentItem(item) 
                self.CurrSearchItem = self.SearchItem
                self.CurrSearchCount = self.CurrSearchCount + 1 
                self.LSearchNo.setText(str(self.SearchMaxCount)) 
                self.LCurrNo.setText(str(self.CurrSearchCount)) 
        else:
            self.ClearSearchData()

    ###############################################################
    ##                      Init and Clear                      ##
    ###############################################################
    def ClearSearchData(self):
        self.SearchItem = ''
        self.SearchMaxCount = 0
        self.CurrSearchCount= 0 
        self.LSearchNo.setText('0')
        self.LCurrNo.setText('0')

    ###############################################################
    ##                      Btn Click Events                     ##
    ###############################################################
    def WriteLogList(self, List, Code):
        self.listWidget.clear()
        #self.tableWidget.clear()
        if via.GetMasterSlave() == 'M':
            self.listWidget.addItems(List)

        else:
            if eld.EcsC.Used == 0: 
                eld.EcsC.CtlPhase = Code
                eld.EcsC.Used = 1

    def Btn_Mes_Log_Clicked(self):
        eld.EcsC.CurrScr = 10
        self.WriteLogList(via.GetMesLogList(), 10)

    def Btn_Cnv_Log_Clicked(self):
        eld.EcsC.CurrScr = 20
        self.WriteLogList(via.GetCnvLogList(), 20)

    def Btn_Bcr_Log_Clicked(self):
        eld.EcsC.CurrScr = 30
        self.WriteLogList(via.GetBcrLogList(), 30)

    def Btn_Bcr_No_Read_Log_Clicked(self):
        eld.EcsC.CurrScr = 40
        self.WriteLogList(via.GetBcrNoReadLogList(), 40)

    def Btn_Stc_Log_Clicked(self):
        eld.EcsC.CurrScr = 50
        self.WriteLogList(via.GetStcLogList(), 50)

    def Btn_Job_Log_Clicked(self):
        eld.EcsC.CurrScr = 60
        self.WriteLogList(via.GetJobLogList(), 60)

    def BtnFindclicked(self):
        self.Search(self.textEditFind.toPlainText())

    def BtnCurrRowSelclicked(self):
        if self.SearchItem != '' and self.textEditFind.toPlainText() != '':            
            self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.tableWidget.setCurrentItem(self.SearchItem[self.CurrSearchCount - 1])
            self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        elif self.tableWidget.selectedItems():
            self.ClearSearchData()
            a = self.tableWidget.selectedItems()
            s = QTableWidgetItem(a[0])
            s = s.text()
            #self.search(s)



app = QApplication(sys.argv)
window = MessWindow()
window.show()
app.exec_()
