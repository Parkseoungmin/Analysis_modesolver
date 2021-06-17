import modesolverpy.mode_solver as ms
import modesolverpy.structure as st
import numpy as np
import pandas as pd

total_list = [] # element : [w_wg,t_soi,t_slab,n_eff]
w_wg_list = np.linspace(0,2,20) # 0.2 ~ 1


def find_n_eff(wg_width:float)->float:
    x_step = 0.02
    y_step = 0.02
    sub_height = 0.5
    sub_width = 2.
    n_sub = 1.4
    n_wg = 3.4
    n_clad = 1.
    wavelength = 1.31
    angle = 90.
    clad_height = 0.5
    film_thickness = 0.5
    wg_height = 0.25
    structure = st.RidgeWaveguide(wavelength, x_step, y_step, wg_height,
                                  wg_width,sub_height,sub_width,clad_height,
                                  n_sub,n_wg,angle,n_clad,film_thickness)
    mode_solver = ms.ModeSolverSemiVectorial(5, semi_vectorial_method='Ex')
    a = mode_solver.solve(structure)
    return a["n_effs"][0].real # 구해야 하는 것 [mode : 0에서의 n_eff]


for i in w_wg_list:
    a = find_n_eff(i)
    total_list.append([i,a])

df = pd.DataFrame(total_list,columns = ['w_wg_list','n_effs'])
print(df.head(5))
if not os.path.exists('.\\res\\csv\\n_effs_01csv'):
    os.makedirs('.\\res\\csv\\')
    df.to_csv(".\\res\\csv\\n_effs_01csv",index=False)
