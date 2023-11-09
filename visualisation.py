import matplotlib.pyplot as plt
import pandas as pd


def pieplot(df, year):

    """create a pie chart at certain year available in dataset and saves it in a file.

    Parameters:
        - df (dataframe): Data Frame.
        - year (int): year of which data needs to be plotted

    Example:
        >>> piechart(spotify_dataset, 2018)

    Returns:
        None
    """

    plt.figure(figsize=(8, 8))
    headers = ["Total Cost of Revenue", "Gross Profit"]

    explode = (0, 0)
    colors = ["skyblue", "orange"]

    row_index = df.loc[df["Date"] == str(year)].index[0]
    values = []

    values.append(
        (df.loc[row_index, "Cost of Revenue"] / df.loc[row_index, "Total Revenue"])
        * 100
    )
    values.append(
        (df.loc[row_index, "Gross Profit"] / df.loc[row_index, "Total Revenue"]) * 100
    )

    plt.pie(
        values,
        explode=explode,
        labels=headers,
        colors=colors,
        autopct="%1.1f%%",
        shadow=True,
        startangle=140,
    )

    plt.title(str(year))

    plt.legend()
    plt.savefig("pieplot_" + str(year) + ".png")
    plt.show()

    return


def lineplot(df, headers):
    """create a line graph over all years available in dataset and saves it in a file.

    Parameters:
        - df (dataframe): Data Frame.
        - headers (list of headers): list of headers

    Example:
        >>> linechart(spotify_dataset, [no_of_users, no of songs])

    Returns:
        None
    """

    plt.figure(figsize=(12, 12))
    plt.title(
        "Comparision of Premium profit and Ad profit over time of spotify revenue"
    )

    for head in headers:
        plt.plot(df["Date"], df[head], label=head)

    # labelling
    plt.xlabel("Year")
    plt.ylabel("Profit in Million")
    # removing white space left and right. Both standard and pandas min/max
    # can be used
    plt.xlim(min(df["Date"]), df["Date"].max())
    plt.legend()
    # save as png
    plt.savefig("lineplot.png")
    plt.show()

    return


def barchart(df):

    """creates a bar chart at where a bar represents no of movies relesed in respective country.

    Parameters:
        - df (dataframe): Data Frame.

    Example:
        >>> barchart(spotify_dataset)

    Returns:
        None
    """

    plt.figure(figsize=(16, 6))
    plt.bar(df["country"], df["count"])
    plt.legend()
    plt.xlabel("Country")
    plt.ylabel("No of Movies Released")
    plt.title('No of movies released in each country')
    plt.savefig("barchart.png")
    plt.show()

    return



csv_file_path = "Spotify Quarterly.csv"
df = pd.read_csv(csv_file_path)
df = df.iloc[1:-1]
df["Date"] = df["Date"].str.split("-").str[2]
summary_year = (
    df.groupby("Date")[
        [
            "Total Revenue",
            "Cost of Revenue",
            "Gross Profit",
            "Premium Gross Profit",
            "Ad gross Profit",
        ]
    ]
    .sum()
    .reset_index()
)
lineplot(summary_year, ["Premium Gross Profit", "Ad gross Profit"])

pieplot(summary_year, 2017)
pieplot(summary_year, 2022)


path_netflix = "netflix1.csv"
df_netflix = pd.read_csv(path_netflix)
summary_country = df_netflix.groupby(["country"]).size().to_frame("count").reset_index()
summary_country = summary_country[summary_country["count"] > 100]
summary_country = summary_country.sort_values(by="count", ascending=False)
summary_country.loc[summary_country["country"] == "United Kingdom", "country"] = "UK"
summary_country.loc[summary_country["country"] == "United States", "country"] = "USA"
summary_country = summary_country[~(summary_country["country"] == "Not Given")]
barchart(summary_country)