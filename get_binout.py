import lasso.dyna
from lasso.dyna import D3plot, ArrayType, Binout
import os


def get_ab(directory: str):
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

