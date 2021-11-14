#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

def imshow(X, resize=None):
    @interact(X=fixed('Image') , resize =widgets.IntSlider(min=10, max=1250))
    PIL_image = Image.open(X)
    resize = PIL_image.resize((resize, resize))
    return resize

