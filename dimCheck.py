import tex2py

from sympy.physics.units.systems.si import dimsys_SI
from sympy.physics.units import time, length, mass

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
        'k': turb_kin_en,
        'l': length, # in DDES
        'L': length, # in SKL
        'p': pressure,
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
        'xk': length}

#----------------------------------------------------------------------------#
# Navier-Stokes
NS_l = r"\frac{\partial \left(\rho U_i \right)}{\partial t}+ \frac{\partial \left( \rho U_i U_j \right)}{\partial x_j}"
NS_r = r"- \frac{\partial p}{\partial x_i} +\frac{\partial \tau^{\star}_{ij}}{\partial x_j} +\rho b_i"

# Menter
Menter_TE_nu_l = r"\frac{\partial \rho \widetilde{\nu}}{\partial t}+\frac{\partial}{\partial x_j} \left(\rho \widetilde{\nu} U_j\right)"
Menter_TE_nu_r = r"C_1 D_1 \rho\widetilde{\nu}\widetilde{S} - C_2 E_{1e}\rho + \frac{\partial}{\partial x_j} \left[ \rho \left( \nu + \frac{\widetilde{\nu}}{\sigma} \right) \frac{\partial \widetilde{\nu}}{\partial x_j}\right]"

# Spalart-Allmaras
SA_TE_nu_l = r"\frac{\partial \rho \widetilde{\nu}}{\partial t}+\frac{\partial}{\partial x_j} \left(\rho \widetilde{\nu} U_j \right)"
SA_TE_nu_r = r"C_{b1}\left(1-f_{v1}\right)\rho\widetilde{S}\widetilde{\nu}+\frac{1}{\sigma} \left\{ \frac{\partial}{\partial x_j} \left[\rho\left(\nu + \widetilde{\nu}\right)\frac{\partial\widetilde{\nu}}{\partial x_j}\right] + C_{b2} \rho \frac{\partial\widetilde{\nu}}{\partial x_j}\frac{\partial \widetilde{\nu}}{\partial x_j} \right\}-\left(C_{w1} f_w -\frac{C_{b1}}{\kappa^2}f_{t2}\right)\rho\left(\frac{\widetilde{\nu}}{d}\right)^2 + f_{t1}\rho \Delta U^2"

# SKL
SKL_TE_Phi_l = r"\frac{\partial \rho \Phi}{\partial t} + \frac{\partial}{\partial x_j} \left(\rho \Phi U_j \right)"
SKL_TE_Phi_r = r"\frac{\Phi}{\widetilde{k}} \rho\nu_t S^2 \left( \zeta_1 - \zeta_2 \left( \frac{L}{L_{v_K}} \right)^2 \right) - \zeta_3 \rho\widetilde{k} + \frac{\partial }{\partial x_j} \left[ \rho \left( \nu + \frac{\nu_t}{\sigma_{\Phi}} \right) \frac{\partial \Phi}{\partial x_j} \right] - 6\rho\nu \frac{\Phi}{d^2} f_\Phi"

# k-epsilon standard
kepsSTD_TE_k_l = r"\frac{\partial \rho k}{\partial t} + \frac{\partial}{\partial x_j} \left(\rho k U_j \right)"
kepsSTD_TE_k_r = r"\tau_{ij} \frac{\partial U_i}{\partial x_j} - \rho\epsilon + \frac{\partial}{\partial x_j} \left[ \rho\left(\nu + \frac{\nu_t}{\sigma_k}\right)\frac{\partial k}{\partial x_j} \right]"

kepsSTD_TE_eps_l = r"\frac{\partial \rho\epsilon}{\partial t} + \frac{\partial}{\partial x_j} \left(\rho\epsilon U_j \right)"
kepsSTD_TE_eps_r = r"C_{\epsilon1}\frac{\epsilon}{k}\tau_{ij}\frac{\partial U_i}{\partial x_j} - C_{\epsilon2}\rho\frac{\epsilon^2}{k} + \frac{\partial}{\partial x_j}\left[\rho\left(\nu + \frac{\nu_t}{\sigma_{\epsilon}}\right)\frac{\partial \epsilon}{\partial x_j} \right]"

# k-epsilon AKN
kepsAKN_TE_k_l = r"\frac{\partial \rho k}{\partial t} + \frac{\partial}{\partial x_j} \left(\rho k U_j \right)"
kepsAKN_TE_k_r = r"\rho\nu_t S^2 - \rho\epsilon + \frac{\partial }{\partial x_j} \left[ \rho\left(\nu + \frac{\nu_t}{\sigma_k} \right) \frac{\partial k}{\partial x_j} \right]"

