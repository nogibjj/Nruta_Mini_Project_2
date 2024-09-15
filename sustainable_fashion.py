# importing libraries
import pandas as pd
import matplotlib.pyplot as plt


# Defining functions for summary statistics
def calculate_mean(column):
    return column.mean()


def calculate_median(column):
    return column.median()


def calculate_std_dev(column):
    return column.std()


def calculate_summary(dataframe):
    return dataframe.describe()


# Plotting functions
def bar_plot(
    dataframe, x_column, y_column, title, xlabel, ylabel, color="skyblue", rotation=45
):
    plt.figure(figsize=(12, 8))
    dataframe.plot(kind="bar", x=x_column, y=y_column, color=color, legend=False)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotation)
    plt.grid(axis="y")
    plt.show()


def pie_chart(dataframe, column, title):
    plt.figure(figsize=(10, 10))
    dataframe[column].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=140)
    plt.title(title)
    plt.ylabel("")
    plt.show()


# Generate statistics and plots
def generate_statistics(
    filepath,
    analysis_column,
    x_column,
    y_column,
    plot_title,
    xlabel,
    ylabel,
    material_column,
    pie_chart_title,
):
    # Reading the data
    dataframe = pd.read_csv(filepath)

    # Extracting the column for analysis
    column = dataframe[analysis_column]

    # Displaying the first 5 rows of the dataframe
    print(dataframe.head())

    # Calculating and printing statistics
    mean = calculate_mean(column)
    median = calculate_median(column)
    std_dev = calculate_std_dev(column)
    summary = calculate_summary(dataframe)

    print(f"The mean of the data is:\n{mean}")
    print("-----------------------------------------")
    print(f"The median of the data is:\n{median}")
    print("-----------------------------------------")
    print(f"The standard deviation of the data is:\n{std_dev}")
    print("-----------------------------------------")
    print(
        f"The summary statistics for the numerical columns in the data are:\n{summary}"
    )

    # Plotting
    # Number of sustainable brands per country
    grouped_data = dataframe.groupby(x_column).size().reset_index(name=y_column)
    bar_plot(grouped_data, x_column, y_column, plot_title, xlabel, ylabel)

    # Distribution of material types
    pie_chart(dataframe, material_column, pie_chart_title)


# Parameters for the analysis
filepath = "sustainable_fashion_trends_2024.csv"
analysis_column = "Carbon_Footprint_MT"
x_column = "Country"
y_column = "Number of Brands"
plot_title = "Number of Sustainable Brands per Country"
xlabel = "Country"
ylabel = "Number of Brands"
material_column = "Material_Type"
pie_chart_title = "Distribution of Material Types"

# Calling the function
generate_statistics(
    filepath,
    analysis_column,
    x_column,
    y_column,
    plot_title,
    xlabel,
    ylabel,
    material_column,
    pie_chart_title,
)
