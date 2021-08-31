from dataclasses import dataclass

@dataclass
class JobLog:
    JobLogDict         = {'DATE':       [], 'JOB_TYPE':     [],'JOB_NO':     [], 'SRC':     [], 'DST':     [], 'MCH':     [], 'SITES':     [], 'SITED': [], 'SITEC': []}
    JobLogDelDict      = {'DATE':       [], 'PGM':     [],'CODE':     [], 'JOB_NO':     [], 'SRC':     [], 'DST':     [], 'MCH':     [], 'SITES': [], 'SITED': [], 'SITEC': []}

    DATE            =       []
    JOB_TYPE        =       []
    JOB_NO          =       []
    SRC             =       []
    DST             =       []
    MCH             =       []
    SITES           =       []
    SITED           =       []
    SITEC           =       []
    PGM             =       []
    CODE            =       []   


