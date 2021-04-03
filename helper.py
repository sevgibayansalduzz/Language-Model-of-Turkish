"""
This hecele method is taken from here: https://github.com/monder0116/NLP-Works/blob/master/work1/hecele.py
"""
import sys
import re

def hecele(x):
    isPython2 = False;
    if sys.version_info[0] < 3:
        isPython2 = True
    i = 0
    vw = "aeıioöuü"
    cn = "bcçdfgğhjklmnprsştvyz"
    if isPython2:
        vw = vw.decode("utf-8")
        cn = cn.decode("utf-8")
    while i < len(x):
        if x[i] in vw:
            if i + 1 < len(x) and x[i+1] in vw:
                return x[0:i+1] + " " + hecele(x[i+1:len(x)])
            elif i + 2 < len(x) and x[i+2] in vw:
                return x[0:i+1] + " " + hecele(x[i+1:len(x)])
            elif i + 3 == len(x) and x[i+1] in cn and x[i+2] in cn:
                return x[0:i+3] + " " + hecele(x[i+3:len(x)])
            elif i + 3 < len(x) and x[i+3] in vw:
                return x[0:i+2] + " " + hecele(x[i+2:len(x)])
            elif i+3 < len(x) and x[i+1] in cn and x[i+2] in cn and x[i+3] in cn:
                return x[0:i+3] + " " + hecele(x[i+3:len(x)])
            elif i + 3 < len(x) and x[i:i+3] == 'str' or 'ktr' or 'ntr':
                return x[0:i+2] + " " + hecele(x[i+2:len(x)])
            else:
                return x[0:i+3] + " " + hecele(x[i+3:len(x)])
        i += 1

    return x

def text_to_syllable(context):
    verbs=context
    verbs=verbs.split(' ')
    hece_arr=[]
    count=0
    for i in verbs:
        heceli=str(hecele(i))
        for t in heceli.split(" "):
            if t!='':
                hece_arr.append(t)
                count+=1
        if i!="":
            hece_arr.append(" ")
            count+=1
    if(len(hece_arr)!=0):
        hece_arr.pop()
    return hece_arr

def check_corpus(context):
    valid_harf=["a","b","c","ç", "d", "e" ,"f" ,"g", "ğ" ,"h" ,"ı" ,"i" ,"j" ,"k", "l"
    ,"m" ,"n" ,"o", "ö", "p" ,"r" ,"s" ,"ş" ,"t" ,"u" ,"ü", "v" ,"y" ,"z"," "]
    ncontext=""
    for i in range(len(context)):
        if context[i] in valid_harf:
            ncontext+=context[i]
        else:
            ncontext+=" "
    return ncontext

def lower(context):
    tr_Bharf={"Ö":"ö", "Ü":"ü","İ":"i","Ş":"ş","Ç":"ç","I":"ı"}
    ncontext=""
    for i in range(len(context)):
        if context[i] in tr_Bharf:
            ncontext+=tr_Bharf[context[i]]
        else:
            ncontext+=context[i].lower()
    return  ncontext
