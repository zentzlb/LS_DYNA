import lasso.dyna
from lasso.dyna import D3plot, ArrayType, Binout
import os

def get_ab(directory: str = r"C:\Users\Logan.Zentz\OneDrive - University of Virginia\Documents\Sled Test\sims\airbag\videos\drop_vent_d3.0_start1000_term2000_height6.0_blow_v14000_blow_s300_ea1_sim"):
    """
    open key file and convert to string
    :param directory: (string)
    :return: text (string)
    """

    path = os.path.join(directory, 'binout0000')
    binout = Binout(path)

    ab = binout.read('abstat', 'pressure')
    print('worked')
    return ab[:, 3]

