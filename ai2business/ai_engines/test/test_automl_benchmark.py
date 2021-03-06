# Copyright 2020 AI2Business. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Test-Environment for automl as benchmark."""
import autokeras as ak
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

from ai2business.ai_engines import automl_neural_network as an


def test_runtime_dataclassifier():

    train_file_path = tf.keras.utils.get_file(
        "train.csv", "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
    )
    test_file_path = tf.keras.utils.get_file(
        "test.csv", "https://storage.googleapis.com/tf-datasets/titanic/eval.csv"
    )

    data_train = pd.read_csv(train_file_path)
    data_test = pd.read_csv(test_file_path)

    x_train = data_train.drop(columns="survived")
    y_train = data_train["survived"]
    x_test = data_test.drop(columns="survived")
    y_test = data_test["survived"]

    context = an.AutoMLPipeline(
        an.DataClassification(max_trials=5, overwrite=True, loss="mean_squared_error")
    )
    context.run_automl()
    context.train = an.AutoMLFit(x_train, y_train, batch_size=32, epochs=100)
    context.run_automl()
    context.train = an.AutoMLEvaluate(x_test, y_test, batch_size=32)
    context.run_automl()
    context.train = an.AutoMLPredict(x_train, batch_size=32)
    context.run_automl()
    assert context.return_automl["model"] != None
    assert isinstance(context.return_automl["prediction"], np.ndarray)
    assert isinstance(context.return_automl["evaluation"], list)


def test_runtime_dataregression():

    data = fetch_california_housing()
    x_train, x_test, y_train, y_test = train_test_split(
        data.data,
        data.target,
        test_size=0.33,
        random_state=42,
    )
    context = an.AutoMLPipeline(
        an.DataRegression(max_trials=3, overwrite=True, loss="mean_squared_error")
    )
    context.run_automl()
    context.train = an.AutoMLFit(x_train, y_train, batch_size=32, epochs=10)
    context.run_automl()
    context.train = an.AutoMLEvaluate(x_test, y_test, batch_size=32)
    context.run_automl()
    context.train = an.AutoMLPredict(x_train, batch_size=32)
    context.run_automl()
    assert context.return_automl["model"] != None
    assert isinstance(context.return_automl["prediction"], np.ndarray)
    assert isinstance(context.return_automl["evaluation"], list)


def test_return_train():

    model = an.DataRegression(max_trials=4)
    context = an.AutoMLPipeline(model)
    assert context.train == model


def test_save_load():

    data = fetch_california_housing()
    x_train, _, y_train, _ = train_test_split(
        data.data,
        data.target,
        test_size=0.33,
        random_state=42,
    )
    context = an.AutoMLPipeline(
        an.DataRegression(max_trials=3, overwrite=True, loss="mean_squared_error")
    )
    context.run_automl()
    context.train = an.AutoMLFit(x_train, y_train, batch_size=32, epochs=10)
    context.run_automl()
    context.train = an.AutoMLSave(model_name="model_autokeras")
    context.run_automl()
    model = an.AutoMLModels().load_model(model_name="model_autokeras")
    assert model != None


def test_multi_model():

    context = an.AutoMLPipeline(
        an.MultiModel(
            inputs=[ak.ImageInput(), ak.StructuredDataInput()],
            outputs=[
                ak.RegressionHead(metrics=["mae"]),
                ak.ClassificationHead(
                    loss="categorical_crossentropy", metrics=["accuracy"]
                ),
            ],
            overwrite=True,
            max_trials=2,
        )
    )
    context.run_automl()
    assert context.return_automl["model"] != None
