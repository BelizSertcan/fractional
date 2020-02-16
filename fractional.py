import numpy as np

# importing xyz file
filename = 'deydoa.txt'
coord = np.genfromtxt(filename, delimiter = '   ', skip_header = 2, dtype = [('atoms','U5'),('x',float),('y',float),('z',float)])

atoms = coord['atoms']

# moving the system to 1st octant
new_x = coord['x']+np.abs(min(coord['x']))
new_y = coord['y']+np.abs(min(coord['y']))
new_z = coord['z']+np.abs(min(coord['z']))

# finding the dimensions of the new molecular system
dim_x = max(new_x)
dim_y = max(new_y)
dim_z = max(new_z)

# calculating fractional coordinates and printing
frac = np.zeros((624,3))
f = open('deydoa_frac', 'w+')
f.write('%i\n\n' %len(coord['x']))
for i in range(len(atoms)):
    frac[i,0] = new_x[i]/dim_x
    frac[i,1] = new_y[i]/dim_y
    frac[i,2] = new_z[i]/dim_z
    f.write('%s %.6f %.6f %.6f\n' % (atoms[i], frac[i,0], frac[i,1], frac[i,2]))
