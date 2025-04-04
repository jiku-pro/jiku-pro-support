
import os
import numpy as np
import h5py
import matplotlib.pyplot as plt

currdir = os.path.dirname( __file__ )  # directory in which this .py script is saved
fpath   = os.path.join( currdir, 'results.h5' )  # full path to results file

with h5py.File(fpath, 'r') as f:
    group      = f['power1d']
    alpha      = float( np.array( group['alpha'] ) )  # Type I error rate
    dt         = float( np.array( group['dt'] ) )     # total simulation duration
    k          = int( np.array( group['k'] ) )        # cluster extent (default 1);  clusters in the excursion set with smaller extents will be ignored when computing probabilities
    niters     = int( np.array( group['niters'] ) )   # number of simulation iterations (i.e., random data samples)
    p_reject0  = float( np.array( group['p_reject0'] ) )   # omnibus null rejection probability under H0 (alpha by defintion)
    p_reject1  = float( np.array( group['p_reject1'] ) )   # omnibus null rejection probability under H1
    p1d_poi0   = np.array( group['p1d_poi0'] )             # (Q,) domain-level (i.e., point-level) power under H0
    p1d_poi1   = np.array( group['p1d_poi1'] )             # (Q,) domain-level (i.e., point-level) power under H1
    z0         = np.array( group['z0'] )              # (niters,) distribution of zmax under H0
    z1         = np.array( group['z1'] )              # (niters,) distribution of zmax under H1
    zstar      = float( np.array( group['zstar'] ) )  # critical threshold for H0 rejection
    Q          = int( np.array( group['Q'] ) )        # number of domain nodes (usually time nodes)
    Z0         = np.array( group['Z0'] )              # (niters,Q) test statistic continua under H0 (null hypothesis)
    Z1         = np.array( group['Z1'] )              # (niters,Q) test statistic continua under H1 (alternative hypothesis)
    two_tailed = bool( np.array( group['two_tailed'] ) )   # two-tailed inference
    
    
    print( 'alpha:', alpha )
    print( 'dt:', np.around(dt, 3) )
    print( 'k:', np.around(k, 3) )
    print( 'niters:', niters )
    print( 'p_reject0:', np.around(p_reject0, 3) )
    print( 'p_reject1:', np.around(p_reject1, 3) )
    print( 'p1d_poi0:', p1d_poi0.shape )
    print( 'p1d_poi1:', p1d_poi1.shape )
    print( 'p_reject1:', np.around(p_reject1, 3) )
    print( 'two_tailed:', two_tailed )
    print( 'z0:', z0.shape )
    print( 'z1:', z1.shape )
    print( 'zstar:', np.around(zstar, 3) )
    print( 'Q:',  Q )
    print( 'Z0:', Z0.shape )
    print( 'Z1:', Z1.shape )
    
    

# plot results
plt.close('all')
fig,axs = plt.subplots( 1, 2, figsize=(9,4), tight_layout=True )

# main power results
ax = axs[0]
plt.setp(ax.get_xticklabels() + ax.get_yticklabels(), size=6)
# q = power1d._plot._get_q(results.Q, None)
q  = np.linspace(0, 1, Q)
ax.plot(q, p1d_poi0, color='k', ls='-', lw=1)
ax.plot(q, p1d_poi1, color='b', ls=':', lw=3, label='Power')
ax.axhline(0.8, ls='--', color='r', label='Conventional target power')
ax.legend(fontsize=8)
ax.set_ylim(-0.03, 1.03)
ax.set_title('Main results')

# distributions:
ax = axs[1]
plt.setp(ax.get_xticklabels() + ax.get_yticklabels(), size=6)
ax.hist(z0, alpha=0.5, bins=21, density=True, color='0.3', edgecolor='0.6', label=r'$z_{\max}$ ($H_0$)')
ax.axvline(zstar, color='0.3', linestyle='--', label=r'Critical z (1 - $\alpha$)')
ax.hist(z1, alpha=0.5, bins=21, density=True, color=(0.1, 0.3, 1), ec=(0.3, 0.5, 1), label=r'$z_{\max}$ ($H_1$)')
ax.set_xlabel(r'$z_{\max}$')
ax.set_ylabel('Density')
ax.legend(fontsize=8)
ax.set_title('Distributions')

# plt.savefig( os.path.join(currdir, 'results.png') )

plt.show()

