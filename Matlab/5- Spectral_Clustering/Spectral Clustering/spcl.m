function [clusters, evalues, evectors] = spcl(data, nbclusters, varargin)
%
% spcl(data, nbclusters, varargin) is a spectral clustering function to
% assemble random unknown data into clusters. after specifying the data and
% the number of clusters, next parameters can vary as wanted. This function
% will construct the fully connected similarity graph of the data.
%
% The first parameter of varargin is the name of the function to use.
%
% The second is the parameter to pass to the function.

% Third parameter is the type of the Laplacian matrix:
% 'unormalized' - unnormalized laplacian matrix
% 'sym' - normalized symmetric laplacian matrix
% 'rw' - normalized asymmetric laplacian matrix
% (if omitted the default will be 'unnormalized')
% 
% then the algorithm used for organizing eigenvectors:
% 'np' - generally used for 2 clusters, one eigenvector must be used, if
% will put positive values in class 1 and negative values in class 2
% 'kmean' - a k-mean algorithm will be used to cluster the given eigenvectors
% 
% finally an eigenvector choice can be added, it can be a vector [vmin
% vmax] or a matrix defining several intervals. if not found the default
% will be [2 2]


plotchoices = {'bo','r+','md','k*','wv'};
lapmatrixchoices = {'unormalized', 'sym', 'rw'};
algochoices = {'np', 'kmean'};
func = 'gaussdist';
count = 1;

%%get all the parameters%%%
if(ischar(varargin{count}))
        
    func = varargin{count};
    count = count + 1;
end

params = varargin{count};
count = count + 1;

if(length(varargin) >= count)
    
    if(sum(strcmp(varargin{count}, lapmatrixchoices)) == 0)

        lapmatrixchoice = 'unormalized';
    else

        lapmatrixchoice = varargin{count};
        count = count + 1;
    end

    if(length(varargin) >= count)
        
        if(sum(strcmp(varargin{count}, algochoices)) == 0)

            clusteralgo = 'np';
        else
            clusteralgo = varargin{count};
            count = count + 1;
        end

        if(length(varargin) >= count)

            eigv = varargin{count};
        else
            
            eigv = [2 2];
        end
    else
        clusteralgo = 'np';
        eigv = [2 2];
    end
else
    
    lapmatrixchoice = 'unormalized';
    clusteralgo = 'np';
    eigv = [2 2];
end
%%all parameters are got%%%

sprintf('Graph choice is fully connected\nLaplacian choice is %s\nCluster algorithm is %s', lapmatrixchoice, clusteralgo)
[nbsamples, dim] = size(data);
wmat = zeros(nbsamples);

for i = 1: nbsamples - 1
    
    wmat(i, i + 1: end) = feval(func, repmat(data(i, :), nbsamples - i, 1), data(i + 1: end,:), params);
end

wmat = wmat + wmat';
dmat = diag(sum(wmat, 2));

if(strcmp(lapmatrixchoice, 'unormalized'))
    
    laplacian = dmat - wmat;
else
    if(strcmp(lapmatrixchoice, 'sym'))
        
        laplacian = eye(nbsamples) - (dmat^-0.5) * wmat * (dmat^-0.5);
    else
        if(strcmp(lapmatrixchoice, 'rw'))
            
            laplacian = eye(nbsamples) - (dmat^-1) * wmat;
        end
    end
end

[evectors, evalues] = eig(laplacian);

newspace = evectors(:, eigv(1,1): eigv(1,2));
n = size(eigv);
for i = 2: n(1)
    
    newspace = [newspace evectors(:, eigv(i,1): eigv(i,2))];
end

if(strcmp(clusteralgo, 'kmean'))
    
    clusters = kmeans(newspace, nbclusters);
else
    clusters = 1 + (newspace > 0);
end

if(dim == 2)
    figure;
    for i = 1: nbclusters

        points = data(clusters == i, :);
        plot(points(:,1), points(:,2), plotchoices{i});
        hold on;
    end
    title('clustered data using spectral clustering');
    grid on;
end