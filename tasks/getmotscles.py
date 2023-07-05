# coding: utf-8
#
#
#
import json
import glob
import re
motif = re.compile(r"{[^}]+}")

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
        for m in it:
            mc = m.group()[1:-1]
            if mc in d.keys():
                if d[mc] != None:
                    print(f"{mc}->{d[mc]}")
                    t = motif.sub(d[mc],t , 1) #[:m.start()] + d[mc] + t[m.end():] 
                    compt += 1
                else: # semble que jamais atteint
                    print(mc, d[mc])
            else:
                d[mc] = None
                print(f"Manque traduction de {mc}.")
        f.close()
    ndftxt = ndf.removesuffix(".template") + ".txt"
    print(f"{ndftxt}: {compt} subs.")
    with open(ndftxt,"w") as g:
        g.write(t)
        g.close()

for ndf in glob.glob("task*.template"):
    traduitFichier(ndf)


k = input("Ok pour écraser le dictionnaire ?")
print(d)
if k in ["o", "O"]:
    with open("suomi-français.json","w") as h:
        h.write(json.dumps(d))
        h.close()

# tout  ça à reprendre ainsi:
# pour chaque fichier template: 
#     pour chaque MC trouvé dans ce fichier: 
#         si la traduction existe, remplacer dasn le fichier txt.
#          si la l'entrée existe mais pas la trduction
#            le signaler
#          si l'entrée n'existe pas
#            la créer avec None dasn le dictionnaire  

          
