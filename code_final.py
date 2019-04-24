#!/usr/bin/env python
# coding: utf-8

# In[34]:


#!/usr/bin/env python


# In[ ]:


import pandas as pd
#Loading the dataset
userItemData = pd.read_csv("file.csv")
userItemData.head()

#Get list of unique items
itemList=list(set(userItemData["ItemId"].tolist()))

#Get count of users
userCount=len(set(userItemData["ItemId"].tolist()))

#Create an empty data frame to store item affinity scores for items.
itemAffinity= pd.DataFrame(columns=('item1', 'item2', 'name', 'score'))
rowCount=0

#For each item in the list, compare with other items.
for ind1 in range(len(itemList)):
    
    #Get list of users who bought this item 1.
    item1Users = userItemData[userItemData.ItemId==itemList[ind1]]["UserId"].tolist()
    
    item1name = userItemData[userItemData.ItemId==itemList[ind1]]["ItemName"].tolist()
    #print("Item 1 ", item1Users)
    
    #Get item 2 - items that are not item 1 or those that are not analyzed already.
    for ind2 in range(ind1, len(itemList)):
        
        if ( ind1 == ind2):
            continue
       
        #Get list of users who bought item 2
        item2Users=userItemData[userItemData.ItemId==itemList[ind2]]["UserId"].tolist()
        
        item2name=userItemData[userItemData.ItemId==itemList[ind2]]["ItemName"].tolist()
        #print("Item 2",item2Users)
        
        #Find score. Find the common list of users and divide it by the total users.
        commonUsers= len(set(item1Users).intersection(set(item2Users)))
        score=float(float(commonUsers) / float(userCount))

        #Add a score for item 1, item 2
        if score!=0.0:
            itemAffinity.loc[rowCount] = [itemList[ind1],itemList[ind2],item2name[0],score]
            rowCount +=1
            #Add a score for item2, item 1. The same score would apply irrespective of the sequence.
            itemAffinity.loc[rowCount] = [itemList[ind2],itemList[ind1],item2name[0],score]
            rowCount +=1
#Check final result
itemAffinity.head()

def stringtonumber(product):
    switcher = {
        "Smartphone":5001,
        "Back cover":5002,
        "Earphones":5003,
        "Tempered glass":5004,
        "Power Bank":5005,
        "Data Cable":5006,
        "Charger":5007,
        "Earphone splitter":5008,
        "Laptop":5009,
        "Laptop bag":5010,
        "Mouse":5011,
        "Keyboard":5012,
        "Pendrive":5013,
        "Memory Card":5014,
        "Hard disk":5015,
    }
    return switcher.get(product, "nothing") 

product=str(raw_input("what product are you looking for?:"))
searchItem=stringtonumber(product)
recoList=itemAffinity[itemAffinity.item1==searchItem][["item2","name","score"]].sort_values("score", ascending=[0])
        
print "Here are some awesome products that you can buy with a", product, "according to our users."
print recoList
print "Enjoy shopping with us."





# In[ ]:




