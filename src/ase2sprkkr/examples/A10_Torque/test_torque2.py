from ase2sprkkr.sprkkr.calculator import SPRKKR
from ase2sprkkr.potentials.potentials import Potential

calculator = SPRKKR()
calculator.input_parameters = 'torque'
# This will create the correct InputParameters object for the 'torque' task.
# Now you can set sub-attributes:
calculator.input_parameters.CONTROL.DATASET = 'Fe'
calculator.input_parameters.MODE.MALF = 0.0
calculator.input_parameters.MODE.MBET = 45.0
calculator.input_parameters.MODE.MGAM = 0.0
potential = Potential()
potential.read_from_file('Fe.pot_new')
calculator.potential = potential
calculator.calculate()

