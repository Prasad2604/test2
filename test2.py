# Importing required libraries
from tabulate import tabulate
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
print()
print()
print()

print("""This is a PBL Project of Group No. 3.

We have written a code for result analysis of FE department UT marks of SEM-I

Choices : - 

    1. Choose 1 if you want the data of whole division, along with the topper of that particular division
    2. Choose 2 if you want the data of particular student""")
print()
print()
while (True):

    print()
    print()
    r = int(input("Enter Your Choice :- "))
    if r == 1:
        i = int(input("Enter Division :- FE"))
        df1 = pd.read_excel(
            r"C:\Users\hplap\Downloads\FE All _ Compiled UT Marklist _ S1 _ AY  2022-23.xlsx", sheet_name=i-1)
        # df = pd.read_excel(r"C:\Users\hplap\Downloads\FE All _ Compiled UT Marklist _ S1 _ AY  2022-23.xlsx")
        data = pd.DataFrame(df1)
        print(tabulate(data, headers='keys', tablefmt='fancy_grid'))
        print()
        print(f"Topper of FE{i} is :- ")
        print()
        maxmarks = data['TOTAL'].max()
        # print(maxmarks)
        student_result = data.loc[data['TOTAL'] == maxmarks]
        bhari = pd.DataFrame(student_result)
        print(tabulate(bhari, headers='keys', tablefmt='fancy_grid'))
    elif r == 2:
        roll = input("Enter roll no of student :- ")
        div = int(roll[1:3])
        if div < 7:
            df1 = pd.read_excel(
                r"C:\Users\hplap\Downloads\FE All _ Compiled UT Marklist _ S1 _ AY  2022-23.xlsx", sheet_name=11)
            data = pd.DataFrame(df1)
            data = data.set_index('ROLL NO.')
            subjects = ['SME', 'EP', 'BEE', 'EM-I', 'EM']
            student_result = data.loc[int(roll)]

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
            sr = pd.DataFrame(student_result)
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
        else:
            df1 = pd.read_excel(
                r"C:\Users\hplap\Downloads\FE All _ Compiled UT Marklist _ S1 _ AY  2022-23.xlsx", sheet_name=12)
            data = pd.DataFrame(df1)
            data = data.set_index('ROLL NO.')
            subjects = ['SME', 'EC', 'BXE', 'EM-I', 'PPS']
            student_result = data.loc[int(roll)]

            sme = student_result['SME']
            chem = student_result['EC']
            bxe = student_result['BXE']
            em_1 = student_result['EM-I']
            pps = student_result['PPS']
            total = student_result['TOTAL']

            SME = sme
            EM1 = em_1
            CHEM = chem
            BXE = bxe
            PPS = pps
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

            m = [SME, EM1, CHEM, BXE, PPS]
            for i in range(5):
                if m[i] < 12:
                    print("Fail")
                    break
            else:
                # print(TOTAL)
                print("Congratulations !!!")
                print("You are passed with a total of ", TOTAL)
    else:
        print("YED ZAVA AHESH K RE TU JARA >>>>> ZETYA VARCHA JARA VACH NA......TONDALA HATH LAVYCHA KHADBADA VATTYE NA......LAVDYA SHETYA UPTYA...")

    '''data = pd.DataFrame(df1)
    specific_roll = data.loc[data['ROLL NO.']==int(roll)]
    print(specific_roll)
    maxmarks = data['TOTAL'].max()
    print(maxmarks)
    student_result = data.loc[data['TOTAL']==maxmarks]
    print(student_result)'''
