import pandas as pd
import pickle

class Pipeline:
    def __init__(self):
        # Carregando os todos os dados
        self.dataset = pd.read_csv('../Dataset/Churn_Modelling.csv')
        
        # Carregando o normalizador
        scaler_file = open('../Scalers/min_max_quantitatives.pkl', 'rb')
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

