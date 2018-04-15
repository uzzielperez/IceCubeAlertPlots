import re
#AMONfile = '17569642_130214.amon'

def purge(dict_):
     # Delete unecessary entries
     del dict_['TITLE']
     del dict_['NOTICE_TYPE']
     del dict_['DISCOVERY_DATE']
     del dict_['DISCOVERY_TIME']
     del dict_['REVISION']
     del dict_['STREAM']
     del dict_['COMMENTS']
    
     return dict_ 

def strSepPurge(text, sep):
    # https://stackoverflow.com/questions/904746/how-to-remove-all-characters-after-a-specific-character-in-python
    head, sep, tail = text.partition(sep)
    return head 

def loadAMON(filename):
    num_dict = {} # dictionary for plotting purposes
    data_dict = {} # full dictionary for relevant variables
    
    with open(filename,'r+') as f:
        for line in f:
            newstring = line
            if ":" in line:
               # Line is a var/value field
                var, value = map(str.strip, line.split(":", 1))
                data_dict[var] = value  #data_dict.update({var,value})             
            if "SRC_RA" in line: 
                src_ra, ra = map(str.strip, line.split(":",1))
                RAhi = f.next().strip()
                data_dict["SRC_RAhi"] = RAhi
                RAlo = f.next().strip()
                data_dict["SRC_RAlo"] = RAlo  
            if "SRC_DEC" in line: 
                src_dec, dec = map(str.strip, line.split(":",1))
                Dechi = f.next().strip()
                data_dict["SRC_DEChi"] = Dechi
                Declo = f.next().strip()
                data_dict["SRC_DEClo"] = Declo

    # Clean dictionary
    num_dict = data_dict
    purge(num_dict)
   
    # Note: Python Strings are immutable
    for key in num_dict:
        e = num_dict[key]
        newstring = e
        # print key, e
        if 'd' in e:
            newstring = re.sub("d* ", "",newstring)
        if "+" in e:
            newstring = newstring[1:]
        newstring = strSepPurge(newstring, '{')
        newstring = strSepPurge(newstring, '[')
        num_dict[key] = newstring
        print (key, newstring) # for debugging

    RASC, DRAHI, DRALO = float(num_dict['SRC_RA']), float(num_dict['SRC_RAhi']), float(num_dict['SRC_RAlo'])
    DEC, DDECHI, DDECLO = float(num_dict['SRC_DEC']), float(num_dict['SRC_DEChi']), float(num_dict['SRC_DEClo'])
    EVNUM, RUN = num_dict['EVENT_NUM'], num_dict['RUN_NUM']
    BOX = None

    return RASC, DRAHI, DRALO, DEC, DDECHI, DDECLO, BOX, EVNUM, RUN 

#print (loadAMON(AMONfile))
