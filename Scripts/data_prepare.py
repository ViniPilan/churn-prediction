import pandas as pd
import psycopg2
import pickle

class Pipeline:
    def __init__(self):
        # Carregando os todos os dados
    	conn = psycopg2.connect(host="ec2-52-20-166-21.compute-1.amazonaws.com",
                        database="defrnttd424q3s",
                        user="adzsrxhiunrkva",
                        password="9b53ade5ea4c20da1afab3a1ae94e98df059325187dec24a3acb72163555f7de", 
                        port='5432')
                        
        self.dataset = pd.read_sql('SELECT * FROM customers', conn)
        
        conn.close()
        
        data.rename({'customerid':'CustomerId', 
		     'surname':'Surname',
		     'creditscore':'CreditScore',
		     'geography':'Geography',
		     'gender':'Gender',
		     'age':'Age',
		     'tenure':'Tenure',
		     'balance':'Balance',
		     'numofproducts':'NumOfProducts',
		     'hascrcard':'HasCrCard',
		     'isactivemember':'IsActiveMember',
		     'estimatedsalary':'EstimatedSalary',
		     'exited':'Exited'}, axis=1, inplace=True)
		     
        
        # Carregando o normalizador
        scaler_file = open('Scalers/min_max_quantitatives.pkl', 'rb')
        self.scaler = pickle.load(scaler_file)
        scaler_file.close()

        # Definindo as variáveis quantitativas
        self.quantitatives = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 
                              'EstimatedSalary', 'Surname_freq']


    def run(self, data_frame):
        data = data_frame.copy()
            
        # Ajuste da coluna Geography
        data['Geography_France'] = data['Geography'].apply(lambda x: 1 if x == 'France' else 0)
        data['Geography_Germany'] = data['Geography'].apply(lambda x: 1 if x == 'Germany' else 0)
        data['Geography_Spain'] = data['Geography'].apply(lambda x: 1 if x == 'Spain' else 0)

        # Correção de formato
        data['Gender_Male'] = data['Gender'].apply(lambda x:1 if x == 'Male' else 0)


        # Extraindo informações do sobrenome
        data['Surname_freq'] = data['Surname'].apply(self.surname_freq)

        # Normalizando variáveis quantitativas
        data[self.quantitatives] = self.scaler.transform(data[self.quantitatives])

        # Organizando ordem das colunas
        data = data[['CreditScore', 'Gender_Male', 'Age', 'Balance',
                     'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary',
                     'Geography_France', 'Geography_Germany', 'Geography_Spain',
                     'Surname_freq']]
                     
        return data

    def surname_freq(self, surname):
        cont = 0
        
        for name in self.dataset['Surname'].values:
            if name == surname:
                cont += 1
                
        return cont

