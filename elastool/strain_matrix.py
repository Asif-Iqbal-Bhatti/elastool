"""
  Elastool -- Elastic toolkit for finite-temperature elastic constants calculations

  Copyright (C) 2019-2020 by Zhong-Li Liu

  This program is free software; you can redistribute it and/or modify it under the
  terms of the GNU General Public License as published by the Free Software Foundation
  version 3 of the License.

  This program is distributed in the hope that it will be useful, but WITHOUT ANY
  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
  PARTICULAR PURPOSE.  See the GNU General Public License for more details.

  E-mail: zl.liu@163.com
"""
from read_input import indict
from numpy import array


def strain_matrix(latt_system, up0):
    strain_matrix_list = []
    if indict['strains_matrix'][0] == 'ohess':
        up = up0
        if indict['dimensional'][0] == '3D':
            if latt_system == 'Cubic':
                strain_matrix_1 = array([[up,    0.,    0.], 
                                            [0.,    0., up/2.], 
                                            [0.,  up/2.,   0.]])
                strain_matrix_list.append(strain_matrix_1)

            elif latt_system == 'Hexagonal':
                strain_matrix_1 = array([[up,    0.,    0.], 
                                            [0.,    0.,    0.], 
                                            [0.,    0.,    0.]])
                strain_matrix_2 = array([[0.,    0.,    0.], 
                                            [0.,    0., up/2.], 
                                            [0.,    up/2., up]])
                strain_matrix_list.extend((strain_matrix_1, strain_matrix_2))
            elif latt_system in ['Trigonal1', 'Trigonal2']:
                strain_matrix_1 = array([[up,    0.,    0.], 
                                            [0.,    0.,    0.], 
                                            [0.,    0.,    0.]])
                strain_matrix_2 = array([[0.,    0.,    0.], 
                                            [0.,    0., up/2.], 
                                            [0.,    up/2.,up]])
                strain_matrix_list.extend((strain_matrix_1, strain_matrix_2))
            elif latt_system in ['Tetragonal1', 'Tetragonal2']:
                strain_matrix_1 = array([[up,    0.,    0.], 
                                            [0.,    0.,    0.], 
                                            [0.,    0.,    0.]])
                strain_matrix_2 = array([[0.,    up/2., 0.], 
                                            [up/2., 0., up/2.], 
                                            [0.,    up/2., up]])
                strain_matrix_list.extend((strain_matrix_1, strain_matrix_2))
            elif latt_system == 'Orthorombic':
                strain_matrix_1 = array([[up,    0.,    0.], 
                                            [0.,    0.,    0.], 
                                            [0.,    0.,    0.]])
                strain_matrix_2 = array([[0.,    0.,    0.], 
                                            [0.,    up,    0.], 
                                            [0.,    0.,    0.]])
                strain_matrix_3 = array([[0.,  up/2.,up/2.], 
                                            [up/2., 0., up/2.], 
                                            [up/2., up/2., up]])
                strain_matrix_list.extend((strain_matrix_1, strain_matrix_2, strain_matrix_3))
            elif latt_system == 'Monoclinic':
                strain_matrix_1 = array([[up,    0.,   0.], 
                                            [0.,    0.,   0.], 
                                            [0.,    0.,   0.]])
                strain_matrix_2 = array([[0.,    0.,   0.], 
                                            [0.,    up,   0.], 
                                            [0.,    0.,   0.]])
                strain_matrix_3 = array([[0.,    0.,   0.], 
                                            [0.,    0.,up/2.], 
                                            [0., up/2.,   up]])
                strain_matrix_4 = array([[0., up/2.,up/2.], 
                                            [up/2., 0.,   0.], 
                                            [up/2., 0.,   0.]])
                strain_matrix_list.extend(
                    (
                        strain_matrix_1,
                        strain_matrix_2,
                        strain_matrix_3,
                        strain_matrix_4,
                    )
                )

            elif latt_system == 'Triclinic':
                strain_matrix_1 = array([[up,    0.,   0.], 
                                            [0.,    0.,   0.], 
                                            [0.,    0.,   0.]])
                strain_matrix_2 = array([[0.,    0.,   0.], 
                                            [0.,    up,   0.], 
                                            [0.,    0.,   0.]])
                strain_matrix_3 = array([[0.,    0.,   0.], 
                                            [0.,    0.,   0.], 
                                            [0.,    0.,   up]])
                strain_matrix_4 = array([[0.,    0.,   0.], 
                                            [0.,    0.,up/2.], 
                                            [0., up/2.,   0.]])
                strain_matrix_5 = array([[0.,    0.,up/2.], 
                                            [0.,    0.,   0.], 
                                            [up/2., 0.,   0.]])
                strain_matrix_6 = array([[0., up/2.,   0.], 
                                            [up/2., 0.,   0.], 
                                            [0.,    0.,   0.]])
                strain_matrix_list.extend(
                    (
                        strain_matrix_1,
                        strain_matrix_2,
                        strain_matrix_3,
                        strain_matrix_4,
                        strain_matrix_5,
                        strain_matrix_6,
                    )
                )

        elif indict['dimensional'][0] == '2D':
            # 2D in-plane strains: in xy plane
            if latt_system == 'isotropy':
                strain_matrix_1 = array([[up,    0.,    0.], 
                                            [0.,    0.,    0.], 
                                            [0.,    0.,    0.]])
                strain_matrix_list.append(strain_matrix_1)

            elif latt_system == 'tetragonal':
                strain_matrix_1 = array([[up,  up/2,    0.], 
                                            [up/2,  0.,    0.], 
                                            [0.,    0.,    0.]])
                strain_matrix_list.append(strain_matrix_1)

            elif latt_system == 'orthotropy':
                strain_matrix_1 = array([[up,  up/2,    0.], 
                                            [up/2,  0.,    0.], 
                                            [0.,    0.,    0.]])
                strain_matrix_2 = array([[0.,    0.,    0.], 
                                            [0.,    up,    0.], 
                                            [0.,    0.,    0.]])
                strain_matrix_list.extend((strain_matrix_1, strain_matrix_2))
            elif latt_system == 'anisotropy':
                strain_matrix_1 = array([[up,    0.,    0.], 
                                            [0.,    0.,    0.], 
                                            [0.,    0.,    0.]])
                strain_matrix_2 = array([[0.,    0.,    0.], 
                                            [0.,    up,    0.], 
                                            [0.,    0.,    0.]])
                strain_matrix_3 = array([[0.,  up/2,    0.], 
                                            [up/2,  0.,    0.], 
                                            [0.,    0.,    0.]])
                strain_matrix_list.extend((strain_matrix_1, strain_matrix_2, strain_matrix_3))
    elif indict['strains_matrix'][0] == 'asess':
        if indict['dimensional'][0] == '3D':
            strain_matrix_1 = up0 * array([[1.,   0.,  0.], 
                                              [0.,   0.,  0.], 
                                              [0.,   0.,  0.]])
            strain_matrix_2 = up0 * array([[0.,   0.,  0.], 
                                              [0.,   1.,  0.], 
                                              [0.,   0.,  0.]])
            strain_matrix_3 = up0 * array([[0.,   0.,  0.], 
                                              [0.,   0.,  0.], 
                                              [0.,   0.,  1.]])
            strain_matrix_4 = up0 * array([[0.,   0,   0.], 
                                              [0.,  0.,1./2.], 
                                              [0.,  1./2.,0.]])
            strain_matrix_5 = up0 * array([[0., 0., 1./2.], 
                                              [0.,   0.,  0.], 
                                              [1./2.,0.,  0.]])
            strain_matrix_6 = up0 * array([[0., 1./2., 0.], 
                                              [1./2.,  0.,0.], 
                                              [0.,   0.,  0.]])
            strain_matrix_list = [strain_matrix_1, strain_matrix_2, strain_matrix_3, strain_matrix_4, strain_matrix_5, strain_matrix_6]

        elif indict['dimensional'][0] == '2D':
            strain_matrix_1 = up0 * array([[1.,    0.,  0.], 
                                              [0.,    0.,  0.], 
                                              [0.,    0.,  0.]])
            strain_matrix_2 = up0 * array([[0.,    0.,  0.], 
                                              [0.,    1.,  0.], 
                                              [0.,    0.,  0.]])
            strain_matrix_3 = up0 * array([[0., 1./2.,  0.], 
                                              [1./2., 0.,  0.], 
                                              [0.,    0.,  0.]])
            strain_matrix_list = [strain_matrix_1, strain_matrix_2, strain_matrix_3]

    elif indict['strains_matrix'][0] == 'ulics':
        if indict['dimensional'][0] == '3D':
            #up = 10. ** (-3.)
            up = up0 / 6.
            strain_matrix_1 = up * array([[1.,   6./2.,  5./2.], 
                                             [6./2.,   2.,  4./2.], 
                                             [5./2.,   4./2.,  3.]])
            strain_matrix_2 = up * array([[-2., -5./2.,  6./2.], 
                                             [-5./2.,  1., -3./2.], 
                                             [6./2.,  -3./2.,  4.]])
            strain_matrix_3 = up * array(
                [
                    [3.0, -4.0 / 2.0, 1.0],
                    [-4.0 / 2.0, -5.0, 6.0 / 2.0],
                    [1.0, 6.0 / 2.0, -1.0],
                ]
            )

            strain_matrix_4 = up * array([[-4., -2./2., -3./2.], 
                                             [-2./2.,  -6., 1./2.], 
                                             [-3./2.,  1./2.,  5.]])
            strain_matrix_5 = up * array([[5.,  -3./2., -1./2.], 
                                             [-3./2.,  4., -2./2.], 
                                             [-1./2., -2./2.,  6.]])
            strain_matrix_6 = up * array([[-6.,  1./2., -4./2.], 
                                             [1./2.,   3.,  5./2.], 
                                             [-4./2.,  5./2., -2.]])
            strain_matrix_list = [strain_matrix_1, strain_matrix_2, strain_matrix_3, strain_matrix_4, strain_matrix_5, strain_matrix_6]

        elif indict['dimensional'][0] == '2D':
            up = up0 / 3.
            strain_matrix_1 = up * array([[1.,  3./2.,   0.], 
                                             [3./2.,  2.,   0.], 
                                             [0.,     0.,   0.]])
            strain_matrix_2 = up * array([[2.,  1./2.,   0.], 
                                             [1./2,   3.,   0.], 
                                             [0.,     0.,   0.]])
            strain_matrix_3 = up * array([[3.,     1.,   0.], 
                                             [1.,     1.,   0.], 
                                             [0.,     0.,   0.]])
            strain_matrix_list = [strain_matrix_1, strain_matrix_2, strain_matrix_3]

    return strain_matrix_list
