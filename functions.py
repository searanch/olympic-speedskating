def clean(x):
    '''function to clean results csv'''
    #Convert time to proper form and cast to float
    x['Time']= x['Time'].str.replace('.', ':')
    x['Time']= x['Time'].str.replace(',', ':')
    x['Time']= x['Time'].str.replace(' ', '')
    # Drop column
    x=x.drop(columns = ['Unnamed: 5'])
    # Rename columns
    x=x.rename(columns={'Unnamed: 2':'Age'})
    return x.head()

clean(stuff)


def time(x):