
function [X,Y,rSquares,outliers_idx] = regoutliers(X0,Y0,noutliers,plotOp)

% Summary: Removes outliers from both variables of bivariate linear 
% regression based on regression residuals.
% 
% Function Description:
% This function accepts two (vector of) variables for which a bivariate
% linear regression analysis is meant to be performed, and removes the
% outliers from both variables. Since the regression residual vector is
% used to detect the outliers, only those records which stand farthest from
% the 1:1 regression line will be detected and removed. If more than one
% outliers is asked to be removed, before removing the next outlier,
% regression residuals will be recalculated to avoid swamping and masking
% effects, then the next farthest point from 1:1 line will be removed and
% so forth. This method differentiates those points that might be outlier
% in a single variable (X or Y) but can fit well in a 1:1 regression
% line-fit from those points that stay in the acceptable range in each of
% the individual input variables (X,Y) but can appear in the outliers when
% the two variables are fitted in the regression line. To detect the
% outlier from the residual's vector, a subfunction is used (this
% subfunction is an enhancement from a work by Vince Petaccio, 2009, and is
% available also as a stand-alone function, "outliers", from Matlab File
% exchange).
%
% --Inputs:
%   X0: vector of dependent variable in bivariate linear regression
%   Y0: vector of independent variable in bivariate linear regression 
%   noutliers: how many outliers should be removed? (1 will be used as
%   default if not provided)
%   plotOp: plotting option, whether to produce a scatterplot of the two
%   input variables before and after each iteration of outliers removal (up
%   to noutliers) or only do calculations (0: don't plot, 1: plot), if 1 is
%   given, plots will be generated in a subplot 
%
% --Outputs:
%   X: vector of dependent variable after removal of the outliers
%   Y: vector of independent variable after removal of the outliers
%   rSquares: a vector of r-square values calculated from the original
%   inputs and after removal of each outlier
%   outliers_idx: indexes of outliers, note that records for these indexes
%   are turned to NaN in X and Y outputs
%
% --Dependency:
%   outliers subfunction, which is included in this code following main 
%   function
%
% --Example:
% X0=10.2:0.2:30; %first vector
% Y0=0.1:0.1:10;  %second vector
% idx=randi(length(Y0),4,1);     %randomly distribute 4 noise
% Y0(idx)=randn(4,1)*10; %produce 4 random noise 
% noutliers=3;    %number of outliers to remove
% plotOp=1;       %0: dont plot, 1: plot
% [X,Y,rSquares,outliers_idx] = regoutliers(X0,Y0,noutliers,plotOp);
% rSquares %print rsquare values calculated from original data and each
% step after removal of outliers, this should show progressively increasing
% values, otherwise number of outliers to be removed should be decreased
% or in some cases increased.
% outliers_idx %print indexes of outlier records in both input vectors
%
% First version: 14 June 2012
% email: sohrabinia.m@gmail.com
%--------------------------------------------------------------------------

% Initialize outputs to 0:
X=0;
Y=0;
outliers_idx=0;

% check the inputs and do the required action:
if nargin <2
    disp(['Error! at least two input X and Y arguments must be provided, '...
        'type help regoutliers for help']);
    return
elseif nargin<3
   noutliers=1;
elseif nargin<4
   plotOp=0;
end

% Initializations:
outliers_idx = NaN(noutliers,1);  
rSquares     = NaN(noutliers+1,1); 

% if plots requested, construct subplot dims and plot original data:
if plotOp==1
    d1=floor(sqrt(noutliers)+1);
    d2=ceil(sqrt(noutliers));
    subplot(d1,d2,1);
    scatter(X0,Y0);
end

% Calculate r-square of original data before outliers removal:   
regStat=regstats(X0,Y0,'linear','rsquare'); 
rSquares(1)=regStat.rsquare;

for i=1:noutliers    
    regStat=regstats(X0,Y0,'linear','r'); %calculate reg. residuals
    [resid,idx]=outliers(regStat.r,1); %remove reg. residual outlier
    if isempty(idx)==0
        outliers_idx(i)=idx; %store outlier index       
    end
    X0(idx)=NaN; %turn outlier to NaN in dependent variable
    Y0(idx)=NaN; %turn outlier to NaN in independent variable
    regStat=regstats(X0,Y0,'linear','rsquare'); %rsq after outlier removal  
    rSquares(i+1)=regStat.rsquare; %store rsq (after outlier removal)
    
    % if requested, scatterplot X vs. Y after removal of outlier: 
    if plotOp==1
        subplot(d1,d2,i+1);
        scatter(X0,Y0);
    end
end
outliers_idx(isnan(outliers_idx))=[];
X=X0; %return dependent var vector with outliers turned to NaN
Y=Y0; %return independent var vector with outliers turned to NaN
end

%% outliers function: remove outliers based on Thompson Tau:
function [X, outliers_idx] = outliers(X0, num_outliers)

% --Summary: outliers are detected using Thompson Tau method and turned to 
% NaN in the output.
%
% --Function Decription: 
% This function accepts a vector and detects the outlier values in the
% vector using Thopson Tau method, which is based on the absolute deviation 
% of each record from the mean of the entire vector, and fills the outliers
% with NaNs in the returned output. The magnitude of Thompson's Tau value 
% corresponding to the number of records in the input vector to the 
% Standard Deviation of the input vector is the rule to decide if any 
% record in in the outlier. The mean, standard deviation (std) and the 
% magnitude of Thompson's Tau (tau*std) are calculated again after removal 
% of each outlier.  
%
% --Inputs:
%   X0: input vector which contains outleirs
%   num_outliers: number of the outliers that should be removed from the
%   input vector
%   
% --Outputs:
%   X: output vector with outliers (if any detected) turned to NaN 
%   outliers_idx: the index(es) of any detected outliers, the more extreme 
%   outliers will be detected first, so the first index refers to the 
%   most extreme outlier and so forth
%
% --Theory of Thompson Tau method: 
%   http://www.mne.psu.edu/me345/Lectures/Outliers.pdf
%   http://www.jstor.org/stable/2345543 (Thompson, 1985)
%
% --Note: this function is an improvement based on Vince Petaccio, 2009:
% http://www.mathworks.com/matlabcentral/fileexchange/24885-remove-outliers
% --Improvements: 
%  1. Handleing NaNs in inputs
%  2. Number of outliers to be removed is restricted to a user defined
%  maximum to avoid uncontrolled shrinking of input dataset
%  3. Filling outliers by NaNs to preserve original dimensions of the input 
%  vector; this is crucial when the input variable is supposed to be used
%  with another variable with the same size (e.g., for plotting, regression
%  calculations, etc.)
%  4. Indexes of the outliers that have been detected and removed are
%  returned so that the user knows which records have been removed. 
%  5. Syntax and algorithm has been siginificantly improved, this includes
%  the logic for detection of the outliers from the upper and lower limits.
%  Logic to detect an outlier is solely based on the absolute distance of
%  each record from the central point rather than detecting the outliers
%  sequentially, which was the case in Vince Petaccio, 2009, where the
%  outliers were detected and removed by order of one from the upper and
%  the next from the lower extremes. This code first arranges the extreme
%  values (upper or lower) to one side of the sorted vector based on the
%  absolute distance from the center while preserving the original
%  arrangment in the input vector. Later, the code removes the farthest
%  point from the central value and continues to do that until
%  num_outliers is reached.
% 
% --Example:
% X0=[2.0, 3.0, -50.5, 4.0, 109.0, 6.0]
% [X, outliers_idx] = outliers(X0, 2)
%
% see also: outliers (works on both vector and matrix).
%--------------------------------------------------------------------------

% Initializations:
outliers_idx=[]; %if no outliers has been found, return empty matrix to 
% avoid problems in indexing based on outliers_idx 

X=[];
if nargin<1
    disp('Error! at least one input argument is necessary');
    return;
elseif nargin<2
    num_outliers=1;
end

n1=length(X0); %Determine the number of samples in datain

if n1 < 3 
    display(['Error! There must be at least 3 samples in the' ...
        ' dataset in order to use this function.']);
    return
end

X=X0; %keep original vector

%Sort the input data vector so that removing the extreme values becomes an 
%arbitrary task, using absolute value of the vector will pile the extremes
%to the upper side of the vector (at first only indexes are required), also
%note that NaNs are considered maximum by sort function:
[X, idx]=sort(abs(X));
X=X0(idx); %sort vector using idx based on abs values
X(isnan(X))=[]; %remove NaNs before calculations
n=length(X); %length after removal of NaNs
nns=n1-n; %NaN elements gathered at the end by sort with default mode


stDev= std(X); %calculate stDev, standard deviation of input vector
xbar = mean(X);%calculate the sample mean

% tau is a vector containing values for Thompson's Tau:
tau =     [1.150; 1.393; 1.572; 1.656; 1.711; 1.749; 1.777; 1.798; 1.815;
    1.829; 1.840; 1.849; 1.858; 1.865; 1.871; 1.876; 1.881; 1.885; 1.889;
    1.893; 1.896; 1.899; 1.902; 1.904; 1.906; 1.908; 1.910; 1.911; 1.913;
    1.914; 1.916; 1.917; 1.919; 1.920; 1.921; 1.922; 1.923; 1.924];

% Determine the value of stDev times Tau
if n > length(tau)
    tauS=1.960*stDev; %For n > 40
else
    tauS=tau(n)*stDev; %For samples of size 3 < n < 40
end


% Compare the values of extreme high/low data points with tauS:
i=1;
while num_outliers > 0
 if abs(abs(X(end))-xbar) > tauS
    X=X(1:end-1);
    n=length(X);
    outliers_idx(i)=idx(end-i-nns+1);
    X0(outliers_idx(i))=NaN;
    i=i+1;
    
    % Determine the NEW value of S times tau
    stDev=std(X);
    xbar=mean(X);
    if n > length(tau)
        tauS=1.960*stDev; %For n > 40
    else
        tauS=tau(n)*stDev; %For samples of size 3 < n < 40
    end  
 end
num_outliers=num_outliers-1; %reduce requested num_outliers by 1
end %end of while
X=X0; %return the output in which outliers are turned to NaN
%disp('Subfunction: outliers called');
end %end of outliers function