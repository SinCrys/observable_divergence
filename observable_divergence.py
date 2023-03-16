import os
import numpy as np
import matplotlib.pyplot as plt

# in mm
sdd_min = 50
sdd_max = 150
sdd_res = 1
pix_size = 0.075
crl_dist = 2400 # 3000
crl_acceptance = 0.125

sdd_range = np.arange(sdd_min, sdd_max+sdd_res, sdd_res)
res_range = np.tan(pix_size/sdd_range)
res_min = np.min(res_range)

crl_div = crl_acceptance/(2*(crl_dist+sdd_range))
crl_max = np.min(crl_div)

fig, ax = plt.subplots(figsize=(18/2.54, 14/2.54))
ax.plot(sdd_range, res_range, c='k', label='Eiger2 [75µm]', lw=2, zorder=2)
ax.axhline(res_min, ls='--', lw=2, c='r', label=f'Obs. limit: {res_min*1e6:.2f} µrad, {np.rad2deg(res_min)*1e3:.2f} mdeg', zorder=1)
ax.plot(sdd_range, crl_div, c='k', ls='-.', label=f'CRL [{crl_dist/1e3:.1f} m]: {crl_max*1e6:.2f} µrad, {np.rad2deg(crl_max)*1e3:.2f} mdeg', lw=2, zorder=2)
ax.set_title('Experimentally resolvable beam divergence')
ax.set_xlabel('Sample to detector distance [mm]')
ax.set_ylabel('Observable divergence [rad]')
ax.set_xlim(sdd_min, sdd_max)
ax.ticklabel_format(scilimits=(-3,3))
plt.minorticks_on()
plt.grid(visible=True, which='major', color='gray', linestyle='-')
plt.grid(visible=True, which='minor', color='gray', linestyle='-', alpha=0.2)
plt.legend()
fig.savefig(os.path.join(os.path.split(__file__)[0], 'obserable_divergence.png'), dpi=600)
plt.show()
