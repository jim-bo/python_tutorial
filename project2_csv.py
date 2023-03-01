# imports
import sys


# functions
def load_data(file_path):
    ''' loads data from TSV'''

    # column headers of interest here
    coi = set(['Disease Free Survival (Months)', 'Mutation Load', 'Neo-antigen Load',\
        'Durable Clinical Benefit', 'Overall Survival (Months)'])
    data = {}

    # just give the dict back
    return data

def cast_data(data):
    '''convert the number to numbers'''

    # do the integers

    # do the floats

    return data

def compute_cb(data):
    '''computes clinical benefit according to paper, 
    add additional key with clinical_benefit = ['CB', 'NCB', 'LTS-NCB']'''

    # loop over each row of data
    data['clinical_benefit'] = list()
    for i in range(len(data['Durable Clinical Benefit'])):

        # CB
        if data['Durable Clinical Benefit'][i] in ['CR', 'PR']:
            data['clinical_benefit'].append('CB')
        
        # CB part 2: SD os>=1year
        elif data['Durable Clinical Benefit'][i] == 'SD' and data['Overall Survival (Months)'][i] >= 12:
            data['clinical_benefit'].append('CB')
        
        # NCB is SD and OS < 1 year
        elif data['Durable Clinical Benefit'][i] == 'SD' and data['Overall Survival (Months)'][i] < 12:
            data['clinical_benefit'].append('NCB')
        
        # long-term survival but no clinical benefit
        elif data['Disease Free Survival (Months)'][i] < 6 and data['Overall Survival (Months)'][i] > 24:
            data['clinical_benefit'].append('LTS-NCB')

        else: 
            data['clinical_benefit'].append('NCB')
        
    return data

def compute_summary(data):
    ''' computes the means as requested'''

    print()

    # loop over category
    for cb in ['NCB', 'LTS-NCB', 'CB']:

        # calc index of cases which have current status
        print(f'clinical_benefit: {cb}, {num_cases}')

        # loop over measure
        for m in ['Mutation Load', 'Neo-antigen Load']:

            # do print statement

        
        print()

def main():
    ''' load data from file and calculate mean'''

    # loads data from CSV into dictionary

    # typecast

    # compute clinical benefit

    # compute the summary


if __name__ == "__main__":
    main()