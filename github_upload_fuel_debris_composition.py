from pickle import FALSE

from xml.etree.ElementTree import PI

import numpy as np

 

import pandas as pd

 

from matplotlib import pyplot as plt

 

from sklearn.datasets import make_classification

 

from sdv.tabular import GaussianCopula

 

from sdv.evaluation import evaluate

 

from itertools import product 

uo2_mass = 20

mass_uo2 = np.random.randint(0, 69, uo2_mass)
 
df1 = pd.DataFrame({"customer_id":mass_uo2})

print (df1)

#####################################

ZrO2_mass = 20

mass_ZrO2 = np.random.randint(0, 25, ZrO2_mass)

df2 = pd.DataFrame({"customer_id":mass_ZrO2})

print (df2)

#########################################################

zr_mass = 20

mass_zr = np.random.randint(0, 16, zr_mass)

df3 = pd.DataFrame({"customer_id":mass_zr})

print (df3)

###################################################################

fe_mass = 20

mass_fe = np.random.randint(0, 20, fe_mass)

df4 = pd.DataFrame({"customer_id":mass_fe})

print (df4)

########################################################################

##################  AFTER 10 YEARS ##################
 

total_mass_u=78000000

total_mass_cm244=616

mass_sm=130000000-total_mass_u

rho_u=19

rho_cm244=13.5

rho_sm=5.84


## sm = structrual material

area=1.96E+05

unit_area=1*1

 
hmax_fuel=total_mass_u/(rho_u*area)

hmax_sm= mass_sm/(rho_sm*area)

hmax_cm244=total_mass_cm244/(rho_cm244*area)

print('hmax fuel',hmax_fuel)

print('hmax_sm',hmax_sm)

print('hmax_cm244l',hmax_cm244)

mass_max_unit_area_u=hmax_fuel*rho_u*unit_area

mass_max_unit_area_cm244=hmax_cm244*rho_cm244*unit_area

mass_max_unit_area_sm=hmax_sm*rho_sm*unit_area

 

hmax=hmax_fuel+hmax_sm+hmax_cm244

 

uranium_height=[]

sm_height=[]

print('max mass cm244',mass_max_unit_area_cm244)
print('max height for all materials',hmax)
 

for mass in range(0,int(mass_max_unit_area_u),int(mass_max_unit_area_u/40.0)):

    print('mass u',mass)

    h_fuel=mass/(rho_u*unit_area)

    uranium_height.append(h_fuel)

    h_sm=hmax-h_fuel

    sm_height.append(h_sm)

 

    print('h uranium',h_fuel)

    print('h sm',h_sm)

    ## we create 40 cases for different mass and height of uranium and structural material

    ## to produce more cases, we create 40 different neutron intensity depends on the mass of the cm244

print('matrix of uranium',uranium_height)

#for mass1 in range(0,int(mass_max_unit_area_cm244),int(mass_max_unit_area_cm244/40.0)):

#    print('mass cm244',mass1)

for mass2 in range(0,int(mass_max_unit_area_sm),int(mass_max_unit_area_sm/40.0)):

    print('mass sm',mass2)

#    h_sm=mass2/(rho_sm*unit_area)

#    print('h sm calculation',h_sm)


array=(list(product([uranium_height],[sm_height])))

data=pd.DataFrame({"uo2":[uranium_height],"zro2":[sm_height]})

array=(list(product(data["uo2"],data["zro2"])))


u_neutron=[]

sm_neutron=[]

neutron_intensity=[]

for n in range(int(1.11E+07),int(6.86E+09),int(6.86E+09/40.0)):

    neutron_intensity.append(n)

    print(neutron_intensity)

 

for r in product(uranium_height, neutron_intensity):

    print ((r[0],r[1]))

    u_neutron.append((r[0],r[1]))

df=pd.DataFrame(u_neutron)

df.to_csv('u_neutron.csv',index=False)

 

for r1 in product(sm_height, neutron_intensity):

    print ((r1[0],r1[1]))

    sm_neutron.append((r1[0],r1[1]))

df1=pd.DataFrame(sm_neutron)

df1.to_csv('sm_neutron.csv',index=False)


print('array',array)

my_df=pd.DataFrame(array)


mass_cm244=[0,mass_max_unit_area_cm244,2.36E-04]

#we divded by 40 to create 40 masses

rho=(mass_u+mass_cm244)/((mass_u/rho_u)+(mass_cm244/rho_cm244))

mass_mix=mass_cm244+mass_u

 
h_fuel=mass_mix/(rho*unit_area)

 
h_sm=hmax-h_fuel

#if we divide by 40 to create 40 positions


# n=[1,40] series start with 1 ends 40

h_sm=h_sm-n*(h_sm/40)

 

mix_array >add(mass_u+mass_cm244)

position_array>add(h_fuel,h_sm)

 


 
