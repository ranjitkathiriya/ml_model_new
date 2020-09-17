import numpy as np
from sklearn.model_selection import train_test_split

from regression_model import pipeline
from regression_model.processing.data_management import load_dataset, save_pipeline
from regression_model.config import config
from regression_model import __version__ as _version
import pandas as pd

import logging


_logger = logging.getLogger(__name__)


def run_training() -> None:
    """Train the model."""

    # read training data
    data = load_dataset(file_name=config.TRAINING_DATA_FILE)
    # _data = pd.read_csv(f"{config.DATASET_DIR}/{config.TRAINING_DATA_FILE}")
    # print(_data.head())

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES], data[config.TARGET], random_state=0
    )  # we are setting the seed here

    y_train = y_train.apply(lambda x: 1 if x == "M" else 0)

    pipeline.price_pipe.fit(X_train[config.FEATURES], y_train)

    _logger.info(f"saving model version: {_version}")
    save_pipeline(pipeline_to_persist=pipeline.price_pipe)


if __name__ == "__main__":
    run_training()
