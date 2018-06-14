

## Support Vector Machine Algorithm

### Dataset - 1 :

**1. Gender Recognition by Voice and Speech Data**

   https://www.kaggle.com/primaryobjects/voicegender

**2. Data Set Information:**

       This database was created to identify a voice as male or female, based upon acoustic properties
       of the voice and speech. The dataset consists of 3,168 recorded voice samples, collected from 
       male and female speakers. The voice samples are pre-processed by acoustic analysis in R using 
       the seewave and tuneR packages, with an analyzed frequency range of 0hz-280hz (human vocal range).

**3. Number of Instances: 3168**

**4. Number of Attributes: 22**

**5. Attribute Information:**
    
    
    
    Target
         - label (male, female) - categorical
    
    Predictors  - numeric
         - meanfreq: mean frequency (in kHz)
         - sd: standard deviation of frequency
         - median: median frequency (in kHz)
         - Q25: first quantile (in kHz)
         - Q75: third quantile (in kHz)
         - IQR: interquantile range (in kHz)
         - skew: skewness (see note in specprop description)
         - kurt: kurtosis (see note in specprop description)
         - sp.ent: spectral entropy
         - sfm: spectral flatness
         - mode: mode frequency
         - centroid: frequency centroid (see specprop)
         - peakf: peak frequency (frequency with highest energy)
         - meanfun: average of fundamental frequency measured across acoustic signal
         - minfun: minimum fundamental frequency measured across acoustic signal
         - maxfun: maximum fundamental frequency measured across acoustic signal
         - meandom: average of dominant frequency measured across acoustic signal
         - mindom: minimum of dominant frequency measured across acoustic signal
         - maxdom: maximum of dominant frequency measured across acoustic signal
         - dfrange: range of dominant frequency measured across acoustic signal
         - modindx: modulation index. 


https://www.kaggle.com/primaryobjects/voicegender


### Dataset - 2 :

**1. Mushroom Data**

   https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data

**2. Data Set Information:**

    This data set includes descriptions of hypothetical samples corresponding to 23 species of 
    gilled mushrooms in the Agaricus and Lepiota Family (pp. 500-525).  Each species is identified 
    as definitely edible, definitely poisonous
    
    The classification goal is to predict if the mushroom is edible or poisonous (e/p).
    

**3. Number of Instances: 8124**

**4. Number of Attributes: 22**

**5. Attribute Information:**
    
    Target
       - class - mushroom category (binary: e:'edible', p:'poisonous') - categorical 
    
    Predictors	- categorical
     - cap-shape            - bell=b,conical=c,convex=x,flat=f,knobbed=k,sunken=s
     - cap-surface          - fibrous=f,grooves=g,scaly=y,smooth=s
     - cap-color            - brown=n,buff=b,cinnamon=c,gray=g,green=r,
                              pink=p,purple=u,red=e,white=w,yellow=y
     - bruises              - bruises=t,no=f
     - odor                 - almond=a,anise=l,creosote=c,fishy=y,foul=f,
                              musty=m,none=n,pungent=p,spicy=s
     - gill-attachment      - attached=a,descending=d,free=f,notched=n
     - gill-spacing         - close=c,crowded=w,distant=d
     - gill-size            - broad=b,narrow=n
     - gill-color           - black=k,brown=n,buff=b,chocolate=h,gray=g,
                              green=r,orange=o,pink=p,purple=u,red=e,white=w,yellow=y
    - stalk-shape           - enlarging=e,tapering=t
    - stalk-root            - bulbous=b,club=c,cup=u,equal=e,
                              rhizomorphs=z,rooted=r,missing=?
    - stalk-surf-abv-ring   - fibrous=f,scaly=y,silky=k,smooth=s
    - stalk-surf-bel-ring   - fibrous=f,scaly=y,silky=k,smooth=s
    - stalk-color-abv-ring  - brown=n,buff=b,cinnamon=c,gray=g,orange=o,
                              pink=p,red=e,white=w,yellow=y
    - stalk-color-bel-ring  - brown=n,buff=b,cinnamon=c,gray=g,orange=o,
                              pink=p,red=e,white=w,yellow=y
    - veil-type             - partial=p,universal=u
    - veil-color            - brown=n,orange=o,white=w,yellow=y
    - ring-number           - none=n,one=o,two=t
    - ring-type             - cobwebby=c,evanescent=e,flaring=f,large=l,
                              none=n,pendant=p,sheathing=s,zone=z
    - spore-print-color     - black=k,brown=n,buff=b,chocolate=h,green=r,
                              orange=o,purple=u,white=w,yellow=y
    - population            - abundant=a,clustered=c,numerous=n,
                              scattered=s,several=v,solitary=y
    - habitat               - grasses=g,leaves=l,meadows=m,paths=p,
                              urban=u,waste=w,woods=d

   https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.names
