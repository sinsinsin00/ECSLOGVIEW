import MesLogDef as     mld
import EcsLogDef as     eld
from pandas import DataFrame
from xml.etree import ElementTree

#엑셀 저장 
#self.df.to_csv(self.DirFolderPath + "\\Mes.csv")

class GetMesLog:
    def __init__(self):
        self.MesLog = mld.MesLog()

    def run(self):
        pass

    ###############################################################
    ##                          Convert                          ##
    ###############################################################
    def Convert(self,CurrFileName,ReadRange,Path):
        MesLogFilePath = Path + '\\' + CurrFileName
        with open('{0}'.format(MesLogFilePath),'r') as filelist :
            ssdata = filelist.readlines()
            dataS = len(ssdata) - len(ssdata) * int(ReadRange) / 100
            #print(dataS)
            ssdata = ssdata[int(dataS):] 
            #print(len(ssdata)*10/100) 
            for line in ssdata:
                if (2000 > len(line)) and (len(line) > 100):
                    TrimData = line.split("  ",1)
                    self.MesLog.MESDATE.append(TrimData[0].replace(" ",""))
                    self.XmlData = TrimData[1].split(']',1)
                    self.MesLog.MESSENDTO.append(self.XmlData[0] + ']')
                    self.MesLog.MASSEGE.append(self.XmlData[1])
                    self.XmlScan(self.XmlData[1])
        
    ###############################################################
    ##                          ConvertWithEncode                ##
    ###############################################################
    def ConvertWithEncode(self,CurrFileName,ReadRange,Path):
        MesLogFilePath = Path + '\\' + CurrFileName
        with open('{0}'.format(MesLogFilePath),'r' ,  encoding='utf-8') as filelist :
            ssdata = filelist.readlines()
            dataS = len(ssdata) - len(ssdata) * int(ReadRange) / 100
            #print(dataS)
            ssdata = ssdata[int(dataS):] 
            #print(len(ssdata)*10/100) 
            for line in ssdata:
                if (2000 > len(line)) and (len(line) > 100):
                    TrimData = line.split("  ",1)
                    self.MesLog.MESDATE.append(TrimData[0].replace(" ",""))
                    self.XmlData = TrimData[1].split(']',1)
                    self.MesLog.MESSENDTO.append(self.XmlData[0] + ']')
                    self.MesLog.MASSEGE.append(self.XmlData[1])
                    self.XmlScan(self.XmlData[1])
        
    ###############################################################
    ##                          Get_Svr_Mes_Log                     ##
    ###############################################################
    def Get_Svr_Mes_Log(self,CurrFileName,ReadRange):
        try:
            try:
                self.Convert(CurrFileName,ReadRange,eld.MES_LOG_PATH)
            except:
                self.ConvertWithEncode(CurrFileName,ReadRange,eld.MES_LOG_PATH)
                    
            return  self.SetDataFrame()

        except Exception as e:
            print('GetMesLogFile : ', e)


    ###############################################################
    ##                          Get_Clt_Mes_Log                     ##
    ###############################################################
    def Get_Clt_Mes_Log(self,CurrFileName,ReadRange):
        try:
            try:
                self.Convert(CurrFileName,ReadRange,eld.CLT_MES_LOG_PATH)
            except:
                self.ConvertWithEncode(CurrFileName,ReadRange,eld.CLT_MES_LOG_PATH)
                    
            return  self.SetDataFrame()

        except Exception as e:
            print('GetMesLogFile : ', e)

    ###############################################################
    ##                          XmlScan                          ##
    ###############################################################
    def XmlScan(self, RXmlData):
        try:
            XmlDataStr = ''
            XmlDataStr = str(RXmlData).replace("  ","").replace(" ","").strip().replace("&",'_')
            XmlDataStr = ElementTree.fromstring(XmlDataStr)

            self.MesLog.MSG_ID.append(getattr(             XmlDataStr.find(        '*MSG_ID'           ), 'text', None))
            self.MesLog.MSG_LEN.append(getattr(            XmlDataStr.find(        '*MSG_LEN'          ), 'text', None))
            self.MesLog.SYSTEM_BYTES.append(getattr(       XmlDataStr.find(        '*SYSTEM_BYTES'     ), 'text', None))
            self.MesLog.EQUIP_ID.append(getattr(           XmlDataStr.find(        '*EQUIP_ID'         ), 'text', None))
            self.MesLog.LOT_ID.append(getattr(             XmlDataStr.find(        '*LOT_ID'           ), 'text', None))
            self.MesLog.FROM.append(getattr(               XmlDataStr.find(        '*FROM'             ), 'text', None))
            self.MesLog.TO.append(getattr(                 XmlDataStr.find(        '*TO'               ), 'text', None))
            self.MesLog.USER_ID.append(getattr(            XmlDataStr.find(        '*SYSTEM_BYTES'     ), 'text', None))
            self.MesLog.PROCESS.append(getattr(            XmlDataStr.find(        '*PROCESS'          ), 'text', None))
            self.MesLog.MDATE.append(getattr(              XmlDataStr.find(        '*DATE'             ), 'text', None))
            self.MesLog.TRAY_GUBUN.append(getattr(         XmlDataStr.find(        '*TRAY_GUBUN'       ), 'text', None))
            self.MesLog.PORT.append(getattr(               XmlDataStr.find(        '*PORT'             ), 'text', None))
            self.MesLog.TRAY_COUNT.append(getattr(         XmlDataStr.find(        '*TRAY_COUNT'       ), 'text', None))
            self.MesLog.TRAY_POSITION.append(getattr(      XmlDataStr.find(        '*TRAY_POSITION'    ), 'text', None))
            self.MesLog.TRAY_ID.append(getattr(            XmlDataStr.find(        '*TRAY_ID'          ), 'text', None))
            self.MesLog.LINE.append(getattr(               XmlDataStr.find(        '*LINE'             ), 'text', None))
            self.MesLog.WORK_NO.append(getattr(            XmlDataStr.find(        '*WORK_NO'          ), 'text', None))
            self.MesLog.SHIP_ECS.append(getattr(           XmlDataStr.find(        '*SHIP_ECS'         ), 'text', None))
            self.MesLog.BATCH.append(getattr(              XmlDataStr.find(        '*BATCH'            ), 'text', None))
            self.MesLog.MAGAZINE_GROUP.append(getattr(     XmlDataStr.find(        '*MAGAZINE_GROUP'   ), 'text', None))
            self.MesLog.MAGAZINE_ADDRESS.append(getattr(   XmlDataStr.find(        '*MAGAZINE_ADDRESS' ), 'text', None))
            self.MesLog.PRIORITIZE.append(getattr(         XmlDataStr.find(        '*PRIORITIZE'       ), 'text', None))
            self.MesLog.RETURN_VALUE.append(getattr(       XmlDataStr.find(        '*RETURN_VALUE'     ), 'text', None))
            self.MesLog.FROM_PORT.append(getattr(          XmlDataStr.find(        '*FROM_PORT'        ), 'text', None))
            self.MesLog.TO_PORT.append(getattr(            XmlDataStr.find(        '*TO_PORT'          ), 'text', None))
            self.MesLog.BANK_ALL.append(getattr(           XmlDataStr.find(        '*BANK_ALL'         ), 'text', None))
            self.MesLog.OPER.append(getattr(               XmlDataStr.find(        '*OPER'             ), 'text', None))
            self.MesLog.ALM_STATE.append(getattr(          XmlDataStr.find(        '*ALM_STATE'        ), 'text', None))
            self.MesLog.ALM_CODE.append(getattr(           XmlDataStr.find(        '*ALM_CODE'         ), 'text', None))
            self.MesLog.ALM_TYPE.append(getattr(           XmlDataStr.find(        '*ALM_TYPE'         ), 'text', None))
            self.MesLog.ALM_TEXT.append(getattr(           XmlDataStr.find(        '*ALM_TEXT'         ), 'text', None))     
            self.MesLog.RECIPE_ID.append(getattr(          XmlDataStr.find(        '*RECIPE_ID'        ), 'text', None))     
        except Exception as e:
            print('XmlScan : ',e)
            print(RXmlData)    

    ###############################################################
    ##                          SetDataFrame                     ##
    ###############################################################
    def SetDataFrame(self):
        self.ClearMesLogDict()
        
        self.MesLog.MesLogDict['DATE']               = self.MesLog.MESDATE
        self.MesLog.MesLogDict['SENDTO']             = self.MesLog.MESSENDTO
        self.MesLog.MesLogDict['FROM_PORT']          = self.MesLog.FROM_PORT
        self.MesLog.MesLogDict['TO_PORT']            = self.MesLog.TO_PORT
        #self.MesLog.MesLogDict['MASSEGE']            = self.MesLog.MASSEGE
        self.MesLog.MesLogDict['MSG_ID']             = self.MesLog.MSG_ID
        self.MesLog.MesLogDict['MSG_LEN']            = self.MesLog.MSG_LEN
        self.MesLog.MesLogDict['SYSTEM_BYTES']       = self.MesLog.SYSTEM_BYTES
        self.MesLog.MesLogDict['EQUIP_ID']           = self.MesLog.EQUIP_ID
        self.MesLog.MesLogDict['LOT_ID']             = self.MesLog.LOT_ID
        self.MesLog.MesLogDict['TO']                 = self.MesLog.TO
        self.MesLog.MesLogDict['USER_ID']            = self.MesLog.USER_ID
        self.MesLog.MesLogDict['MDATE']              = self.MesLog.MDATE
        self.MesLog.MesLogDict['TRAY_GUBUN']         = self.MesLog.TRAY_GUBUN
        self.MesLog.MesLogDict['PORT']               = self.MesLog.PORT
        self.MesLog.MesLogDict['TRAY_COUNT']         = self.MesLog.TRAY_COUNT
        self.MesLog.MesLogDict['TRAY_POSITION']      = self.MesLog.TRAY_POSITION
        self.MesLog.MesLogDict['TRAY_ID']            = self.MesLog.TRAY_ID
        self.MesLog.MesLogDict['LINE']               = self.MesLog.LINE
        self.MesLog.MesLogDict['WORK_NO']            = self.MesLog.WORK_NO
        self.MesLog.MesLogDict['SHIP_ECS']           = self.MesLog.SHIP_ECS
        self.MesLog.MesLogDict['BATCH']              = self.MesLog.BATCH
        self.MesLog.MesLogDict['MAGAZINE_GROUP']     = self.MesLog.MAGAZINE_GROUP
        self.MesLog.MesLogDict['MAGAZINE_ADDRESS']   = self.MesLog.MAGAZINE_ADDRESS
        self.MesLog.MesLogDict['PRIORITIZE']         = self.MesLog.PRIORITIZE
        self.MesLog.MesLogDict['RETURN_VALUE']       = self.MesLog.RETURN_VALUE
        self.MesLog.MesLogDict['BANK_ALL']           = self.MesLog.BANK_ALL
        self.MesLog.MesLogDict['OPER']               = self.MesLog.OPER
        self.MesLog.MesLogDict['ALM_STATE']          = self.MesLog.ALM_STATE
        self.MesLog.MesLogDict['ALM_CODE']           = self.MesLog.ALM_CODE
        self.MesLog.MesLogDict['ALM_TYPE']           = self.MesLog.ALM_TYPE
        self.MesLog.MesLogDict['ALM_TEXT']           = self.MesLog.ALM_TEXT
        self.MesLog.MesLogDict['RECIPE_ID']          = self.MesLog.RECIPE_ID
        
        self.ClearMesLogData()

        df = DataFrame.from_dict(self.MesLog.MesLogDict,orient='index')
        df = df.transpose()
        return df


    ###############################################################
    ##                          ClearMesLogDict                  ##
    ###############################################################
    def ClearMesLogDict(self):
        self.MesLog.MesLogDict  = {'DATE':       [], 'SENDTO':       [], 'MSG_ID':       [], 'FROM_PORT':        [], 'TO_PORT':          [],  'MSG_LEN':         [], 'SYSTEM_BYTES':     [], 'EQUIP_ID':         [], 'LOT_ID':           [],  
                                'TO':          [], 'USER_ID':      [], 'PROCESS':      [], 'MDATE':            [], 'TRAY_GUBUN':       [], 'PORT':             [], 'TRAY_COUNT':       [], 'TRAY_POSITION':    [], 'TRAY_ID':          [],
                                'FROM':        [],'LINE':          [], 'WORK_NO':      [], 'SHIP_ECS':         [], 'BATCH':            [], 'MAGAZINE_GROUP':   [], 'MAGAZINE_ADDRESS': [], 'PRIORITIZE':       [], 'RETURN_VALUE':     [], 
                                'MASSEGE':     [], 'BANK_ALL':     [], 'OPER':         [], 'ALM_STATE':        [], 'ALM_CODE':         [], 'ALM_TYPE':         [], 'ALM_TEXT':         [], 'RECIPE_ID':        []}

    ###############################################################
    ##                          ClearMesLogData                  ##
    ###############################################################
    def ClearMesLogData(self):
        self.MesLog.XmlData             = []
        self.MesLog.MESSENDTO           = []
        self.MesLog.MASSEGE             = []
        self.MesLog.MESDATE             = []
        self.MesLog.MSG_ID              = []
        self.MesLog.MSG_LEN             = []
        self.MesLog.SYSTEM_BYTES        = []
        self.MesLog.EQUIP_ID            = []
        self.MesLog.LOT_ID              = []
        self.MesLog.FROM                = []
        self.MesLog.TO                  = []
        self.MesLog.USER_ID             = []
        self.MesLog.PROCESS             = []
        self.MesLog.MDATE               = []
        self.MesLog.TRAY_GUBUN          = []
        self.MesLog.PORT                = []
        self.MesLog.TRAY_COUNT          = []
        self.MesLog.TRAY_POSITION       = []
        self.MesLog.TRAY_ID             = []
        self.MesLog.LINE                = []
        self.MesLog.WORK_NO             = []
        self.MesLog.SHIP_ECS            = []
        self.MesLog.BATCH               = []
        self.MesLog.MAGAZINE_GROUP      = []
        self.MesLog.MAGAZINE_ADDRESS    = []
        self.MesLog.PRIORITIZE          = []
        self.MesLog.RETURN_VALUE        = []
        self.MesLog.FROM_PORT           = []
        self.MesLog.TO_PORT             = []
        self.MesLog.BANK_ALL            = []
        self.MesLog.OPER                = []
        self.MesLog.ALM_STATE           = []
        self.MesLog.ALM_CODE            = []
        self.MesLog.ALM_TYPE            = []
        self.MesLog.ALM_TEXT            = []
        self.MesLog.RECIPE_ID           = []

    