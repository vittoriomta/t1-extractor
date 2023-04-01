
import os
import pandas as pd
import pdfplumber
import re

def extract(dir):

    dir = 'upload'
        

    Digit = [].append
    Mrn = [].append
    Weight = [].append
    Seal = [].append
    Cargo = [].append
    Count = 0
    rows = []
    Filename = [].append


    for file in os.listdir(dir):
            if not file.endswith(".pdf"):
                continue
            with open(os.path.join(dir,file), 'rb') as pdfFileObj:

                pdf = pdfplumber.open(pdfFileObj)
                for page in pdf.pages:
                    total_pages = len(pdf.pages)
                    #salta i pdf scannerizzati
                    i = pdf.pages[0]
                    if not i.extract_text():
                        pass


                    if total_pages <= 2:

                        #PAGE 1
                        try:
                            Filename = file
                            f_p = pdf.pages[0]
                            text = f_p.extract_text()
                            Digit = (text.split('\n')[23].split()[1])
                            Mrn = (text.split('\n')[4].split()[6])
                            if Mrn == "Dich.sic.(S00)":
                                Mrn = (text.split('\n')[4].split()[7])
                            Weight = (text.split('\n')[9].split()[2])
                        except (IndexError):
                            pass
                        else:
                            pass
                        #PAGE2
                        s_p = pdf.pages[1]
                        text = s_p.extract_text()
                        try:
                            Seal = (text.split('\n')[12].split()[:5]) #da pulire  
                        except (IndexError):
                            pass
                        # if  Seal[2] == '---':
                        #     Seal = (text.split('\n')[12].split()[:5])
                            
                        # else:
                        #     pass
                        try:    
                            Cargo = (text.split('\n')[12].split()[7:])
                        except (IndexError):
                            pass
                        try: 
                            if  Digit == '.':
                                Digit = (text.split('\n')[14])
                            else:
                                pass
                        except (IndexError):
                            pass
                        try:
                            if  len(Digit) != 11:
                                Digit = (text.split('\n')[15])
                        except (IndexError):
                            pass
                        try:
                            if  len(Digit) != 11:
                                Digit = (text.split('\n')[16])
                        except (IndexError):
                            pass
                        try:
                            Cargo2 = (text.split('\n')[18].split()[8:])
                            CL_Cargo2 = listToString(Cargo2)
                            Cargo.append(CL_Cargo2)
                        except (IndexError):
                            pass
                        try:
                            Cargo3 = (text.split('\n')[24].split()[8:])
                            CL_Cargo3 = listToString(Cargo3)
                            Cargo.append(CL_Cargo3)
                        except (IndexError):
                            pass

                        # if Cargo == None:
                        #     try:
                        #         Cargo_3 = (text.split('\n')[12])
                        #         CL_Cargo_3 = str(Cargo_3)
                        #         Cargo.append(CL_Cargo_3)
                        #     except (IndexError):
                        #         pass
                        # else:
                        #     pass

                    elif total_pages <= 7:
                        #PAGE 3
                        try:
                            t_p = pdf.pages[2]
                            text = t_p.extract_text()
                        except (IndexError):
                            pass
                        try:
                            Cargo4 = (text.split('\n')[12].split()[8:])
                            CL_Cargo4 = listToString(Cargo4)
                            Cargo.append(CL_Cargo4)
                        except (IndexError):
                            pass
                        try:
                            Cargo5 = (text.split('\n')[18].split()[8:])
                            CL_Cargo5 = listToString(Cargo5)
                            Cargo.append(CL_Cargo5)
                        except (IndexError):
                            pass
                        try:
                            Cargo6 = (text.split('\n')[24].split()[8:])
                            CL_Cargo6 = listToString(Cargo6)
                            Cargo.append(CL_Cargo6)
                        except (IndexError):
                            pass

                        #PAGE 4
                        try:
                            fourth_p = pdf.pages[3]
                            text = fourth_p.extract_text()
                        except (IndexError):
                            pass
                        try:
                            Cargo7 = (text.split('\n')[12].split()[8:])
                            CL_Cargo7 = listToString(Cargo7)
                            Cargo.append(CL_Cargo7)
                        except (IndexError):
                            pass
                        try:
                            Cargo8 = (text.split('\n')[18].split()[8:])
                            CL_Cargo8 = listToString(Cargo8)
                            Cargo.append(CL_Cargo8)
                        except (IndexError):
                            pass
                        try:
                            Cargo9 = (text.split('\n')[24].split()[8:])
                            CL_Cargo9 = listToString(Cargo9)
                            Cargo.append(CL_Cargo9)
                        except (IndexError):
                            pass

                        #PAGE 5
                        try:
                            c_p = pdf.pages[4]
                            text = c_p.extract_text()
                        except (IndexError):
                            pass
                        try:
                            Cargo10 = (text.split('\n')[12].split()[8:])
                            CL_Cargo10 = listToString(Cargo10)
                            Cargo.append(CL_Cargo10)
                        except (IndexError):
                            pass
                        try:
                            Cargo11 = (text.split('\n')[18].split()[8:])
                            CL_Cargo11 = listToString(Cargo11)
                            Cargo.append(CL_Cargo11)
                        except (IndexError):
                            pass
                        try:
                            Cargo12 = (text.split('\n')[24].split()[8:])
                            CL_Cargo12 = listToString(Cargo12)
                            Cargo.append(CL_Cargo12)
                        except (IndexError):
                            pass

                    elif total_pages <= 10:
                        #PAGE 6
                        try:
                            six_p = pdf.pages[5]
                            text = six_p.extract_text()
                        except (IndexError):
                            pass
                        try:
                            Cargo13 = (text.split('\n')[12].split()[7:])
                            CL_Cargo13 = listToString(Cargo13)
                            Cargo.append(CL_Cargo13)
                        except (IndexError):
                            pass
                        try:
                            Cargo14 = (text.split('\n')[18].split()[8:])
                            CL_Cargo14 = listToString(Cargo14)
                            Cargo.append(CL_Cargo14)
                        except (IndexError):
                            pass
                        try:
                            Cargo15 = (text.split('\n')[24].split()[8:])
                            CL_Cargo15 = listToString(Cargo15)
                            Cargo.append(CL_Cargo15)
                        except (IndexError):
                            pass

                        #PAGE 7
                        try:
                            sev_p = pdf.pages[6]
                            text = sev_p.extract_text()
                        except (IndexError):
                            pass
                        try:
                            Cargo16 = (text.split('\n')[12].split()[7:])
                            CL_Cargo16 = listToString(Cargo16)
                            Cargo.append(CL_Cargo16)
                        except (IndexError):
                            pass
                        try:
                            Cargo17 = (text.split('\n')[18].split()[8:])
                            CL_Cargo17 = listToString(Cargo17)
                            Cargo.append(CL_Cargo17)
                        except (IndexError):
                            pass
                        try:
                            Cargo18 = (text.split('\n')[24].split()[8:])
                            CL_Cargo18 = listToString(Cargo18)
                            Cargo.append(CL_Cargo18)
                        except (IndexError):
                            pass

                        #PAGE 8
                        try:
                            eig_p = pdf.pages[7]
                            text = eig_p.extract_text()
                        except (IndexError):
                            pass
                        try:
                            Cargo19 = (text.split('\n')[12].split()[7:])
                            CL_Cargo19 = listToString(Cargo19)
                            Cargo.append(CL_Cargo19)
                        except (IndexError):
                            pass
                        try:
                            Cargo20 = (text.split('\n')[18].split()[8:])
                            CL_Cargo20 = listToString(Cargo20)
                            Cargo.append(CL_Cargo20)
                        except (IndexError):
                            pass
                        try:
                            Cargo21 = (text.split('\n')[24].split()[8:])
                            CL_Cargo21 = listToString(Cargo21)
                            Cargo.append(CL_Cargo21)
                        except (IndexError):
                            pass

                        #PAGE 9
                        try:
                            nin_p = pdf.pages[8]
                            text = nin_p.extract_text()
                        except (IndexError):
                            pass
                        try:
                            Cargo22 = (text.split('\n')[12].split()[7:])
                            CL_Cargo22 = listToString(Cargo22)
                            Cargo.append(CL_Cargo22)
                        except (IndexError):
                            pass
                        try:
                            Cargo23 = (text.split('\n')[18].split()[8:])
                            CL_Cargo23 = listToString(Cargo23)
                            Cargo.append(CL_Cargo23)
                        except (IndexError):
                            pass
                        try:
                            Cargo24 = (text.split('\n')[24].split()[8:])
                            CL_Cargo24 = listToString(Cargo24)
                            Cargo.append(CL_Cargo24)
                        except (IndexError):
                            pass

                        #PAGE 10
                        try:
                            ten_p = pdf.pages[9]
                            text = ten_p.extract_text()
                        except (IndexError):
                            pass
                        try:
                            Cargo25 = (text.split('\n')[12].split()[7:])
                            CL_Cargo25 = listToString(Cargo25)
                            Cargo.append(CL_Cargo25)
                        except (IndexError):
                            pass
                        try:
                            Cargo26 = (text.split('\n')[18].split()[8:])
                            CL_Cargo26 = listToString(Cargo26)
                            Cargo.append(CL_Cargo26)
                        except (IndexError):
                            pass
                        try:
                            Cargo27 = (text.split('\n')[24].split()[8:])
                            CL_Cargo27 = listToString(Cargo27)
                            Cargo.append(CL_Cargo27)
                        except (IndexError):
                            pass


            def listToString(clean):
                str1 = " "
                return (str1.join(clean))
            CL_Weight = Weight
            Count == len(rows)
            CL_Seal = listToString(Seal).replace('1 SIG. OR.', '').replace('1 SIG.', '').replace('---', '').replace('OR.', '').replace('1 PROT.N.4699/RU-25/02/21 SEAL', '').replace('PROT.N.4699/RU-25', '').replace('PROT.4699/RU-25/02/21 - SEAL', '').replace('PROT.4699', '').replace('1 ', '').replace(' ', '').replace('AUT.', '')
            CL_Mrn = str(Mrn).replace('MRN', '')
            CL_Cargo = listToString(Cargo).replace('Imballaggio', '').replace('---', '').replace('SIG./', '')
            CL_Cargo_clean = re.sub(r"\d+", "", CL_Cargo).replace(' ', '')
            df = [Count,Filename,Digit,CL_Mrn,CL_Weight,CL_Seal,CL_Cargo_clean,]
            rows.append(df)
            df2 = pd.DataFrame((rows), columns=['Id.','Filename','Container', 'Mrn', 'Weight','Seal','Cargo'])
            df2.to_excel(('output/Raw_Data.xlsx'), index=False)

