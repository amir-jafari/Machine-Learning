function weight = gaussdist(xi, xj, sigma)

weight = exp(-sum(((xi - xj) .^ 2) ./ sigma, 2));