%% Fit Polynomial to Trigonometric Function
% 
%%
% Generate 10 points equally spaced along a sine curve in the interval
% |[0,4*pi]|.

% Copyright 2015 The MathWorks, Inc.

x = linspace(0,4*pi,10);
y = sin(x);
%%
% Use |polyfit| to fit a 7th-degree polynomial to the points.
p = polyfit(x,y,7);
%%
% Evaluate the polynomial on a finer grid and plot the results.
x1 = linspace(0,4*pi);
y1 = polyval(p,x1);
figure
plot(x,y,'o')
hold on
plot(x1,y1)
hold off