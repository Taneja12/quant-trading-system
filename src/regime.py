from hmmlearn.hmm import GaussianHMM

def fit_hmm(X, n_regimes=3):
    model = GaussianHMM(
        n_components=n_regimes,
        covariance_type="full",
        n_iter=500,
        random_state=42
    )
    model.fit(X)
    return model
