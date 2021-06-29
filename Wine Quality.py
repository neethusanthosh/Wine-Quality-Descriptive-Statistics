#!/usr/bin/env python
# coding: utf-8

# ### About the Data set (Wine Quality.csv)
# Attribute Information:
# 
# The dataset are related to red and white variants of the "Vinho Verde" wine. Vinho verde is a unique product from the Minho (northwest) region of Portugal. Medium in alcohol, is it particularly appreciated due to its freshness (specially in the summer). 
# 
#     1 - fixed acidity 
#     2 - volatile acidity 
#     3 - citric acid 
#     4 - residual sugar 
#     5 - chlorides 
#     6 - free sulfur dioxide 
#     7 - total sulfur dioxide 
#     8 - density 
#     9 - pH 
#     10 - sulphates 
#     11 - alcohol Output variable (based on sensory data): 
#     12 - quality (score between 0 and 10)

# ## 1. Load the libraries:

# In[5]:


data=pd.read_csv('wine_data.csv')


# ## 2. Importing the dataset:

# In[6]:


data


# ## 3.EDA Descriptive Statistics:

# ### 3.1.  Measures of Central Tendency
# 
# Measures of Central Tendency define significant, representative and adequate values for a set of data, depending on what you want to analyze. They are the 
# 
# 1. mean
# 2. median
# 3. quantiles and mode.

# ### 3.2 Check the  mean ,Mode, Median and Quantile for dataset?

# #### Mean

# In[7]:


data.mean()


# #### Mode

# In[8]:


data.mode()


# #### Median and Quantile

# ### 3.4 check (Quantile 25%,50%,75%) for dataset

# #### Quantile 25%

# In[9]:


data.quantile(.25)


# 
# #### Quantile 50%

# In[10]:


data.quantile(.5)


# #### Quantile 75%

# In[11]:


data.quantile(.75)


# ## 4. Measures of Dispersion

# Measures of Dispersion are measures that indicate how spread the data is, or how they vary. The measures of dispersion are range, variance, standard deviation and the absolute deviation, or mean absolute deviation.

# ### 4.1 check the Range,Variance,Standard Deviation,Absolute Deviation or Mean Absolute Deviation?

# #### Range

# In[12]:


data.max()-data.min()


# #### Variance

# In[13]:


data.var()


# #### Standard Deviation

# In[14]:


data.std()


# #### Absolute Deviation or Mean Absolute Deviation

# ## 5. Covariance and Correlation

# 1. Covariance is a numerical measure that indicates the inter-dependency between two variables. 
# 2. Covariance indicates how two variables behave together in relation to their averages. 
# 3. A covariance of 0 indicates that the variables are totally independant, while a high and positive covariance value means that a variable is big when the other is big. Analogously, a negative covariance with a high absolute value means that one variable is big when the other is small.
# 4. Covariance can be calculated through the cov() function. 

# ### 5.1 Check the Covariance and Correlation scores . write your Observations?

# #### Covariance

# In[15]:


data.cov()


# #### Correlation

# In[16]:


data.corr()


# #### Observation:
#     
# 

# If we consider quality as parameter We can't observe any corelation between other feature and Quality where as alcohol shows a fare bit good correlation .
