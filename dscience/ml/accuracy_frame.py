from __future__ import annotations
import logging
from typing import Sequence, Union, Iterable
import pandas as pd
from dscience.core.extended_df import *

logger = logging.getLogger("dscience")


class AccuracyCountFrame(SimpleFrame):
    pass


class AccuracyFrame(OrganizingFrame):
    """
    Has columns 'label', 'score', 'prediction', and 'score_for_prediction', with one row per prediction.
    """

    @classmethod
    def required_columns(cls) -> Sequence[str]:
        return ["label", "prediction", "score", "score_for_prediction"]

    def counts(self) -> AccuracyCountFrame:
        df = self.copy()
        df["score"] = df["label"] == df["prediction"]
        df = self.groupby("label").sum()[["score"]]
        return AccuracyCountFrame(AccuracyCountFrame(df.reset_index()))

    def means(self) -> AccuracyCountFrame:
        df = self.copy()
        df["score"] = df["label"] == df["prediction"]
        df = self.groupby("label").mean()[["score"]] * 100.0
        return AccuracyCountFrame(AccuracyCountFrame(df.reset_index()))

    def with_label(self, label: Union[str, Iterable[str]]) -> AccuracyFrame:
        if isinstance(label, str):
            return self.__class__.retype(self[self["label"] == label])
        else:
            return self.__class__.retype(self[self["label"].isin(label)])

    def boot_mean(self, b: int, q: float = 0.95) -> BaseFrame:
        """
        Calculates a confidence interval of the mean from bootstrap over the rows.
        :param b: The number of bootstrap samples
        :param q: The high quantile, between 0 and 1.
        :return: A DataFrame with columns 'label', 'lower', and 'upper'.
        """
        data = []
        for repeat in range(b):
            samples = self.sample(len(self), replace=True)
            data.append(samples.groupby("label")[["score"]].mean().reset_index())
        upper = (
            AccuracyFrame(pd.concat(data))
            .groupby("label")
            .quantile(q)
            .rename(columns={"label": "upper"})["upper"],
        )
        lower = (
            AccuracyFrame(pd.concat(data))
            .groupby("label")
            .quantile(1 - q)
            .rename(columns={"label": "lower"})["lower"]
        )
        return BaseFrame(pd.merge(upper, lower, left_index=True, right_index=True))


class AccuracyFrames:
    @classmethod
    def concat(cls, *views: Sequence[AccuracyFrame]) -> AccuracyFrame:
        return AccuracyFrame(pd.concat(views, sort=False))


__all__ = ["AccuracyFrame", "AccuracyFrames"]
