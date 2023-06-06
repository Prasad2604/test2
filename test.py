from tabulate import tabulate
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

df1 = pd.read_excel(r"C:\Users\hplap\Downloads\FE All _ Compiled UT Marklist _ S1 _ AY  2022-23.xlsx",sheet_name=11)
#df = pd.read_excel(r"C:\Users\hplap\Downloads\FE All _ Compiled UT Marklist _ S1 _ AY  2022-23.xlsx")
data = pd.DataFrame(df1)
#print(data)

#index = pd.Index(range(1, 824))
data = data.set_index('ROLL NO.')
# maxValues = data.max(skipna=False)
# print(maxValues)


print()
print()
# n = int(input("Enter the no of students you wanna access data for??"))
print()
roll_num = int(input("Enter your roll no : "))


subjects = ['SME', 'EP', 'BEE', 'EM-I', 'EM']


student_result = data.loc[roll_num]


sme = student_result['SME']
phy = student_result['EP']
bee = student_result['BEE']
em_1 = student_result['EM-I']
em = student_result['EM']
total = student_result['TOTAL']

SME = sme
EM1 = em_1
PHY = phy
BEE = bee
EM = em
TOTAL = total
# print(data)
sr = pd.DataFrame(student_result)
# data.groupby('BEE')['ROLL NO.'].nunique().plot(kind='bar')
# plt.show
print()
print("-----------------------------------------")
print("  !   FE DEPARTMENT STUDENT RESULT    !  ")
print("----------------------------------------- ")
print(tabulate(sr, headers='keys', tablefmt='fancy_grid'))
print()
print()
print("RESULT:")
print("-------")

m = [SME, EM1, PHY, BEE, EM]
for i in range(5):
    if m[i] < 12:
        print("Fail")
        break
else:
    # print(TOTAL)
    print("Congratulations !!!")
    print("You are passed with a total of ", TOTAL)

    
    '''print()
print('-----------------------------------------------------')
print('MAXIMUM RESULT :-')
print('-----------------------------------------------------')
max_result = data.loc[10807]
mr = pd.DataFrame(max_result)
print(tabulate(mr, headers='keys', tablefmt='fancy_grid'))
print()
print('-----------------------------------------------------')'''
