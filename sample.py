import matplotlib
matplotlib.use("TkAgg")
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras import optimizers
from sklearn.metrics import mean_squared_error


def test(model):
    

def predict_random(df_prescaled, X_test, model):
    sample = X_test.sample(n=1, random_state=np.random.randint(low=0, high=10000))
    idx = sample.index[0]
    actual_score = df_prescaled.loc[idx, 'score']
    predicted_score = model.predict(sample)[0][0]
    rmse = np.sqrt(np.square(predicted_score-actual_score))

    print("Actual score : {:0.2f}".format(actual_score))
    print("Predicted score : {:0.2f}".format(predicted_score))
    print("RMSE: {:0.2f}".format(rmse))


def main():
    try:
        print("Reading in the dataset. This will take some time..")
        df = pd.read_csv('KBO_data.csv')
    except:
        print("""
            Dataset not found in your computer.
            Please follow the instructions
            """)
        quit()

    """
    print(df.head())
    print(df.isnull().sum())
    print(df.describe())
    
    df['score'].hist(bins=20)
    plt.xlabel("Score")
    plt.title("Histogram of Score")
    plt.show()
    """

    # Scale the features
    df_prescaled = df.copy()
    df_scaled = df.drop(['score'], axis=1)
    df_scaled = scale(df_scaled)
    cols = df.columns.tolist()
    cols.remove('score')
    df_scaled = pd.DataFrame(df_scaled, columns=cols, index=df.index)
    df_scaled = pd.concat([df_scaled, df['score']], axis=1)
    df = df_scaled.copy()

    # Split the dataframe into a training and testing set
    X = df.loc[:, df.columns != 'score']
    y = df.loc[:, 'score']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Build neural network in Keras
    model = Sequential()
    model.add(Dense(256, activation='relu', input_dim=X_train.shape[1]))
    model.add(Dense(128, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(16, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(4, activation='relu'))
    model.add(Dense(1))

    adam = optimizers.Adam(lr = 0.001)
    model.compile(loss='mse', optimizer='adam', metrics=['mse'])

    model.fit(X_train, y_train, epochs=200)

    # Results
    train_pred = model.predict(X_train)
    train_rmse = np.sqrt(mean_squared_error(y_train, train_pred))
    test_pred = model.predict(X_test)
    test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))
    print("Train RMSE: {:0.2f}".format(train_rmse))
    print("Test RMSE: {:0.2f}".format(test_rmse))
    print('------------------------------------')

    x = 1

    while x == 1:
        predict_random(df_prescaled, X_test, model)
        x = int(input())

if __name__ == "__main__":
    main()
