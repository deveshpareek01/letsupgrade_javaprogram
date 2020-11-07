#problem 1
print("guess correct word of OBANWRI\nA. RANIBOW\nB. RAINBOW\nC. BOWRANI\nD. ROBWANI")
e=input("")
if(e=='A'or e=='C' or e=='D'):
    print("worng choice")
elif(e=='B'):
    print('right choice')


#problem 2:
str="lets upgrade"
print(str.upper())


#problem 3:
Cost_prize=int(input(""))
Sell_prize=int(input(""))
if(Cost_prize>Sell_prize):
    print("Loss")
elif(Cost_prize<Sell_prize):
    print("Profit")
else:
    print("Neither")


#problem 4
euro=int(input(""))
indian=euro*80
print(indian)