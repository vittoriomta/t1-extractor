import pandas as pd


def masterall():
    # load the first pandas file
    df1 = pd.read_excel('input/Master.xls')

    # load the second pandas file
    df2 = pd.read_excel('output/Data_sorted.xlsx')

    # merge the two dataframes based on the 'Container' column
    merged_df = pd.merge(df1, df2, on='Container', how='left')



    merged_df['Sigillo'] = merged_df['Seal']
    merged_df['Unnamed: 20'] = merged_df['Mrn']
    merged_df['Merce'] = merged_df['Cargo']
    merged_df['Peso lordo merce'] = merged_df['Weight']


    merged_df = merged_df.drop(['Unnamed: 27', 'Unnamed: 28', 'Unnamed: 29',
        'Unnamed: 30', 'Lunghezza vagone (m)', 'Peso vagone (kg)',
        'Posizione vagone', 'Tipo vagone', 'Unnamed: 35', 'Unnamed: 36',
        'Unnamed: 37', 'Id.', 'Filename', 'Mrn', 'Weight', 'Seal', 'Cargo'], axis=1)

    # save the merged dataframe to a new csv file
    merged_df.to_excel('output/merged_file.xlsx', index=False)


