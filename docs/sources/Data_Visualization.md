<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L718)</span>

### DataVisualization


```python
ai2business.visualization.data_visualization.DataVisualization()
```


DataVisualization is in charge of executing the functions.

During the execution, `DataVisualization` can construct several product
variations using the same building steps.

!!! example "General introduction into using plot-functions!"
    ```python
    >>> from ai2business.macros import oneliner as one
    >>> from ai2business.visualization import data_visualization as dav

    >>> df_dict_years = one.TrendSearch.four_step_search(keyword_list=[ "2017", "2018", "2019", "2020", "2021", ])

    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(df_dict_years["get_interest_over_time"])
    >>> data.builder = builder

    # Here any kind of plot function can be called
    >>> data.lineplot()
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
!!! tip "Activating hidden functions of the `seaborn`-module!"
    Due to the seaborn module's complexity, only the significant __four__
    variables (x_label, y_label, hue, palette) are defined in
    `DesignerDataVisualization`. However, all other seaborn-module options
    can be individual activated by`**kwargs` in each function separately.


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L771)</span>

### visual_missing_data


```python
DataVisualization.visual_missing_data(n_columns=0, per_columns=0.0, cmap="seismic", **kwargs)
```


Visualizing possible missing data.

Args:
    n_columns (int, optional): The cap on the number of columns to include in the filtered DataFrame. Defaults to 0.
    per_columns (float, optional): The cap on the percentage fill of the columns in the filtered DataFrame. Defaults to 0.0.
    cmap (str, optional): The color of the heatmap. Defaults to "seismic".

!!! note "Visualization of nullity results, respectively, missing values!"

    Possible missing data will be visualized by:

    1. nullity matrix highlights out patterns and structures in data completion.

        ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/nullity/get_nullity_matrix_bc6141f519e4eea9e6a0d5fe84115d65.png?raw=true){: loading=lazy }

    2. nullity bar shows the available data as a series of single bars.

        ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/nullity/get_nullity_bar_9918e972a769781d322ba1e18fe8f86c.png?raw=true){: loading=lazy }

    3. nullity heatmap point out the correlation between the presence and absence data.

        ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/nullity/get_nullity_heatmap_d46e69f559bd7b713b7a6c3ceb0f9968.png?raw=true){: loading=lazy }

    4. nullity dendrogram visualize the correlate variable completion.

        ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/nullity/get_nullity_dendrogram_15a148832cd43d6d249d56671a0fab6f.png?raw=true){: loading=lazy }

    For more information see: [https://github.com/ResidentMario/missingno](https://github.com/ResidentMario/missingno)


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L831)</span>

### lineplot


```python
DataVisualization.lineplot(**kwargs)
```


Create a given line plot based on seaborn.
!!! example "Line Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.lineplot()
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_lineplot_d1f5c1875c5fac03668674031f8af390.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L847)</span>

### pointplot


```python
DataVisualization.pointplot(**kwargs)
```


Create a given point plot based on seaborn.
!!! example "Point Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.pointplot()
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/appearance/get_pointplot_3216f41c8e8eb4977ab1870368daea37.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L863)</span>

### scatterplot


```python
DataVisualization.scatterplot(**kwargs)
```


Create a given scatter plot based on seaborn.
!!! example "Scatter Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.scatterplot()
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_scatterplot_b14dfb01022e343d587d4ba4b39ee56c.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L879)</span>

### swarmplot


```python
DataVisualization.swarmplot(**kwargs)
```


Create a given swarm plot based on seaborn.
!!! example "Swarm Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.swarmplot()
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_swarmplot_fa34ed63066eb6800f6e4300d3787da2.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L895)</span>

### distributionplot


```python
DataVisualization.distributionplot(**kwargs)
```


Create a given distribution plot based on seaborn.
!!! example "Distribution Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.distributionplot()
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_distributionplot_68a2aea492d392e6f1b81420cfed43ef.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L910)</span>

### relationalplot


```python
DataVisualization.relationalplot(**kwargs)
```


Create a given relational plot based on seaborn.
!!! example "Relational Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.relationalplot()
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_relationalplot_2ca3df8a2c1238c50f00e3822f3b94f1.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L926)</span>

### categoryplot


```python
DataVisualization.categoryplot(**kwargs)
```


Create a given category plot based on seaborn.
!!! example "Category Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.categoryplot()
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_categoryplot_3628ede87a6e217e30435bdcd9a9ce3b.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L942)</span>

### boxplot


```python
DataVisualization.boxplot(multiboxen=False, **kwargs)
```


Create a given box plot based on seaborn.

Args:
    multiboxen (bool, optional): Allows to draw multi boxen per object. Defaults to False.

!!! example "Box Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.boxplot(multiboxen=False)
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_boxplot_a0023f9b0bc21741142a69f40baf5c43.png?raw=true){: loading=lazy }
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.boxplot(multiboxen=True)
    >>> builder.data_figure.save_all_figures(folder=folder)
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_boxenplot_56ae2969afd82d78d7585b14e938df29.png?raw=true){: loading=lazy }
    ```


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L974)</span>

### stripplot


```python
DataVisualization.stripplot(**kwargs)
```


Create a given strip plot based on seaborn.
!!! example "Strip Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.stripplot()
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_stripplot_4ce7af555a14c09c6f48ab7b13990dd7.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L990)</span>

