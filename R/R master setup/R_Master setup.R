# Install Packages

cat('\014')
rm(list = ls())
graphics.off()

requiredPackages = c('plyr', 'ggplot2' , 'ggtern', 'datasets', 'dplyr', 'nnet', 'MASS', 
                     'fun', 'stats','ggmap','maps', 'igraph', 'Rcpp', 'stringr', 'zoo', 
                     'NLP', 'xlsx', 'gplots', 'reshape2')

for(p in requiredPackages){
if(!is.element(p, installed.packages()[,1])){install.packages(p)} else {cat(p, "is installed \"", "\"\n")}
}


