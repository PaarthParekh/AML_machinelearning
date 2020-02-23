import pandas as pd
import os
import argparse

def make_file():
    parser=argparse.ArgumentParser()
    parser.add_argument("-f","-file_name",help="Name of the file")
    args=parser.parse_args()
    df=pd.read_csv(args.f,header=None)
    list_pred=[]
    list_prob=[]
    for i in range(0,len(df.index),7):
        a=df[0][i]+df[0][i+1]+df[0][i+2]+df[0][i+3]+df[0][i+4]+df[0][i+5]+df[0][i+6]
        if a>=2:
            list_pred.append(1)
            list_prob.append(a/7)
        elif  a==1:
            list_pred.append(0)
            list_prob.append(1-a/7)
        else:
            list_pred.append(0)
            list_prob.append(1)
    with open ("./files/Test_Pred.csv","w") as fh:
        fh.write("Predictive"+"\t"+"Probability"+"\n")
        for i in range(len(list_pred)):
            fh.write(str(list_pred[i])+"\t"+str(list_prob[i])+"\n")
def get_values():
    df=pd.read_csv("./files/AMLTraining.csv")
    valpre=df.iloc[:1431,:]
    valemp=df.iloc[1432:,:]
    valemp=valemp.reset_index(drop=True)
    return valpre,valemp
def writetocsv(valpre,valempt):
    df=pd.read_csv("./files/Test_Pred.csv",sep="\t")
    new_df=df.loc[df.index.repeat(8)].reset_index(drop=True)
    new_df["Predictive"]=new_df["Predictive"].replace(0,"normal")
    new_df["Predictive"]=new_df["Predictive"].replace(1,"aml")
    valempt["Label"]=new_df["Predictive"]
    valpre.to_csv("./files/Final_File.csv",index=False)
    valempt.to_csv("./files/Final_File.csv",mode="a",index=False,header=False)
    valempt["Prob"]=new_df["Probability"]
    valempt.to_csv("./files/Final_File1.csv",mode="a",index=False)
def main():
    make_file()
    valp,vale=get_values()
    writetocsv(valp,vale)

if __name__=="__main__":
    main()

