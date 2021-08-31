from dataclasses import dataclass

@dataclass
class MesLog:
    MesLogDict         = {'DATE':       [], 'SENDTO':       [], 'MSG_ID':       [], 'FROM_PORT':        [], 'TO_PORT':          [],  'MSG_LEN':         [], 'SYSTEM_BYTES':     [], 'EQUIP_ID':         [], 'LOT_ID':           [],  
                         'TO':          [], 'USER_ID':      [], 'PROCESS':      [], 'MDATE':            [], 'TRAY_GUBUN':       [], 'PORT':             [], 'TRAY_COUNT':       [], 'TRAY_POSITION':    [], 'TRAY_ID':          [],
                         'FROM':        [],'LINE':          [], 'WORK_NO':      [], 'SHIP_ECS':         [], 'BATCH':            [], 'MAGAZINE_GROUP':   [], 'MAGAZINE_ADDRESS': [], 'PRIORITIZE':       [], 'RETURN_VALUE':     [], 
                         'MASSEGE':     [], 'BANK_ALL':     [], 'OPER':         [], 'ALM_STATE':        [], 'ALM_CODE':         [], 'ALM_TYPE':         [], 'ALM_TEXT':         [], 'RECIPE_ID':        []}


    XmlData                       = []
    MESSENDTO                     = []
    MASSEGE                       = []
    MESDATE                       = []
    MSG_ID                        = []
    MSG_LEN                       = []
    SYSTEM_BYTES                  = []
    EQUIP_ID                      = []
    LOT_ID                        = []
    FROM                          = []
    TO                            = []
    USER_ID                       = []
    PROCESS                       = []
    MDATE                         = []
    TRAY_GUBUN                    = []
    PORT                          = []
    TRAY_COUNT                    = []
    TRAY_POSITION                 = []
    TRAY_ID                       = []
    LINE                          = []
    WORK_NO                       = []
    SHIP_ECS                      = []
    BATCH                         = []
    MAGAZINE_GROUP                = []
    MAGAZINE_ADDRESS              = []
    PRIORITIZE                    = []
    RETURN_VALUE                  = []
    FROM_PORT                     = []
    TO_PORT                       = []
    BANK_ALL                      = []
    OPER                          = []
    ALM_STATE                     = []
    ALM_CODE                      = []
    ALM_TYPE                      = []
    ALM_TEXT                      = []
    RECIPE_ID                     = []

