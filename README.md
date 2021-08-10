# Sentiment-Analysis
Sentiment analysis using Machine Learning models (BERT, LightGBM, Logistic Regression) 

# Summary

## Metrics
The BERT model outperform significantly the LightGBM and Logistic Regression models (Accuracy of ~0.70 vs ~0.65). However, all models 

### Logistic Regression
| Métrica | Train | Test | Dublin dataset |
| ----- | --- | ----- |  ----- |
| Accuracy | 0.770 | 0.811 | 0.653 |
| f1 | 0.78 | 0.82 | 0.61 |
| recall | 0.80 | 0.85 | 0.55 |
| precision | 0.76 | 0.79 | 0.69 |

### LightGBM Regression
| Métrica | Train | Test | Dublin dataset |
| ----- | --- | ----- |  ----- |
| Accuracy | 0.757 | 0.708 | 0.644 |
| f1 | 0.77 | 0.74 | 0.68 |
| recall | 0.82 | 0.84 | 0.75 |
| precision | 0.73 | 0.67 | 0.62 |

### BERT
| Métrica | Train | Test | Dublin dataset |
| ----- | --- | ----- |  ----- |
| Accuracy | 0.869 | 0.841 | 0.692 |
| f1 | 0.87 | 0.85 | 0.70 |
| recall | 0.88 | 0.87 | 0.71 |
| precision | 0.86 | 0.83 | 0.69 |




> ## TODO
> ### DATA
1.   In-depth Exploration Data Analysis to get a better understand of text
2.   Analyze in detail model errors on dublin dataset
3.   Find a better dataset to fine tune BERT
4.   Create new variables from raw text (i.e. number of words, capital letter, emoticons, etc)
5.   Improve data cleaning and preprocessing for Logistic Regression and LightGBM(stopwords, lematization)

> ### MODEL
1.   Try novel architectures like GPT3
2.   Train with complete dataset in both BERT and LightGBM
3.   Add early stopping in training

> ### SOFTWARE
1.   Define a requirement with libraries versions to version problem. Ideally, create a docker file to solve operative system incompatibilities.
2.   Create technical and functional documentation.
3.   Create a file with parameters.
4.   Create unit testing of functions.
5.   Add Logger class.
