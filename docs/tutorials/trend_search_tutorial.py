"""
## Building a search trend dataframe

Trend search can be differs roughly in two major criteria:

1. An *active* driven search by using `keyword` like "Corona", "S&P 500", "Hope"
2. A *passive* driven search by using the community feedback to gather actual topics.

In this context, the `trend-search`-module is a designed as a [builder model](https://en.wikipedia.org/wiki/Builder_pattern) to add much searches as required in a collection `{}`.
"""

"""shell
pip install git+https://github.com/AI2Business/ai2business.git
"""

"""
### Loading the model `trends_collector`

"""

from ai2business.kpi_collector import trends_collector

"""

Setup the search with the keyword list and write it into the `builder`

"""

keyword_list: list = ["Corona", "S&P 500", "Hope"]
trends = trends_collector.TrendsCollector()
builder = trends_collector.DesignerTrendsCollector(keyword_list=keyword_list)
trends.builder = builder

"""

### Add the `trend-search` functions, in this particular case:

1. Searching over time
2. Searching in a special area
3. Searching for related queries
4. Searching for realted topics

All the information will be generated and stored in the `builder`.

"""

trends.find_interest_over_time()
trends.find_interest_by_region()
trends.find_related_topics()
trends.find_related_queries()

"""

With the use of the builder's property-attribute, a dictionary will be returned consisting of pandas-data frames and dictionaries. The key-names are the function names.

```python
>>> results = builder.trends.return_product
>>> result.keys()
... dict_keys(['get_interest_over_time', 'get_interest_by_region', 'get_related_topics', 'get_related_queries'])

```

Note
----

It is important to immediately transfer the return value to a variable because a second return will return an empty dictionary.


### Return the objects of the `builder` in the dictionary

"""

results = builder.trends.return_product

print(results.keys())

print(results)

"""

Due to the fact that the dataframes are pandas-dataframes, all pandas commands can be easily applied, like plot, for example.

"""

results["get_interest_over_time"].plot(title="Search Trend of the Big Three (per time)")

results["get_interest_by_region"].plot.bar(
    title="Search Trend of the Big Three (per location)", figsize=(28, 12)
)

"""

Also, the stored data in a dictionary are saved as pandas dataframe so that the trend results can be then easily analyzed again the default commands of pandas.

"""

for key in keyword_list:
    results["get_related_queries"][key]["top"].plot.bar(
        x="query", title=f"Related Queries for {key}"
    )

"""

Finally, also non-visual commands like correlation analysis are working fine.

"""

results["get_interest_by_region"].corr("pearson")

results["get_interest_by_region"].corr("kendall")

results["get_interest_by_region"].corr("spearman")
