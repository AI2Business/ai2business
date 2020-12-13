"""Auto Machine Learning Services based on [AutoKERAS](https://autokeras.com) for:

1. Images
2. Text
3. Structured Data
4. Time Series
5. Mixture Models like Text + Images
"""
from abc import ABC, abstractmethod
from typing import Any, Callable

import autokeras as ak
from tensorflow.keras.models import load_model


class AutoMLModels:
    """The Auto-Machine Learning Models

    Here is the list of the current implemented auto-machine learning models from [AutoKERAS](https://autokeras.com):

    1. [Image-Classification](https://autokeras.com/tutorial/image_classification/)
    2. [Image-Regression](https://autokeras.com/tutorial/image_regression/)
    3. [Text-Classification](https://autokeras.com/tutorial/text_classification/)
    4. [Text-Regression](https://autokeras.com/tutorial/text_regression/)
    5. [Structured-Data-Classification](https://autokeras.com/tutorial/structured_data_classification/)
    6. [Structured-Data-Regression](https://autokeras.com/tutorial/structured_data_regression/)
    7. [Mulit-Models](https://autokeras.com/tutorial/multi/)
    9. [Time-Series-Forcast](https://github.com/keras-team/autokeras/blob/9a6c49badad67a03d537de8cebbe6ea6eb66fa69/autokeras/tasks/time_series_forecaster.py)


    Here is text


    # Arguments:
        directory (str, optional): Path of the directory to save the search outputs. Defaults to None.
        loss (str, optional): Keras loss function. Defaults to None, which means 'mean_squared_error'.
        objective (str, optional): Model metric. Defaults to "val_loss".
        overwrite (bool, optional): Overwrite existing projects. Defaults to False.
        project_name (str, optional): Project Name. Defaults to "AutoML_DeepLearning".
        max_model_size (int, optional): Maximum number of models to evaluate. Defaults to None.
        max_trials (int, optional): Maximum number of trials for building a model. Defaults to 100.
        metrics (str, optional): The metric of the validation. Defaults to None.
        seed (int, optional): Random shuffling number. Defaults to None.
        tuner (str, optional): The tuner is engine for suggestions the concept of the new models. It can be either a string 'greedy', 'bayesian', 'hyperband' or 'random' or a subclass of AutoTuner. If it is unspecific, the  first evaluates the most commonly used models for the task before exploring other models
    """

    def __init__(
        self,
        directory: str = None,
        loss: str = None,
        objective: str = "val_loss",
        overwrite: bool = False,
        project_name: str = "AutoML_DeepLearning",
        max_model_size: int = None,
        max_trials: int = 1,
        metrics: str = None,
        seed: int = None,
        tuner: str = None,
    ) -> None:
        """Defining the common parameters for all models.

        Text

        Args:
            directory (str, optional): Path of the directory to save the search outputs. Defaults to None.
            loss (str, optional): Keras loss function. Defaults to None, which means 'mean_squared_error'.
            objective (str, optional): Model metric. Defaults to "val_loss".
            overwrite (bool, optional): Overwrite existing projects. Defaults to False.
            project_name (str, optional): Project Name. Defaults to "AutoML_DeepLearning".
            max_model_size (int, optional): Maximum number of models to evaluate. Defaults to None.
            max_trials (int, optional): Maximum number of trials for building a model. Defaults to 100.
            metrics (str, optional): The metric of the validation. Defaults to None.
            seed (int, optional): Random shuffling number. Defaults to None.
            tuner (str, optional): The tuner is engine for suggestions the concept of the new models. It can be either a string 'greedy', 'bayesian', 'hyperband' or 'random' or a subclass of AutoTuner. If it is unspecific, the  first evaluates the most commonly used models for the task before exploring other models
        """
        self.directory = directory
        self.loss = loss
        self.objective = objective
        self.overwrite = overwrite
        self.project_name = project_name
        self.max_model_size = max_model_size
        self.max_trials = max_trials
        self.metrics = metrics
        self.seed = seed
        self.tuner = tuner

    def image_classification(
        self, num_classes: int = None, multi_label: bool = False, **kwargs
    ) -> ak.ImageClassifier:
        """Image Classification.

        Description

        # Arguments:
            num_classes (int, optional): Number of classes. Defaults to None.
            multi_label (bool, optional): The target is multi-labeled. Defaults to False.

        Returns:
            ak.ImageClassifier: AutoKERAS image classification class.
        """
        return ak.ImageClassifier(
            num_classes=num_classes,
            multi_label=multi_label,
            loss=self.loss,
            metrics=self.metrics,
            project_name=self.project_name,
            max_trials=self.max_trials,
            directory=self.directory,
            objective=self.objective,
            tuner=self.tuner,
            overwrite=self.overwrite,
            seed=self.seed,
            max_model_size=self.max_model_size,
            **kwargs,
        )

    def image_regression(self, output_dim: int = None, **kwargs) -> ak.ImageRegressor:
        """Image Regression.

        Args:
            output_dim (int, optional): Number of output dimensions. Defaults to None.

        Returns:
            ak.ImageRegressor: AutoKERAS image regression class.
        """
        return ak.ImageRegressor(
            output_dim=output_dim,
            loss=self.loss,
            metrics=self.metrics,
            project_name=self.project_name,
            max_trials=self.max_trials,
            directory=self.directory,
            objective=self.objective,
            tuner=self.tuner,
            overwrite=self.overwrite,
            seed=self.seed,
            max_model_size=self.max_model_size,
            **kwargs,
        )

    def text_classification(
        self, num_classes: int = None, multi_label: bool = False, **kwargs
    ) -> ak.TextClassifier:
        """Text Classification.

        Args:
            num_classes (int, optional): Number of classes. Defaults to None.
            multi_label (bool, optional): The target is multi-labeled. Defaults to False.


        Returns:
            ak.TextClassifier: AutoKERAS text classification class.
        """
        return ak.TextClassifier(
            num_classes=num_classes,
            multi_label=multi_label,
            loss=self.loss,
            metrics=self.metrics,
            project_name=self.project_name,
            max_trials=self.max_trials,
            directory=self.directory,
            objective=self.objective,
            tuner=self.tuner,
            overwrite=self.overwrite,
            seed=self.seed,
            max_model_size=self.max_model_size,
            **kwargs,
        )

    def text_regression(self, output_dim: int = None, **kwargs) -> ak.TextRegressor:
        """Text Regression.

        Args:
            output_dim (int, optional): Number of output dimensions. Defaults to None.

        Returns:
            ak.TextRegressor: AutoKERAS text regression class.
        """
        return ak.TextRegressor(
            output_dim=output_dim,
            loss=self.loss,
            metrics=self.metrics,
            project_name=self.project_name,
            max_trials=self.max_trials,
            directory=self.directory,
            objective=self.objective,
            tuner=self.tuner,
            overwrite=self.overwrite,
            seed=self.seed,
            max_model_size=self.max_model_size,
            **kwargs,
        )

    def data_classification(
        self,
        column_names: list = None,
        column_types: dict = None,
        num_classes: int = None,
        multi_label: bool = False,
        **kwargs,
    ) -> ak.StructuredDataClassifier:
        """Data Classification.

        Args:
            column_names (list, optional): Name of the columns. Defaults to None.
            column_types (dict, optional): Type of the columns. Defaults to None.
            num_classes (int, optional): Number of classes. Defaults to None.
            multi_label (bool, optional): The target is multi-labeled. Defaults to False.

        Returns:
            ak.StructuredDataClassifier: AutoKERAS data classification class.
        """
        return ak.StructuredDataClassifier(
            column_names=column_names,
            column_types=column_types,
            num_classes=num_classes,
            multi_label=multi_label,
            loss=self.loss,
            metrics=self.metrics,
            project_name=self.project_name,
            max_trials=self.max_trials,
            directory=self.directory,
            objective=self.objective,
            tuner=self.tuner,
            overwrite=self.overwrite,
            seed=self.seed,
            max_model_size=self.max_model_size,
            **kwargs,
        )

    def data_regression(
        self,
        column_names: list = None,
        column_types: dict = None,
        output_dim: int = None,
        **kwargs,
    ) -> ak.StructuredDataRegressor:
        """Data Regression.

        Args:
            column_names (list, optional): Name of the columns. Defaults to None.
            column_types (dict, optional): Type of the columns. Defaults to None.
            output_dim (int, optional): Number of output dimensions. Defaults to None.

        Returns:
            ak.StructuredDataRegressor: AutoKERAS data regression class.
        """
        return ak.StructuredDataRegressor(
            column_names=column_names,
            column_types=column_types,
            output_dim=output_dim,
            loss=self.loss,
            metrics=self.metrics,
            project_name=self.project_name,
            max_trials=self.max_trials,
            directory=self.directory,
            objective=self.objective,
            tuner=self.tuner,
            overwrite=self.overwrite,
            seed=self.seed,
            max_model_size=self.max_model_size,
            **kwargs,
        )

    def timeseries_forecaster(
        self,
        column_names: list = None,
        column_types: dict = None,
        output_dim: int = None,
        lookback: int = None,
        predict_from: int = 1,
        predict_until: int = None,
        **kwargs,
    ) -> ak.TimeseriesForecaster:
        """Forecast of timeseries.

        Args:
            column_names (list, optional): Name of the columns. Defaults to None.
            column_types (dict, optional): Type of the columns. Defaults to None.
            output_dim (int, optional): Number of output dimensions. Defaults to None.
            lookback (int, optional): History range for each prediction. Defaults to None.
            predict_from (int, optional): Starting point for the time series. Defaults to 1.
            predict_until (int, optional): Finishing point for the time series. Defaults to None.

        Returns:
            ak.TimeseriesForecaster: AutoKERAS timeseries forecast class.
        """
        return ak.TimeseriesForecaster(
            column_names=column_names,
            column_types=column_types,
            output_dim=output_dim,
            lookback=lookback,
            predict_from=predict_from,
            predict_until=predict_until,
            loss=self.loss,
            metrics=self.metrics,
            project_name=self.project_name,
            max_trials=self.max_trials,
            directory=self.directory,
            objective=self.objective,
            tuner=self.tuner,
            overwrite=self.overwrite,
            seed=self.seed,
            max_model_size=self.max_model_size,
            **kwargs,
        )

    def multi_model(self, inputs: list, outputs: list, **kwargs) -> ak.AutoModel:
        """Composition of multi-model of different types of networks.

        Args:
            inputs (list): A list of `input node instances` of the AutoModel.
            outputs (list): A list of `output node instances` of the AutoModel.
        Returns:
            ak.AutoModel: AutoKERAS AutoModel class.
        """
        return ak.AutoModel(
            inputs=inputs,
            outputs=outputs,
            project_name=self.project_name,
            max_trials=self.max_trials,
            directory=self.directory,
            objective=self.objective,
            tuner=self.tuner,
            overwrite=self.overwrite,
            seed=self.seed,
            max_model_size=self.max_model_size,
        )

    @staticmethod
    def load_model(model_name: str = "model_autokeras") -> Callable:
        """Loading AutoKERAS project.

        Args:
            model_name (str, optional): Path of the model to load. Defaults to "model_autokeras".

        Returns:
            Callable: Any callable AutoKERAS project
        """
        return load_model(f"{model_name}", custom_objects=ak.CUSTOM_OBJECTS)


