from data_cleanup import *
import matplotlib.pyplot as plt

plt.pie(BM_orders, labels=bm_store_num_dict,autopct='%1.1f%%')
plt.title('BM Orders')
plt.show()

plt.pie(LM_orders, labels=lm_store_num_dict,autopct='%1.1f%%')
plt.title('LM Orders')
plt.show()

plt.pie(Total_orders, labels=total_store_num_dict,autopct='%1.1f%%')
plt.title('Total Orders')
plt.show()
