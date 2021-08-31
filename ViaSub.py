import EcsLogDef as eld

###############################################################
##                          GET                              ##
###############################################################
def GetMasterSlave():
    return eld.MASTER_SLAVE

def GetMasterIp():
    return eld.MASTER_COMPUTER_IP

def GetMesLogList():
    return eld.MES_LOG_LIST

def GetCnvLogList():
    return eld.CNV_LOG_LIST

def GetBcrLogList():
    return eld.BCR_LOG_LIST

def GetBcrNoReadLogList():
    return eld.BCR_NOREAD_LOG_LIST

def GetStcLogList():
    return eld.STC_LOG_LIST

def GetJobLogList():
    return eld.JOB_LOG_LIST

def GetFrSvrMesLogFileList():
    return eld.FR_SVR_MES_LOG_FILE_LIST

def GetFrSvrCnvLogFileList():
    return eld.FR_SVR_CNV_LOG_FILE_LIST

def GetFrSvrBcrLogFileList():
    return eld.FR_SVR_BCR_LOG_FILE_LIST

def GetFrSvrBcrNoReadLogFileList():
    return eld.FR_SVR_BCR_NO_READ_LOG_FILE_LIST

def GetFrSvrStcLogFileList():
    return eld.FR_SVR_STC_LOG_FILE_LIST

def GetFrSvrJobLogFileList():
    return eld.FR_SVR_JOB_LOG_FILE_LIST
    

###############################################################
##                          SET                              ##
###############################################################
def SetFrSvrMesLogList(MESLOG):
    eld.FR_SVR_MES_LOG_FILE_LIST = MESLOG

def SetFrSvrCnvLogList(CNVLOG):
    eld.FR_SVR_CNV_LOG_FILE_LIST = CNVLOG

def SetFrSvrBcrLogList(BCRLOG):
    eld.FR_SVR_BCR_LOG_FILE_LIST = BCRLOG

def SetFrSvrBcrNoReadLogList(BCRNOREADLOG):
    eld.FR_SVR_BCR_NO_READ_LOG_FILE_LIST = BCRNOREADLOG

def SetFrSvrStcLogList(STCLOG):
    eld.FR_SVR_STC_LOG_FILE_LIST = STCLOG

def SetFrSvrJobLogList(JOBLOG):
    eld.FR_SVR_JOB_LOG_FILE_LIST = JOBLOG


###############################################################
##                          Clear                            ##
###############################################################

def Clear():
    eld.EcsC.CtlPhase = 99
    eld.EcsC.Used = 0