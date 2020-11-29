# from __future__ import annotations

from abc import ABC, abstractmethod, abstractproperty, abstractstaticmethod

import pandas as pd
import yfinance as yf


class BuilderFinanceCollector(ABC):
    @abstractproperty
    def return_dataframe(self) -> None:
        pass

    @abstractproperty
    def return_dict(self) -> None:
        pass

    @abstractstaticmethod
    def all_trickers(self) -> None:
        pass

    @abstractmethod
    def get_chart_history(self) -> None:
        pass

    @abstractmethod
    def get_isin_code(self) -> None:
        pass

    @abstractmethod
    def get_major_holders(self) -> None:
        pass

    @abstractmethod
    def get_institutional_holders(self) -> None:
        pass

    @abstractmethod
    def get_mutualfund_holders(self) -> None:
        pass

    @abstractmethod
    def get_dividends(self) -> None:
        pass

    @abstractmethod
    def get_splits(self) -> None:
        pass

    @abstractmethod
    def get_actions(self) -> None:
        pass

    @abstractmethod
    def get_info(self) -> None:
        pass

    @abstractmethod
    def get_calendar(self) -> None:
        pass

    @abstractmethod
    def get_recommendations(self) -> None:
        pass

    @abstractmethod
    def get_earnings(self) -> None:
        pass

    @abstractmethod
    def get_quarterly_earnings(self) -> None:
        pass

    @abstractmethod
    def get_financials(self) -> None:
        pass

    @abstractmethod
    def get_quarterly_financials(self) -> None:
        pass

    @abstractmethod
    def get_balancesheet(self) -> None:
        pass

    @abstractmethod
    def get_quarterly_balancesheet(self) -> None:
        pass

    @abstractmethod
    def get_cashflow(self) -> None:
        pass

    @abstractmethod
    def get_quarterly_cashflow(self) -> None:
        pass

    @abstractmethod
    def get_sustainability(self) -> None:
        pass

    @abstractmethod
    def get_options(self) -> None:
        pass


class DesignerFinanceCollector(BuilderFinanceCollector):
    def __init__(self, key_word_list: list) -> None:
        self.key_word_list = key_word_list
        self.tickers = yf.Tickers(" ".join(self.key_word_list))
        self.df = pd.DataFrame()
        self.dict = {}

    @property
    def return_dataframe(self) -> pd.DataFrame:
        return self.df

    @property
    def return_dict(self) -> dict:
        return self.dict

    @staticmethod
    def all_trickers(
        tickers: yf.Tickers, key_word_list: list, func: str
    ) -> pd.DataFrame:
        return {key_word.upper(): getattr(
                getattr(tickers.tickers, key_word.upper()), func
            ) for key_word in key_word_list}

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
        self.dict = self.all_trickers(
            tickers=self.tickers, key_word_list=self.key_word_list, func="isin"
        )

    def get_major_holders(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers, key_word_list=self.key_word_list, func="major_holders"
        )

    def get_institutional_holders(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers,
            key_word_list=self.key_word_list,
            func="institutional_holders",
        )

    def get_mutualfund_holders(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers,
            key_word_list=self.key_word_list,
            func="mutualfund_holders",
        )

    def get_dividends(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers, key_word_list=self.key_word_list, func="dividends"
        )

    def get_splits(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers, key_word_list=self.key_word_list, func="splits"
        )

    def get_actions(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers, key_word_list=self.key_word_list, func="actions"
        )

    def get_info(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers, key_word_list=self.key_word_list, func="info"
        )

    def get_calendar(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers, key_word_list=self.key_word_list, func="calendar"
        )

    def get_recommendations(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers,
            key_word_list=self.key_word_list,
            func="recommendations",
        )

    def get_earnings(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers,
            key_word_list=self.key_word_list,
            func="earnings",
        )

    def get_quarterly_earnings(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers,
            key_word_list=self.key_word_list,
            func="quarterly_earnings",
        )

    def get_financials(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers,
            key_word_list=self.key_word_list,
            func="financials",
        )

    def get_quarterly_financials(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers,
            key_word_list=self.key_word_list,
            func="quarterly_financials",
        )

    def get_balancesheet(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers,
            key_word_list=self.key_word_list,
            func="balancesheet",
        )

    def get_quarterly_balancesheet(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers,
            key_word_list=self.key_word_list,
            func="quarterly_balancesheet",
        )

    def get_cashflow(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers,
            key_word_list=self.key_word_list,
            func="cashflow",
        )

    def get_quarterly_cashflow(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers,
            key_word_list=self.key_word_list,
            func="quarterly_cashflow",
        )

    def get_sustainability(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers,
            key_word_list=self.key_word_list,
            func="sustainability",
        )

    def get_options(self) -> None:
        self.dict = self.all_trickers(
            tickers=self.tickers,
            key_word_list=self.key_word_list,
            func="options",
        )


class FinanceCollector:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> BuilderFinanceCollector:
        return self._builder

    @builder.setter
    def builder(self, builder: BuilderFinanceCollector) -> property:
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
        self.builder.get_isin_code()

    def find_major_holders(self) -> None:
        self.builder.get_major_holders()

    def find_institutional_holders(self) -> None:
        self.builder.get_institutional_holders()

    def find_mutualfund_holders(self) -> None:
        self.builder.get_mutualfund_holders()

    def find_dividends(self) -> None:
        self.builder.get_dividends()

    def find_splits(self) -> None:
        self.builder.get_splits()

    def find_actions(self) -> None:
        self.builder.get_actions()

    def find_info(self) -> None:
        self.builder.get_info()

    def find_calendar(self) -> None:
        self.builder.get_calendar()

    def find_recommendations(self) -> None:
        self.builder.get_recommendations()

    def find_earnings(self) -> None:
        self.builder.get_earnings()

    def find_quarterly_earnings(self) -> None:
        self.builder.get_quarterly_earnings()

    def find_financials(self) -> None:
        self.builder.get_financials()

    def find_quarterly_financials(self) -> None:
        self.builder.get_quarterly_financials()

    def find_balancesheet(self) -> None:
        self.builder.get_balancesheet()

    def find_quarterly_balancesheet(self) -> None:
        self.builder.get_quarterly_balancesheet()

    def find_cashflow(self) -> None:
        self.builder.get_cashflow()

    def find_quarterly_cashflow(self) -> None:
        self.builder.get_quarterly_cashflow()

    def find_sustainability(self) -> None:
        self.builder.get_sustainability()

    def find_options(self) -> None:
        self.builder.get_options()
