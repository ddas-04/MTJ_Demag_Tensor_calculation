import numpy as np
import scipy.special as sc

def F(k, v):
	# numerical result is verified with https://keisan.casio.com/exec/system/1244989948
	return (sc.ellipkinc(v, k*k))  
	
def E(k, v):
	# numerical result is verified with https://keisan.casio.com/exec/system/1244989948
	return (sc.ellipeinc(v, k*k))
	
a=float(input('Enter a = ' ))
b = float(input('Enter b = ' ))
c = float(input('Enter c = ' ))

v=np.arccos(c/a)

psi=np.arccos(b/a)

if a==b and b==c:
	Nxx=1/3.0
	Nyy=1/3.0
	Nzz=1/3.0

elif a==b:
	k=(np.sin(psi))/(np.sin(v))
	alpha=np.arcsin(k)
	
	prefac_Nz= (np.cos(psi)*np.cos(v))/(((np.sin(v))**3) * (np.cos(alpha))**2)
	t1 = (np.sin(v)*np.cos(psi))/np.cos(v)
	Nzz = prefac_Nz*(t1-E(k,v))
	
	Nxx=0.5*(1-Nzz)
	Nyy=0.5*(1-Nzz)
	
elif b==c:
	k=(np.sin(psi))/(np.sin(v))
	alpha=np.arcsin(k)
	prefac_Nx=(np.cos(psi)*np.cos(v))/(((np.sin(v))**3)*(np.sin(alpha))**2)
	Nxx=prefac_Nx*(F(k,v)-E(k,v))
	
	Nyy=0.5*(1-Nxx)
	Nzz=0.5*(1-Nxx)
	
else:
	k=(np.sin(psi))/(np.sin(v))
	alpha=np.arcsin(k)
	prefac_Nx=(np.cos(psi)*np.cos(v))/(((np.sin(v))**3)*(np.sin(alpha))**2)
	Nxx=prefac_Nx*(F(k,v)-E(k,v))
	
	prefac_Ny=(np.cos(psi)*np.cos(v))/((np.sin(v))**3*(np.sin(alpha))**2*(np.cos(alpha))**2)
	t3=((np.sin(alpha))**2*np.sin(v)*np.cos(v))/(np.cos(psi))
	Nyy=prefac_Ny*(E(k,v)-((np.cos(alpha))**2)*F(k,v)-t3)
	
	prefac_Nz= (np.cos(psi)*np.cos(v))/(((np.sin(v))**3) * (np.cos(alpha))**2)
	t1 = (np.sin(v)*np.cos(psi))/np.cos(v)
	Nzz = prefac_Nz*(t1-E(k,v))
	
print('Nxx = ' + str(Nxx))
print('Nyy = ' + str(Nyy))
print('Nzz = ' + str(Nzz))

print('Nxx+Nyy+Nzz = ' + str(Nxx+Nyy+Nzz))
	
	
	
	
