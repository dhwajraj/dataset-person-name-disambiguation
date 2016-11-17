def cleanRes(str):
    a = str.split("resource/")
    if len(a)<2:
        return ""
    name = a[1]
    name =name.split("(")[0]
    return name.replace("_"," ").replace(">","").strip()

def printIR(fullname, disamb):
    lab="n"
    print fullname+"\t"+fullname+"\t"+lab
    exp = fullname.split()
    lname = exp[-1]
    if fullname!=disamb:
        if lname!=disamb and exp[0]!=disamb:
            lab="y"
    print fullname+"\t"+disamb+"\t"+lab

lineDict=dict()
for line in open('disambiguations_en.ttl'):
    line = line.strip()
    l = line.split(" ")
    if len(l)>=3:
        lineDict[l[2]]=line
uniquePersonNames = set()
for line in open('persondata_en.nt'):
    line = line.strip()
    key = line.split()[0]
    uniquePersonNames.add(key)

for key in uniquePersonNames:
    if key in lineDict:
        cand = lineDict[key]
        arr=cand.split()
        printIR(cleanRes(arr[2]),cleanRes(arr[0]))

for line in open('DBLP10k.csv'):
    l = line.strip().split(';')
    lab="n"
    if l[0]=="t":
        if l[1]=="f":
            lab="y"
        print l[2]+"\t"+l[3]+"\t"+lab
