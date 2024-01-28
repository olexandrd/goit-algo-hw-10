# LinProg & Monte Carlo method

## LinProg

Added linear programming algorithm for calculating linprod task. 

Requirements: `pulp` lib

Run: 
```
python3 01/linprog.py
```

## Monte Carlo method

Used Monte Carlo method for integral calculation and compare with results provided by SpiPy.

Requirements: `scipy` lib

Run:
```
python3 02/monte_carlo.py
```

### Results

Program output: 
```
Approximate integral: 2.6804091490240545, 
 error estimate: 1.87244451657424e-16, 
 Samples: 100000 

Approximate integral: 2.666749518881174, 
 error estimate: 5.921189464667501e-18, 
 Samples: 100000000 

SciPy result: 2.6666666666666665, SciPy error: 2.9605947323337504e-14 

Methods results difference for 100000 samples: 
 0.005153430884020482 or 0.52%
Methods results difference for 100000000 samples: 
 3.10695804402461e-05 or 0.0031%
```

For Monte Carlo method were performed 2 runs with 100000 and 100000000 samples. 
The difference between SciPy and Monte Carlo methods becomes less pronounced with a larger number of simulations, as expected.
