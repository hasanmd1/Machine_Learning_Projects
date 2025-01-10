from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, roc_auc_score


def check_evaluation(y_test, y_pred, risk_score):
    # Calculate and print the accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.4f}")

    # Print classification report for detailed metrics
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # Calculate and print ROC AUC score
    roc_auc = roc_auc_score(y_test, risk_score)
    print(f"ROC AUC Score: {roc_auc:.4f}")


def draw_confusion_matrix(y_test, y_pred):
    conf_matrix = confusion_matrix(y_test, y_pred)
    return conf_matrix
