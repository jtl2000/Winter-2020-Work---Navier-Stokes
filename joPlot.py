#!/usr/bin/env python
# coding: utf-8

# In[79]:


import numpy as np
import matplotlib.pyplot as plt

def JoPlot(ax, data1, titlename, param_dict):
    ax.spines["top"].set_visible(True)    
    ax.spines["bottom"].set_visible(True)    
    ax.spines["right"].set_visible(True)    
    ax.spines["left"].set_visible(True) 

    font=16
    
    ax.get_xaxis().tick_bottom()    
    ax.get_yaxis().tick_left() 
    
    for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
             ax.get_xticklabels() + ax.get_yticklabels()):
        item.set_fontsize(font)

    plt.yticks(fontsize=14)    
    plt.xticks(fontsize=14) 

    plt.grid(True)
    plt.title(titlename, fontsize=font+5)
    
    out = ax.plot(data1, **param_dict)
    return out


# In[80]:


#plt.figure(figsize=(12, 14)) 
#ax = plt.subplot(111)
#JoPlot(ax, height, data1, titlename)

