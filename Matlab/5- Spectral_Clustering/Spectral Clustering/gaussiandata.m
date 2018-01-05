%using generatedata to generate gaussian data

close all;
clear all;
clc;

nbclasses = 3;
nbsamples = 2000;
dim = 2;

details = cell(nbclasses, 3);
details{1, 1} = [4 8]; %mean for class 1
details{2, 1} = [1 1]; %mean for class 2
details{3, 1} = [9 2]; %mean for class 3
details{1, 2} = [1.6 2.3]; %std for class 1
details{2, 2} = [2.5 1.9]; %std for class 2
details{3, 2} = [1.5 1.9]; %std for class 3

[data, class] = generatedata(nbsamples, nbclasses, dim, 'gaussian', details, true);