# all lengths in microns

from math import asin, tan, pi, atan
import matplotlib.pyplot as plt

numerical_aperture = 0.1
refractive_index = 1.5
mode_field_diameter = 6

output_unit_spacing = 2.5 * mode_field_diameter

output_spacing_1 = 4 * output_unit_spacing
output_spacing_2 = 1 * output_unit_spacing
output_spacing_3 = 2 * output_unit_spacing

slab_length = 2000

def acceptance_angle(numerical_aperture):
    return asin(numerical_aperture)

class waveguide_output:
    def __init__(self,coordinates):
        self.coordinates = coordinates

    def calculate_angle(self):
        return atan(-self.coordinates[0]/slab_length)

    def calculate_footprint(self,slab_length,numerical_aperture):

        return slab_length * (tan(self.calculate_angle() + acceptance_angle(numerical_aperture)) \
                              + tan(self.calculate_angle() - acceptance_angle(numerical_aperture)))

    def draw_propagation_angle(self,slab_length,numerical_aperture):

        plt.plot(self.coordinates[0], self.coordinates[1],'xr')

        plt.plot(self.coordinates[0] + slab_length * tan(self.calculate_angle()),slab_length,'xr')

        plt.plot([self.coordinates[0], self.coordinates[0]+ slab_length * tan(self.calculate_angle())],\
                 [self.coordinates[1], slab_length],'--b')

        plt.plot([self.coordinates[0], self.coordinates[0] + slab_length * tan(self.calculate_angle() \
                                                                               + acceptance_angle(numerical_aperture))], \
                 [self.coordinates[1], slab_length], '-b')

        plt.plot([self.coordinates[0], self.coordinates[0] + slab_length * tan(self.calculate_angle() \
                                                                               - acceptance_angle(numerical_aperture))], \
                 [self.coordinates[1], slab_length], '-b')

waveguide1 = waveguide_output([0, 0])
print((180/pi)*waveguide1.calculate_angle())
waveguide1.draw_propagation_angle(slab_length, numerical_aperture)

waveguide2 = waveguide_output([-output_spacing_1, 0])
print((180/pi)*waveguide2.calculate_angle())
waveguide2.draw_propagation_angle(slab_length, numerical_aperture)

waveguide3 = waveguide_output([output_spacing_2, 0])
print((180/pi)*waveguide3.calculate_angle())
waveguide3.draw_propagation_angle(slab_length, numerical_aperture)

waveguide4 = waveguide_output([output_spacing_2 + output_spacing_3, 0])
print((180/pi)*waveguide4.calculate_angle())
waveguide4.draw_propagation_angle(slab_length, numerical_aperture)





