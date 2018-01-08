import numpy as np

from sir import SlicedAverageVarianceEstimation
from sir import datasets


def test_sir():
    X, y = datasets.make_cubic(random_state=123)

    save = SlicedAverageVarianceEstimation().fit(X, y)

    true_beta = (1 / np.sqrt(2)) * np.hstack((np.ones(2), np.zeros(8)))
    angle = np.dot(true_beta, save.components_[:, 0])
    np.testing.assert_allclose(np.abs(angle), 1, rtol=1e-1)
