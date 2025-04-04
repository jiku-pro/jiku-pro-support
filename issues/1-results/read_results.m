

clear;  clc

% read all results

fpath      = 'results.h5';

alpha      = hdf5read(fpath, '/power1d/alpha');
dt         = hdf5read(fpath, '/power1d/dt');
k          = hdf5read(fpath, '/power1d/k');
niters     = hdf5read(fpath, '/power1d/k');
p_reject0  = hdf5read(fpath, '/power1d/p_reject0');
p_reject1  = hdf5read(fpath, '/power1d/p_reject1');
p1d_poi0   = hdf5read(fpath, '/power1d/p1d_poi0');
p1d_poi1   = hdf5read(fpath, '/power1d/p1d_poi1');
two_tailed = hdf5read(fpath, '/power1d/two_tailed');
z0         = hdf5read(fpath, '/power1d/z0');
z1         = hdf5read(fpath, '/power1d/z1');
zstar      = hdf5read(fpath, '/power1d/zstar');
Q          = hdf5read(fpath, '/power1d/Q');
Z0         = hdf5read(fpath, '/power1d/Z0')';
Z1         = hdf5read(fpath, '/power1d/Z1')';



% plot results

close all
figure('Position', [10 10 900 400])
subplot(121)
q = linspace(0, 1, Q);
plot(q, p1d_poi0, 'k-', 'LineWidth',1);
hold on
plot(q, p1d_poi1, 'b:', 'LineWidth',3);
plot([0 1],[1 1]*0.8, 'r--' )
ylim([-0.03, 1.03] )
title('Main results')

subplot(122)
histogram(z0, 21, 'Normalization', 'pdf', 'FaceColor',[1 1 1]*0.7, 'FaceAlpha', 0.5);
hold on
plot([1 1]*zstar, ylim, 'k--', 'LineWidth', 3)
histogram(z1, 21, 'Normalization', 'pdf', 'FaceColor','b', 'FaceAlpha', 0.5);
xlabel('zmax')
ylabel('Density')
legend('zmax (H0)', 'Critical z (1-alpha)', 'zmax (H1)')
title('Distributions')