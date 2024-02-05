#!/usr/bin/env python
# coding: utf-8

# # import libraries

# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[2]:


file_path = 'Salaries.csv'


# In[3]:


df = pd.read_csv(file_path)


# # Fetch details for given dataset

# In[4]:


print(df.head())


# In[5]:


print(df.info())


# In[6]:


print(df.describe())


# In[7]:


unique_values = df['salary'].unique()
print("Unique values in Salary:", unique_values)


# In[8]:


unique_values = df['yrs.since.phd'].unique()
print("Unique values in yrs.since.phd:", unique_values)


# In[9]:


missing_values = df.isnull().sum()
print("Missing values per column:\n", missing_values)


# # Q-4 a.	Create a bivariate plot that shows the relationship between the “salary” and “yrs.since.phd” features. The plot must have a title, x label, and y label. 

# In[15]:


x_variable = 'yrs.since.phd'
y_variable = 'salary'

# Creating a scatter plot
plt.scatter(df[x_variable], df[y_variable], label='Bivariate Plot', color='blue', marker='o')

# Adding labels and title
plt.xlabel(f'{x_variable}')
plt.ylabel(f'{y_variable}')
plt.title('Relation between Yrs_Since_PHD - Salary')


# # Q-4 b.	Create a bivariate plot that shows the relationship between the “salary” and “yrs.since.phd”. The plot must have a title, x label, y label, and smooth line that shows the linear relationship between the two features. 

# In[18]:


# Creating a line plot with a regression line
sns.regplot(x='yrs.since.phd', y='salary', data=df)
plt.title('Relation between Yrs_Since_PHD - Salary')
plt.show()


# # Q-4c.	Create a bivariate plot that shows the relationship between the “salary” and “yrs.since.phd”. The plot must have a title, x label, y label, and smooth line that shows the linear relationship between the two features. The datapoints must be colored by the professor “rank”. 

# In[19]:


x_variable = 'yrs.since.phd'
y_variable = 'salary'


# Creating a scatter plot with color-coded datapoints based on 'rank'

sns.scatterplot(x=x_variable, y=y_variable, hue='rank', data=df, palette='viridis')

# Adding labels and title
plt.xlabel(f'{x_variable}')
plt.ylabel(f'{y_variable}')
plt.title('Relation between Yrs_Since_PHD - Salary')

# Displaying the legend
plt.legend()

