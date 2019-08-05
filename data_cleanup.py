import pandas as pd
import numpy as np

details = "order_details.csv"
number_of_orders = 'total_orders.csv'
orders_per_store = 'orders.csv'
revenue_number = 'total_revenue.csv'
revenue_per_store = 'revenue.csv'
location_dict = {}
convert_dict = {}
bm_store_num_dict = []
lm_store_num_dict = []
total_store_num_dict = bm_store_num_dict + lm_store_num_dict

details = pd.read_csv(details)
details = details.drop(details.columns[0:3], axis=1)
details['Name and Location'] = details['Name and Location'].replace(location_dict, regex=True)
details['Items Cost'] = details['Items Cost'].str.replace('$', '')
details['Items Cost'] = details['Items Cost'].astype(float)
details['Commission'] = details['Commission'].str.replace('$', '')
details['Commission'] = details['Commission'].astype(float)
favor_com = details['Commission'].sum()

store16_d = details[details['Name and Location'].str.contains('#16')]
store17_d = details[details['Name and Location'].str.contains('#17')]
store21_d = details[details['Name and Location'].str.contains('#21')]
store19_d = details[details['Name and Location'].str.contains('#19')]
store35_d = details[details['Name and Location'].str.contains('#35')]
store64_d = details[details['Name and Location'].str.contains('#64')]
store65_d = details[details['Name and Location'].str.contains('#65')]
storeL1_d = details[details['Name and Location'].str.contains('#L1')]
storeL2_d = details[details['Name and Location'].str.contains('#L2')]
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

BM_rev = revenue_per_store['#64'] + revenue_per_store['#19'] + revenue_per_store['#65'] + revenue_per_store['#21'] + \
         revenue_per_store['#16'] + revenue_per_store['#17'] + revenue_per_store['#35']
LM_rev = revenue_per_store['#L1'] + revenue_per_store['#L2'] + revenue_per_store['#L3'] + revenue_per_store['#L4'] + \
         revenue_per_store['#L5']

BM_revs = np.array([revenue_per_store['#64'].sum(), revenue_per_store['#19'].sum(), revenue_per_store['#65'].sum(),
                    revenue_per_store['#21'].sum(), revenue_per_store['#16'].sum(), revenue_per_store['#17'].sum(),
                    revenue_per_store['#35'].sum()])

LM_revs = np.array([revenue_per_store['#L1'].sum(), revenue_per_store['#L2'].sum(), revenue_per_store['#L3'].sum(),
                    revenue_per_store['#L4'].sum(), revenue_per_store['#L5'].sum()])
Total_sales = np.concatenate((BM_revs, LM_revs))

number_of_orders = pd.read_csv(number_of_orders)
number_of_orders = number_of_orders.loc[0][0]
number_of_orders = float(number_of_orders)

revenue_number = pd.read_csv(revenue_number)
revenue_number = revenue_number.loc[0][0]
revenue_number = float((revenue_number.strip('$')).replace(',', ''))
our_rev = '%.2f' % (revenue_number - favor_com)
BM_orders = np.array([orders_per_store['#64'].sum(), orders_per_store['#19'].sum(), orders_per_store['#65'].sum(),
                      orders_per_store['#21'].sum(), orders_per_store['#16'].sum(), orders_per_store['#17'].sum(),
                      orders_per_store['#35'].sum()])
LM_orders = np.array([orders_per_store['#L1'].sum(), orders_per_store['#L2'].sum(), orders_per_store['#L3'].sum(),
                      orders_per_store['#L4'].sum(), orders_per_store['#L5'].sum()])
Total_orders = np.concatenate((BM_orders, LM_orders))

LM_Items_mean = np.nanmean(np.array(
    [storeL1_d['Items Cost'].mean(), storeL2_d['Items Cost'].mean(), storeL5_d['Items Cost'].mean(),
     storeL4_d['Items Cost'].mean(), storeL3_d['Items Cost'].mean()]))
LM_Items_median = np.nanmedian(np.array(
    [storeL1_d['Items Cost'].median(), storeL2_d['Items Cost'].median(), storeL5_d['Items Cost'].median(),
     storeL4_d['Items Cost'].median(), storeL3_d['Items Cost'].median()]))
LM_Com_mean = np.nanmean(np.array(
    [storeL1_d['Commission'].mean(), storeL2_d['Commission'].mean(), storeL5_d['Commission'].mean(),
     storeL4_d['Commission'].mean(), storeL3_d['Commission'].mean()]))
LM_Com_median = np.nanmedian(np.array(
    [storeL1_d['Commission'].median(), storeL2_d['Commission'].median(), storeL5_d['Commission'].median(),
     storeL4_d['Commission'].median(), storeL3_d['Commission'].median()]))
LM_Runner_mean = np.nanmean(np.array(
    [storeL1_d['Runner Rating'].mean(), storeL2_d['Runner Rating'].mean(), storeL5_d['Runner Rating'].mean(),
     storeL4_d['Runner Rating'].mean(), storeL3_d['Runner Rating'].mean()]))
