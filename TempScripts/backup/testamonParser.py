import os 
import fnmatch
text = 'this is text'
os.system("echo %s | grep 't*' >> file.txt" %text)

AMONfile = '17569642_130214.amon'

def loadAMON(filename):
    plot_dict = {}
    data_dict = {}
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
   # get dictionary list of values for cleaning 
    v = data_dict.values() #list(data_dict.values())
    cleaned = fnmatch.filter(v,'+' )
    return data_dict, plot_dict 

print loadAMON(AMONfile)
