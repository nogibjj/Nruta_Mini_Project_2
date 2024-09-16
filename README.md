[![Lint](https://github.com/nogibjj/Nruta_Mini_Project_2/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Nruta_Mini_Project_2/actions/workflows/lint.yml)
[![Format](https://github.com/nogibjj/Nruta_Mini_Project_2/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Nruta_Mini_Project_2/actions/workflows/format.yml)
[![Test](https://github.com/nogibjj/Nruta_Mini_Project_2/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Nruta_Mini_Project_2/actions/workflows/test.yml)
[![Install](https://github.com/nogibjj/Nruta_Mini_Project_2/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Nruta_Mini_Project_2/actions/workflows/install.yml)

# IDS 706 Week 2 Mini Project - Pandas Descriptive Statistics Script

## 🏗️ Requirements
- Python script using Pandas for descriptive statistics
- Read a dataset (CSV or Excel)
- Generate summary statistics (mean, median, standard deviation)
- Create at least one data visualization

## 🚀 How to Run
1. Clone the repository:

```bash
$ git clone https://github.com/nogibjj/Nruta_Mini_Project_2.git
$ cd Nruta_Mini_Project_2
```

2. Install the required dependencies:

```bash
$ pip install -r requirements.txt
```

3. Run the script:

```bash
$ python sustainable_fashion.py
```

3. Generate Markdown and visualizations:

- The output summary statistics will be saved in `sustainable_fashion.md`.
- Visualizations (bar chart and pie chart) will be saved as `bar_plot.png` and `pie_chart.png`.

## 📦 Installation
Make sure you have the latest version of Python installed. To install the necessary libraries:

```bash
$ pip install pandas matplotlib tabulate
```

## 🧪 Testing
You can run the script and test the output with the dataset provided. To check the correctness of the statistics and visualizations, run:

```bash
$ make test
```

## 📊 Output
After running the script, you will see:

- Summary statistics for numerical columns (mean, median, std deviation).
- Bar chart and pie chart visualizations saved in the root folder.

## 🔍 Visualizations
The script generates two visualizations:

1. Bar Chart - Displays the relationship between selected features.
2. Pie Chart - Breaks down categories for easier comparison.