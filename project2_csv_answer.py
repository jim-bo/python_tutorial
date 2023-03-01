# imports
import sys
import os
from statistics import mean


# functions
def load_data(file_path):
    ''' loads data from TSV'''

    # loads data into a list of strings
    with open(file_path) as fin:
        lines = fin.readlines()

    # get the header
    header = lines[0].split("\t")

    # get the index of the columns of interest
    cols = {}
    coi = set(['Disease Free Survival (Months)', 'Mutation Load', 'Neo-antigen Load',\
        'Durable Clinical Benefit', 'Overall Survival (Months)'])

    for idx, c in enumerate(header):
        if c in coi:
            cols[c] = idx

    # create empty dictionary for data
    data = {}
    for c in cols:
        data[c] = []

    # iterate over the remainder of the file to build dictionary of data
    for line in lines[1::]:
        tokens = line.split('\t')
        
        for col, idx in cols.items(): 
            data[col].append(tokens[idx])

    # just give the dict back
    return data

def cast_data(data):
    '''convert the number to numbers'''

    # do the integers
    for c in ['Mutation Load', 'Neo-antigen Load']:
        for i in range(len(data[c])):
            data[c][i] = int(data[c][i])

    # do the floats
    for c in ['Disease Free Survival (Months)', 'Overall Survival (Months)']:
        for i in range(len(data[c])):
            data[c][i] = float(data[c][i])

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
        tmp = []
        for idx, val in enumerate(data['clinical_benefit']):
            if val == cb:
                tmp.append(idx)

        print(f'clinical_benefit: {cb}, {len(tmp)}')

        # loop over measure
        for m in ['Mutation Load', 'Neo-antigen Load']:

            out = mean([data[m][x] for x in tmp])

            print(f'{cb}, {m} mean: {out:.2f}')
        
        print()

def main():
    ''' load data from file and calculate mean'''

    # loads data from CSV into dictionary
    data = load_data(sys.argv[1])

    # typecast
    data = cast_data(data)

    # compute clinical benefit
    data = compute_cb(data)

    # compute the summary
    compute_summary(data)



if __name__ == "__main__":
    main()