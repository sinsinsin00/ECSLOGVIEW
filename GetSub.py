    ###############################################################
    ##                          WDataSeparator                   ##
    ###############################################################
def WDataSeparator(CommandCode,Data):
    Result =[]
    CommandType = type(CommandCode)

    if CommandType == str:
        Result.append(CommandCode)
    elif CommandType == list:
        Result.append(CommandCode[0])
        
    Result.append(Data)

    return Result

    ###############################################################
    ##                          RDataSeparator                   ##
    ###############################################################
def RDataSeparator(Rbuff):
    if type(Rbuff) == bytes:
        Rbuff = Rbuff.decode()
    try:
        Rbuff = eval(Rbuff)
    except:
        print("RDataSeparator : eval Error")
        return '0'
    Result = []
    RbuffType = type(Rbuff)

    if RbuffType == str:
        RbuffLen = len(Rbuff)
        if RbuffLen > 2:
            Result.append(Rbuff[:2])
            Result.append(Rbuff[2:])
        else:
            Result.append(Rbuff[:2])

    elif RbuffType == list:
        RbuffLen = len(Rbuff)
        if RbuffLen >= 2:
            Result = Rbuff[:1]
            Result.append(Rbuff[1:2])
            Result.append(Rbuff[2:3])
            Result.append(Rbuff[3:4])
        else:
            Result = Rbuff[:1]

    elif RbuffType == int:
        Result.append(str(Rbuff))

    return Result
