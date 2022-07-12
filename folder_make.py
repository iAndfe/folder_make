def folders_make(csv_name):
        import os
        import pandas as pd
        df = pd.read_csv(str(csv_name))
        foldernames = df.iloc[:,0].to_list()
  
        for items in foldernames:
                os.mkdir(str(items))

#folders_make(input())
folders_make('alpha.csv')
