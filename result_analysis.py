import pandas as pd
import openpyxl

df = pd.read_excel(r"C:\Users\hplap\Downloads\FE All _ Compiled UT Marklist _ S1 _ AY  2022-23.xlsx")
data = pd.DataFrame(df)

index = pd.Index(range(10101,10176))
data = data.set_index(index)

print()
print()
print()
roll_num = int(input("ENTER YOUR ROLL NO :"))



student_result = data.loc[roll_num]

sme = student_result['SME']
phy = student_result['EP']
bee = student_result['BEE']
em_1 = student_result['EM-I']
em = student_result['EM']
total = student_result['TOTAL (150)']

SME = sme
EM1 = em_1
PHY = phy
BEE = bee
EM = em
TOTAL = total


print("_______________")
print("  !   FE DEPARTMENT STUDENT RESULT    !  ")
print("----------------------------------------- ")
print(student_result)
print()
print()
print("RESULT:")
print("-------")

if EM1 < 12 :
    print("You are failed in EM-1 subject ")

if SME < 12 :
    print("You are failed in SME subject ")

if PHY < 12 :
    print("You are failed in PHYSICS subject ")  

if BEE < 12 :
    print("You are failed in BEE subject ") 

if EM < 12:
    print("You are failed in ENGG.MECHANICS subject")


else:
    print("CONGRATULATIONS  !!!! \nYou are passed with a total of ", TOTAL)