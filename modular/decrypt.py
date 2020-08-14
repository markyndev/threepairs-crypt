from datetime import datetime
import sys
nom = datetime.now()

alvo  = str(input("[Decoder]: "))
dcdA = alvo.upper().replace("222!", "A");
dcdB = dcdA.replace("422@", "B");
dcdC = dcdB.replace("822#", "C");
dcdD = dcdC.replace("162$", "D");
dcdE = dcdD.replace("322%", "E");
dcdF = dcdE.replace("642^", "F");
dcdG = dcdF.replace("128&", "G");
dcdH = dcdG.replace("256*", "H");
dcdI = dcdH.replace("512(", "I");
dcdJ = dcdI.replace("102)", "J");
dcdK = dcdJ.replace("204-", "K");
dcdL = dcdK.replace("404_", "L");
dcdM = dcdL.replace("814+", "M");
dcdN = dcdM.replace("162=", "N");
dcdO = dcdN.replace("326|", "O");
dcdP = dcdO.replace("654[", "P");
dcdQ = dcdP.replace("132]", "Q");
dcdR = dcdQ.replace("262{", "R");
dcdS = dcdR.replace("524}", "S");
dcdT = dcdS.replace("104;", "T");
dcdU = dcdT.replace("202:", "U");
dcdV = dcdU.replace("412<", "V");
dcdW = dcdV.replace("838>", "W");
dcdX = dcdW.replace("162.", "X");
dcdY = dcdX.replace("332,", "Y");
dcdZ = dcdY.replace("674?", "Z");
dcdSPC = dcdZ.replace("984~", " ");

fln = dcdSPC
print("")
print("==============================RESULT=================================")
print("")
print(dcdSPC)
print("")
print("=====================================================================")
