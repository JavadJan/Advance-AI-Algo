import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter  # Import for 'M' formatting
from load_csv import load


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
    df = load("population_total.csv")

    # 1. Set 'country' as the index so we can locate 'Germany' easily
    df = df.set_index('country')

    # 2. Extract Germany's row and transpose (.T) it into a column
    germany_data = df.loc[['Germany', 'France']].T

    # 3. Rename the index to 'Year' and reset it to make it a column
    germany_data.index.name = 'Year'
    germany_data = germany_data.reset_index()
    germany_data["Germany"] = germany_data["Germany"].apply(convert_to_numeric)
    germany_data["France"] = germany_data["France"].apply(convert_to_numeric)
    germany_data["Year"] = germany_data["Year"].astype(int)
    print(germany_data)
    germany_data = germany_data[(germany_data["Year"] >= 1800) & (
        germany_data["Year"] <= 2050)]
    germany_data = germany_data.sort_values("Year")

    # 4. Plot using standard subplots to preserve margin spacing
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.lineplot(data=germany_data, x='Year', y='Germany',
                 ax=ax, color='blue', label='Germany')
    sns.lineplot(data=germany_data, x='Year', y='France',
                 ax=ax, color='green', label='France')

    # 5. Set the 40-year interval step sizes
    ax.set_xticks(range(1800, 2051, 40))
    ax.set_yticks(range(20000000, 60000001, 20000000))  # Minor ticks for Y-axis

    # 6. Format the Y-axis numbers to display '20M', '40M', etc.
    def millions_formatter(x, pos):
        return f'{int(x / 1_000_000)}M' if x != 0 else '0'

    ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))

    # 7. Add text metadata
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')
    
    ax.legend(loc='lower right')

    plt.tight_layout()  # Extra assurance everything fits nicely
    plt.show()


if __name__ == "__main__":
    main()
