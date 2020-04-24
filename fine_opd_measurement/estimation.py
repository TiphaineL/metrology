import numpy as np

wavelengths = np.array([.83025, .7953, .830, .795])
lambda_1 = .795
lambda_2 = .830

true_opd = 2

phase_error = .02

def synthetic_wavelength(wavelength_1,wavelength_2):
    return wavelength_1*wavelength_2 / (wavelength_1 - wavelength_2)

def wave_number(wavelength):
    return 2*np.pi / wavelength

def phase_from_opd(opd,wave_number):
    return wave_number * opd

def phase_from_opd_modulo(opd,wave_number):
    return modulo_minus_plus_pi(phase_from_opd(opd,wave_number))

def modulo_2pi(angle):
    return angle % (2*np.pi)

def modulo_minus_plus_pi(angle):
    angle = modulo_2pi(angle)
    return np.where(angle > np.pi, angle-2*np.pi, angle)

def estimated_opd(phase_1,phase_2,wavenumber_1,wavenumber_2):
    return modulo_minus_plus_pi(phase_1 - phase_2) / (wavenumber_1 - wavenumber_2)

def estimated_opd_3(phases_measured, wavenumbers):
    t = 0
    sum_of_phases = 0
    sum_of_wavenumbers = 0
    for i in range(int(len(phases_measured) / 2)):
        t += 2 * i
        sum_of_phases += phases_measured[t] - phases_measured[t+1]
        sum_of_wavenumbers += wavenumbers[t] - wavenumbers[t+1]
    return modulo_minus_plus_pi(sum_of_phases) / sum_of_wavenumbers

def better_opd_estimate(n,wavelength,phase):
    return (phase/wave_number(wavelength)) + n*wavelength

def unambiguous_range(wavenumber_1,wavenumber_2):
    return np.pi / (wavenumber_1 - wavenumber_2)

def estimated_n(measured_opd,measured_phase,wavelength):
    return np.round( (measured_opd - (measured_phase/wave_number(wavelength)) )/wavelength )

def add_random_noise_to_data(data,mean,std):
    return data + np.random.normal(mean,std,data.shape)

def opd_error(true_opd, estimated_opd):
    return abs(true_opd - estimated_opd)

wave_numbers = wave_number(wavelengths)
print('wave numbers',wave_numbers)
true_phases = phase_from_opd_modulo(true_opd,wave_numbers)
measured_phases = add_random_noise_to_data(true_phases,0,phase_error)
print('measured phases',measured_phases)
opd_3 = estimated_opd_3(measured_phases,wave_numbers)
estimated_ns = estimated_n(opd_3,measured_phases,wavelengths)
better_opds = better_opd_estimate(estimated_ns,wavelengths,measured_phases)

print('opd 3',opd_3)
print("estimated n's ",estimated_ns)
print('Better opd estimates ',better_opds)
print('opd 3 error',opd_error(true_opd,opd_3))
print('opd better error',opd_error(true_opd,better_opds))
print('Unambiguous range ',np.pi/(wave_numbers[0]-wave_numbers[1]-wave_numbers[3]+wave_numbers[2]))
print()

k_1 = wave_number(lambda_1)
k_2 = wave_number(lambda_2)

true_phi_1 = phase_from_opd_modulo(true_opd,k_1)
true_phi_2 = phase_from_opd_modulo(true_opd,k_2)

measured_phi_1 = float(true_phi_1 + np.random.normal(0,phase_error,1))
measured_phi_2 = float(true_phi_2 + np.random.normal(0,phase_error,1))

hat_opd = estimated_opd(measured_phi_1,measured_phi_2,k_1,k_2)

estimated_n1 = estimated_n(hat_opd,measured_phi_1,lambda_1)
estimated_n2 = estimated_n(hat_opd,measured_phi_2,lambda_2)

better_opd_1 = better_opd_estimate(estimated_n1,lambda_1,measured_phi_1)
better_opd_2 = better_opd_estimate(estimated_n2,lambda_2,measured_phi_2)

unambiguous_range = unambiguous_range(k_1,k_2)

synthetic_wavelength = synthetic_wavelength(lambda_1,lambda_2)

print('k1 ',k_1)
print('k2 ',k_2)
print('True opd ',true_opd)
print('True phi_1',true_phi_1,', measured phi_1 ',measured_phi_1)
print('True phi_2',true_phi_2,', measured phi_2 ',measured_phi_2)
print('Estimated opd ',hat_opd)
print('Estimated n1 ',estimated_n1)
print('Estimated n2 ',estimated_n2)
print('Better opd estimate 1 ',better_opd_1)
print('Better opd estimate 2 ',better_opd_2)
print('Opd error before ',opd_error(true_opd,hat_opd))
print('Opd error after 1 ', opd_error(true_opd,better_opd_1))
print('Opd error after 2 ', opd_error(true_opd,better_opd_2))
print('Unambiguous range ',unambiguous_range,'microns')
print('Synthetic wavelength ',synthetic_wavelength)