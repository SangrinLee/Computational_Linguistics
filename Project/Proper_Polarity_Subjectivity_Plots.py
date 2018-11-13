
# coding: utf-8

# In[91]:

import warnings
warnings.filterwarnings('ignore')

# Handle table-like data and matrices
import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import seaborn as sns

get_ipython().magic(u'matplotlib inline')
mpl.style.use( 'ggplot' )
sns.set_style( 'white' )
pylab.rcParams[ 'figure.figsize' ] = 8 , 6


# In[92]:

def plot_histograms( df , variables , n_rows , n_cols ):
    fig = plt.figure( figsize = ( 16 , 12 ) )
    for i, var_name in enumerate( variables ):
        ax=fig.add_subplot( n_rows , n_cols , i+1 )
        df[ var_name ].hist( bins=10 , ax=ax )
        ax.set_title( 'Skew: ' + str( round( float( df[ var_name ].skew() ) , ) ) ) # + ' ' + var_name ) #var_name+" Distribution")
        ax.set_xticklabels( [] , visible=False )
        ax.set_yticklabels( [] , visible=False )
    fig.tight_layout()  # Improves appearance a bit.
    plt.show()
    
def plot_distribution( df , var , target , **kwargs ):
    row = kwargs.get( 'row' , None )
    col = kwargs.get( 'col' , None )
    facet = sns.FacetGrid( df , hue=target , aspect=4 , row = row , col = col )
    facet.map( sns.kdeplot , var , shade= True )
    facet.set( xlim=( 0 , df[ var ].max() ) )
    facet.add_legend()

def plot_categories( df , cat , target , **kwargs ):
    row = kwargs.get( 'row' , None )
    col = kwargs.get( 'col' , None )
    facet = sns.FacetGrid( df , row = row , col = col )
    facet.map( sns.barplot , cat , target )
    facet.add_legend()

def plot_correlation_map( df ):
    corr = stressData.corr()
    _ , ax = plt.subplots( figsize =( 12 , 10 ) )
    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )
    _ = sns.heatmap(
        corr, 
        cmap = cmap,
        square=True, 
        cbar_kws={ 'shrink' : .9 }, 
        ax=ax, 
        annot = True, 
        annot_kws = { 'fontsize' : 12 }
    )

def describe_more( df ):
    var = [] ; l = [] ; t = []
    for x in df:
        var.append( x )
        l.append( len( pd.value_counts( df[ x ] ) ) )
        t.append( df[ x ].dtypes )
    levels = pd.DataFrame( { 'Variable' : var , 'Levels' : l , 'Datatype' : t } )
    levels.sort_values( by = 'Levels' , inplace = True )
    return levels

def plot_variable_importance( X , y ):
    tree = DecisionTreeClassifier( random_state = 99 )
    tree.fit( X , y )
    plot_model_var_imp( tree , X , y )
    
def plot_model_var_imp( model , X , y ):
    imp = pd.DataFrame( 
        model.feature_importances_  , 
        columns = [ 'Importance' ] , 
        index = X.columns 
    )
    imp = imp.sort_values( [ 'Importance' ] , ascending = True )
    imp[ : 10 ].plot( kind = 'barh' )
    print (model.score( X , y ))


# In[204]:

stressData = pd.read_csv('fullStress.csv')
# if stressData["polarity"][0] < 0:
# num_list = [item for item in stressData["polarity"] if item >= 0]
# print num_list
# for i in stressData["polarity"]:
#     if i < 0:
#         print i

# negative = stressData.ix[(stressData["polarity"] <= 0)]["gender"].count()
# positive = stressData.ix[(stressData["polarity"] > 0)]["gender"].count()
# zero = stressData.ix[(stressData["polarity"] == 0)]["text"].count()
# print negative
# print zero
# print positive

# negative_m = stressData.ix[(stressData["polarity"] <= 0) & (stressData["gender"] == "M")]["gender"].count()
# negative_f = stressData.ix[(stressData["polarity"] <= 0) & (stressData["gender"] == "F")]["gender"].count()
# negative_o = stressData.ix[(stressData["polarity"] <= 0) & (stressData["gender"] == "O")]["gender"].count()
# positive_m = stressData.ix[(stressData["polarity"] > 0) & (stressData["gender"] == "M")]["gender"].count()
# positive_f = stressData.ix[(stressData["polarity"] > 0) & (stressData["gender"] == "F")]["gender"].count()
# positive_o = stressData.ix[(stressData["polarity"] > 0) & (stressData["gender"] == "O")]["gender"].count()

# print negative_m
# print negative_f
# print negative_o
# print positive_m
# print positive_f
# print positive_o

findwork = stressData.ix[(stressData["text"] != "" )]["gender"]
stressData2 = stressData.ix[(stressData["polarity"] <= 0)]
print stressData2["gender"].count()
print stressData2[stressData2["text"].str.contains("work")]["gender"].count()
#print findwork

#polarity less than 0

# file1 = pd.read_csv('finalStress.csv')

# file2 = pd.read_csv('finalStressed.csv')
# file3 = pd.read_csv('full#Stressed.csv')
# file4 = pd.read_csv('results-#stress.csv')
# file5 = pd.read_csv('results-don\'t stressWednesday16.csv')
# file6 = pd.read_csv('results-don\'t worryWednesday16.csv')
# file7 = pd.read_csv('results-not stressedFriday14.csv')
# file8 = pd.read_csv('results-too stressedWednesday16.csv')

# frames = [file1, file2, file3, file4, file5, file6, file7, file8]
# fullStress = pd.concat(frames)

# fullStress.to_csv('fullStress.csv', sep = ',')


# In[163]:

fullStress.shape


# In[164]:

print stressData.shape
# print stressedData.shape


# In[165]:

# print stressData['text']


# In[166]:

# plot_correlation_map( stressData )
plot_correlation_map( fullStress )


# In[167]:

# plot_correlation_map( stressedData )


# In[168]:

# plt.plot(stressData.polarity)


# In[169]:

# a = plt.axes([-1.0, 1.0, 2.5, 2.5])
# ax = sns.countplot(x="polarity", hue = "gender", data=stressData, ax=a)
a = plt.axes([-1.0, 1.0, 2.5, 2.5])
ax = sns.countplot(x="polarity", hue = "gender", data=fullStress, ax=a)


# In[170]:

# a = plt.axes([-1.0, 1.0, 2.5, 2.5])
# ax = sns.countplot(x="subjectivity", hue = "gender", data=stressData, ax=a)
a = plt.axes([-1.0, 1.0, 2.5, 2.5])
ax = sns.countplot(x="subjectivity", hue = "gender", data=fullStress, ax=a)


# In[101]:

# a = plt.axes([-1.0, 1.0, 2.5, 2.5])
# ax = sns.countplot(x="subjectivity", hue = "sex", data=stressedData, ax=a)


# In[59]:

# a = plt.axes([-1.0, 1.0, 2.5, 2.5])
# ax = sns.countplot(x="polarity", hue = "sex", data=stressedData, ax=a)


# In[ ]:



