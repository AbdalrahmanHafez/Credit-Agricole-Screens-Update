import win32com.client
import os

app = win32com.client.Dispatch('Photoshop.Application')

app.Open(r"C:\Users\dahom\Desktop\ps_screen\Project.psd")

doc = app.Application.ActiveDocument

print(doc.ArtLayers)
testlayer = doc.ArtLayers["1"]
testlayer.visiable = False
