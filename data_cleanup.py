import pandas as pd
import numpy as np

details = "order_details.csv"
number_of_orders = 'total_orders.csv'
orders_per_store = 'orders.csv'
revenue_number = 'total_revenue.csv'
revenue_per_store = 'revenue.csv'
location_dict = {
    "Name and Location": "Date",
    "Bill Miller BBQ - 136 West Slaughter Lane": "#64",
    "Bill Miller BBQ - 14718 North Interstate 35 Frontage Road": "#19",
    "Bill Miller BBQ - 1646 Main Street #3393": "#65",
    "Bill Miller BBQ - 1651 West Whitestone Boulevard": "#21",
    "Bill Miller BBQ - 709 East Ben White Boulevard": "#16",
    "Bill Miller BBQ - 8103 Burnet Road": "#17",
    "Bill Miller BBQ - 8700 U.S. 290": "#35",
    "Laguna Madre Seafood Company - 10614 Westover Hills Boulevard": "#L3",
    "Laguna Madre Seafood Company - 18195 U.S. 281": "#L4",
    "Laguna Madre Seafood Company - 25127 Interstate 10": "#L5"
}
convert_dict = {'Date': str, '#64': float, '#19': float, '#65': float, '#21': float, '#16': float, '#17': float,
                '#35': float, '#L3': float, '#L4': float, '#L5': float}
bm_store_num_dict = ['#64', '#19', '#65', '#21', '#16', '#17', '#35']
lm_store_num_dict = ['#L3', '#L4', '#L5']
total_store_num_dict = bm_store_num_dict+lm_store_num_dict

details = pd.read_csv(details)
details = details.drop(details.columns[0:3], axis=1)
details['Name and Location'] = details['Name and Location'].replace(location_dict, regex=True)
store16_d = details[details['Name and Location'].str.contains('#16')]
store17_d = details[details['Name and Location'].str.contains('#17')]
store19_d = details[details['Name and Location'].str.contains('#19')]
store35_d = details[details['Name and Location'].str.contains('#35')]
store64_d = details[details['Name and Location'].str.contains('#64')]
store65_d = details[details['Name and Location'].str.contains('#65')]
storeL3_d = details[details['Name and Location'].str.contains('#L3')]
storeL4_d = details[details['Name and Location'].str.contains('#L4')]
storeL5_d = details[details['Name and Location'].str.contains('#L5')]


orders_per_store = pd.read_csv(orders_per_store)
orders_per_store = orders_per_store.drop(orders_per_store.index[0])
orders_per_store = orders_per_store.rename(index=str, columns=location_dict)
orders_per_store = orders_per_store.astype(convert_dict)

revenue_per_store = pd.read_csv(revenue_per_store)
revenue_per_store = revenue_per_store.drop(revenue_per_store.index[0])
revenue_per_store = revenue_per_store.rename(index=str, columns=location_dict)
revenue_per_store['#64'] = revenue_per_store['#64'].str.replace('$', '')
revenue_per_store['#19'] = revenue_per_store['#19'].str.replace('$', '')
revenue_per_store['#65'] = revenue_per_store['#65'].str.replace('$', '')
revenue_per_store['#21'] = revenue_per_store['#21'].str.replace('$', '')
revenue_per_store['#16'] = revenue_per_store['#16'].str.replace('$', '')
revenue_per_store['#17'] = revenue_per_store['#17'].str.replace('$', '')
revenue_per_store['#35'] = revenue_per_store['#35'].str.replace('$', '')
revenue_per_store['#L3'] = revenue_per_store['#L3'].str.replace('$', '')
revenue_per_store['#L4'] = revenue_per_store['#L4'].str.replace('$', '')
revenue_per_store['#L5'] = revenue_per_store['#L5'].str.replace('$', '')
revenue_per_store = revenue_per_store.astype(convert_dict)

number_of_orders = pd.read_csv(number_of_orders)
number_of_orders = number_of_orders.loc[0][0]
number_of_orders = float((number_of_orders.strip('$')).replace(',', ''))
number_of_orders = float(number_of_orders)

revenue_number = pd.read_csv(revenue_number)
revenue_number = revenue_number.loc[0][0]
revenue_number = float((revenue_number.strip('$')).replace(',', ''))
favor_rev = '%.2f' % (revenue_number - (revenue_number * .15))
BM_orders = np.array([orders_per_store['#64'].sum(), orders_per_store['#19'].sum(), orders_per_store['#65'].sum(),
                      orders_per_store['#21'].sum(), orders_per_store['#16'].sum(), orders_per_store['#17'].sum(),
                      orders_per_store['#35'].sum()])
LM_orders = np.array([orders_per_store['#L3'].sum(), orders_per_store['#L4'].sum(), orders_per_store['#L5'].sum()])
Total_orders = np.concatenate((BM_orders,LM_orders))


print('Revenue: $' + str(revenue_number), '\nRevenue less Favor 10%: $' + str(favor_rev))
print('\nOrders Per Store\n#64:', orders_per_store['#64'].sum(), '\n#19:', orders_per_store['#19'].sum(), '\n#65:',
      orders_per_store['#65'].sum(), '\n#21:', orders_per_store['#21'].sum(), '\n#16:', orders_per_store['#16'].sum(),
      '\n#17:', orders_per_store['#17'].sum(), '\n#35:', orders_per_store['#35'].sum(), '\n#L3:',
      orders_per_store['#L3'].sum(), '\n#L4:', orders_per_store['#L4'].sum(), '\n#L5:', orders_per_store['#L5'].sum())
print('Total BM Orders:',BM_orders.sum(),'\nTotal LM Orders:',LM_orders.sum(),'\nTotal Orders:',number_of_orders)