class AutoMLRoutines:
    """The fitting routine for the different models of `AutoMLModels`."""

    def __init__(self, model: AutoMLModels) -> None:
        """Defining the initial AutoKERAS model.

        Args:
            model (AutoMLModels): Current used model like: AutoMLModels()timeseries_forecast()
        """
        self.model = model

    def fit_model(
        self,
        x_train: Any,
        y_train: Any,
        batch_size: int = 32,
        epochs: int = None,
        callbacks: list = None,
        validation_split: float = 0.2,
        validation_data: Any = None,
        **kwargs,
    ) -> None:
        """Fitting of the auto machine learning model.

        Args:
            x_train (Any): Training data of `x` as 2d-array
            y_train (Any): Training data of `y` as 1d- or 2d-array
            batch_size (int, optional): Size of the batch. Defaults to 32.
            epochs (int, optional): The number of epochs to train each model during the search. Defaults to None.
            callbacks (list, optional): Applied Keras callbacks. Defaults to None.
            validation_split (float, optional): Fraction of the training data to be used as validation data. Defaults to 0.2.
            validation_data (Any, optional): Data on which to evaluate the loss and any model metrics at the end of each epoch. Defaults to None.
        """
        self.model.fit(
            x=x_train,
            y=y_train,
            batch_size=batch_size,
            epochs=epochs,
            callbacks=callbacks,
            validation_split=validation_split,
            validation_data=validation_data,
            **kwargs,
        )
        return self.model


