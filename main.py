from turtle import *
import box
import letterA
import letterB
import letterC
import letterD
import letterE
import letterF
import letterG
import letterH
import letterI
import letterJ
import letterK
import letterL
import letterM
import letterN
import letterO
import letterP
import letterQ
import letterR
import letterS
import letterT
import letterU
import letterV
import letterW
# import letterX
# import letterY
# import letterZ



val = list(input("Enter Your Name : "))
name = {
    "a":letterA.letter1,
    "b":letterB.letter2,
    "c":letterC.letter3,
    "d":letterD.letter4,
    "e":letterE.letter5,
    "f":letterF.letter6,
    "g":letterG.letter7,
    "h":letterH.letter8,
    "i":letterI.letter9,
    "j":letterJ.letter10,
    "k":letterK.letter11,
    "l":letterL.letter12,
    "m":letterM.letter13,
    "n":letterN.letter14,
    "o":letterO.letter15,
    "p":letterP.letter16,
    "q":letterQ.letter17,
    "r":letterR.letter18,
    "s":letterS.letter19,
    "t":letterT.letter20,
    "u":letterU.letter21,
    "v":letterV.letter22,
    "w":letterW.letter23,
    # "x":letterX.letter24,
    # "y":letterY.letter25,
    # "z":letterZ.letter26,


}



speed(2)
pensize(20)
bgcolor('black')
color('green')
penup()
right(180)
forward(300)
right(180)


count=0
for num in val:
    try:
        count=count+1
        name.get(num)()
    except TypeError:
        print("invalid input")

box.box(count)

done()