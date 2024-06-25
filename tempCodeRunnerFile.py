    
    # Sum values separated by lines containing different strings in the 'names' column
    print("\nSum of values separated by unique strings in the 'names' column:\n")
    sum_by_names = df.groupby('names').sum()
    print(sum_by_names)