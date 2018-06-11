

## Logistic Regression Algorithm

### Dataset - 1 :

**1. Wine Quality Data**

   http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv

**2. Data Set Information:**

    The datasets is related to red variant of the Portuguese "Vinho Verde" wine.
    For more details, consult: http://www.vinhoverde.pt/en/ or the reference [Cortez et al., 2009].
    Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables 
    are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).
    
    The inputs include objective tests (e.g. PH values) and the output is based on sensory data
    (median of at least 3 evaluations made by wine experts). The wine quality is graded between 
    0 (very bad) and 10 (very excellent)

**3. Number of Instances: 1599**

**4. Number of Attributes: 12**

**5. Attribute Information:**
    
    
    
    Target
        - quality (score between 0 and 10) - categorical
    
    Predictors  - numeric
        - fixed acidity 
        - volatile acidity
        - citric acid
        - residual sugar
        - chlorides
        - free sulfur dioxide
        - total sulfur dioxide
        - density
        - pH
        - sulphates
        - alcohol

http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality.names


### Dataset - 2 :

**1. Bank Marketing Data**

   https://archive.ics.uci.edu/ml/datasets/bank+marketing

**2. Data Set Information:**

    The data is related with direct marketing campaigns of a Portuguese banking institution. The 
    marketing campaigns were  based on phone calls. Often, more than one contact to the same client
    was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no')
    subscribed. 
    
    The classification goal is to predict if the client will subscribe (yes/no) a term deposit (variable y).
    

**3. Number of Instances: 41188**

**4. Number of Attributes: 21**

**5. Attribute Information:**
    
    Target
       - y - has the client subscribed a term deposit? (binary: 'yes','no') - categorical 
    
    Predictors	
       - age - age in years (numeric)
       - job : type of job (categorical)
       - marital : marital status (categorical)
       - education (categorical)
       - default: has credit in default? (categorical)
       - housing: has housing loan? (categorical)
       - loan: has personal loan? (categorical)
       - contact: contact communication type (categorical) 
       - month: last contact month of year (categorical)
       - day_of_week: last contact day of the week (categorical')
       
       - duration: last contact duration, in seconds (numeric). 
                   Important note: this attribute highly effects the output target g., if duration=0 
                   then y='no'). Yet, the duration is not known before a call is performed. Also, after 
                   the end of the call  is obviously known.
                   Thus, this input should only be included for benchmark purposes and should be 
                   discarded if the intention s to have a realistic predictive model
                   
       - campaign: number of contacts performed during this campaign and for this client (numeric)
       
       - pdays: number of days that passed by after the client was last contacted from a previous 
                campaign (numeric)
       
       - previous: number of contacts performed before this campaign and for this client (numeric)
       - poutcome: outcome of the previous marketing campaign (categorical)
       - emp.var.rate: employment variation rate - quarterly indicator (numeric)
       - cons.price.idx: consumer price index - monthly indicator (numeric) 
       - cons.conf.idx: consumer confidence index - monthly indicator (numeric) 
       - euribor3m: euribor 3 month rate - daily indicator (numeric)
       - nr.employed: number of employees - quarterly indicator (numeric)

   https://archive.ics.uci.edu/ml/datasets/bank+marketing
