from datetime import datetime
nom = datetime.now()
hour = int(nom.strftime("%H"))
alvo  = str(input("[Encode]: "))
keyA = alvo.upper().replace("A", "222!");
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