kepsAKN_TE_eps_l = r"\frac{\partial \rho\epsilon}{\partial t} + \frac{\partial}{\partial x_j} \left(\rho\epsilon U_j \right)"
kepsAKN_TE_eps_r = r"C_{\epsilon1} \frac{\epsilon}{k} \rho\nu_t S^2 - C_{\epsilon2}f_{\epsilon2}\rho\frac{\epsilon^2}{k} + \frac{\partial }{\partial x_j}  \left[  \rho\left(\nu + \frac{\nu_t}{\sigma_\epsilon} \right) \frac{\partial \epsilon}{\partial x_j} \right]"

# k-omega original Wilcox
komWilcox_TE_k_l = r"\frac{\partial \rho k}{\partial t} + \frac{\partial}{\partial x_j} \left(\rho k U_j \right)"
komWilcox_TE_k_r = r"\tau_{ij}\frac{\partial U_i}{\partial x_j} - \beta^{\star} \rho k \omega + \frac{\partial}{\partial x_j}\left[ \rho\left(\nu + \sigma^{\star} \nu_t\right)\frac{\partial k}{\partial x_j}\right]"

komWilcox_TE_om_l = r"\frac{\partial \rho \omega}{\partial t} + \frac{\partial}{\partial x_j} \left(\rho \omega U_j \right)"
komWilcox_TE_om_r = r"\alpha \frac{\omega}{k}\tau_{ij}\frac{\partial U_i}{\partial x_j} - \beta \rho\omega^2 + \frac{\partial}{\partial x_j}\left[ \rho\left(\nu + \sigma^{\star} \nu_t\right)\frac{\partial \omega}{\partial x_j}\right]"

# k-tau
###
###

# k-omega TNT
komTNT_TE_k_l = r"\frac{\partial \rho k}{\partial t} + \frac{\partial}{\partial x_j} \left(\rho k U_j \right)"
komTNT_TE_k_r = r"P_k - \beta^{\star}\rho\omega k + \frac{\partial }{\partial x_j}  \left[  \rho\left(\nu + \nu_t\sigma_k \right) \frac{\partial k}{\partial x_j} \right]"

komTNT_TE_om_l = r"\frac{\partial \rho \omega}{\partial t} + \frac{\partial}{\partial x_j} \left(\rho \omega U_j \right)"
komTNT_TE_om_r = r"\frac{\alpha}{\nu_t}P_k - \beta\rho\omega^2 + \frac{\partial }{\partial x_j}  \left[  \rho\left( \nu + \nu_t\sigma_\omega \right) \frac{\partial \omega}{\partial x_j} \right]  + \rho\frac{\sigma_{d}}{\omega} \frac{\partial k}{\partial x_j}\frac{\partial \omega}{\partial x_j}"

# k-omega SST
komSST_TE_k_l = r"\frac{\partial \rho k}{\partial t} + \frac{\partial}{\partial x_{j}}\left(\rho U_{j}k \right)"
komSST_TE_k_r = r"P_{k}-\beta^{\star} \rho k \omega+\frac{\partial}{\partial x_{j}}\left[\left(\mu + \sigma_{k}\mu_{t}\right)\frac{\partial k}{\partial x_{j}}\right]"

komSST_TE_om_l = r"\frac{\partial \rho \omega}{\partial t} + \frac{\partial}{\partial x_{j}}\left(\rho U_{j}\omega \right)"
komSST_TE_om_r = r"P_{\omega}-\beta \rho \omega^{2} + \frac{\partial}{\partial x_{j}}\left[\left(\mu + \sigma_{\omega}\mu_{t}\right)\frac{\partial \omega}{\partial x_{j}}\right] + 2 \rho \left(1-F_1\right) \frac{\sigma_{\omega 2}}{\omega} \frac{\partial k}{\partial x_{j}}\frac{\partial \omega}{\partial x_{j}}"

# kSkL
kSkL_TE_k_l = r"\frac{\partial \rho k}{\partial t}+\frac{\partial}{\partial x_{j}}(\rho U_{j}k)"
kSkL_TE_k_r = r"P_{k}-C_{\mu}^{\frac{3}{4}}\rho \frac{k^{2}}{\Phi} - 2 \mu \frac{k}{d^2} + \frac{\partial}{\partial x_{j}} \left[\left(\mu+\frac{\mu_{t}}{\sigma_{k}}\right)\frac{\partial k}{\partial x_{j}}\right]"

kSkL_TE_Phi_l = r"\frac{\partial \rho \Phi}{\partial t}+\frac{\partial}{\partial x_{j}}\left(\rho U_{j}\Phi\right)"
kSkL_TE_Phi_r = r"\frac{\Phi}{k}P_{k}\left[\zeta_{1}-\zeta_{2}\left(\frac{L}{L_{v_K}}\right)^{2}\right]-\zeta_{3}\rho k - 6 \mu \frac{\Phi}{d^2}f_{\Phi}+\frac{\partial}{\partial x_{j}}\left[\left(\mu+\frac{\mu_{t}}{\sigma_{\Phi}}\right)\frac{\partial \Phi}{\partial x_{j}}\right]"

