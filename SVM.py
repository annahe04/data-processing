import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
import matplotlib.pyplot as plt


if __name__ == "__main__":
    features = pd.read_csv('finalresults.csv', usecols = ['g_x_mean', 'g_x_std', 'g_x_max_to_min', 'g_x_median', 'g_y_mean', 'g_y_std', 'g_y_max_to_min', 'g_y_median', 'g_z_mean', 'g_z_std', 'g_z_max_to_min', 'g_z_median', 'a_x_mean', 'a_x_std', 'a_x_max_to_min', 'a_x_median', 'a_y_mean', 'a_y_std', 'a_y_max_to_min', 'a_y_median', 'a_z_mean',  'a_z_std', 'a_z_max_to_min', 'a_z_median'])
    X = np.array(features)
    y = np.array(pd.read_csv('finalresults.csv', usecols = ['motion']))
    class_names = np.array(['Downstiars', 'Jog', 'Sit', 'Stand', 'Upstairs', 'Walk'])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    svm_model = svm.SVC(kernel='linear', C=1.0).fit(X_train, y_train)
    svm_model.fit(X_train, y_train)

    np.set_printoptions(precision=2)
    
    title_options = [
        ("Confusion matrix, without normalization", None),
        ("Normalized confusion matrix", "true"),
    ]
    
    y_pred = svm_model.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    
    for title, normalize in title_options:
        disp = ConfusionMatrixDisplay.from_estimator(
            svm_model,
            X_test,
            y_test,
            display_labels = class_names,
            cmap = plt.cm.Blues,
            normalize=normalize,
        )
        
        disp.ax_.set_title(title)
        print(title)
        print(disp.confusion_matrix)
        
    plt.show()