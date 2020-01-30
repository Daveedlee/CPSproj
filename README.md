# Chicago Public School Project

## Progression
  1. Dataset acquired from Chicago Data Portal
  2. Exploratory data analysis has been performed
  3. Two hypotheses has been tested
  4. **The findings have been presented**
  
  
## Introduction
The whole idea of analyzing CPS (Chicago Public School) dataset came rather whimsically-I was watching DNC presidential debate one night and the guy I could relate to most (Andrew Yang) said the following:
    
    "70-75% of kids' academic performance is determined by out-of-school factors: 
    parental time, income, neighborhood, and etc. Putting resources into families' 
    hands would improve kids' abilities to learn."
    
It all made sense; of course the other factors matter. The question was that would it show? "Well, it should," I thought. And that's how this project began.

## Datasets
Affordable Rental Housing Developments

* https://catalog.data.gov/dataset/affordable-rental-housing-developments-ef5c2/resource/4bbbc75c-6083-4168-b34f-662dbbe5b97f

Chicago Public Schools - School Progress Reports SY1819

* https://catalog.data.gov/dataset/chicago-public-schools-school-progress-reports-sy1819/resource/3b087de5-b047-47fa-8ece-2ff667b84fb9

Census Data - Selected socioeconomic indicators in Chicago, 2008 – 2012

* https://data.cityofchicago.org/resource/kn9c-c2s2.json

## Methodology
The biggest question that loomed over my head as I approached this project was perhaps what many policymakers (hopefully) wonder: what makes a school better than the others? Is it the football team or is it the debate team? Or maybe the award-winning faculty? My answer to this question was rather a student get better academically over time. The dataset provided by the Chicago Public Schools had this metric called "Student Growth Rate." I took the growth rate and merged with the dataset that had the "Prosperity Rating" and "Hardship Index." Finally, I performed a T-test on the merged dataset using scipy.

## Metrics to consider:
  1. Student Growth Rating (SGR)
    - SGR measures the percent increase in standardized exam scores in course of two years and compares them to the national average. 1: below average, 2: average, 3: above average, 4: far above average
  2. Hardship Index
    - Amalgamation of unemployment, education, per capita income, poverty, crowded housing, dependency. Ranked by neighborhood (lower the better)
  
## Findings
Test 1: Top 10 neighborhoods vs the rest
The mean SGR of top 10 neighborhoods, according to Hardship Index, was compared against the rest of the neighborhoods. 
* Null Hypothesis: The mean SGR of the schools in top 10 neighborhoods **doesn't differ** significantly when compared to the mean SGR of the other neighborhoods.
* Alternative Hypothesis: The mean SGR of the schools in top 10 neighborhoods **differs** significantly when compared to the mean SGR of the other neighborhoods.

Results:
* Critical t-value = 1.795
* **p-value = 0.1019**
=> Failed to reject the null hypothesis; we failed to find an evidence to reject the claim that the SGR doesn't vary by the location of the school.

Test 2: Chartered schools vs non-chartered school
The SGR mean of chartered schools was compared against non-chartered schools.
* Null Hypothesis: The mean SGR of chartered schools doesn't differ significantly when compared to the mean SGR of non-chartered schools.
* Alternative Hypothesis: The mean SGR of chartered schools differs significantly when compared to the mean SGR of non-chartered schools.

Results:
* Critical t-value = 1.68
* **p-value = 0.0012**
=> Reject the null hypothesis; the test statistics show an evidence to reject the null hypothesis.

## Conclusion
The conclusion, as forementioned, was quite anti-climatic. According to the test, it isn't true that the schools in better neighborhood have better chance of improving a student's standardized test score. The reason I ran the second test was to check if SGR as a metric could be trusted. Once again, I was surprised when the result showed that chartered schools have better chance of improving a student's SGR score-it seems to have some meaning. So, was Andrew Yang wrong? Well, I wouldn't say that conclusively. There are a few to consider: it could be that good students may not improve as much. Or it could be that the parental time, as mentioned by Andrew, has more parts to play. Furthermore, it should be noted that 35 schools did not provide student growth rate.

