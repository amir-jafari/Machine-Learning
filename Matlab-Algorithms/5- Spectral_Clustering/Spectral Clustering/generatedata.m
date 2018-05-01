function [data, class] = generatedata(nbsamples, nbclasses, dim, dist, details, blackplot)
%nbsamples is used to specify how many data samples to generate
%
%nbclasses is used to specify how many classes to consider when generating
%the data
%
%dim is the dimension of each sample (for graphical representation use dim
%equal to 2)
%
%dist specify how the data are generated:
%'gaussian' means the data will be a gaussian distribution with a certain
%mean and standard deviation. details should be a cell (nbclasses, 2) and
%each row contains first the mean and second the std, and each mean or std
%is a vector of dimension dim
%
%'circles' means the data will be distributed as circles with a certain
%mean which means the center, a radius and a std to express how much points
%will deviate from the radius, details should be a cell (nbclasses, 5) and
%each row contains first the mean of dimension dim, then the radius of
%dimension 1, and std of dimension dim. the fourth detail is:
%'complete' for a whole circle
%'uhalf' for the upper half of the circle
%'lhalf' for the lower half of the circle
%and the fifth detail is the wanted percentage of the circle
%
%details contains in each row informations about the type of distribution
%
%blackplot when set to positive integer means that all data will be plotted
%as black circles if dimension is two (used for unsupervised learning
%

data = randn(nbsamples, dim);
class = randi(nbclasses, [1, nbsamples]);

if(blackplot)

    plotchoice = {'ko','ko','ko','ko','ko'};
else
    
    plotchoice = {'bo','r+','md','k*','wv'};
end

if(strcmp(dist, 'gaussian') > 0)
    
    for i = 1: nbsamples
        
        data(i, :) = details{class(i), 1} + details{class(i), 2} .* data(i, :);
    end
    
    if(dim == 2)
        
        figure;
        for i = 1: nbclasses

            hold on;
            points = data(class == i, :);
            plot(points(:,1), points(:,2), plotchoice{i});
        end
        title('generated data');
        grid on;
    end
end

if(strcmp(dist, 'circles') > 0)
    
    uhalf = ones(nbclasses, 1);
    lhalf = ones(nbclasses, 1);
    
    for i = 1: nbclasses
        
        if(strcmp(details{i, 4}, 'uhalf'))
            uhalf(i) = -1;
        end
        
        if(strcmp(details{i, 4}, 'lhalf'))
            lhalf(i) = -1;
        end
    end
    
    for i = 1: nbsamples
        
        edge = round(details{class(i), 2} * details{class(i), 5} / 100);
        coord = randi([-edge edge], [1, dim]);
        if(randi([-3 3] > 0))
            
            coord(end) = -1 * uhalf(class(i))* sqrt(details{class(i), 2} ^ 2 - (sum(coord(1: dim - 1) .^ 2)));
        else
            
            coord(end) = 1 * lhalf(class(i)) * sqrt(details{class(i), 2} ^ 2 - (sum(coord(1: dim - 1) .^ 2)));
        end
        
        data(i, :) = coord + details{class(i), 1} + details{class(i), 3} .* data(i, :);
    end
    
    if(dim == 2)
        
        figure;
        for i = 1: nbclasses

            hold on;
            points = data(class == i, :);
            plot(points(:,1), points(:,2), plotchoice{i});
        end
        title('generated data');
        grid on;
    end
end