import pandas as pd
import psycopg2
import os

os.system('kaggle datasets download "shubh0799/churn-modelling"')
os.system('mv ./churn-modelling.zip ../Dataset')

data = pd.read_csv('../Dataset/churn-modelling.zip').drop('RowNumber', axis=1)

conn = psycopg2.connect(host="ec2-52-20-166-21.compute-1.amazonaws.com",
                        database="defrnttd424q3s",
                        user="adzsrxhiunrkva",
                        password="9b53ade5ea4c20da1afab3a1ae94e98df059325187dec24a3acb72163555f7de", 
                        port='5432')

cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS customers')

cursor.execute('CREATE TABLE customers (CustomerId integer primary key, Surname text, CreditScore integer, Geography text, Gender text, Age integer, Tenure integer, Balance decimal, NumOfProducts integer, HasCrCard integer, IsActiveMember integer, EstimatedSalary decimal, Exited integer);')

index = data.index.to_list()
n0 = len(index)
i = -1

while i<n0:
    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string = f""" INSERT INTO customers VALUES ({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"""

    except:
        pass

    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass

    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass


    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass


    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass


    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass

    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass

    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass

    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass

    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass

    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass

    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass


    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass


    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass


    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass

    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass

    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass

    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass

    try:
        i += 1
        d1 = data.loc[i].to_dict()
        d1['Surname'] = d1['Surname'].replace("'", '"')
        string += f",\n({d1['CustomerId']}, '{d1['Surname']}', {d1['CreditScore']}, '{d1['Geography']}', '{d1['Gender']}', {d1['Age']}, {d1['Tenure']}, {d1['Balance']}, {d1['NumOfProducts']}, {d1['HasCrCard']}, {d1['IsActiveMember']}, {d1['EstimatedSalary']}, {d1['Exited']})"
    except:
        pass
    
    try:
        if string is not None:
            cursor.execute(string)
        
        string = None
        
        os.system('clear')
        print('Progress: %.2f%% i:%d' % (100*i/n0, i))        
    
    except Exception as e:
        print(e)

cursor.execute('commit')

conn.close()