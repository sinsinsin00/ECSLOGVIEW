
from dataclasses import dataclass

MASTER_COMPUTER_IP             = '192.168.0.193'
#MASTER_COMPUTER_IP             = '127.0.0.1'
#MASTER_COMPUTER_IP             = '192.168.0.55'
MASTER_SLAVE                   = '' 
ECS_LOG_DIR                    = ''

CLT_MES_LOG_PATH               = ''
CLT_CNV_LOG_PATH               = ''
CLT_BCR_LOG_PATH               = ''
CLT_BCR_NOREAD_PATH            = ''
CLT_STC_LOG_PATH               = ''
CLT_JOB_LOG_PATH               = ''

MES_LOG_PATH                   = ''
CNV_LOG_PATH                   = ''
BCR_LOG_PATH                   = ''
BCR_NOREAD_PATH                = ''
STC_LOG_PATH                   = ''
JOB_LOG_PATH                   = ''

MES_LOG_LIST                   = ''
CNV_LOG_LIST                   = ''
BCR_LOG_LIST                   = ''
BCR_NOREAD_LOG_LIST            = ''
STC_LOG_LIST                   = ''
JOB_LOG_LIST                   = ''

RCP_TITLE_M          = 'ECSLOGCHK-Svr'
RCP_TITLE_C          = 'ECSLOGCHK-Clt'

FR_SVR_MES_LOG_FILE_LIST = []
FR_SVR_CNV_LOG_FILE_LIST = []
FR_SVR_BCR_LOG_FILE_LIST = []
FR_SVR_BCR_NO_READ_LOG_FILE_LIST = []
FR_SVR_STC_LOG_FILE_LIST = []
FR_SVR_JOB_LOG_FILE_LIST = []

@dataclass
class EcsC:
    Used                = 0
    CommSts             = 0 
    RxEnd               = 0
    CtlPhase            = 0
    CurrScr             = 0
    Data_Transfered     = 0
    Data_MaxLength      = 0
    ChoiseCurrentItem   = ''