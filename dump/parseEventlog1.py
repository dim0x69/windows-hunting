#!/usr/bin/python

import csv
from collections import defaultdict

aclList = {}
with open("processaccessed.csv") as csvf:
    d = csv.reader(csvf)
    for row in d:
        eventdata = row[-1]
        eventdataLines = eventdata.splitlines()
        acl = None
        sourceimage = None
        for l in eventdataLines:
            if "SourceImage" in l:
                sourceimagel = l.split()[1:]
                sourceimage = "".join(sourceimagel)
            if "GrantedAccess" in l:
                acl = l.split()[1]
        if acl == None: continue
        if acl in aclList and sourceimage in aclList[acl]:
            aclList[acl][sourceimage] += 1
        else:
            if acl not in aclList:
                aclList[acl] = {}
            aclList[acl][sourceimage] = 1


for acl in aclList.keys():
    for sourceimage in aclList[acl].keys():
        print(acl + ","  + sourceimage + "," + str(aclList[acl][sourceimage]))
