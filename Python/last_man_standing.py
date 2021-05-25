#Substitute two equal letters by the next letter of the alphabet (two letters convert to one): The equal letters do not have to be adjacent.
#Repeat this operation until there are no possible substitutions left.
#Return a string.


alph={"aa":"b",
"bb":"c",
"cc":"d",
"dd":"e",
"ee":"f",
"ff":"g",
"gg":"h",
 "hh":"i",
 "ii":"j",
 "jj":"k",
 "kk":"l",
 "mm":"n",
 "nn":"o",
 "oo":"p",
 "pp":"q",
 "qq":"r",
 "rr":"s",
 "ss":"t",
 "tt":"u",
 "uu":"v",
 "vv":"w",
 "ww":"x",
 "xx":"y",
 "yy":"z",
 "zz":"a"}

def last_survivors(string):
    pair=""
    
    for i in range(len(string)-1):
        if string[i]==string[i+1]:
           pair=string[i]+string[i+1]
           string.replace((pair),alph[pair])
           return last_survivors(string.replace((pair),alph[pair]))
    print(string)
              


last_survivors("uussggug")
