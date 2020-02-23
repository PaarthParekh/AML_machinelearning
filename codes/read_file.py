import pandas as pd
import os
def file_load():
    file_list = list()
    i=0
    for file in sorted(os.listdir()):
        if file.endswith('.CSV'):
            df = pd.read_csv(file)
            quantile=df.quantile([0.20,0.40,0.50,0.60,0.80])
            quant=quantile.append((df.max(axis=0)).T,ignore_index=True)
            quant2=quant.append((df.min(axis=0)).T,ignore_index=True)
            file_list.append(quant2)
            i+=1
        if(i==8):
            i=0
            all_days = pd.concat(file_list, axis=1, ignore_index=True)
            all_days.to_csv("./files/all.csv",mode='a',header=False,index=False)
            file_list= list()

def normalize_col():
    df=pd.read_csv("./files/all.csv",header=None)
    normalized_df=(df-df.mean())/df.std()
    training_data=normalized_df.iloc[:1253,:]
    testing_data=normalized_df.iloc[1253:,:]
    #print(training_data)
    testing_data.to_csv("./files/testing_data.csv",header=False,index=False)
    return training_data

def get_values():
    df=pd.read_csv("./files/AMLTraining.csv")
    valpre=df.iloc[:1431,:]
    for i in range(0,1432,8):
        for j in range(i,(i+7)):
            val=valpre.iloc[[j]]
            #print(val)
            val.to_csv("./files/values.csv",mode="a",index=False,header=False)

def final_file(training_data):
    val=pd.read_csv("./files/values.csv",header=None)
    val.loc[val[3]=="aml",4]=1
    val.loc[val[3]=="normal",4]=0
    training_data[56]=val[4]
    training_data[57]=val[3]
    training_data.to_csv("./files/final_prod.csv",index=False,header=False)

def main():
    file_load()
    training_data=normalize_col()
    get_values()
    final_file(training_data)

if __name__=="__main__":
    main()

