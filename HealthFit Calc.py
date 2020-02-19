'''''''''''''''''''''''
Python Package Imports
'''''''''''''''''''''''
import math
from getpass import getuser

'''''''''''''''''''''
User Input
'''''''''''''''''''''
pcnam = getuser()
print('\n# Welcome # To * HealthFit Calculator *\n\nSystem Name Detected : '+pcnam)
print("\nKindly Note : \n1. If Out of Range Values are Submitted then You will be Asked to Enter Them Again")
print("2. If Wrong Values are Submitted then the Program will Exit and You Have to Re-Run it Again")
print("\nYour Name : ", end = '')
urnam=input()

try:
	aej = 0
	while not int(aej) in range(1,121):
		aej = input("Age : ")
	gndr = 1001
	while not int(gndr) in range(0,2):
		gndr = input("Gender : Enter 1 if Male or 0 if Female : ")
	staps = 222222
	while not int(staps) in range(0,30000):
		staps = input("Steps Walked throughout the Day : ")
	hait = 0
	while not int(hait) in range(1,200):
		hait = input("Height (in cm): ")
	weit = 0
	while not int(weit) in range(1,300):
		weit = input("Weight (in kg): ")
except:
	print("Wrong Values Entered! Kindly Re-run the Program and Enter Proper Values")
	exit()

'''''''''''''''''
Dictionaries
'''''''''''''''''
bmidict = { "<16" : "Severe Thinness",
        "16-17" : "Moderate Thinness",
        "17-18.5" : "Mild Thinness",
        "18.5-25" : "Normal",
        "25-30" : "Overweight",
        "30-35" : "Obese Class I",
        "35-40" : "Obese Class II",
        ">40" : "Obese Class III"
}

"""""""""""""""
Py Mains
"""""""""""""""
cm2m=int(hait)/100
print('Your Height in m is : ',cm2m, end='')
cm2ftin=round(float(hait)/30.48,3)
cm2indec, cm2ft = math.modf(cm2ftin)
cm2in=cm2indec*12
cm2in3=round(float(cm2in),3)
print('\nYour Height in Feet/Inches is : ',cm2ft,'Feet',cm2in3,'Inches', end='')

bmi=round(int(weit)/(cm2m*cm2m),1)
if bmi<16:
	bmiresult = bmidict["<16"]
elif bmi>=16 and bmi<17:
	bmiresult = bmidict["16-17"]
elif bmi>=17 and bmi<18.5:
	bmiresult = bmidict["17-18.5"]
elif bmi>=18.5 and bmi<25:
	bmiresult = bmidict["18.5-25"]
elif bmi>=25 and bmi<30:
	bmiresult = bmidict["25-30"]
elif bmi>=25 and bmi<35:
	bmiresult = bmidict["30-35"]
elif bmi>=25 and bmi<40:
	bmiresult = bmidict["35-40"]
else:
	bmiresult = bmidict[">40"]
print('\nBMI : ', bmi, 'kg/m\N{SUPERSCRIPT TWO}','(',bmiresult,')', end='')
if gndr=='1':
	caco=5
	iws=52.0
	hmw=1.9
elif gndr=='0':
	caco=161
	iws=45.5
	hmw=2.2
bmrf = 10*float(weit) + 6.25*float(hait) - 5*float(aej) + float(caco)
print('\nBMR Note : You Can Consume',bmrf,'Calories in a Day to Maintain Your Body Weight', end='')
idwt = round(float(iws) + float(hmw)*float(cm2in3),1)
print('\nYour Ideal Weight is : ', idwt, 'Kgs', end='')
print('\nDistance Walked : ', round(int(staps)/1400,1), 'Km', end='')
print('\nCalories Burned : ', round(int(staps)*0.04,1), 'Calories', end='')