LM_Runner_median = np.nanmedian(np.array(
    [storeL1_d['Runner Rating'].median(), storeL2_d['Runner Rating'].median(), storeL5_d['Runner Rating'].median(),
     storeL4_d['Runner Rating'].median(), storeL3_d['Runner Rating'].median()]))
LM_Rating_mean = np.nanmean(np.array(
    [storeL1_d['Item Rating'].mean(), storeL2_d['Item Rating'].mean(), storeL5_d['Item Rating'].mean(),
     storeL4_d['Item Rating'].mean(), storeL3_d['Item Rating'].mean()]))
LM_Rating_median = np.nanmedian(np.array(
    [storeL1_d['Item Rating'].median(), storeL2_d['Item Rating'].median(), storeL5_d['Item Rating'].median(),
     storeL4_d['Item Rating'].median(), storeL3_d['Item Rating'].median()]))
LM_Time_mean = np.nanmean(np.array(
    [storeL1_d['Time at Merchant'].mean(), storeL2_d['Time at Merchant'].mean(), storeL5_d['Time at Merchant'].mean(),
     storeL4_d['Time at Merchant'].mean(), storeL3_d['Time at Merchant'].mean()]))
LM_Time_median = np.nanmedian(np.array([storeL1_d['Time at Merchant'].median(), storeL2_d['Time at Merchant'].median(),
                                        storeL5_d['Time at Merchant'].median(), storeL4_d['Time at Merchant'].median(),
                                        storeL3_d['Time at Merchant'].median()]))

BM_Items_mean = np.nanmean(np.array(
    [store16_d['Items Cost'].mean(), store17_d['Items Cost'].mean(), store19_d['Items Cost'].mean(),
     store21_d['Items Cost'].mean(), store35_d['Items Cost'].mean(), store64_d['Items Cost'].mean(),
     store65_d['Items Cost'].mean()]))
BM_Items_median = np.nanmedian(np.array(
    [store16_d['Items Cost'].median(), store17_d['Items Cost'].median(), store19_d['Items Cost'].median(),
     store21_d['Items Cost'].median(), store35_d['Items Cost'].median(), store64_d['Items Cost'].median(),
     store65_d['Items Cost'].median()]))

BM_Com_mean = np.nanmean(np.array(
    [store16_d['Commission'].mean(), store17_d['Commission'].mean(), store19_d['Commission'].mean(),
     store21_d['Commission'].mean(), store35_d['Commission'].mean(), store64_d['Commission'].mean(),
     store65_d['Commission'].mean()]))
BM_Com_median = np.nanmedian(np.array(
    [store16_d['Commission'].median(), store17_d['Commission'].median(), store19_d['Commission'].median(),
     store21_d['Commission'].median(), store35_d['Commission'].median(), store64_d['Commission'].median(),
     store65_d['Commission'].median()]))
BM_Runner_mean = np.nanmean(np.array(
    [store16_d['Runner Rating'].mean(), store17_d['Runner Rating'].mean(), store19_d['Runner Rating'].mean(),
     store21_d['Runner Rating'].mean(), store35_d['Runner Rating'].mean(), store64_d['Runner Rating'].mean(),
     store65_d['Runner Rating'].mean()]))
BM_Runner_median = np.nanmedian(np.array(
    [store16_d['Runner Rating'].median(), store17_d['Runner Rating'].median(), store19_d['Runner Rating'].median(),
     store21_d['Runner Rating'].median(), store35_d['Runner Rating'].median(), store64_d['Runner Rating'].median(),
     store65_d['Runner Rating'].median()]))
BM_Rating_mean = np.nanmean(np.array(
    [store16_d['Item Rating'].mean(), store17_d['Item Rating'].mean(), store19_d['Item Rating'].mean(),
     store21_d['Item Rating'].mean(), store35_d['Item Rating'].mean(), store64_d['Item Rating'].mean(),
     store65_d['Item Rating'].mean()]))
BM_Rating_median = np.nanmedian(np.array(
    [store16_d['Item Rating'].median(), store17_d['Item Rating'].median(), store21_d['Item Rating'].median(),
     store21_d['Item Rating'].median(), store35_d['Item Rating'].median(), store65_d['Item Rating'].median(),
     store64_d['Item Rating'].median()]))
BM_Time_mean = np.nanmean(np.array(
    [store16_d['Time at Merchant'].mean(), store17_d['Time at Merchant'].mean(), store21_d['Time at Merchant'].mean(),
     store21_d['Time at Merchant'].mean(), store35_d['Time at Merchant'].mean(), store65_d['Time at Merchant'].mean(),
     store64_d['Time at Merchant'].mean()]))
BM_Time_median = np.nanmedian(np.array([store16_d['Time at Merchant'].median(), store17_d['Time at Merchant'].median(),
                                        store21_d['Time at Merchant'].median(), store21_d['Time at Merchant'].median(),
                                        store35_d['Time at Merchant'].median(), store65_d['Time at Merchant'].median(),
                                        store64_d['Time at Merchant'].median()]))
