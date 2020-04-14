import pandas as pd

def main():
    
    (

        pd.read_csv('sklearn/data/raw/Melbourne_housing_FULL.csv')
        .loc[:,['Rooms','Distance','Bathroom','Car','Landsize','BuildingArea','Price']]
        .dropna()
        .reset_index(drop=True)
        .to_csv('sklearn/data/regression_dataset01_melbourne.csv',sep=';',index=False)

    )
    
    print('dataset created!')

if __name__ == '__main__':
    main()
