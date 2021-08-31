import StcLogDef        as          sld    
import EcsLogDef        as          eld
from pandas import DataFrame

class GetStcLog:
    def __init__(self):
        self.StcLog = sld.StcLog()

    ###############################################################
    ##                          Convert                          ##
    ###############################################################
    def Convert(self, CurrFileName, ReadRange, Path):
        StcLogFilePath = Path + '\\' + CurrFileName
        with open('{0}'.format(StcLogFilePath),'r') as filelist :
            ssdata = filelist.readlines()
            dataS = len(ssdata) - len(ssdata) * int(ReadRange) / 100
            #print(dataS)
            ssdata = ssdata[int(dataS):] 
            #print(len(ssdata)*10/100) 
            for line in ssdata:
                if (2000 > len(line)) :
                    TrimData                        =                   line.split(", ")
                    self.StcLog.DATE.append        (                    TrimData[7]                                           )
                    self.StcLog.STC_NO.append      (                    TrimData[0]                                           )
                    self.StcLog.IO.append          (                    TrimData[1]                                           )
                    self.StcLog.JOB_TYPE.append    (                    TrimData[2]                                           )
                    self.StcLog.JOB_NO.append      (                    TrimData[4]                                           )
                    self.StcLog.STC_CURR_LOC.append(                    TrimData[5]                                           )
                    self.StcLog.JOB_INFO.append    (                    TrimData[6]                                           )
                    self.StcLog.PASSED_SEC.append  (                    TrimData[8].replace('\n','')                          )


    ###############################################################
    ##                          Convert_With_Encode              ##
    ###############################################################
    def Convert_With_Encode(self, CurrFileName, ReadRange, Path):
        StcLogFilePath = Path + '\\' + CurrFileName
        with open('{0}'.format(StcLogFilePath),'r' ,  encoding='utf-8') as filelist :
            ssdata = filelist.readlines()
            dataS = len(ssdata) - len(ssdata) * int(ReadRange) / 100
            #print(dataS)
            ssdata = ssdata[int(dataS):] 
            #print(len(ssdata)*10/100) 
            for line in ssdata:
                if (2000 > len(line)) :
                    TrimData                        =                   line.split(", ")
                    self.StcLog.DATE.append        (                    TrimData[7]                                           )
                    self.StcLog.STC_NO.append      (                    TrimData[0]                                           )
                    self.StcLog.IO.append          (                    TrimData[1]                                           )
                    self.StcLog.JOB_TYPE.append    (                    TrimData[2]                                           )
                    self.StcLog.JOB_NO.append      (                    TrimData[4]                                           )
                    self.StcLog.STC_CURR_LOC.append(                    TrimData[5]                                           )
                    self.StcLog.JOB_INFO.append    (                    TrimData[6]                                           )
                    self.StcLog.PASSED_SEC.append  (                    TrimData[8].replace('\n','')                          )

    ###############################################################
    ##                      Get_Svr_Stc_Log                  ##
    ###############################################################
    def Get_Svr_Stc_Log(self,CurrFileName,ReadRange):
        try:
            try:
                self.Convert(CurrFileName,ReadRange,eld.STC_LOG_PATH)
            except:
                self.Convert_With_Encode(CurrFileName,ReadRange,eld.STC_LOG_PATH)
                    
            return  self.Set_Data_Frame()

        except Exception as e:
            print('Get_Svr_Stc_Log : ', e)

    ###############################################################
    ##                       Get_Clt_Stc_Log                 ##
    ###############################################################
    def Get_Clt_Stc_Log(self,CurrFileName,ReadRange):
        try:
            try:
                self.Convert(CurrFileName,ReadRange,eld.CLT_STC_LOG_PATH)
            except:
                self.Convert_With_Encode(CurrFileName,ReadRange,eld.CLT_STC_LOG_PATH)
                    
            return  self.Set_Data_Frame()

        except Exception as e:
            print('GetStc_LogFile : ', e)

    ###############################################################
    ##                       Set_Data_Frame                      ##
    ###############################################################
    def Set_Data_Frame(self):
        self.Clear_Stc_Log_Dict()
        
        self.StcLog.StcLogDict['DATE']                      = self.StcLog.DATE     
        self.StcLog.StcLogDict['STC_NO']                    = self.StcLog.STC_NO        
        self.StcLog.StcLogDict['IO']                        = self.StcLog.IO            
        self.StcLog.StcLogDict['JOB_TYPE']                  = self.StcLog.JOB_TYPE     
        self.StcLog.StcLogDict['JOB_NO']                    = self.StcLog.JOB_NO        
        self.StcLog.StcLogDict['STC_CURR_LOC']              = self.StcLog.STC_CURR_LOC  
        self.StcLog.StcLogDict['JOB_INFO']                  = self.StcLog.JOB_INFO      
        self.StcLog.StcLogDict['PASSED_SEC']                = self.StcLog.PASSED_SEC    

        
        self.Clear_Stc_Log_Data()

        df = DataFrame.from_dict(self.StcLog.StcLogDict,orient='index')
        df = df.transpose()
        return df

    ###############################################################
    ##                       Clear_Stc_Log_Dict              ##
    ###############################################################
    def Clear_Stc_Log_Dict(self):
        self.StcLog.StcLogDict         = {'DATE':       [], 'STC_NO':     [],'IO':     [], 'JOB_TYPE':     [], 'JOB_NO':     [], 'STC_CURR_LOC':     [], 'JOB_INFO':     [], 'PASSED_SEC': []}

    ###############################################################
    ##                       Clear_Stc_Log_Data              ##
    ###############################################################
    def Clear_Stc_Log_Data(self):
        self.StcLog.DATE            = []
        self.StcLog.STC_NO          = []
        self.StcLog.IO              = []
        self.StcLog.JOB_TYPE        = []
        self.StcLog.JOB_NO          = []
        self.StcLog.STC_CURR_LOC    = []
        self.StcLog.JOB_INFO        = []
        self.StcLog.PASSED_SEC      = []




