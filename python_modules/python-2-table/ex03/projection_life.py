import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from load_csv import load
from matplotlib.ticker import FuncFormatter  # Import for 'M' formatting


def convert_to_numeric(elm: str) -> int:
    """convert a string to an integer, handling errors gracefully"""
    if "M" in elm:
        return int(float(elm.replace("M", "")) * 1_000_000)
    elif "K" in elm:
        return int(float(elm.replace("K", "")) * 1_000)
    else:
        try:
            return int(elm)
        except ValueError:
            return 0


def main():
    df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df0 = load("life_expectancy_years.csv")
    df1900 = df0[['country', '1900']]
    df1900['expectancy'] = df1900['1900']
    df1900.drop(columns='1900', inplace=True)
    df1900['gross national product'] = df['1900']
    df1900['gross national product'] = df1900['gross national product'].astype(
        int)
    df1900['expectancy'] = df1900['expectancy'].astype(float)

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.scatterplot(data=df1900, x='gross national product',
                    y='expectancy', ax=ax, color='blue')
    ax.set_xticks([300, 1000, 10000])

    def millions_formatter(x, pos):
        if x < 1000:
            return f'{int(x)}'
        return f'{int(x / 1_000)}K' if x != 0 else '0'
    ax.xaxis.set_major_formatter(FuncFormatter(millions_formatter))

    # 7. Add text metadata
    plt.xlabel('Gross national product')
    plt.ylabel('Life Expectancy')
    plt.title('1900')

    ax.legend(loc='lower right')

    plt.tight_layout()  # Extra assurance everything fits nicely
    plt.show()


if (__name__ == "__main__"):
    main()
