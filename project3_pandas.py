# imports
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# config
pd.set_option('display.max_columns', None) 
pd.set_option('display.max_rows', None)  

def compute_cb(row):
    
    # CB
    if row['Durable Clinical Benefit'] in ['CR', 'PR']:
        return 'CB'
    
    # CB part 2: SD os>=1year
    if row['Durable Clinical Benefit'] == 'SD' and row['Overall Survival (Months)'] >= 12:
        return 'CB'
    
    if row['Durable Clinical Benefit'] == 'SD' and row['Overall Survival (Months)'] > 1:
        return 'NCB'
    
    if row['Disease Free Survival (Months)'] < 6 and row['Overall Survival (Months)'] > 24:
        return 'LTS-NCB'
    
    # no benefit
    return 'NCB'


def main(file_path):
    ''' load data from file and calculate mean'''

    # loads data from CSV into dictionary
    mel_df = ??

    # typecast # no-need pandas auto-infers
    #print(mel_df.dtypes)

    # compute clinical benefit
    mel_df['clinical_benefit'] = ??

    # compute the summary

    # create a boxplot
    ...
    plt.savefig('plot.png')

if __name__ == "__main__":
    main(sys.argv[1])