%using generatedata to generate circle data

close all;
clear all;
clc;

nbclasses = 2;
nbsamples = 2000;
dim = 2;

details = cell(nbclasses, 5);
details{1, 1} = [250 150]; %center for class 1
details{1, 2} = 250; %radius for class 1
details{1, 3} = [10 10]; %std for class 1
details{1, 4} = 'lhalf';
details{1, 5} = 100;

details{2, 1} = [0 0]; %center for class 2
details{2, 2} = 250; %radius for class 2
details{2, 3} = [10 10]; %std for class 2
details{2, 4} = 'uhalf';
details{2, 5} = 100;

%details{3, 1} = [0 0]; %mean for class 3
%details{3, 2} = 150; %radius for class 3
%details{3, 3} = [5 5]; %std for class 3


[data, class] = generatedata(nbsamples, nbclasses, dim, 'circles', details, true);