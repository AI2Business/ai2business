[**View in Colab**](https://colab.research.google.com/github/ai2business/ai2business/blob/main/docs/ipynb/timeseries_forecast_tutorial.ipynb)   &nbsp; &nbsp;[**GitHub source**](https://github.com/ai2business/ai2business/blob/main/docs/tutorials/timeseries_forecast_tutorial.py)

## Runing a small timeseries forecast

Before running a time series forecast, the initial data set has to be generated first via oneliner. The online `four_step_search` combines four types of trend search:

1. Overtime
2. By regions
3. By related topics
4. By related queries

However, this example is only focusing on the dateframe from *Overtime*.



```python
!pip install git+https://github.com/AI2Business/ai2business.git

```


```python
from ai2business.macros import oneliner

```

Hence, search trend for the years "2017", "2018", "2019", and "2020" will be generated and plotted.

### Note

A dependency between the years is obviously given, even if single event trigger breakouts.



```python
keyword_list: list = ["2017", "2018", "2019", "2020"]
timeframe = oneliner.TrendSearch.four_step_search(keyword_list=keyword_list)
timeframe["get_interest_over_time"].plot()

```

And the Pearson-correlation shows the negative linear dependency between the current and previous year.



```python
timeframe["get_interest_over_time"].corr()

dataset = timeframe["get_interest_over_time"].drop(columns="isPartial")

print(dataset)

```

### Loading the automl modul.



```python
from sklearn.model_selection import train_test_split

from ai2business.ai_engines import automl_neural_network as an

```

### Setup the Timeseries Forecaster.



```python
x_train, y_train, x_test, y_test = train_test_split(
    dataset.iloc[:, 0:2].values,
    dataset.iloc[:, 3].values,
    test_size=0.33,
    random_state=42,
)
context = an.AutoMLPipeline(an.TimeseriesForecaster())
context.run_automl()

```

### Fitting the Timeseries Forecaster.



```python
context.train = an.AutoMLFit(x_train, y_train, batch_size=32, epochs=1)
context.run_automl()

```

### Evaluate the Timeseries Forecaster.



```python
context.train = an.AutoMLEvaluate(x_test, y_test, batch_size=32)
context.run_automl()

```