### hexagonplot


```python
DataVisualization.hexagonplot(**kwargs)
```


Create a given hexagon plot based on seaborn.
!!! example "Hexagonal Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.hexagonalplot()
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_hexagonplot_bee62ec100c2ea9dc2bc6e71d18cf3d6.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L1006)</span>

### histogramplot


```python
DataVisualization.histogramplot(**kwargs)
```


Create a given histogram plot based on seaborn.
!!! example "Histogram Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.histogramplot()
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/appearance/get_histogramplot_ceed49b02f48ef9f57e863fbcc98f5dd.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L1022)</span>

### violinplot


```python
DataVisualization.violinplot(**kwargs)
```


Create a given violin plot based on seaborn.
!!! example "Violin Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.violinplot()
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_violinplot_9956ae30ad1f00a5b5869a4da95754d9.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L1038)</span>

### residualplot


```python
DataVisualization.residualplot(**kwargs)
```


Create a given residual plot based on seaborn.
!!! example "Residual Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.residualplot()
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_violinplot_9956ae30ad1f00a5b5869a4da95754d9.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L1054)</span>

### regressionplot


```python
DataVisualization.regressionplot(map=False, **kwargs)
```


Create a given regression plot based on seaborn.

Args:
    map (bool, optional): Creates the regression plot as map. Defaults to False.

!!! example "Regression Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.regressionplot(map=False)
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_regressionplot_a1987483cda51c9c884abd44b4def6ef.png?raw=true){: loading=lazy }
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.regressionmapplot(map=True)
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_density_mapplot_aa27faf44d09f3cf3e1ca549bfe12d1b.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L1087)</span>

### densitymap


```python
DataVisualization.densitymap(kde=False, **kwargs)
```


Create a given density map based on seaborn.

Args:
    kde (bool, optional): Plots the density as kernel density. Defaults to False.

!!! example "Density Map Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.kerneldensitymapplot(map=False)
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_kerneldensity_mapplot_da7caa95343a14497e78afff0fb304fb.png?raw=true){: loading=lazy }
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.densitymapplot(map=True)
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_density_mapplot_aa27faf44d09f3cf3e1ca549bfe12d1b.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L1120)</span>

### clustermap


```python
DataVisualization.clustermap(method="pearson", min_periods=1, **kwargs)
```


Create a given cluster map based on seaborn.

Args:
    method (str, optional): Method of the correlation type ('pearson', 'kendall', 'spearman' or callable method of correlation). Defaults to "pearson".
    min_periods (int, optional): Minimum number of observations required per pair of columns to have a valid result. Defaults to 1.

!!! example "Cluster Map Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.clustermapplot()
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_cluster_mapplot_212509d11bc11b8d2de8e09a98760a5a.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L1145)</span>

### heatmap


```python
DataVisualization.heatmap(**kwargs)
```


Create a given heat map based on seaborn.
!!! example "Heat Map Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.heatmapplot()
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_heat_mapplot_6efd63f601845f3b57c63a82a360464d.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L1161)</span>

### correlationmap


```python
DataVisualization.correlationmap(diagonal=False, method="pearson", min_periods=1, **kwargs)
```


Create a given correlation map based on seaborn.

Args:
    diagonal (bool, optional): Only the lower diagonal elements will be plotted. Defaults to False.
    method (str, optional): Method of the correlation type ('pearson', 'kendall', 'spearman' or callable method of correlation). Defaults to "pearson".
    min_periods (int, optional): Minimum number of observations required per pair of columns to have a valid result. Defaults to 1.

!!! example "Correlation Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.diagonalcorrelationplot(map=False)
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_diagonal_correlationplot_edcbab55666e77860eebdc5b73d45b6d.png?raw=true){: loading=lazy }
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.correlationplot(map=True)
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_correlationplot_227d61e793e336cf86e41ec7b6ec33d6.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L1205)</span>

### pairmap


```python
DataVisualization.pairmap(complex=False, **kwargs)
```


Create a pair map based on seaborn.

Args:
    complex (bool, optional): Turn on the `get_complex_pairmapplot`. Defaults to False.

!!! example "Pair Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.complexpairmapplot(map=False)
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_complex_pairmapplot_fb3ba50582340191e6f1b27328d60f7f.png?raw=true){: loading=lazy }
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.pairmapplot(map=True)
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_pairmapplot_292a3bb10c014dc2dd57a6a12eb608d3.png?raw=true){: loading=lazy }


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/visualization/data_visualization.py#L879)</span>

### swarmplot


```python
DataVisualization.swarmplot(**kwargs)
```


Create a given swarm plot based on seaborn.
!!! example "Swarm Plot"
    ```python
    >>> from ai2business.visualization import data_visualization as dav
    >>> data = dav.DataVisualization()
    >>> builder = dav.DesignerDataVisualization(dataframe)
    >>> data.builder = builder
    >>> data.swarmplot()
    >>> builder.data_figure.save_all_figures(folder=folder)
    ```
    ![Placeholder](https://github.com/AI2Business/ai2business/blob/main/docs/images/plottypes/get_swarmplot_fa34ed63066eb6800f6e4300d3787da2.png?raw=true){: loading=lazy }


----

