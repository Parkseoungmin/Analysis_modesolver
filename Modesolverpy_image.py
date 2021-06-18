import modesolverpy.mode_solver as ms
import modesolverpy.structure as st
import os

# All units are relative.  [um] were chosen in this case.
x_step = 0.02
y_step = 0.02
n_sub = 1.4
n_wg = 3.4
n_clad = 1.
wavelength = 1.55
angle = 90.
sub_height = 0.5
sub_width = 2.
clad_height = 0.5
wg_height = 0.25
film_thickness = 0.5

wg_width = 0.5



structure = st.RidgeWaveguide(wavelength,
                              x_step,
                              y_step,
                              wg_height,
                              wg_width,
                              sub_height,
                              sub_width,
                              clad_height,
                              n_sub,
                              n_wg,
                              angle,
                              n_clad,
                              film_thickness)

if not os.path.exists('.\\res\\figure\\example_structure_1.dat'):
    os.makedirs('.\\res\\figure\\')
    structure.write_to_file(".\\res\\figure\\example_structure_1.dat")

mode_solver = ms.ModeSolverSemiVectorial(5, semi_vectorial_method='Ex')
mode_solver.solve(structure)


mode_solver.write_modes_to_file('example_modes_1.dat')