class AutoMLPipeline:
    """The Pipeline structure for training and testing of auto machine learning models."""

    def __init__(self, train: Any) -> None:
        """Initialization of the pipeline.
        Args:
            train (Any): Any type of auto machine learning model or its attribute.
        """
        self._train = train
        self.automl_model = {"model": None, "prediction": None, "evaluation": None}

    @property
    def train(self) -> Any:
        """Return the training results.
        Returns:
            Any: Any type of auto machine learning model or its attribute.
        """
        return self._train

    @train.setter
    def train(self, train: Any) -> None:
        """Setting of the training results.

        Args:
            train (Any): Any type of auto machine learning model or its attribute.
        """

    def run_automl(self):
        """Perform the job and update the auto machine learning model."""
        self.automl_model = self._train.perform_job(self.automl_model)

    @property
    def return_automl(self) -> dict:
        """Return auto machine learning model.

        Returns:
            dict: Dictionary with the keys: `model` (AutoKERAS class), `prediction` and `evaluation`.
        """
        return self.automl_model


class Procedure(ABC):
    """Abstract class of the training procedure.

    Args:
        ABC (class): Helper class that provides a standard way to create an ABC using inheritance.
    """

    @abstractmethod
    def perform_job(self):
        """Abstractmethod of perform_job."""
        pass