# Full RSM
RSM_TE_R_l = r"\frac{\partial \rho R_{ij}}{\partial t}+\frac{\partial}{\partial x_{j}}\left(\rho U_{j} R_{ij} \right)"
RSM_TE_R_r = r"\rho P_{ij} + \rho \Pi_{ij} - \rho \epsilon_{ij} + \rho D_{ij}"

RSM_P_l = r"P_{ij}"
RSM_P_r = r"- R_{ik} \frac{\partial U_j}{\partial x_k} - R_{jk} \frac{\partial U_i}{\partial x_k}"

RSM_Pi_l = r"\Pi_{ij}"
RSM_Pi_r = r"- \left( \beta^{\star}C_1 k \omega + C_1^{\star} P_{kk}/2 \right)  a_{ij} + \beta^{\star}C_2 k \omega \left( a_{ik} a_{kj} -   a_{kl} a_{kl} \delta_{ij}/3 \right) + \left( C_3 - C_3^{\star} \sqrt{ a_{kl} a_{kl}} \right) k S_{ij} + C_4  k \left( a_{ik} S_{jk} + a_{jk}  S_{ik} - 2a_{kl}  S_{kl} \delta_{ij}/3 \right) + C_5   k \left(  a_{ik}  \Omega_{jk} +  a_{jk}  \Omega_{ik} \right)"

RSM_D_l = r"\rho D_{ij}"
RSM_D_r = r"\frac{\partial}{\partial x_j}\left[\left(\nu+\nu_t\frac{C_6}{\beta^{\star}}\right)\frac{\partial\tau_{ij}}{\partial x_j}\right]"

# DDES
DDES_TE_k_l = r"\frac{\partial \rho k}{\partial t}+\frac{\partial}{\partial x_{j}}\left(\rho U_{j}k \right)"
DDES_TE_k_r = r"P_k - \frac{\rho k^{\frac{3}{2}}}{l_t} + \frac{\partial}{\partial x_j} \left(\rho\left(\nu + \nu_t \sigma_k\right)\frac{\partial k}{\partial x_j}\right)"

# XLES
XLES_TE_k_l = r"\frac{\partial \rho k}{\partial t} + \frac{\partial}{\partial x_j} \left(\rho k U_j \right)"
XLES_TE_k_r = r"P_k -\frac{\rho k^{\frac{3}{2}}}{l_t}  +\frac{\partial }{\partial x_j}  \left[ \rho \left(\nu+\nu_t\sigma_k \right) \frac{\partial k}{\partial x_j} \right]"

XLES_TE_om_l = r"\frac{\partial \rho \omega}{\partial t} + \frac{\partial}{\partial x_j} \left(\rho \omega U_j \right)"
XLES_TE_om_r = r"P_{\omega} - \beta_{\omega} \rho \omega^2 + \frac{\sigma_d \rho}{\omega} \frac{\partial k}{\partial x_i}\frac{\partial \omega}{\partial x_i} + \frac{\partial}{\partial x_j} \left(\rho \left(\nu + \sigma_{\omega} \nu_t \right) \frac{\partial \omega}{\partial x_j}\right)"

# PANS
PANS_TE_k_l = r"\frac{\partial \rho k}{\partial t} + \frac{\partial}{\partial x_j} \left(\rho k U_j \right)"
PANS_TE_k_r = r"P_k - \beta^{\star} \rho \omega k + \frac{\partial}{\partial x_j} \left[\rho \left(\nu + \nu_t \sigma_k \frac{f_{\omega}}{f_k} \right) \frac{\partial k}{\partial x_j}\right]"

PANS_TE_om_l = r"\frac{\partial \rho \omega}{\partial t} + \frac{\partial}{\partial x_j} \left(\rho \omega U_j \right)"
PANS_TE_om_r = r"\frac{\alpha}{\nu_t} P_k - \left(P' - \frac{P'}{f_{\omega}} + \frac{\beta \rho \omega}{f_{\omega}}\right) \omega + \frac{\partial}{\partial x_j} \left[ \rho\left(\nu + \nu_t \sigma_{\omega} \frac{f_{\omega}}{f_k} \right) \frac{\partial \omega}{\partial x_j}\right] + 2 \frac{\sigma_{\omega2} \rho}{\omega} \frac{f_{\omega}}{f_k} (1-F_1) \frac{\partial k}{\partial x_j} \frac{\partial \omega}{\partial x_j}"

#----------------------------------------------------------------------------#
expr1 = tex2py.convert_str(RSM_D_l)
expr2 = tex2py.convert_str(RSM_D_r)

dim1 = eval(expr1, dims)
dim2 = eval(expr2, dims)

try:
    check = dimsys_SI.equivalent_dims(dim1, dim2)
except:
    check = False
