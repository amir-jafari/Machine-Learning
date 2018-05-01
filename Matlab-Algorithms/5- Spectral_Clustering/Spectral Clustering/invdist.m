function weight = invdist(xi, xj)

weight = 1 ./ (1 + sum((xi - xj) .^ 2, 2));