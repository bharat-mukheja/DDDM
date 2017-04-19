import pandas as pd
import numpy as np
import os
from sklearn import preprocessing


def input_output(selected_countries, selected_categories, weights):
    countries = {'af': 'Afghanistan', 'ba': 'Bahrain', 'cy': 'Cyprus', 'eg': 'Egypt', 'ir': 'Iran', 'iz': 'Iraq', 'is': 'Israel', 'jo': 'Jordan',
                 'ku': 'Kuwait', 'le': 'Lebanon', 'ly': 'Libya', 'mu': 'Oman',
                 'pk': 'Pakistan', 'qa': 'Qatar', 'rs': 'Russia', 'sa': 'Saudi Arabia', 'su': 'Sudan', 'sy': 'Syria', 'tu': 'Turkmenistan', 'ae': 'UAE',
                 'us': 'USA', 'ym': 'Yemen'}
    dataframes = []
    i = 0
    weight_vector = []
    for category in selected_categories:
        print(os.getcwd())
        url = 'balanceofpower\\data\\'+category + '.csv'
        dataframe = pd.read_csv(url)
        ncols = len(dataframe.columns)
        for j in range(0, ncols - 1):
            weight_vector.append(weights[i])
        dataframes.append(dataframe)
        i += 1
    # print(len(dataframes))
    truth_table = dataframes[0]
    for dataframe in dataframes[1:]:
        truth_table = truth_table.merge(dataframe, on='Country', how='outer')
    truth_table = truth_table.loc[truth_table['Country'].isin(selected_countries)]

    final_columns = truth_table.columns.tolist()

    truth_table = truth_table.replace(np.NaN, 0)
    truth_table_temp = truth_table

    country = truth_table_temp['Country']
    del truth_table_temp['Country']

    min_max_scaler = preprocessing.MinMaxScaler()
    np_scaled = min_max_scaler.fit_transform(truth_table)
    data = pd.DataFrame(np_scaled)
    # data = truth_table_temp

    for i in range(0, len(data.index)):
        for j in range(0, len(weight_vector)):
            data.iloc[i, j] = round(data.iloc[i, j], 4)

    scores = []
    for i in range(0, len(data.index)):
        score_vector = np.array(list(data.iloc[i])) * np.array(weight_vector)
        scores.append(round(sum(score_vector), 2))
    data['scores'] = scores

    country_column = []
    for name in country:
        country_column.append(countries[name])
    data['Country'] = country_column
    cols = data.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    data = data[cols]
    final_columns.append('Score')
    data.columns = final_columns
    data = data.sort(['Score'], ascending=0)
    # final_data=pd.DataFrame(data,index=country)

    # final_data.iloc[0:len(ncols(data)-1),axis=0]=data.iloc[0:len(ncols(data)-1),axis=0]

    return data


#list1 = ['qa', 'rs', 'pk']
#list2 = ['economy', 'society', 'geography', 'demographics', 'infrastructure']
#list3 = [1, 2, 3, 4, 5]

#print(input_output(list1, list2, list3))
