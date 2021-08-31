import BarLogDef as     bld    
import EcsLogDef as     eld
from  pandas import DataFrame

class GetBarLog:
    def __init__(self):
        self.BarLog = bld.BarLog()

    ###############################################################
    ##                          Convert                          ##
    ###############################################################
    def Convert(self, CurrFileName, ReadRange, Path):
        BarLogFilePath = Path + '\\' + CurrFileName
        with open('{0}'.format(BarLogFilePath),'r') as filelist :
            ssdata = filelist.readlines()
            dataS = len(ssdata) - len(ssdata) * int(ReadRange) / 100
            #print(dataS)
            ssdata = ssdata[int(dataS):] 
            #print(len(ssdata)*10/100) 
            for line in ssdata:
                if (2000 > len(line)) :
                    TrimData                        =                  line.split(",",3)
                    self.BarLog.DATE.append        (                    TrimData[0]                )
                    self.BarLog.PORT.append        (                    TrimData[1]                )
                    self.BarLog.TRAY_ID.append     (                    TrimData[2]                )


    ###############################################################
    ##                          Convert_With_Encode              ##
    ###############################################################
    def Convert_With_Encode(self, CurrFileName, ReadRange, Path):
        BarLogFilePath = Path + '\\' + CurrFileName
        with open('{0}'.format(BarLogFilePath),'r' ,  encoding='utf-8') as filelist :
            ssdata = filelist.readlines()
            dataS = len(ssdata) - len(ssdata) * int(ReadRange) / 100
            #print(dataS)
            ssdata = ssdata[int(dataS):] 
            #print(len(ssdata)*10/100) 
            for line in ssdata:
                if (2000 > len(line)) :
                    TrimData                         =                  line.split(",",3)
                    self.BarLog.DATE.append        (                    TrimData[0]                )
                    self.BarLog.PORT.append        (                    TrimData[1]                )
                    self.BarLog.TRAY_ID.append     (                    TrimData[2]                )
    
    ###############################################################
    ##                      Get_Svr_Bar_Log                      ##
    ###############################################################
    def Get_Svr_Bar_Log(self,CurrFileName,ReadRange):
        try:
            try:
                self.Convert(CurrFileName,ReadRange,eld.BCR_LOG_PATH)
            except:
                self.Convert_With_Encode(CurrFileName,ReadRange,eld.BCR_LOG_PATH)
                    
            return  self.Set_Data_Frame()

        except Exception as e:
            print('Get_Svr_Bar_Log : ', e)

    ###############################################################
    ##                       Get_Clt_Bar_Log                     ##
    ###############################################################
    def Get_Clt_Bar_Log(self,CurrFileName,ReadRange):
        try:
            try:
                self.Convert(CurrFileName,ReadRange,eld.CLT_BCR_LOG_PATH)
            except:
                self.Convert_With_Encode(CurrFileName,ReadRange,eld.CLT_BCR_LOG_PATH)
                    
            return  self.Set_Data_Frame()

        except Exception as e:
            print('GetBCRLogFile : ', e)

    ###############################################################
    ##                       Set_Data_Frame                      ##
    ###############################################################
    def Set_Data_Frame(self):
        self.Clear_Bar_Log_Dict()
        
        self.BarLog.BarLogDict['DATE']                  = self.BarLog.DATE     
        self.BarLog.BarLogDict['PORT']                  = self.BarLog.PORT     
        self.BarLog.BarLogDict['TRAY_ID']                  = self.BarLog.TRAY_ID     

  
        
        self.Clear_Bar_Log_Data()

        df = DataFrame.from_dict(self.BarLog.BarLogDict,orient='index')
        df = df.transpose()
        return df

    ###############################################################
    ##                       Clear_Bar_Log_Dict                  ##
    ###############################################################
    def Clear_Bar_Log_Dict(self):
        self.BarLog.BarLogDict         = {'DATE':       [], 'PORT':       [], 'TRAY_ID':     [] }

    ###############################################################
    ##                       Clear_Bar_Log_Data                  ##
    ###############################################################
    def Clear_Bar_Log_Data(self):
        self.BarLog.DATE        = []
        self.BarLog.PORT        = []
        self.BarLog.TRAY_ID     = []
