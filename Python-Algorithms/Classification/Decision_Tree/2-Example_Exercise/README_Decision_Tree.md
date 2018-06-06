
## Decision Tree Algorithm

### Dataset - 1 :

**1. Balance Scale Weight & Distance Data**

   https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.data

**2. Data Set Information:**

	 This data set was generated to model psychologicalexperimental results. Each example is classified 
    as having the	balance scale tip to the right, tip to the left, or be balanced. The attributes are
    the left weight, the left	distance, the right weight, and the right distance. 
    The correct way to find the class is the greater of (left-distance * left-weight) and 
    (right-distance * right-weight) If they are equal, it is balanced.

**3. Number of Instances: 625**

**4. Number of Attributes: 5**

**5. Attribute Information:**
    
    Target
       - Class Name  (Left, Balanced, Right) - Categorical 
    
    Predictors
       - Left-Weight    - Numeric
       - Left-Distance  - Numeric
       - Right-Weight   - Numeric
       - Right-Distance - Numeric

https://archive.ics.uci.edu/ml/machine-learning-databases/balance-scale/balance-scale.names


### Dataset - 2 :

**1. Banknote Authentication Data**

   http://archive.ics.uci.edu/ml/datasets/banknote+authentication

**2. Data Set Information:**

    Data were extracted from images that were taken from genuine and forged banknote-like specimens. 
    For digitization, an industrial camera usually used for print inspection was used. The final images 
    have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale 
    pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract 
    features from images.
    

**3. Number of Instances: 1372**

**4. Number of Attributes: 5**

**5. Attribute Information:**
    
    Target
       - Class  (Genuine, Forged) - Categorical 
    
    Predictors
       - Variance of Wavelet Transformed image - Numeric
       - Skewness of Wavelet Transformed image - Numeric
       - Curtosis of Wavelet Transformed image - Numeric
       - Entropy of image 					           - Numeric


   http://archive.ics.uci.edu/ml/datasets/banknote+authentication



