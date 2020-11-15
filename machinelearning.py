import matplotlib

matplotlib.use("TkAgg")
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import mean_squared_error


def test(model):
    try:
        df = pd.read_csv('KBO_test_data.csv')
    except:
        print("""
        Dataset not found in your computer.
        Please follow the instructions.
        """)
        quit()

    df_prescaled = df.copy()
    df_scaled = df.drop(['def', 'atck'], axis=1)
    df_scaled = scale(df_scaled)
    cols = df.columns.tolist()
    cols.remove('def')
    cols.remove('atck')
    df_scaled = pd.DataFrame(df_scaled, columns=cols, index=df.index)
    df_scaled = pd.concat([df_scaled, df['def'], df['atck']], axis=1)
    df = df_scaled.copy()

    X = df.loc[:, (df.columns != 'def') & (df.columns != 'atck')]
    y = df.loc[:, (df.columns == 'def') | (df.columns == 'atck')]

    predicted_score = model.predict(X)

    teamList = ['OB', 'LT', 'SS', 'HH', 'HT', 'LG', 'SK', 'WO']
    win = [[0, '두산'],
           [0, '롯데'],
           [0, '삼성'],
           [0, '한화'],
           [0, 'KIA'],
           [0, 'LG'],
           [0, 'SK'],
           [0, '넥센']]
    scoreTable = [[0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0]]

    for i in range(0, 56):
        defTeam = y.values[i][0]
        atckTeam = y.values[i][1]

        for j in range(0, 9):
            if teamList[j] == defTeam:
                defIdx = j
                break

        for j in range(0, 9):
            if teamList[j] == atckTeam:
                atckIdx = j
                break;

        scoreTable[atckIdx][defIdx] = float(predicted_score[i])

    # print(scoreTable)

    for i in range(0, 8):
        for j in range(0, 8):
            if i < j:
                if scoreTable[i][j] > scoreTable[j][i]:
                    win[i][0] += 3
                elif scoreTable[i][j] == scoreTable[j][i]:
                    win[i][0] += 1
                    win[j][0] += 1
                else:
                    win[j][0] += 3

    win.sort(reverse=True)

    for i in range(0, 8):
        print(str(i + 1) + "위 : " + str(win[i][1]))

    print("")
    print("")


def predict_random(df_prescaled, X_test, model):
    sample = X_test.sample(n=1, random_state=np.random.randint(low=0, high=10000))
    idx = sample.index[0]
    actual_score = df_prescaled.loc[idx, 'score']
    predicted_score = model.predict(sample)[0][0]
    rmse = np.sqrt(np.square(predicted_score - actual_score))

    print("Actual Score : {:0.2f}".format(actual_score))
    print("Predicted Score : {:0.2f}".format(predicted_score))
    print("RMSE : {:0.2f}".format(rmse))


def main():
    try:
        print("Reading in the dataset. This will take some time..")
        df = pd.read_csv('KBO_data.csv')
    except:
        print("""
        Dataset not found in your computer.
        Please follow the instructions.
        """)
        quit()

    # Scale the features
    df_prescaled = df.copy()
    df_scaled = df.drop(['score'], axis=1)
    df_scaled = scale(df_scaled)
    cols = df.columns.tolist()
    cols.remove('score')
    df_scaled = pd.DataFrame(df_scaled, columns=cols, index=df.index)
    df_scaled = pd.concat([df_scaled, df['score']], axis=1)
    df = df_scaled.copy()

    # Split the dataframe into a training set and testing set
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

    model.compile(loss='mse', optimizer='adam', metrics=['mse'])

    model.fit(X_train, y_train, epochs=200)

    # Results
    train_pred = model.predict(X_train)
    train_rmse = np.sqrt(mean_squared_error(y_train, train_pred))
    test_pred = model.predict(X_test)
    test_rmse = np.sqrt(mean_squared_error(y_test, test_pred))

    print("Train RMSE : {:0.2f}".format(train_rmse))
    print("Test RMSE : {:0.2f}".format(test_rmse))
    print("--------------------------------------------")

    test(model)

    """
    x = 1

    while x == 1:
        predict_random(df_prescaled, X_test, model)
        x = int(input())
    """


if __name__ == "__main__":
    main()

