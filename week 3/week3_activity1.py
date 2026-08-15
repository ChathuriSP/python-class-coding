from ucimlrepo import fetch_ucirepo

def main():
    # Fetch dataset
    iris = fetch_ucirepo(id=53)

    # Data (as pandas dataframes)
    X = iris.data.features
    y = iris.data.targets

# metadata
    print("Total number of data is:", len(X))
    print("Total number of different flowers available is:", y.iloc[:, 0].nunique())
    print("The names of all different flowers are:")

    for name in y.iloc[:, 0].unique():
        print(name)

#print(iris.metadata)

# variable information
#print(iris.variables)
# Execute the main function
if __name__ == "__main__":
    main()