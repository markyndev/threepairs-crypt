from datetime import datetime
nom = datetime.now()
print("   ████████ ██████   ██████ ")
print("      ██    ██   ██ ██      ")
print("      ██    ██████  ██      ")
print("      ██    ██      ██      ")
print("      ██    ██       ██████ ")
print("")
alvo  = input("Decode$ ")

keyA = alvo.replace("222!", "A");
keyB = keyA.replace("422@", "B");
keyC = keyB.replace("822#", "C");
keyD = keyC.replace("162$", "D");
keyE = keyD.replace("322%", "E");
keyF = keyE.replace("642^", "F");
keyG = keyF.replace("128&", "G");
keyH = keyG.replace("256*", "H");
keyI = keyH.replace("512(", "I");
keyJ = keyI.replace("102)", "J");
keyK = keyJ.replace("204-", "K");
keyL = keyK.replace("404_", "L");
keyM = keyL.replace("814+", "M");
keyN = keyM.replace("162=", "N");
keyO = keyN.replace("326|", "O");
keyP = keyO.replace("654[", "P");
keyQ = keyP.replace("132]", "Q");
keyR = keyQ.replace("262{", "R");
keyS = keyR.replace("524}", "S");
keyT = keyS.replace("104;", "T");
keyU = keyT.replace("202:", "U");
keyV = keyU.replace("412<", "V");
keyW = keyV.replace("838>", "W");
keyX = keyW.replace("162.", "X");
keyY = keyX.replace("332,", "Y");
keyZ = keyY.replace("674?", "Z");
keySPC = keyZ.replace("984~", " ");

fln = keySPC
print("")
print("==============================RESULT=================================")
print("")
print(keySPC)
print("")
print("=====================================================================")
