import BarNoReadDef as     bnd    
import EcsLogDef as     eld
from pandas import DataFrame

class GetBarNoRead:
    def __init__(self):
        self.BarNoRead = bnd.BarNoRead()

    ###############################################################
    ##                          Convert                          ##
    ###############################################################
    def Convert(self, CurrFileName, ReadRange, Path):
        BarNoReadFilePath = Path + '\\' + CurrFileName
        with open('{0}'.format(BarNoReadFilePath),'r') as filelist :
            ssdata = filelist.readlines()
            dataS = len(ssdata) - len(ssdata) * int(ReadRange) / 100
            #print(dataS)
            ssdata = ssdata[int(dataS):] 
            #print(len(ssdata)*10/100) 
            for line in ssdata:
                if (2000 > len(line)) :
                    TrimData                        =                  line.split(",",2)
                    self.BarNoRead.DATE.append        (                    TrimData[0].replace('"','')                )
                    self.BarNoRead.PORT.append        (                    TrimData[2].replace('\n','').replace('"','')                )


    ###############################################################
    ##                          Convert_With_Encode              ##
    ###############################################################
    def Convert_With_Encode(self, CurrFileName, ReadRange, Path):
        BarNoReadFilePath = Path + '\\' + CurrFileName
        with open('{0}'.format(BarNoReadFilePath),'r' ,  encoding='utf-8') as filelist :
            ssdata = filelist.readlines()
            dataS = len(ssdata) - len(ssdata) * int(ReadRange) / 100
            #print(dataS)
            ssdata = ssdata[int(dataS):] 
            #print(len(ssdata)*10/100) 
            for line in ssdata:
                if (2000 > len(line)) :
                    TrimData                         =                  line.split(",",2)
                    self.BarNoRead.DATE.append        (                    TrimData[0]                )
                    self.BarNoRead.PORT.append        (                    TrimData[2].replace('\n','')                    )

    ###############################################################
    ##                      Get_Svr_Bar_No_Read                  ##
    ###############################################################
    def Get_Svr_Bar_No_Read(self,CurrFileName,ReadRange):
        try:
            try:
                self.Convert(CurrFileName,ReadRange,eld.BCR_NOREAD_PATH)
            except:
                self.Convert_With_Encode(CurrFileName,ReadRange,eld.BCR_NOREAD_PATH)
                    
            return  self.Set_Data_Frame()

        except Exception as e:
            print('Get_Svr_Bar_No_Read : ', e)

    ###############################################################
    ##                       Get_Clt_Bar_No_Read                 ##
    ###############################################################
    def Get_Clt_Bar_No_Read(self,CurrFileName,ReadRange):
        try:
            try:
                self.Convert(CurrFileName,ReadRange,eld.CLT_BCR_NOREAD_PATH)
            except:
                self.Convert_With_Encode(CurrFileName,ReadRange,eld.CLT_BCR_NOREAD_PATH)
                    
            return  self.Set_Data_Frame()

        except Exception as e:
            print('GetBCRLogFile : ', e)

    ###############################################################
    ##                       Set_Data_Frame                      ##
    ###############################################################
    def Set_Data_Frame(self):
        self.Clear_Bar_No_Read_Dict()
        
        self.BarNoRead.BarNoReadDict['DATE']                  = self.BarNoRead.DATE     
        self.BarNoRead.BarNoReadDict['PORT']                  = self.BarNoRead.PORT     


  
        
        self.Clear_Bar_No_Read_Data()

        df = DataFrame.from_dict(self.BarNoRead.BarNoReadDict,orient='index')
        df = df.transpose()
        return df

    ###############################################################
    ##                       Clear_Bar_No_Read_Dict              ##
    ###############################################################
    def Clear_Bar_No_Read_Dict(self):
        self.BarNoRead.BarNoReadDict         = {'DATE':       [], 'PORT':       []}

    ###############################################################
    ##                       Clear_Bar_No_Read_Data              ##
    ###############################################################
    def Clear_Bar_No_Read_Data(self):
        self.BarNoRead.DATE        = []
        self.BarNoRead.PORT        = []

