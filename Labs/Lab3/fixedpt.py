# import libraries
import numpy as np
    
def driver():

# test functions 
     f1 = lambda x: (10/(x+4))**(1/2)
     alpha1 = 1.3652300134140976

     Nmax = 100
     tol = 10e-10

# test f1 '''
     x0 = 1.5
     [xstar, ier, vec] = fixedpt_iter(f1,x0,tol,Nmax)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('The vector is:', vec)
     print('Error message reads:',ier)
     alph = ooc(vec, alpha1)
     print('OOC:', alpha)


# define routines
def fixedpt_iter(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    v = []
    
    while (count <Nmax):
       count = count +1
       x1 = f(x0)
       v.append(x1)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          vec_full = np.array(v)
          return [xstar, ier, vec_full]
       vec_full = np.array(v)
       x0 = x1
    xstar = x1
    ier = 1
    return [xstar, ier, vec_full]
    
def ooc(vec, p):
	pk = vec_full[-2]
	ek = np.abs(pk - p)
	pkplus = vec_full[-1]
	ekplus = np.abs(pkplus-p)
	pkminus = vec_full[-3]
	ekminus = np.abs(pkminus-p)
	alpha = ((np.ln(pkplus/pk))/(np.lp(pk/pkminus)))
	
	return [alpha]
    

driver()

