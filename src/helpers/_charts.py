import matplotlib.pyplot as plt
from pandas import DataFrame, Series
from numpy.typing import ArrayLike
from textwrap import wrap


def _wrap_labels(labels: ArrayLike, width: int = 18) -> list[str]:
    """Wrap chart labels without truncating the underlying text."""

    return ["\n".join(wrap(str(label), width=width)) for label in labels]


def pie_chart(data: Series, title: str) -> None:
    """Helper function to create Pie-chart.

    Args:
        data (Series): Generate the series from df[filter].value_counts()
        title (str): Title for the Pie chart

    Refer to [Matplotlib](https://matplotlib.org/stable/plot_types/stats/pie.html)
    for more information
    """
    _, ax = plt.subplots()
    ax.pie(
        x=data,
        labels=[str(label) for label in data.index],
        autopct="%1.0f%%",
        startangle=90,
    )
    ax.set_title(title)
    plt.show()


def bar_chart(categories: ArrayLike, category_freq: ArrayLike, title: str) -> None:
    """Helper function to create Bar-chart.

    Args:
        categories (ArrayLike): X-axis
        category_freq (ArrayLike): Values for the bars where the bars are taken
        from categories (ensure order)
        title (str): Title for bar chart

    Refer to [Matplotlib](https://matplotlib.org/stable/plot_types/basic/bar.html)
    for more information
    """
    _, ax = plt.subplots(figsize=(9, 5))
    ax.bar(x=range(len(categories)), height=category_freq)
    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels(_wrap_labels(categories), rotation=0)
    ax.set_title(title)
    plt.tight_layout()
    plt.show()


def box_plot(likert_data: DataFrame, title: str, scale: str, vert: bool) -> None:
    """Generates a box-plot for each column in the Dataframe.

    Args:
        likert_data (DataFrame): Dataframe containing likert data columns
        title (str): Title of the plot
    """

    _, ax = plt.subplots(figsize=(10, 5))
    ax.boxplot(likert_data, tick_labels=_wrap_labels(likert_data.columns), vert=vert)
    plt.title(title)
    plt.xlabel(scale)  # Range for responses eg: (0 - 4)
    plt.tight_layout()
    plt.show()
