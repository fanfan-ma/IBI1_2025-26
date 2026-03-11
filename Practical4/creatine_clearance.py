# firstly give out the input prompts
# prove the input, if right, go ahead to calculation. If not, print something as a reminder
# calculate CrCl accroding to the gender, you can write it into two formulas respectively
# estimate which input is wrong and give the relevant reminder, you can use the "not"
# if user gives illegal value, print a reminder
while True: # make sure that only the legal value could continue to the next step
    try:
        age = int(input("Please enter your age in years: ")) # remember to change the data type so that you could calculate later!
        weight = float(input("Please enter your weight in kg: "))
        Cr = float(input("Please enter your creatine concentration in µmol/l:"))
        break
    except:
        print("Please enter a valid number for age, weight and creatine concentration") # to give the warning if user enters illegal value
gender = input("Please enter your gender as male/female: ")
if age < 100 and 20 < weight < 80 and 0 < Cr < 100 and gender in ("male","female"): # checkout the input. Remember that the string need to be enclosed in auotation marks!
    if gender == "male":
        CrCl = (140 - age) * weight / 72 / Cr
    if gender == "female":
        CrCl = (140 - age) * weight / 72 / Cr * 0.85
    print("Your rate of creatine filtration is" , CrCl)
if not age < 100:
    print("Please enter your correct age")
if not 20 < weight < 80:
    print("Please enter your correct weight")
if not gender in ("male","female"):
    print("Please enter your correct gender")
if not 0 < Cr < 100:
    print("Please enter your correct creatine concentration")
