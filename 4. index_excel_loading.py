import pandas as pd
import os
import datetime
def excel_loading(s,r,t):
    df=pd.read_excel("C:\\Users\\chaitu\\Desktop\\opencv\\bcd.xlsx")
    x=list(df['Register number'])
    if r not in x:
        df.loc[len(df.index)]=[s,r,t]
    df.to_excel("C:\\Users\\chaitu\\Desktop\\opencv\\bcd.xlsx",index=False)

def date_wise_loading(s,r,a):
    df=pd.read_excel("C:\\Users\\chaitu\Desktop\\opencv\\abc.xlsx")
    t=datetime.date.today()
    res="C:\\Users\\chaitu\\Desktop\\opencv\\attendence list\\"
    c=os.listdir("C:\\Users\\chaitu\\Desktop\\opencv\\attendence list")
    x=res+str(t)+".xlsx"
    y=str(t)+".xlsx"
    if y not in c:
        pf=pd.DataFrame(columns=['Student name', 'Regd number', 'Time'])
        pf.to_excel(x,index=False)
    elif y in c:
        pf=pd.read_excel(x)
        b=list(pf['Regd number'])
        if r not in b:
            pf.loc[len(pf.index)]=[s,r,a]
            pf.to_excel(x,index=False)
        else:
            print("your details are already noted,so please check it!")

# a=datetime.datetime.now()
# a=a.strftime("%X")
#date_wise_loading('saketh',545,a)

        
