import seaborn as sns
import matplotlib.pyplot as plt
from load_csv import load

def main():
    df = load("life_expectancy_years.csv")
    
    # 1. Set 'country' as the index so we can locate 'Germany' easily
    df = df.set_index('country')
    
    # 2. Extract Germany's row and transpose (.T) it into a column
    germany_data = df.loc[['Germany']].T
    
    # 3. Rename the index to 'Year' and reset it to make it a column
    germany_data.index.name = 'Year'
    germany_data = germany_data.reset_index()
    
    # Ensure Year values are numeric so the plot order is correct
    germany_data['Year'] = germany_data['Year'].astype(int)

    # 4. Plot the newly structured data
    plt.figure()
    sns.lineplot(data=germany_data, x='Year', y='Germany')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.title('Germany Life Expectancy in Projection')
    plt.show()

if __name__ == "__main__":
    main()

