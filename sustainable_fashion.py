from mylib.make_functions import *

filepath = "sustainable_fashion_trends_2024.csv"


# loading the data
def load_df(filepath):
    df = load_dataset(filepath)
    return df


# Generate statistics
def generate_statistics(df, analysis_col):

    # Displaying the first 5 rows of the dataframe
    print(df.head())

    # Calculating and printing statistics
    mean = calculate_mean(df, analysis_col)
    median = calculate_median(df, analysis_col)
    std_dev = calculate_std_dev(df, analysis_col)
    summary = calculate_summary(df)

    print(f"The mean of the data is:\n{mean}")
    print("-----------------------------------------")
    print(f"The median of the data is:\n{median}")
    print("-----------------------------------------")
    print(f"The standard deviation of the data is:\n{std_dev}")
    print("-----------------------------------------")
    print(
        f"The summary statistics for the numerical columns in the data are:\n{summary}"
    )


# generating the plots
def generate_plots(df, x_col, y_col, plot_title, xlabel, ylabel, pie_col, pie_title):
    # Plotting
    # Number of sustainable brands per country
    grouped_data = df.groupby(x_col).size().reset_index(name=y_col)
    bar_plot(grouped_data, x_col, y_col, plot_title, xlabel, ylabel)

    # Distribution of material types
    pie_chart(df, pie_col, pie_title)


# Parameters for the analysis

analysis_col = "Carbon_Footprint_MT"
x_col = "Country"
y_col = "Number of Brands"
plot_title = "Number of Sustainable Brands per Country"
xlabel = "Country"
ylabel = "Number of Brands"
pie_col = "Material_Type"
pie_title = "Distribution of Material Types"

# Loading the data
df = load_df(filepath)

# Call generate_statistics
generate_statistics(df, analysis_col)

# Call generate_plots
generate_plots(df, x_col, y_col, plot_title, xlabel, ylabel, pie_col, pie_title)
