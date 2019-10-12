
# coding: utf-8

# In[ ]:


# Load Library
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[ ]:


# Load Data
data = pd.read_csv("AppStore.csv")


# In[ ]:


data.head()


# ## Preprocessing

# In[ ]:


data.describe()


# In[ ]:


# take columns
data.columns


# In[ ]:


# drop nan values
data.dropna(inplace=True)


# In[ ]:


# drop columns
data.drop(['URL', 'ID','Icon URL','Description',],axis=1,inplace=True)


# In[ ]:


data.head()


# # EDA

# In[ ]:


plt.figure(figsize=(9, 7), dpi=80)
plt.title("Average User Rating")
plt.grid()
sns.countplot(y=data['Average User Rating'], palette='viridis')


# In[ ]:


plt.figure(figsize=(9, 7), dpi=80)
plt.title("Price")
plt.grid()
sns.countplot(x=data['Price'], palette='viridis')
plt.show()


# In[ ]:


plt.figure(figsize=(9, 4), dpi=80)
plt.title('Age Rating')
plt.grid()
sns.countplot(y=data['Age Rating'], palette='viridis')
plt.show()


# In[ ]:


data['Size'].hist(bins=90)


# In[ ]:


print(' *** Most Developers ***')
data['Developer'].value_counts()[:10]


# In[ ]:


data['Genres'].value_counts()[:20]

