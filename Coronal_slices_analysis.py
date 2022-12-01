#                             Average per coronal slice

import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from scipy.stats import sem
plt.rcParams['figure.dpi'] = 5000

img_liste=["/pass/to/OD/WM/template.nii.gz"]
for i in range(len(img_liste)):
    img=nib.load(img_liste[i])    
data =img.get_data()

# Slice mean and SEM
brain_slice_mean=[]
brain_slice_sem=[]
for i in range(0,159):
    slice=data[:,i,:]
    vox_list=slice.flatten().tolist()
    vox_list=list(filter(lambda num: num != 0.0, vox_list))
    SE=sem(vox_list) #Standard Error
    vox_list=[np.mean(vox_list)]
    if str(vox_list)=="[nan]": #no brain voxel in the slice
        brain_slice_mean.append([0])
        brain_slice_sem.append(0)
    else: # at least one brain voxel in the slice
        brain_slice_mean.append(vox_list)
        brain_slice_sem.append(SE)
brain_slice_mean = [item for sublist in brain_slice_mean for item in sublist] 


# Histogram
import seaborn as sns
x=np.arange(len(brain_slice_mean))
y=brain_slice_mean
ax = sns.barplot(x, y, color='#FC5A50')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
for index, label in enumerate(ax.get_xticklabels()):
   if index % 10 == 0:
      label.set_visible(True)
   else:
      label.set_visible(False)
#plt.title('')
plt.xlabel('Coronal slices')
plt.ylabel('Mean OD')
plt.xlim([20, 140])
plt.ylim([0.7, 0.9])
plt.errorbar(x, y, brain_slice_sem, linestyle='None', elinewidth=1, fmt='k', marker='None')
plt.show()

