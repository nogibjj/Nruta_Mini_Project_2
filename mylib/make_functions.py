import pandas as pd
import matplotlib.pyplot as plt


# loading dataset
def load_dataset(filepath):
    df = pd.read_csv(filepath)
    return df


# Defining functions for summary statistics
def calculate_mean(df, col):
    return df[col].mean()


def calculate_median(df, col):
    return df[col].median()


def calculate_std_dev(df, col):
    return df[col].std()


def calculate_summary(df):
    return df.describe()


# Plotting functions
# creating a bar chart
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
    return plt.show()


# creating a pie chart
def pie_chart(dataframe, column, title):
    plt.figure(figsize=(10, 10))
    dataframe[column].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=140)
    plt.title(title)
    plt.ylabel("")
    return plt.show()
