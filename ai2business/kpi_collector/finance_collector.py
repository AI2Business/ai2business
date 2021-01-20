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
"""Finance Collection Module: Collecting Financial and Ticker Trends via http-API."""
from abc import ABC, abstractmethod, abstractproperty, abstractstaticmethod

import pandas as pd
import yfinance as yf
from typing import Callable


class BuilderFinanceCollector(ABC):
    """BuilderTrendsCollector contains the abstract properties and methods.

    `BuilderTrendsCollector` specifies the properties and methods for creating the
    different parts of the `DesignerFinanceCollector` objects.

    Args:
        ABC (class): Helper class that provides a standard way to create an ABC using inheritance.
    """

    @abstractproperty
    def stock(self) -> None:
        """Abstract property of stock."""

    @abstractstaticmethod
    def all_trickers() -> None:
        """Abstract staticmethod of all_tickers."""

    @abstractmethod
    def get_chart_history(self) -> None:
        """Abstract method of get_chart_history."""

    @abstractmethod
    def get_isin_code(self) -> None:
        """Abstract method of get_isin_code."""

    @abstractmethod
    def get_major_holders(self) -> None:
        """Abstract method of get_major_holders."""

    @abstractmethod
    def get_institutional_holders(self) -> None:
        """Abstract method of get_institutional_holders."""

    @abstractmethod
    def get_mutualfund_holders(self) -> None:
        """Abstract method of get_mutualfund_holders."""

    @abstractmethod
    def get_dividends(self) -> None:
        """Abstract method of get_dividends."""

    @abstractmethod
    def get_splits(self) -> None:
        """Abstract method of get_splits."""

    @abstractmethod
    def get_actions(self) -> None:
        """Abstract property of get_actions."""

    @abstractmethod
    def get_info(self) -> None:
        """Abstract method of get_info."""

    @abstractmethod
    def get_calendar(self) -> None:
        """Abstract method of get_calendar."""

    @abstractmethod
    def get_recommendations(self) -> None:
        """Abstract method of get_recommendations."""

    @abstractmethod
    def get_earnings(self) -> None:
        """Abstract method of get_earnings."""

    @abstractmethod
    def get_quarterly_earnings(self) -> None:
        """Abstract method of get_quarterly_earnings."""

    @abstractmethod
    def get_financials(self) -> None:
        """Abstract method of get_financials."""

    @abstractmethod
    def get_quarterly_financials(self) -> None:
        """Abstract method of get_quarterly_financials."""

    @abstractmethod
    def get_balancesheet(self) -> None:
        """Abstract method of get_balancesheet."""

    @abstractmethod
    def get_quarterly_balancesheet(self) -> None:
        """Abstract method of get_quarterly_balancesheet."""

    @abstractmethod
    def get_cashflow(self) -> None:
        """Abstract method of get_cashflow."""

    @abstractmethod
    def get_quarterly_cashflow(self) -> None:
        """Abstract method of get_quarterly_cashflow."""

    @abstractmethod
    def get_sustainability(self) -> None:
        """Abstract method of get_sustainability."""

    @abstractmethod
    def get_options(self) -> None:
        """Abstract method of get_options."""


class FinanceProduct:
    """FinanceProduct contains the dictionary and the return value of it."""

    def __init__(self) -> None:
        """Initialization of FinanceProduct."""
        self.product_parts = {}

    def add_product(self, key: Callable, value: pd.DataFrame or dict) -> None:
        """Add the components of the trend search to the dictionary.

        Args:
            key (Callable): Used trend search function
            value (pd.DataFrame or dict): Return value as dataframe or dictionary of the function.
        """
        self.product_parts[key.__name__] = value

    @property
    def list_product_parts(self) -> str:
        """List of the product parts in the dictionary."""
        return f"Product parts: {', '.join(self.product_parts)}"

    @property
    def return_product(self) -> dict:
        """Returns the product as a dictionary

        Returns:
            dict: The product dictionary contains the product and ist function name as `key`.
        """
        return self.product_parts


