import math

work = True

def gainQU():

    gender = input("Firstly are you a Male or Female?(male/female)\n")
    if gender.lower().strip() == "male":
        print("Thank you sir. Now lets calculate your Lean Bulk Calories.")
    elif gender.lower().strip() == "female":
        print("Thank you madam. Now lets Calcualate your Lean Bulk.")
    else:
        gender = input("\nYou might have miss typed somethign try again.\n")
    print("\nFirst off we need to calcualte your Basal Metabolic Rate(BMR). Your BMR is your rate of energy intake you need to maintain your body weight.")
    x = float(input("\n\nHow much do you weigh?(lbs)\n") )
    y = float(contKG(x))
    z = float(input("\n\nHow Tall are you?(inches)\n") )
    z = float(contCM(z))
    u = float(input("\n\nWhat is your age?\n") )
    a = 0
    actLevel = int(input("\n\nOn a scale of 1-5, How active are you?\n1- little to no exercise\n2- light exercise/sorts 1-3 days/week\n3-Moderatly active 3-5 days a week.\n4-Very active 6-7 days a week.\n5-Extra Active\n"))
    if actLevel == 1:
        a = 1.15
    elif actLevel == 2:
        a = 1.35
    elif actLevel == 3:
        a = 1.55
    elif actLevel == 4:
        a = 1.725
    elif actLevel == 5:
        a = 1.9
    bmr = float(calcBMR(gender, y, z, u,a))
    bmr = round(bmr, 3)
    bmr = bmr + 250
    print("Your BMR is:")
    print(float(bmr))
    print("That's great!!\nNow we can begin to calculate your Macro for Weight gain/muscle building.\n")
    protein = calcPR(x)
    fat = calcFT(bmr)
    carbs = calcCB(bmr,protein,fat)
    print("For your MACROS you should be eating: \n")
    convtG(protein, fat, carbs)
    return bmr

def contKG(y):
    y = float(y * .453592)
    return y

def contCM(z):
    z = float(z * 2.54)
    return z

def calcBMR(gender,y,z,u,a):
    if gender.lower().strip() == "male":
        BMR = float( 5 + (10 * y) + (6.25 * z) - (5 * u))
        BMR = float(BMR * a)
        return BMR
    elif gender.lower().strip() == "female":
        BMR = float((10 * y) + (6.25 * z) - (5 * u) - 161)
        BMR = float(BMR * a)
        return BMR

def calcPR(x):
    x = x * 4
    return x

def calcFT(bmr):
    bmr = float(bmr * .20)
    bmr = round(bmr, 3)
    return bmr

def calcCB(bmr,protein,fat):
    i = float(protein + fat)
    carbs = float(bmr - i)
    return i

def convtG(x,y,z):
    x = float(x/4)
    x = round(x,2)
    print("Protein(grams)")
    print(float(x))
    y = float(y/9)
    y = round(y,2)
    print("Fat(grams)")
    print(float(y))
    z = float(z/4)
    z = round(z,2)
    print("Carbohydrates(grams)")
    print(float(z))
    return 0

print("Hello!!\nThis is a Dietary calculator for those looking to gain Muscle/Weight")
cont = input("\nWould you like to calculate a Dietary plan?(yes)\n")

if cont.lower().strip() == "yes":

    print("\n\nGreat\n\n\nWelcome to the Diet Planner 2700. My mission is to help you build diet/workout plan to reach your goal!!\n\nFirst let's find out what you want to do.")
    while work == True:
            type = input("\nWould you like to lose or gain weight.(Type gain or lose)\n")
            if type.lower().strip() == "gain":
                print("\n\nFantastic!! Lets get Started!!\n\nFor gaining weight we're going to use a method called Lean Bulking.\n\nLean Bulking is Different than the typically Bulking.")
                x1 = input("Bulking is usually when someone eats a huge amounts of carboydrates and fats and could put on a ton of Body fat.\nLean Bulking Diet Focuses more on Carbohydrates and Fats\nIt also Focuses more on Eating as much calories as you burn that Day.\n(Type anything to Continue)")
                print("Say you Burn 2000 calories a day just as an Example and burn 500 when you work out. In order to Lean Bulk you want to eat 2500 Calories of food in order to make up for the calories burnt and rebuild muscle.")
                print("Lean bulking is Desgiend to Eat more Protein and Whole grains to Build muscle slowly over time than what the interent calls a Dirty Bulk.")
                calculations = float(gainQU())
                work = False
            elif type.lower().strip() == "lose":
                print("y")
                work = False
            else:
                    print("\nYou might have miss typed somethign try again.\n")
    else:
        print("\nTerminating Program")
