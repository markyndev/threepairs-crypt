from datetime import datetime
nom = datetime.now()
hour = int(nom.strftime("%H"))
print("")
print("_____________________________")
print("|                           |")
print("| 1.         CODER          |")
print("| 2.         DECODER        |")
print("| 3.         INFO           |")
print("| 4.         QUIT           |")
print("|                           |")
print("─────────────────────────────")
print("")
alvo  = int(input("[CHOOSE]: "))
if alvo == 1:
 print("")
 print("")
 txt  = str(input("[ENCODE]: ")).upper()
 keyA = txt.replace("A", "222!");
 keyB = keyA.replace("B", "422@");
 keyC = keyB.replace("C", "822#");
 keyD = keyC.replace("D", "162$");
 keyE = keyD.replace("E", "322%"); 
 keyF = keyE.replace("F", "642^");  
 keyG = keyF.replace("G", "128&"); 
 keyH = keyG.replace("H", "256*");
 keyI = keyH.replace("I", "512(");
 keyJ = keyI.replace("J", "102)");
 keyK = keyJ.replace("K", "204-");
 keyL = keyK.replace("L", "404_");
 keyM = keyL.replace("M", "814+");
 keyN = keyM.replace("N", "162=");
 keyO = keyN.replace("O", "326|");
 keyP = keyO.replace("P", "654[");
 keyQ = keyP.replace("Q", "132]");
 keyR = keyQ.replace("R", "262{");
 keyS = keyR.replace("S", "524}");
 keyT = keyS.replace("T", "104;");
 keyU = keyT.replace("U", "202:");
 keyV = keyU.replace("V", "412<");
 keyW = keyV.replace("W", "838>");
 keyX = keyW.replace("X", "162.");
 keyY = keyX.replace("Y", "332,");
 keyZ = keyY.replace("Z", "674?");
 keySPC = keyZ.replace(" ", "984~");
 print("")
 print("==============================RESULT=================================")
 print("")
 print(keySPC)
 print("")
 print("=====================================================================")
elif alvo == 2:
 print("")
 print("")
 decodl  = input("[Decode]: ")
  
 dcdA = decodl.replace("222!", "A");
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
 print(dcdSPC.lower())
 print("")
 print("=====================================================================")

elif alvo == 3:
 print("")
 print("ThreePair`s Encoder/Decoder")
 print("Project: https://github.com/markyndev/threepairs-crypt/")
 print("")
elif alvo == 4:
 quit()
