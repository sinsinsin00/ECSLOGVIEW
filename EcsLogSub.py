from os import path as ospath , makedirs, listdir
import EcsLogDef as eld

def MkDirEcsLog(DirEcsLog):
    try:
        if not ospath.exists(DirEcsLog):
            makedirs(DirEcsLog)
    except Exception as e:
        print('MkDir : ',e)

def InitialRoutine():
    eld.ECS_LOG_DIR                 = ospath.dirname(ospath.abspath(__file__))

    eld.CLT_MES_LOG_PATH        =   r'{0}\EcsLog\Mes'.format(eld.ECS_LOG_DIR)
    eld.CLT_CNV_LOG_PATH        =   r'{0}\EcsLog\Cnv'.format(eld.ECS_LOG_DIR)
    eld.CLT_BCR_LOG_PATH        =   r'{0}\EcsLog\Bar'.format(eld.ECS_LOG_DIR)
    eld.CLT_BCR_NOREAD_PATH     =   r'{0}\EcsLog\NoRead'.format(eld.ECS_LOG_DIR)
    eld.CLT_STC_LOG_PATH        =   r'{0}\EcsLog\Stc'.format(eld.ECS_LOG_DIR)
    eld.CLT_JOB_LOG_PATH        =   r'{0}\EcsLog'.format(eld.ECS_LOG_DIR)

    eld.MES_LOG_PATH            =   r'D:\EcsLog\Mes'
    eld.CNV_LOG_PATH            =   r'D:\EcsLog\Cnv'      
    eld.BCR_LOG_PATH            =   r'D:\EcsLog\Bar'       
    eld.BCR_NOREAD_PATH         =   r'D:\EcsLog\NoRead'       
    eld.STC_LOG_PATH            =   r'D:\EcsLog\Stc'      
    eld.JOB_LOG_PATH            =   r'D:\EcsLog'

    eld.JOB_LOG_LIST                = [f for f in listdir(eld.JOB_LOG_PATH) if ospath.isfile(ospath.join(eld.JOB_LOG_PATH,f))]
    eld.MES_LOG_LIST                = listdir(eld.MES_LOG_PATH)
    eld.CNV_LOG_LIST                = listdir(eld.CNV_LOG_PATH)
    eld.BCR_LOG_LIST                = listdir(eld.BCR_LOG_PATH)
    eld.STC_LOG_LIST                = listdir(eld.STC_LOG_PATH)
    eld.BCR_NOREAD_LOG_LIST         = listdir(eld.BCR_NOREAD_PATH)
   
    MkDirEcsLog(eld.CLT_MES_LOG_PATH)
    MkDirEcsLog(eld.CLT_CNV_LOG_PATH)
    MkDirEcsLog(eld.CLT_BCR_LOG_PATH)
    MkDirEcsLog(eld.CLT_STC_LOG_PATH)
    MkDirEcsLog(eld.CLT_BCR_NOREAD_PATH)


    
if __name__ == '__main__':
    InitialRoutine()
    # print(   eld.ECS_LOG_DIR                   )
    # print(   eld.JOB_LOG_LIST                  )
    # print(   eld.MES_LOG_LIST                  )
    # print(   eld.CNV_LOG_LIST                  )
    # print(   eld.BCR_LOG_LIST                  )
    # print(   eld.STC_LOG_LIST                  )
    # print(   eld.BCR_NOREAD_LOG_LIST           )
    