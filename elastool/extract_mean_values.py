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
from pandas import DataFrame
from numpy import nan


def get_stress(outcar_file, tag):
    num_record = 0
    dirs = ['XX', 'YY', 'ZZ', 'YZ', 'ZX', 'XY']
    df = DataFrame([], columns=dirs)

    for line in open(outcar_file, 'r'):
        if tag in line:
            l = line.split()
            if tag == 'Total+kin.':
                stresses = [float(l[1]),float(l[2]),float(l[3]),float(l[5]),float(l[6]),float(l[4])]
            elif tag == 'in kB':
                stresses = [float(l[2]),float(l[3]),float(l[4]),float(l[6]),float(l[7]),float(l[5])]
            df_new = DataFrame([stresses], columns=dirs)
            df = df_new if num_record == 0 else df.append(df_new, ignore_index=True)
            num_record += 1
    return df


def mean_stress(outcar_file, num_last_samples, tag):
    df = get_stress(outcar_file, tag)
    stress_data = df.tail(num_last_samples)
    # in order: XX, YY, ZZ, XY, YZ, ZX
    #for direction in stress_data.columns:
    dirs = ['XX', 'YY', 'ZZ', 'YZ', 'ZX', 'XY']
    return [stress_data[direction].mean() for direction in dirs]


def get_pressure(outcar_file):
    num_record = 0
    dirs = ['pressure']
    df = DataFrame([], columns=dirs)
    for line in open(outcar_file, 'r'):
        if 'pressure =' in line:
            l = line.split()
            pressure = [float(l[3]) + float(l[8])]
            df_new = DataFrame([pressure], columns=dirs)
            df = df_new if num_record == 0 else df.append(df_new, ignore_index=True)
            num_record += 1
    return df


def mean_pressure(outcar_file, num_last_samples):
    df = get_pressure(outcar_file)
    pressure_data = df.tail(num_last_samples)
    # in order: XX, YY, ZZ, XY, YZ, ZX
    #for direction in stress_data.columns:
    dirs = ['pressure']
    pressure_list = [pressure_data[direction].mean() for direction in dirs]
    return pressure_list[0]


def get_temperature(outcar_file):
    num_record = 0
    dirs = ['temperature']
    df = DataFrame([], columns=dirs)

    for line in open(outcar_file, 'r'):
        if 'mean temperature' in line:
            l = line.split()
            temperature = [float(l[4])]
            df_new = DataFrame([temperature], columns=dirs)
            df = df_new if num_record == 0 else df.append(df_new, ignore_index=True)
            num_record += 1
    return df


def mean_temperature(outcar_file, num_last_samples):
    df = get_temperature(outcar_file)
    temperature_data = df.tail(num_last_samples)
    # in order: XX, YY, ZZ, XY, YZ, ZX
    #for direction in stress_data.columns:
    dirs = ['temperature']
    temperature_list = [temperature_data[direction].mean() for direction in dirs]
    return temperature_list[0]


def get_volume(vasprun_file):
    num_record = 0
    dirs = ['volume']
    df = DataFrame([], columns=dirs)
    for line in open(vasprun_file, 'r'):
        if 'volume' in line:
            l = line.split()
            volume = [float(l[2])]
            df_new = DataFrame([volume], columns=dirs)
            df = df_new if num_record == 0 else df.append(df_new, ignore_index=True)
            num_record += 1
    return df


def mean_volume(vasprun_file, num_last_samples):
    df = get_volume(vasprun_file)
    volume_data = df.tail(num_last_samples)
    dirs = ['volume']
    volume_list = [volume_data[direction].mean() for direction in dirs]
    return volume_list[0]

    
if __name__ == '__main__':
    #get_stress()
    outcar_file = 'OUTCAR'
    num_last_samples = 1
    tag = 'in kB'
    p = get_pressure(outcar_file)
    print(len(p))
    stress = mean_stress(outcar_file, num_last_samples, tag)
    print(stress)
    pressure = mean_pressure(outcar_file, num_last_samples)
    print(pressure)
    print(pressure is nan)
    temperature = mean_temperature(outcar_file, num_last_samples)
    print(temperature)
    vasprun_file = 'vasprun.xml'
    num_last_samples = 1000
    v = mean_volume(vasprun_file, num_last_samples)
    print(v)
