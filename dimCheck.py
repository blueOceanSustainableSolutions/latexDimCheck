## Original author: Manuel Rentschler
# Modifications to read complete latex files by Maarten Klapwijk
# 08-06-2021

import tex2py

from sympy.physics.units.systems.si import dimsys_SI
from sympy.physics.units import time, length, mass

import numpy as np

# Define new dimensions based on SI
area = length**2
volume = length**3
speed = length/time
acceleration = length/time**2
viscosity_kin = length**2/time
dissip_rate = 1/time
turb_dissip_rate = length**2/time**3

# Define derived dimensions
force = mass*acceleration
pressure = force/area
density = mass/volume
viscosity_dyn = viscosity_kin*density
strain_rate = speed/length
stress = force/area
turb_kin_en = speed**2
prod_k = stress*speed/length
prod_omega = prod_k/viscosity_kin
prod_PANS = density*turb_kin_en/viscosity_kin
RSM_specific = turb_dissip_rate
RSM_specStress = stress/density
cavitySourceTerm = mass/(volume*time)

# Assignment of dimensions
dims = {'alpha': 1,
        'beta': 1,
        'betaomega': 1,
        'delta': 1, # Kronecker delta in RSM
        'epsilon': turb_dissip_rate,
        'kappa': 1,
        'mu': viscosity_dyn,
        'nu': viscosity_kin,
        'omega': dissip_rate,
        'Omega': dissip_rate, # in RSM
        'Phi': viscosity_kin, # in SKL and kSkL
        'rho': density,
        'sigma': 1,
        'sigmak': 1,
        'sigmaomega': 1,
        'tau': stress,
        'zeta': 1,
        'a': 1, # anisotropy tensor in RSM
        'b': acceleration, # bodyforce in NS?
        'C': 1,
        'd': length, # distance in SA, kSkL
        'D': 1,
        'Dij': RSM_specific,
        'E': turb_kin_en, # E in Menter?
        'f': 1,
        'fomega': 1,
        'fk': 1,
        'F': 1,
        'betastar': 1,
        'Psi': 1,
        'psi': 1,
        'pi': 1,
        'T': time,
        'k': turb_kin_en,
        'l': length, # in DDES
        'L': length, # in SKL
        'p': pressure,
        'n': 1,
        'q': volume/area,
        'P': prod_PANS, # P' in PANS
        'Piij': RSM_specific,
        'Pij': RSM_specific,
        'Pk': prod_k,
        'Pkk': RSM_specific,
        'Pomega': prod_omega,
        'Rij': RSM_specStress,
        'Rik': RSM_specStress,
        'Rjk': RSM_specStress,
        'S': strain_rate,
        't': time,
        'u': speed,
        'U': speed,
        'x': length,
        'Scav' : cavitySourceTerm,
        'xk': length}

#----------------------------------------------------------------------------#
#### Main
inputFile = "testFiles/KLAPWIJKetal2021.tex"

stringToSearch = "equation"


# Find equations linenumbers in file (for now only {equation})
eqLineNumStart = np.array((),int)
eqLineNumEnd = np.array((),int)

with open(inputFile) as myFile:
    for num, line in enumerate(myFile, 1):
        if "\\begin{"+stringToSearch+"}" in line:
            eqLineNumStart = np.append(eqLineNumStart,num)
        if "\end{"+stringToSearch+"}" in line:
            eqLineNumEnd = np.append(eqLineNumEnd,num)
            
if len(eqLineNumStart) != len(eqLineNumEnd):
  print("Mismatch between start and end of equations. ERROR!\n")



# open file for equations extraction 
myFile = open(inputFile)
lines = myFile.readlines()

equationNum = 0

for i in range(0,len(eqLineNumStart)):
  equationNum += 1
  if np.mod(i,10) == 0:
    print("Processed", equationNum,"equations of", len(eqLineNumStart))
  equation = ' '.join(lines[(eqLineNumStart[i]):(eqLineNumEnd[i]-1)])
  
  # Remove excess labels
  if "\label{" in equation:
    print("Label found in between lines:", eqLineNumStart[i],"to",eqLineNumEnd[i]-1, "Move to \\begin{equation} line!\n")
    continue
  if "\\begin{cases}" in equation:
    print("Cases found in equation:", eqLineNumStart[i],"to",eqLineNumEnd[i]-1, "Not processed!\n")
    continue

  # Modify inequalities and approximations
  equation = tex2py.prepare_eq(equation)

  # Check number of =
  if equation.count("=") != 1:
    print("Equals sign count:",equation.count("="),"Impossible to distinguish LHS and RHS for lines:", eqLineNumStart[i],"to",eqLineNumEnd[i]-1, "CHECK!\n")
    continue


  # Divide into LHS and RHS, and convert
  equalsLoc = str.find(equation,"=")


  LHS = tex2py.convert_str(equation[:equalsLoc])
  RHS = tex2py.convert_str(equation[equalsLoc+1:])

 
  # Evaluate dimensions
  try:
    dim1 = eval(LHS, dims)
  except:
    print("Undefined variable in LHS of lines:", eqLineNumStart[i],"to",eqLineNumEnd[i]-1,"\n\nLHS:",equation[:equalsLoc],"\n")
    dim1 = eval(LHS, dims) 
  try:
    dim2 = eval(RHS, dims)
  except:
    print("\nUndefined variable in RHS of lines:", eqLineNumStart[i],"to",eqLineNumEnd[i]-1,"\n\nRHS:",equation[equalsLoc+1:],"\n")
    print(equation)
    dim2 = eval(RHS, dims) 




  try:
      check = dimsys_SI.equivalent_dims(dim1, dim2)
  except:
      check = False
  print("I need to implement final error messages",check)

myFile.close()



# EOF
