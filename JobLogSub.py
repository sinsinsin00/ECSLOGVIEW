import JobLogDef       as          sld    
import EcsLogDef       as          eld
from pandas import DataFrame

class GetJobLog:
    def __init__(self):
        self.JobLog = sld.JobLog()

    ###############################################################
    ##                          Convert                          ##
    ###############################################################
    def Convert(self, CurrFileName, ReadRange, Path):
        JobLogFilePath = Path + '\\' + CurrFileName
        with open('{0}'.format(JobLogFilePath),'r') as filelist :
            ssdata = filelist.readlines()
            dataS = len(ssdata) - len(ssdata) * int(ReadRange) / 100
            #print(dataS)
            ssdata = ssdata[int(dataS):] 
            #print(len(ssdata)*10/100) 

            TrimCurrFileName = CurrFileName.split('.')
            if TrimCurrFileName[0] == 'JOBLOG':
                for line in ssdata:
                    if (2000 > len(line)) :
                        TrimData                            =                      line.replace("       ",'  ').replace("    ","  ")
                        TrimData                            =                      TrimData.split("  ")
                        self.JobLog.DATE     .append        (                      TrimData[0]                                           )
                        self.JobLog.JOB_TYPE .append        (                      TrimData[1]                                           )
                        self.JobLog.JOB_NO   .append        (                      TrimData[2]                                           )
                        self.JobLog.SRC      .append        (                      TrimData[3]                                           )   
                        self.JobLog.DST      .append        (                      TrimData[4]                                           )
                        self.JobLog.MCH      .append        (                      TrimData[5]                                           )   
                        self.JobLog.SITES    .append        (                      TrimData[6]                                           )
                        self.JobLog.SITED    .append        (                      TrimData[7]                                           )
                        self.JobLog.SITEC    .append        (                      TrimData[8].replace('\n','')                          )
            else: 
                for line in ssdata:
                    if (2000 > len(line)) : 
                        TrimData                        =                     line.split("  ")
                        self.JobLog.DATE     .append        (                      TrimData[0]                                           )
                        self.JobLog.PGM      .append        (                      TrimData[1]                                           )
                        self.JobLog.CODE     .append        (                      TrimData[6]                                           )
                        self.JobLog.JOB_NO   .append        (                      TrimData[7]                                           )
                        self.JobLog.SRC      .append        (                      TrimData[8]                                           )   
                        self.JobLog.DST      .append        (                      TrimData[9]                                           )
                        self.JobLog.MCH      .append        (                      TrimData[10]                                          )
                        self.JobLog.SITES    .append        (                      TrimData[11]                                          )
                        self.JobLog.SITED    .append        (                      TrimData[12]                                          )
                        self.JobLog.SITEC    .append        (                      TrimData[13]                                          )


    ###############################################################
    ##                          Convert_With_Encode              ##
    ###############################################################
    def Convert_With_Encode(self, CurrFileName, ReadRange, Path):
        JobLogFilePath = Path + '\\' + CurrFileName
        with open('{0}'.format(JobLogFilePath),'r' ,  encoding='utf-8') as filelist :
            ssdata = filelist.readlines()
            dataS = len(ssdata) - len(ssdata) * int(ReadRange) / 100
            #print(dataS)
            ssdata = ssdata[int(dataS):] 
            #print(len(ssdata)*10/100) 

            TrimCurrFileName = CurrFileName.split('.')
            if TrimCurrFileName[0] == 'JOBLOG':
                for line in ssdata:
                    if (2000 > len(line)) :
                        TrimData                            =                      line.replace("       ",'  ').replace("    ","  ")
                        TrimData                            =                      TrimData.split("  ")
                        self.JobLog.DATE     .append        (                      TrimData[0]                                           )
                        self.JobLog.JOB_TYPE .append        (                      TrimData[1]                                           )
                        self.JobLog.JOB_NO   .append        (                      TrimData[2]                                           )
                        self.JobLog.SRC      .append        (                      TrimData[3]                                           )   
                        self.JobLog.DST      .append        (                      TrimData[4]                                           )
                        self.JobLog.MCH      .append        (                      TrimData[5]                                           )   
                        self.JobLog.SITES    .append        (                      TrimData[6]                                           )
                        self.JobLog.SITED    .append        (                      TrimData[7]                                           )
                        self.JobLog.SITEC    .append        (                      TrimData[8].replace('\n','')                          )
            else: 
                for line in ssdata:
                    if (2000 > len(line)) : 
                        TrimData                            =                      line.split("  ")
                        self.JobLog.DATE     .append        (                      TrimData[0]                                           )
                        self.JobLog.PGM      .append        (                      TrimData[1]                                           )
                        self.JobLog.CODE     .append        (                      TrimData[6]                                           )
                        self.JobLog.JOB_NO   .append        (                      TrimData[7]                                           )
                        self.JobLog.SRC      .append        (                      TrimData[8]                                           )   
                        self.JobLog.DST      .append        (                      TrimData[9]                                           )
                        self.JobLog.MCH      .append        (                      TrimData[10]                                          )
                        self.JobLog.SITES    .append        (                      TrimData[11]                                          )
                        self.JobLog.SITED    .append        (                      TrimData[12]                                          )
                        self.JobLog.SITEC    .append        (                      TrimData[13].replace('\n','')                         )

    ###############################################################
    ##                      Get_Svr_Job_Log                  ##
    ###############################################################
    def Get_Svr_Job_Log(self, CurrFileName, ReadRange):
        try:
            try:
                self.Convert(CurrFileName,ReadRange,eld.JOB_LOG_PATH)
            except:
                self.Convert_With_Encode(CurrFileName,ReadRange,eld.JOB_LOG_PATH)
                return  self.Set_Data_Frame()
                    
            return  self.Set_Data_Frame(CurrFileName)

        except Exception as e:
            print('Get_Svr_Job_Log : ', e)

    ###############################################################
    ##                       Get_Clt_Job_Log                 ##
    ###############################################################
    def Get_Clt_Job_Log(self, CurrFileName, ReadRange):
        try:
            try:
                self.Convert(CurrFileName,ReadRange,eld.CLT_JOB_LOG_PATH)
            except:
                self.Convert_With_Encode(CurrFileName,ReadRange,eld.CLT_JOB_LOG_PATH)
                    
            return  self.Set_Data_Frame(CurrFileName)

        except Exception as e:
            print('GetStc_LogFile : ', e)

    ###############################################################
    ##                       Set_Data_Frame                      ##
    ###############################################################
    def Set_Data_Frame(self, CurrFileName):
        self.Clear_Job_Log_Dict()

        TrimCurrFileName = CurrFileName.split('.')
        if TrimCurrFileName[0] == 'JOBLOG':
            self.JobLog.JobLogDict['DATE']                          = self.JobLog.DATE     
            self.JobLog.JobLogDict['JOB_TYPE']                      = self.JobLog.JOB_TYPE       
            self.JobLog.JobLogDict['JOB_NO']                        = self.JobLog.JOB_NO            
            self.JobLog.JobLogDict['SRC']                           = self.JobLog.SRC   
            self.JobLog.JobLogDict['DST']                           = self.JobLog.DST       
            self.JobLog.JobLogDict['MCH']                           = self.JobLog.MCH  
            self.JobLog.JobLogDict['SITES']                         = self.JobLog.SITES     
            self.JobLog.JobLogDict['SITED']                         = self.JobLog.SITED   
            self.JobLog.JobLogDict['SITEC']                         = self.JobLog.SITEC   

            df = DataFrame.from_dict(self.JobLog.JobLogDict,orient='index')
            df = df.transpose()
        else:
            self.JobLog.JobLogDelDict['DATE']                          = self.JobLog.DATE     
            self.JobLog.JobLogDelDict['PGM']                           = self.JobLog.PGM       
            self.JobLog.JobLogDelDict['CODE']                          = self.JobLog.CODE
            self.JobLog.JobLogDelDict['JOB_NO']                        = self.JobLog.JOB_NO               
            self.JobLog.JobLogDelDict['SRC']                           = self.JobLog.SRC   
            self.JobLog.JobLogDelDict['DST']                           = self.JobLog.DST       
            self.JobLog.JobLogDelDict['MCH']                           = self.JobLog.MCH  
            self.JobLog.JobLogDelDict['SITES']                         = self.JobLog.SITES     
            self.JobLog.JobLogDelDict['SITED']                         = self.JobLog.SITED   
            self.JobLog.JobLogDelDict['SITEC']                         = self.JobLog.SITEC   
            
            df = DataFrame.from_dict(self.JobLog.JobLogDelDict,orient='index')
            df = df.transpose()



        self.Clear_Job_Log_Data()


        return df

    ###############################################################
    ##                       Clear_Job_Log_Dict                  ##
    ###############################################################
    def Clear_Job_Log_Dict(self):
        self.JobLog.JobLogDict         = {'DATE':       [], 'JOB_TYPE':     [],'JOB_NO':     [], 'SRC':     [], 'DST':     [], 'MCH':     [], 'SITES':     [], 'SITED': [], 'SITEC': []}
        self.JobLog.JobLogDelDict      = {'DATE':       [], 'PGM':     [],'CODE':     [], 'JOB_NO':     [], 'SRC':     [], 'DST':     [], 'MCH':     [], 'SITES': [], 'SITED': [], 'SITEC': []}

    ###############################################################
    ##                       Clear_Job_Log_Data                  ##
    ###############################################################
    def Clear_Job_Log_Data(self):
        self.JobLog.DATE            =       []
        self.JobLog.JOB_TYPE        =       []
        self.JobLog.JOB_NO          =       []
        self.JobLog.SRC             =       []
        self.JobLog.DST             =       []
        self.JobLog.MCH             =       []
        self.JobLog.SITES           =       []
        self.JobLog.SITED           =       []
        self.JobLog.SITEC           =       []
        self.JobLog.PGM             =       []
        self.JobLog.CODE            =       []   


