# Code Written by Michel Thiebaut de Schotten
# how to install python please follow http://www.bcblab.com/BCB/Coding/Coding.html instructions
# How to install Amico
# download AMICO https://github.com/agoragames/amico – click on clone
# in the terminal, in the dowloaded folder of AMICO please run  pip install .


# Library
import amico
import os, sys
print ("python NoddiThis.py Subjectname bvalfile.bval bvalfile.bvec DWI.nii mask.nii niftifilename.scheme")
Subject = sys.argv[1]
Bval = sys.argv[2]
Bvec = sys.argv[3]
DWI = sys.argv[4]
Mask = sys.argv[5]

#Do NODDI things
amico.core.setup()
ae = amico.Evaluation("", "")
amico.util.fsl2scheme(Bval, Bvec)
#os.rename(Subject + "_DWIMULTISHELL_sorted_MD_C_native.scheme","NODDI_protocol.scheme")
os.rename("eddy_corrected_data.scheme","NODDI_protocol.scheme")
ae.load_data(dwi_filename = DWI, scheme_filename = "NODDI_protocol.scheme", mask_filename = Mask, b0_thr = 0)
ae.set_model("NODDI")
#the long step
ae.generate_kernels()

#the rest
ae.load_kernels()
ae.fit()
ae.save_results()

#rename the AMICO folder
os.rename("AMICO",Subject)
