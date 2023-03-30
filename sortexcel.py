import pandas as pd
import os
import glob


def sortdocs(df1, df2):
    # Load the first file into a pandas DataFrame
    df1 = pd.read_excel('folder/input/Master.xls')
    # Load the second file into a pandas DataFrame
    df2 = pd.read_excel('folder/output/Raw_Data.xlsx')

    # Filter out values in df1['Container'] that are not in df2['Container']
    mask = df1['Container'].isin(df2['Container'])
    filtered_df1 = df1[mask]

    # Create a dictionary mapping container values to their index in filtered_df1
    container_order = dict(zip(filtered_df1['Container'], range(len(filtered_df1))))

    # Define a function to return the sort index for each row in df2
    def sort_index(row):
        return container_order.get(row['Container'], -1)

    # Add a new column to df2 with the sort index
    df2['sort_index'] = df2.apply(sort_index, axis=1)

    # Filter out rows where sort_index is -1 (i.e., where Container is not in df1)
    df2_filtered = df2[df2['sort_index'] != -1]

    # Sort df2_filtered based on the sort index column
    df2_sorted = df2_filtered.sort_values('sort_index')

    # Drop the sort index column
    df2_sorted = df2_sorted.drop('sort_index', axis=1)

    # Save the sorted second DataFrame to a new file
    df2_sorted.to_excel('folder/output/Data_sorted.xlsx', index=False)
