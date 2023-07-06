# coding: utf-8
#
#
#
import json
import glob
import re
motif = re.compile(r"{{[^}]+}}")

#
# constitution en RAM du dictionaire
#
with open("suomi-français.json","r") as g:
    _ = g.read()
    d = json.loads(_)    
    g.close()


def traduitFichier(ndf):
    compt = 0
    with open(ndf,"r") as f:
        s = f.read()
        t = s 
        it = motif.finditer(s)
        i = 0
        for m in it:
            i +=1
            mc = m.group()[2:-2] # retrait des {{ }}
            if mc in d.keys():
                if d[mc] != None:
                    t = motif.sub(d[mc],t , 1) #[:m.start()] + d[mc] + t[m.end():] 
                    compt += 1
            else:
                d[mc] = None
                print(f"Manque traduction de {mc}.")
        f.close()
    ndftxt = ndf.removesuffix(".template") + ".txt"
    if i>0:
        print(f"{ndftxt}: {compt/i*100}% ")
    else:
        print(f"{ndftxt}: 0% ")
    with open(ndftxt,"w") as g:
        g.write(t)
        g.close()

for ndf in glob.glob("**.template"):
    traduitFichier(ndf)

print("Dictionnaire mis à jour :")
print(d)
with open("suomi-français.json","w") as h:
    h.write(json.dumps(d))
    h.close()
