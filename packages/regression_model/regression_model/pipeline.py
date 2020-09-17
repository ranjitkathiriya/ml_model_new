from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

from xgboost import XGBClassifier

import logging


_logger = logging.getLogger(__name__)


price_pipe = Pipeline(
    [
        ("scaler", MinMaxScaler()),
        ("classfier", XGBClassifier()),
    ]
)
