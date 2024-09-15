# importing libraries
import pandas as pd
import matplotlib.pyplot as plt


# defining functions for the summary statistics
def calculate_mean(insert_column):
    return insert_column.mean()


def calculate_median(insert_column):
    return insert_column.median()


def calculate_std_dev(insert_column):
    return insert_column.std()


# overall summary statistics for the data
def calculate_summary(dataframe):
    return dataframe.describe()


# plotting the data


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


def generate_statistics(filepath):
    # extracting the column for analysis
    column = dataframe[analysis_column]

    # generating the first 5 rows to see if the data has been stored correctly
    print(dataframe())

    # calling functions to pass the loaded data frame
    mean = calculate_mean(column)
    median = calculate_median(column)
    std_dev = calculate_std_dev(column)
    summary = calculate_summary(dataframe)

    # printing the statements
    print(f"The mean of the data is:\n{mean}")
    print("-----------------------------------------")
    print(f"The median of the data is:\n{median}")
    print("-----------------------------------------")
    print(f"The standard deviation of the data is:\n{std_dev}")
    print("-----------------------------------------")
    print(
        f"The summary statistics for the numerical columns in the data are:\n{summary}"
    )


# adding the file path
filepath = "sustainable_fashion_trends_2024.csv"
dataframe = pd.read_csv(filepath)

# setting the parameters to generate statistics
analysis_column = "Carbon_Footprint_MT"

# calling the generate_statistics function
generate_statistics(filepath)

# setting the parameters for the bar plot
# plot #1 - number of sustainable brands per country
x_column = filepath["Country"]
y_column = filepath["Brand"]
title = "Number of sustainable brands per country"
x_label = "Country"
y_label = "Number of Brands"

# calling the plot_bar function
bar_plot(x_column, y_column, title, x_label, y_label)

# setting the parameters for the pie chart
material_column = "Material_Type"
plot_title = "Distribution of Material Types"

# Call the pie_chart function
pie_chart(dataframe, material_column, plot_title)
