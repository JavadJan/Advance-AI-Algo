from load_image import ft_load
from pimp_image import ft_invert, ft_blue, ft_green, ft_grey, ft_red
import matplotlib.pyplot as plt

array = ft_load("animal.jpeg")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
plt.tight_layout()
plt.show()
print(ft_invert.__doc__)