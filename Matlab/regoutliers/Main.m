clc
close all
clear 

X0=10.2:0.2:30; %first vector
Y0=0.1:0.1:10;  %second vector
idx=randi(length(Y0),4,1);     %randomly distribute 4 noise
Y0(idx)=randn(4,1)*10; %produce 4 random noise 
noutliers=3;    %number of outliers to remove
plotOp=1;       %0: dont plot, 1: plot
[X,Y,rSquares,outliers_idx] = regoutliers(X0,Y0,noutliers,plotOp)