class ImageClassification(Procedure):
    """ImageClassification.

    Args:
        Procedure (ABC):  Helper class that provides a standard way to create an ABC using inheritance.
    """

    def perform_job(self, automl_model: dict) -> dict:
        _ = automl_model
        model = AutoMLModels().image_classification()
        return {"model": AutoMLRoutines(model), "prediction": None, "evaluation": None}


class ImageRegression(Procedure):
    """ImageRegression.

    Args:
        Procedure (ABC):  Helper class that provides a standard way to create an ABC using inheritance.
    """

    def perform_job(self, automl_model: dict) -> dict:
        _ = automl_model
        model = AutoMLModels().image_regression()
        return {"model": AutoMLRoutines(model), "prediction": None, "evaluation": None}


class TextClassification(Procedure):
    """TextClassification.

    Args:
        Procedure (ABC):  Helper class that provides a standard way to create an ABC using inheritance.
    """

    def perform_job(self, automl_model: dict) -> dict:
        _ = automl_model
        model = AutoMLModels().text_classification()
        return {"model": AutoMLRoutines(model), "prediction": None, "evaluation": None}


class TextRegression(Procedure):
    """TextRegression.

    Args:
        Procedure (ABC):  Helper class that provides a standard way to create an ABC using inheritance.
    """

    def perform_job(self, automl_model: dict) -> dict:
        _ = automl_model
        model = AutoMLModels().text_regression()
        return {"model": AutoMLRoutines(model), "prediction": None, "evaluation": None}


class DataClassification(Procedure):
    """DataClassification [summary]

    Args:
        Procedure (ABC):  Helper class that provides a standard way to create an ABC using inheritance.
    """

    def perform_job(self, automl_model: dict) -> dict:
        _ = automl_model
        model = AutoMLModels().data_classification()
        return {"model": AutoMLRoutines(model), "prediction": None, "evaluation": None}


class DataRegression(Procedure):
    """DataRegression [summary]

    Args:
        Procedure (ABC):  Helper class that provides a standard way to create an ABC using inheritance.
    """

    def perform_job(self, automl_model: dict) -> dict:
        _ = automl_model
        model = AutoMLModels().data_regression()
        return {"model": AutoMLRoutines(model), "prediction": None, "evaluation": None}


class TimeseriesForecaster(Procedure):
    """TimeseriesForecaster [summary]

    Args:
        Procedure (ABC):  Helper class that provides a standard way to create an ABC using inheritance.
    """

    def perform_job(self, automl_model: dict) -> dict:
        _ = automl_model
        model = AutoMLModels().timeseries_forecaster()
        return {"model": AutoMLRoutines(model), "prediction": None, "evaluation": None}


class MultiModel(Procedure):
    """MultiModel [summary]

    Args:
        Procedure (ABC):  Helper class that provides a standard way to create an ABC using inheritance.
    """

    def perform_job(self, automl_model: dict) -> dict:
        _ = automl_model
        model = AutoMLModels().multi_model()
        return {"model": AutoMLRoutines(model), "prediction": None, "evaluation": None}


