import matplotlib.pyplot as plt # J'importe la librairie pour tracer des courbes, en la nommant plt pour plus de simplicité.

x = [1.05,2,4,10.8] # Distance, in cm
λ = [410.2,434.0,486.1,656.3] # Wavelength, in nm

plt.ylabel('Distance, in cm')
plt.xlabel('Evolution of Wavelength, in nm')
plt.title('Evolution of the wavelength (λ), according to the distance in spectrum (x)')
plt.plot(λ, x, c=[101/255.0, 191/255.0, 247/255.0], linestyle='-', marker='o')
plt.show()