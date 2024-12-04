#!/usr/bin/env python
# coding: utf-8

# In[17]:


import win32com.client
import os
from photoshop import Session
import photoshop.api as ps
import keyboard
import time
import subprocess
import winsound
import shutil
from tqdm import tqdm

input_dir = r"C:\Users\dahom\Desktop\ps_screen\Resize_PSD\input"
output_dir = r"C:\Users\dahom\Desktop\ps_screen\Resize_PSD\output"


# In[10]:


app = win32com.client.Dispatch('Photoshop.Application')
app.DisplayDialogs = 3


# In[11]:


#allLayers=[]
def getAllLayers(doc, allLayers):
    for i in range(0, len(doc.Layers)):
        layer = doc.Layers[i]
        if(layer.typename == 'ArtLayer'):
            allLayers.append(layer)
        else:
            getAllLayers(layer, allLayers)
    return allLayers

def rasterizeProblematic():
    problematic = ["Vector Smart Object copy", "Vector Smart Object"]
    for layer in getAllLayers(doc, []):
        if(layer.Kind == 17 and layer.name in problematic):
#             print(f'\t rasterizing {layer.name}')
            layer.Rasterize(6)


# In[12]:


# app = win32com.client.Dispatch('Photoshop.Application')
# app.Open(r"C:\Users\dahom\Desktop\ps_screen\Project.psd")
# doc = app.Application.ActiveDocument


# In[13]:


def saveTo(path, method=2):
    if(method == 0): #PSD
#         doc.SaveAs(SaveIn=path, AsCopy=True, ExtensionType=2)
        options = win32com.client.Dispatch('Photoshop.PhotoshopSaveOptions')
        options.embedColorProfile = True;
        options.alphaChannels = True;
        doc.SaveAs(SaveIn=path, AsCopy=False, Options=options, ExtensionType=2)
    elif(method == 1):
        options = win32com.client.Dispatch('Photoshop.PNGSaveOptions')
        doc.SaveAs(SaveIn=path, Options=options, AsCopy=True, ExtensionType=2)
    else:
        # Very small Size compared to SaveAs
        options = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')
        options.Format = 13
        options.PNG8 = False
        doc.Export(ExportIn=path, ExportAs=2, Options=options)


# In[18]:


for root, directories, files in os.walk(input_dir, topdown=False):
    for file in tqdm(files):
        file_path = os.path.join(root, file)
        noextFile = os.path.splitext(file)[0]
        #print(f'{len(os.listdir(input_dir))} proccessing ({file})')
        app.Open(file_path)
        doc = app.Application.ActiveDocument
        rasterizeProblematic()
        doc.ResizeImage(800, 600, 150, 8)
        saveTo(os.path.join(output_dir, noextFile), 1) # save to output
        saveTo(os.path.join(output_dir, file),0) # save to output
        doc.Close(2)
        os.remove(file_path) #remove from input
#         1/0


# In[ ]:




