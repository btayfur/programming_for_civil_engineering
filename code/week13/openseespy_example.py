import openseespy.opensees as ops
import opsvis as opsv

import matplotlib.pyplot as plt

ops.wipe()
ops.model('basic', '-ndm', 2, '-ndf', 3)

colL, girL = 4., 6.

Acol, Agir = 2.e-3, 6.e-3
IzCol, IzGir = 1.6e-5, 5.4e-5

E = 200.e9

Ep = {1: [E, Acol, IzCol],
      2: [E, Acol, IzCol],
      3: [E, Agir, IzGir]}

# Nodes
# Ground floor nodes (y=0)
ops.node(1, 0., 0.)           # Left bottom corner
ops.node(2, girL, 0.)         # Middle bottom
ops.node(3, 2*girL, 0.)       # Middle bottom 2
ops.node(4, 3*girL, 0.)       # Right bottom corner

# 1. floor nodes (y=colL)
ops.node(5, 0., colL)         # Left 1. floor
ops.node(6, girL, colL)       # Middle 1. floor
ops.node(7, 2*girL, colL)     # Middle 1. floor 2
ops.node(8, 3*girL, colL)     # Right 1. floor

# 2. floor nodes (y=2*colL)
ops.node(9, 0., 2*colL)       # Left 2. floor
ops.node(10, girL, 2*colL)    # Middle 2. floor
ops.node(11, 2*girL, 2*colL)  # Middle 2. floor 2
ops.node(12, 3*girL, 2*colL)  # Right 2. floor

# Ground floor nodes fixed
ops.fix(1, 1, 1, 1)
ops.fix(2, 1, 1, 0)
ops.fix(3, 1, 1, 0)
ops.fix(4, 1, 1, 0)

opsv.plot_model()
plt.title('plot_model before defining elements')
plt.savefig('model_before_elements.png', dpi=300, bbox_inches='tight')
plt.clf()

ops.geomTransf('Linear', 1)

# Columns - Ground floor to 1. floor
ops.element('elasticBeamColumn', 1, 1, 5, Acol, E, IzCol, 1)   # Left column
ops.element('elasticBeamColumn', 2, 2, 6, Acol, E, IzCol, 1)   # Middle column 1
ops.element('elasticBeamColumn', 3, 3, 7, Acol, E, IzCol, 1)   # Middle column 2
ops.element('elasticBeamColumn', 4, 4, 8, Acol, E, IzCol, 1)   # Right column

# Columns - 1. floor to 2. floor
ops.element('elasticBeamColumn', 5, 5, 9, Acol, E, IzCol, 1)   # Left column
ops.element('elasticBeamColumn', 6, 6, 10, Acol, E, IzCol, 1)  # Middle column 1
ops.element('elasticBeamColumn', 7, 7, 11, Acol, E, IzCol, 1)  # Middle column 2
ops.element('elasticBeamColumn', 8, 8, 12, Acol, E, IzCol, 1)  # Right column

# Beams - 1. floor
ops.element('elasticBeamColumn', 9, 5, 6, Agir, E, IzGir, 1)   # 1. bay
ops.element('elasticBeamColumn', 10, 6, 7, Agir, E, IzGir, 1)  # 2. bay
ops.element('elasticBeamColumn', 11, 7, 8, Agir, E, IzGir, 1)  # 3. bay

# Beams - 2. floor
ops.element('elasticBeamColumn', 12, 9, 10, Agir, E, IzGir, 1)  # 1. bay
ops.element('elasticBeamColumn', 13, 10, 11, Agir, E, IzGir, 1) # 2. bay
ops.element('elasticBeamColumn', 14, 11, 12, Agir, E, IzGir, 1) # 3. bay

Px = 2.e+3
Wy = -10.e+3
Wx = 0.

# Apply distributed loads to all beams
Ew = {9: ['-beamUniform', Wy, Wx],   # 1. floor 1. bay
      10: ['-beamUniform', Wy, Wx],  # 1. floor 2. bay
      11: ['-beamUniform', Wy, Wx],  # 1. floor 3. bay
      12: ['-beamUniform', Wy, Wx],  # 2. floor 1. bay
      13: ['-beamUniform', Wy, Wx],  # 2. floor 2. bay
      14: ['-beamUniform', Wy, Wx]}  # 2. floor 3. bay

ops.timeSeries('Constant', 1)
ops.pattern('Plain', 1, 1)

# Apply point loads to each floor
ops.load(5, Px, 0., 0.)   # Left 1. floor
ops.load(6, Px, 0., 0.)   # Middle 1. floor
ops.load(7, Px, 0., 0.)   # Middle 1. floor 2
ops.load(8, Px, 0., 0.)   # Right 1. floor

ops.load(9, Px, 0., 0.)   # Left 2. floor
ops.load(10, Px, 0., 0.)  # Middle 2. floor
ops.load(11, Px, 0., 0.)  # Middle 2. floor 2
ops.load(12, Px, 0., 0.)  # Right 2. floor

for etag in Ew:
    ops.eleLoad('-ele', etag, '-type', Ew[etag][0], Ew[etag][1],
                Ew[etag][2])

ops.constraints('Transformation')
ops.numberer('RCM')
ops.system('BandGeneral')
ops.test('NormDispIncr', 1.0e-6, 6, 2)
ops.algorithm('Linear')
ops.integrator('LoadControl', 1)
ops.analysis('Static')
ops.analyze(1)

ops.printModel()

opsv.plot_model()
plt.title('plot_model after defining elements')
plt.savefig('model_after_elements.png', dpi=300, bbox_inches='tight')
plt.clf()

opsv.plot_load()
plt.savefig('load_diagram.png', dpi=300, bbox_inches='tight')
plt.clf()

opsv.plot_reactions()
plt.savefig('reactions.png', dpi=300, bbox_inches='tight')
plt.clf()

# sfac = 80.

opsv.plot_defo()
plt.savefig('deformation.png', dpi=300, bbox_inches='tight')
plt.clf()
# opsv.plot_defo(sfac)
# fmt_interp = {'color': 'blue', 'linestyle': 'solid', 'linewidth': 1.2, 'marker': '.', 'markersize': 6}
# opsv.plot_defo(sfac, fmt_interp=fmt_interp)

# 4. plot N, V, M forces diagrams

sfacN, sfacV, sfacM = 3.e-5, 3.e-5, 3.e-5

opsv.section_force_diagram_2d('N', sfacN)
plt.title('Axial force distribution')
plt.savefig('axial_force.png', dpi=300, bbox_inches='tight')
plt.clf()

opsv.section_force_diagram_2d('T', sfacV)
plt.title('Shear force distribution')
plt.savefig('shear_force.png', dpi=300, bbox_inches='tight')
plt.clf()

opsv.section_force_diagram_2d('M', sfacM)
plt.title('Bending moment distribution')
plt.savefig('bending_moment.png', dpi=300, bbox_inches='tight')
plt.clf()

print("All figures are saved as PNG:")
print("- model_before_elements.png")
print("- model_after_elements.png") 
print("- load_diagram.png")
print("- reactions.png")
print("- deformation.png")
print("- axial_force.png")
print("- shear_force.png")
print("- bending_moment.png")

exit()