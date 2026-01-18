from xgboost import XGBClassifier

def train_xgb(X_train, y_train):
    model = XGBClassifier(
        n_estimators=200,
        max_depth=5,
        learning_rate=0.05,
        random_state=42
    )
    model.fit(X_train, y_train)
    return model
