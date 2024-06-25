import pandas as pd
import numpy as np
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

FileFoundCheck = False
choice = [0]  # Use a list to hold the choice value to allow modification in functions

def askRunning():
    running = input("Deseja continuar? (s/n): ")
    if running == 's':
        choice[0] = 0
    elif running == 'n':
        choice[0] = 11
    else:
        print("Opção inválida. Tente novamente.")
        askRunning()

# Ensure the file path is correct and the file exists
try:
    df = pd.read_csv('itch-analytics.csv')
    print(df.info())
    FileFoundCheck = True
except FileNotFoundError:
    print("File 'itch-analytics.csv' not found. Please check the file path.")

# 1. Prepare the data
X = df[['Views']]  # Features
y = df['Downloads']  # Target variable

# 2. Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Select a regression model
model = LinearRegression()

# 4. Train the model
model.fit(X_train, y_train)

# 5. Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# 6. Predict
# Example: Predicting for a new game with 1000 views and 500 downloads
new_game_features = np.array([[1000]])
prediction = model.predict(new_game_features)
print(f"Predicted Statistic: {prediction[0]}")

if FileFoundCheck:
    while choice[0] != 11:
        print("\nEscolha quais relatórios deseja emitir:\n")
        print("1 - Emitir as 5 primeiras linhas")
        print("2 - Emitir as 5 últimas linhas")
        print("3 - Tipo de dados de cada coluna")
        print("4 - Número de linhas e colunas dos dados")
        print("5 - Quantidade de células vazias em cada coluna")
        print("6 - Quantidade de valores únicos em cada coluna")
        print("7 - Estatísticas do sumário dos dados")
        print("8 - Correlação entre as colunas")
        print("9 - Soma final de todos os valores em cada coluna")
        print("10 - Soma total dos valores categorizados por jogo")
        print("11 - Sair do programa\n")
        try:
            choice[0] = int(input())
        except ValueError:
            print("Valor inválido. Tente novamente.")
            continue
        
        if choice[0] == 1:
            print("Displaying the first 5 rows of the data:\n")
            print(df.head())
            askRunning()
        elif choice[0] == 2:
            print("Displaying the last 5 rows of the data:\n")
            print(df.tail())
            askRunning()
        elif choice[0] == 3:
            print("Displaying the data types of each column:\n")
            print(df.dtypes)
            askRunning()
        elif choice[0] == 4:
            print("\nDisplaying the number of rows and columns in the data:\n")
            print(df.shape)
            askRunning()
        elif choice[0] == 5:
            print("\nDisplaying the number of missing values in each column:\n")
            print(df.isnull().sum())
            askRunning()
        elif choice[0] == 6:
            print("\nDisplaying the number of unique values in each column:\n")
            print(df.nunique())
            askRunning()
        elif choice[0] == 7:
            print("\nDisplaying the summary statistics of the data:\n")
            print(df.describe())
            askRunning()
        elif choice[0] == 8:
            numeric_df = df.select_dtypes(include=[np.number])
            print("\nDisplaying the correlation between the columns:\n")
            print(numeric_df.corr())
            askRunning()
        elif choice[0] == 9:
            print("\nSum of all values in each column:\n")
            print(df.sum(numeric_only=True))
            askRunning()
        elif choice[0] == 10:
            print("\nSum of values separated by unique strings in the 'names' column:\n")
            sum_by_names = df.groupby('Name').sum(numeric_only=True)
            print(sum_by_names)
            askRunning()
        elif choice[0] == 11:
            print("Saindo do programa...")
            sys.exit(0)
        else:
            print("Escolha inválida. Tente novamente.")