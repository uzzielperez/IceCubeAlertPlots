import fnmatch
AMONfile = '17569642_130214.amon'


def purge(dict_):
    for key, value in dict_.iteritems():
        #if "" in key: # remove key-val pair from the dictionary
        #del dict_['STREAM']
        del dict_['TITLE']
        del dict_['NOTICE_TYPE']
        del dict_['DISCOVERY_DATE']
        del dict_['DISCOVERY_TIME']
        del dict_['REVISION']
        del dict_['STREAM']
        del dict_['COMMENTS']

       # replace unwanted characters]
        v = dict_.values() # for python3 list(dict_.values()) 
        for e in v:
            if "d" in e: 
                e.replace("d", "")
            if "+" in e:
                e.replace("+", "") 
            remove_this_string = fnmatch.filter(v,' {+*')  
            remove_this_string2 = fnmatch.filter(v, '[*]')
            remove_this_string3 = fnmatch.filter(v, 'galactic*') 
            remove_this_string4 = fnmatch.filter(v, 'ecliptic*')
 #            if remove_this_string[0] in e:
 #                e.replace(remove_this_string[0], "")
 #            if remove_this_string2[0] in e:
 #                e.replace(remove_this_string2[0], "")
 #            if remove_this_string3[0] in e:
 #                e.replace(remove_this_string3[0], "")
 #            if remove_this_string4[0] in e:
 #                e.replace(remove_this_string4[0], "")
        print remove_this_string
        print remove_this_string2
        print remove_this_string3
        print remove_this_string4
        return dict_ 
    
def loadAMON(filename):
    num_dict = {} # dictionary for plotting purposes
    data_dict = {} # full dictionary for relevant variables
    with open(filename,'r') as f:
        for line in f:
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
    purge(data_dict)
    return data_dict, num_dict 

print loadAMON(AMONfile)
