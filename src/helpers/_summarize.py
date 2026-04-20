from pandas import Series, DataFrame
from numpy.typing import ArrayLike


def create_freq_table(title: str, counts: Series, frequencies: Series):
    """Helper function to generate a frequency table.

    Args:
        series (Series): For us, this would be a column of our dataset eg: df["gender"]
        name (str): Name for the table

    Returns:
        Styler: Stylized table containing summary statistics of the given column
    """

    # Combine into a mini DataFrame
    summary_df = DataFrame({
        'Frequency (n)': counts,
        'Distribution (%)': frequencies
    })

    # Beautify using the .style attribute (See: https://pandas.pydata.org/docs/user_guide/style.html)
    return summary_df.style.format({'Distribution (%)': '{:.1f}%'})\
                           .set_caption(title)