class AutoMLFit(Procedure):
    """Auto Machine Learning Routine for fitting.


    Args:
        Procedure (ABC):  Helper class that provides a standard way to create an ABC using inheritance.
    """

    def __init__(
        self,
        x_train: Any,
        y_train: Any,
        batch_size: int = 32,
        epochs: int = None,
        callbacks: list = None,
        validation_split: float = 0.2,
        validation_data: Any = None,
        **kwargs,
    ) -> None:
        """Initialization the Auto Machine Learning Routine for fitting.

        Args:
            x_train (Any): Training data of `x` as 2d-array
            y_train (Any): Training data of `y` as 1d- or 2d-array
            batch_size (int, optional): Size of the batch. Defaults to 32.
            epochs (int, optional): The number of epochs to train each model during the search. Defaults to None.
            callbacks (list, optional): Applied Keras callbacks. Defaults to None.
            validation_split (float, optional): Fraction of the training data to be used as validation data. Defaults to 0.2.
            validation_data (Any, optional): Data on which to evaluate the loss and any model metrics at the end of each epoch. Defaults to None.
        """
        self.x_train = x_train
        self.y_train = y_train
        self.batch_size = batch_size
        self.epochs = epochs
        self.callbacks = callbacks
        self.validation_split = validation_split
        self.validation_data = validation_data
        self.kwargs = kwargs

    def perform_job(self, automl_model: dict):
        """Perform the of job of class `AutoMLPredict`.

        Args:
            automl_model (dict): Dictionary with the keys: `model` (AutoKERAS class), `prediction` and `evaluation`.

        Returns:
            dict: Updated dictionary for key `model`.
        """
        return {
            "model": automl_model["model"].fit_model(
                x_train=self.x_train,
                y_train=self.y_train,
                epochs=self.epochs,
                callbacks=self.callbacks,
                validation_split=self.validation_split,
                validation_data=self.validation_data,
                **self.kwargs,
            ),
            "prediction": None,
            "evaluation": None,
        }


class AutoMLPredict(Procedure):
    """Auto Machine Learning Routine for predicting.

    Args:
        Procedure (ABC):  Helper class that provides a standard way to create an ABC using inheritance.
    """

    def __init__(
        self,
        x_train: Any,
        batch_size: int = 32,
        **kwargs,
    ) -> None:
        """Initialization the Auto Machine Learning Routine for predicting.

        Args:
            x_train (Any): Training data of `x` as 2d-array
            batch_size (int, optional): Size of the batch. Defaults to 32.
        """
        self.x_train = x_train
        self.batch_size = batch_size
        self.kwargs = kwargs

    def perform_job(self, automl_model: dict) -> dict:
        """Perform the of job of class `AutoMLPredict`.

        Args:
            automl_model (dict): Dictionary with the keys: `model` (AutoKERAS class), `prediction` and `evaluation`.

        Returns:
            dict: Updated dictionary for key `prediction`.
        """
        return {
            "model": automl_model["model"],
            "prediction": automl_model["model"].predict(
                x=self.x_train, batch_size=self.batch_size, **self.kwargs
            ),
            "evaluation": automl_model["evaluation"],
        }


class AutoMLEvaluate(Procedure):
    """Auto Machine Learning Routine for evaluating.

    Args:
        Procedure (ABC):  Helper class that provides a standard way to create an ABC using inheritance.
    """

    def __init__(
        self, x_test: Any, y_test: Any = None, batch_size: int = 32, **kwargs
    ) -> None:
        """Initialization the Auto Machine Learning Routine for evaluating.

        Args:
            x_test (Any): Testing data of `x` as 2d-array
            y_test (Any, optional): Testing data of `y` as 1d- or 2d-array. Defaults to None.
            batch_size (int, optional): Size of the batch. Defaults to 32.
        """
        self.x_test = x_test
        self.y_test = y_test
        self.batch_size = batch_size
        self.kwargs = kwargs

    def perform_job(self, automl_model: dict) -> dict:
        """Perform the of job of class `AutoMLEvaluate`.

        Args:
            automl_model (dict): Dictionary with the keys: `model` (AutoKERAS class), `prediction` and `evaluation`.

        Returns:
            dict: Updated dictionary for key `evaluation`.
        """
        return {
            "model": automl_model["model"],
            "prediction": automl_model["prediction"],
            "evaluation": automl_model["model"].evaluate(
                x=self.x_test,
                y=self.y_test,
                batch_size=self.batch_size,
                **self.kwargs,
            ),
        }


class AutoMLSave(Procedure):
    """Auto Machine Learning Routine for saving

    Args:
        Procedure (ABC):  Helper class that provides a standard way to create an ABC using inheritance.
    """

    def __init__(self, model_name: str) -> None:
        """Initialization of saving the model.

        Args:
            model_name (str): Name of the Auto Machine Learning model to save.
        """
        self.model_name = model_name

    def perform_job(self, automl_model: dict):
        """Perform the of job of class `AutoMLSave`.

        Args:
            automl_model (dict): [description]
        """
        _model = automl_model.export_model()
        _model.save(f"{self.model_name}", save_format="tf")