class DesignerFinanceCollector(BuilderFinanceCollector):
    """DesignerTrendsCollector contains the specific implementation of
    `BuilderFinanceCollector`.

    `DesignerTrendsCollector` contains the specific implementation of
    `BuilderFinanceCollector` based on the external library `yfinance`.

    Args:
        BuilderFinanceCollector (class): Abstract class that provides the implementations of the properties and methods.
    """

    def __init__(self, keyword_list: list) -> None:
        """Initialization of DesignerFinanceCollector

        Args:
            keyword_list (list): Keyword-list with the tickers to search for.
        """
        self.keyword_list = keyword_list
        self.tickers = {str(isin): yf.Ticker(isin) for isin in self.keyword_list}
        self.df = pd.DataFrame()
        self.dict = {}
        self.reset()

    def reset(self) -> None:
        """Reset the product to empty."""
        self._product = FinanceProduct()

    @property
    def stock(self) -> FinanceProduct:
        """Return the trend results.

        Returns:
            FinanceProduct: (class) FinanceProduct contains the dictionary and the return value of it.
        """
        product = self._product
        self.reset()
        return product

    @staticmethod
    def all_trickers(
        tickers: yf.Tickers, keyword_list: list, func: str
    ) -> pd.DataFrame:
        """all_trickers [summary]

        [extended_summary]

        Args:
            tickers (yf.Tickers): Finance market data downloader.
            keyword_list (list): Keyword-list with the tickers to search for.
            func (str): Specific class as string.

        """
        return {
            keyword: getattr(getattr(tickers.tickers, keyword), func)
            for keyword in keyword_list
        }

    def get_chart_history(
        self,
        period: str,
        interval: str,
        start: str,
        end: str,
        prepost: bool,
        actions: bool,
        auto_adjust: bool,
        proxy: str,
        threads: bool,
        group_by: str,
        progress: bool,
        **kwargs,
    ) -> None:
        """Request the history of the chart for given tickers.

        Args:
            period (str): Period of the chart history; valid options: `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, or `ytd,max`. It can either be used the `period`-parameter or the combination of `start`- and `end`-parameter.
            interval (str): Interval, respectively, time step in the period; valid options: `1m`, `2m`, `5m`, `15m`, `30m`, `60m`, `90m`, `1h`, `1d`, `5d`, `1wk`, `1mo`, or `3mo`. The intraday data cannot extend last 60 days.
            start (str): Download start date string (YYYY-MM-DD) or _datetime.
            end (str): Download end date string (YYYY-MM-DD) or _datetime.
            prepost (bool): Group by 'ticker' or 'column'.
            actions (bool): Including Pre and Post market data in results.
            auto_adjust (bool): Adjusting all OHLC automatically.
            proxy (str): Downloading the dividend plus stock splits data.
            threads (bool): Specifying the number of download threads.
            group_by (str): Grouping by ticker or column.
            progress (bool): Showing progress bar.
        """
        self.df = self.tickers.history(
            period=period,
            interval=interval,
            start=start,
            end=end,
            prepost=prepost,
            actions=actions,
            auto_adjust=auto_adjust,
            proxy=proxy,
            threads=threads,
            group_by=group_by,
            progress=progress,
            **kwargs,
        )

    def get_isin_code(self) -> None:
        """Request for the International Securities Identification Number (ISIN)."""
        self.dict = self.all_trickers(
            tickers=self.tickers, keyword_list=self.keyword_list, func="isin"
        )

    def get_major_holders(self) -> None:
        """Request for the major holders of the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers, keyword_list=self.keyword_list, func="major_holders"
        )

    def get_institutional_holders(self) -> None:
        """Request for the institutional holders of the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers,
            keyword_list=self.keyword_list,
            func="institutional_holders",
        )

    def get_mutualfund_holders(self) -> None:
        """Request for the mutualfund holders of the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers,
            keyword_list=self.keyword_list,
            func="mutualfund_holders",
        )

    def get_dividends(self) -> None:
        """Request for the dividend of the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers, keyword_list=self.keyword_list, func="dividends"
        )

    def get_splits(self) -> None:
        """Request for the splits of the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers, keyword_list=self.keyword_list, func="splits"
        )

    def get_actions(self) -> None:
        """Request for the dividends and splits of the ticker together."""
        self.dict = self.all_trickers(
            tickers=self.tickers, keyword_list=self.keyword_list, func="actions"
        )

    def get_info(self) -> None:
        """Request for information about the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers, keyword_list=self.keyword_list, func="info"
        )

    def get_calendar(self) -> None:
        """Request for information about upcoming events of the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers, keyword_list=self.keyword_list, func="calendar"
        )

    def get_recommendations(self) -> None:
        """Request for the analyst recommendations for the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers,
            keyword_list=self.keyword_list,
            func="recommendations",
        )

    def get_earnings(self) -> None:
        """Request for the yearly earnings of the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers,
            keyword_list=self.keyword_list,
            func="earnings",
        )

    def get_quarterly_earnings(self) -> None:
        """Request for the yearly quarterly of the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers,
            keyword_list=self.keyword_list,
            func="quarterly_earnings",
        )

    def get_financials(self) -> None:
        """Request for the yearly financial information of the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers,
            keyword_list=self.keyword_list,
            func="financials",
        )

    def get_quarterly_financials(self) -> None:
        """Request for the quarterly financial information of the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers,
            keyword_list=self.keyword_list,
            func="quarterly_financials",
        )

    def get_balancesheet(self) -> None:
        """Request for the yearly balancesheet of the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers,
            keyword_list=self.keyword_list,
            func="balancesheet",
        )

    def get_quarterly_balancesheet(self) -> None:
        """Request for the quarterly balancesheet of the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers,
            keyword_list=self.keyword_list,
            func="quarterly_balancesheet",
        )

    def get_cashflow(self) -> None:
        """Request for the yearly cashflow of the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers,
            keyword_list=self.keyword_list,
            func="cashflow",
        )

    def get_quarterly_cashflow(self) -> None:
        """Request for the quarterly cashflow of the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers,
            keyword_list=self.keyword_list,
            func="quarterly_cashflow",
        )

    def get_sustainability(self) -> None:
        """Request for information about the sustainability of the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers,
            keyword_list=self.keyword_list,
            func="sustainability",
        )

    def get_options(self) -> None:
        """Request for information about the options of the ticker."""
        self.dict = self.all_trickers(
            tickers=self.tickers,
            keyword_list=self.keyword_list,
            func="options",
        )


class FinanceCollector:
    """FinanceCollector is in charge for executing the functions.

    During the execution, `FinanceCollector` can construct several product variations
    using the same building steps.
    """

    def __init__(self) -> None:
        """Initialize a fresh and empty builder."""
        self._builder = None

    @property
    def builder(self) -> BuilderFinanceCollector:
        """Builder as a property with value None.

        Returns:
            BuilderFinanceCollector: A builder class, that contains the abstract properties and methods.
        """
        return self._builder

    @builder.setter
    def builder(self, builder: BuilderFinanceCollector):
        """Sets the builder according to BuilderFinanceCollector.

        Args:
            builder (BuilderFinanceCollector): A builder class, that contains the abstract properties and methods.
        """
        self._builder = builder

    def find_chart_histogram(
        self,
        period: str = "1mo",
        interval: str = "1d",
        start: str = None,
        end: str = None,
        prepost: bool = False,
        actions: bool = True,
        auto_adjust: bool = True,
        proxy: str = None,
        threads: bool = True,
        group_by: str = "column",
        progress: bool = True,
        **kwargs,
    ) -> None:
        """Performa a search about the history charts of the tickers.

        Args:
            period (str, optional): Period of the chart history; valid options: `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, or `ytd,max`. It can either be used the `period`-parameter or the combination of `start`- and `end`-parameter. Defaults to "1mo".
            interval (str, optional): Interval, respectively, time step in the period; valid
            options: `1m`, `2m`, `5m`, `15m`, `30m`, `60m`, `90m`, `1h`, `1d`, `5d`, `1wk`, `1mo`, or `3mo`. The intraday data cannot extend last 60 days. Defaults to "1d".
            start (str, optional): Download start date string (YYYY-MM-DD) or _datetime. Defaults to None.
            end (str, optional): Download end date string (YYYY-MM-DD) or _datetime. Defaults to None.
            prepost (bool, optional):  Group by 'ticker' or 'column'. Defaults to False.
            actions (bool, optional):  Including Pre and Post market data in results. Defaults to True.
            auto_adjust (bool, optional): Adjusting all OHLC automatically. Defaults to True.
            proxy (str, optional): Downloading the dividend plus stock splits data. Defaults to None.
            threads (bool, optional): Specifying the number of download threads. Defaults to True.
            group_by (str, optional): Grouping by ticker or column.Defaults to "column".
            progress (bool, optional): Showing progress bar. Defaults to True.
        """
        self.builder.get_chart_history(
            period=period,
            interval=interval,
            start=start,
            end=end,
            prepost=prepost,
            actions=actions,
            auto_adjust=auto_adjust,
            proxy=proxy,
            threads=threads,
            group_by=group_by,
            progress=progress,
            **kwargs,
        )

    def find_isin_code(self) -> None:
        """Perform a search for the International Securities Identification Number (ISIN)."""
        self.builder.get_isin_code()

    def find_major_holders(self) -> None:
        """Perform a search for the major holders of the ticker."""
        self.builder.get_major_holders()

    def find_institutional_holders(self) -> None:
        """Perform a search for the institutional holders of the ticker."""
        self.builder.get_institutional_holders()

    def find_mutualfund_holders(self) -> None:
        """Perform a search for the mutualfund holders of the ticker."""
        self.builder.get_mutualfund_holders()

    def find_dividends(self) -> None:
        """Perform a search for the dividends of the ticker."""
        self.builder.get_dividends()

    def find_splits(self) -> None:
        """Perform a search for the splits of the ticker."""
        self.builder.get_splits()

    def find_actions(self) -> None:
        """Perform a search for the dividends and splits of the ticker together."""
        self.builder.get_actions()

    def find_info(self) -> None:
        """Perform a search for the information about the ticker."""
        self.builder.get_info()

    def find_calendar(self) -> None:
        """Perform a search for information about the upcoming events of the ticker."""
        self.builder.get_calendar()

    def find_recommendations(self) -> None:
        """Perform a search for the analyst recommendations of the ticker."""
        self.builder.get_recommendations()

    def find_earnings(self) -> None:
        """Perform a search for the yearly earnings of the ticker."""
        self.builder.get_earnings()

    def find_quarterly_earnings(self) -> None:
        """Perform a search for the quarterly earnings of the ticker."""
        self.builder.get_quarterly_earnings()

    def find_financials(self) -> None:
        """Perform a search for the yearly financial information of the ticker."""
        self.builder.get_financials()

    def find_quarterly_financials(self) -> None:
        """Perform a search for the quarterly financial information of the ticker."""
        self.builder.get_quarterly_financials()

    def find_balancesheet(self) -> None:
        """Perform a search for the yearly balancesheet of the ticker."""
        self.builder.get_balancesheet()

    def find_quarterly_balancesheet(self) -> None:
        """Perform a search for the quarterly balancesheet of the ticker."""
        self.builder.get_quarterly_balancesheet()

    def find_cashflow(self) -> None:
        """Perform a search for the yearly cashflow of the ticker."""
        self.builder.get_cashflow()

    def find_quarterly_cashflow(self) -> None:
        """Perform a search for the quarterly cashflow of the ticker."""
        self.builder.get_quarterly_cashflow()

    def find_sustainability(self) -> None:
        """Perform a search for the sustainability of the ticker."""
        self.builder.get_sustainability()

    def find_options(self) -> None:
        """Perform a search for the options of the ticker."""
        self.builder.get_options()
