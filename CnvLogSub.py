import CnvLogDef as     cld    
import EcsLogDef as     eld
from pandas import DataFrame

class GetCnvLog:
    def __init__(self):
        self.CnvLog = cld.CnvLog()

    ###############################################################
    ##                          Convert                          ##
    ###############################################################
    def Convert(self, CurrFileName, ReadRange, Path):
        CnvLogFilePath = Path + '\\' + CurrFileName
        with open('{0}'.format(CnvLogFilePath),'r') as filelist :
            ssdata = filelist.readlines()
            dataS = len(ssdata) - len(ssdata) * int(ReadRange) / 100
            #print(dataS)
            ssdata = ssdata[int(dataS):] 
            #print(len(ssdata)*10/100) 
            for line in ssdata:
                if (2000 > len(line)) :
                    TrimData                         =       line.split(",",4)
                    TrimPassedTime                   =       TrimData[2].split(':')

                    self.CnvLog.ERRORDATE.append(            TrimData[0]                )
                    self.CnvLog.DATE.append     (            TrimData[1]                )
                    self.CnvLog.PASSEDMM.append (            TrimPassedTime[0]          )
                    self.CnvLog.PASSEDSS.append (            TrimPassedTime[1]          )
                    self.CnvLog.SITE.append     (            TrimData[3]                )


    ###############################################################
    ##                          Convert_With_Encode              ##
    ###############################################################
    def Convert_With_Encode(self, CurrFileName, ReadRange, Path):
        CnvLogFilePath = Path + '\\' + CurrFileName
        with open('{0}'.format(CnvLogFilePath),'r' ,  encoding='utf-8') as filelist :
            ssdata = filelist.readlines()
            dataS = len(ssdata) - len(ssdata) * int(ReadRange) / 100
            #print(dataS)
            ssdata = ssdata[int(dataS):] 
            #print(len(ssdata)*10/100) 
            for line in ssdata:
                if (2000 > len(line)) :
                    TrimData                         =       line.split(",",4)
                    TrimPassedTime                   =       TrimData[2].split(':')

                    self.CnvLog.ERRORDATE.append(            TrimData[0]                )
                    self.CnvLog.DATE.append     (            TrimData[1]                )
                    self.CnvLog.PASSEDMM.append (            TrimPassedTime[0]          )
                    self.CnvLog.PASSEDSS.append (            TrimPassedTime[1]          )
                    self.CnvLog.SITE.append     (            TrimData[3]                )
    
    ###############################################################
    ##                      Get_Svr_Cnv_Log                      ##
    ###############################################################
    def Get_Svr_Cnv_Log(self,CurrFileName,ReadRange):
        try:
            try:
                self.Convert(CurrFileName,ReadRange,eld.CNV_LOG_PATH)
            except:
                self.Convert_With_Encode(CurrFileName,ReadRange,eld.CNV_LOG_PATH)
                    
            return  self.Set_Data_Frame()

        except Exception as e:
            print('Get_Svr_Cnv_Log : ', e)

    ###############################################################
    ##                       Get_Clt_Cnv_Log                     ##
    ###############################################################
    def Get_Clt_Cnv_Log(self,CurrFileName,ReadRange):
        try:
            try:
                self.Convert(CurrFileName,ReadRange,eld.CLT_CNV_LOG_PATH)
            except:
                self.Convert_With_Encode(CurrFileName,ReadRange,eld.CLT_MES_LOG_PATH)
                    
            return  self.Set_Data_Frame()

        except Exception as e:
            print('GetMesLogFile : ', e)

    ###############################################################
    ##                       Set_Data_Frame                      ##
    ###############################################################
    def Set_Data_Frame(self):
        self.Clear_Cnv_Log_Dict()
        
        self.CnvLog.CnvLogDict['ERRORDATE']             = self.CnvLog.ERRORDATE
        self.CnvLog.CnvLogDict['DATE']                  = self.CnvLog.DATE     
        self.CnvLog.CnvLogDict['PASSEDMM']              = self.CnvLog.PASSEDMM 
        self.CnvLog.CnvLogDict['PASSEDSS']              = self.CnvLog.PASSEDSS 
        self.CnvLog.CnvLogDict['SITE']                  = self.CnvLog.SITE     
  
        
        self.Clear_Cnv_Log_Data()

        df = DataFrame.from_dict(self.CnvLog.CnvLogDict,orient='index')
        df = df.transpose()
        return df

    def Clear_Cnv_Log_Dict(self):
        self.CnvLog.CnvLogDict         = {'ERRORDATE':       [], 'DATE':       [], 'PASSEDMM':     [], 'PASSEDSS':     [], 'SITE':    [] }

    def Clear_Cnv_Log_Data(self):
        self.CnvLog.ERRORDATE           = []
        self.CnvLog.DATE                = []
        self.CnvLog.PASSEDMM            = []
        self.CnvLog.PASSEDSS            = []
        self.CnvLog.SITE                = []