import matplotlib.pyplot as plt
from sklearn import metrics


def plot_learning_curves(history, arr):
    fig, ax = plt.subplots(1, 2, figsize=(20, 5))
    for idx in range(2):
        ax[idx].plot(history.history[arr[idx][0]])
        ax[idx].plot(history.history[arr[idx][1]])
        ax[idx].legend([arr[idx][0], arr[idx][1]],fontsize=18)
        ax[idx].set_xlabel('A ',fontsize=16)
        ax[idx].set_ylabel('B',fontsize=16)
        ax[idx].set_title(arr[idx][0] + ' X ' + arr[idx][1],fontsize=16)


def evaluate_model(y_hat, y_pred):

  print(metrics.confusion_matrix(y_hat, y_pred))
  print(metrics.classification_report(y_hat, y_pred))
  print("Accuracy Score: %.3f" % metrics.accuracy_score(y_hat, y_pred))