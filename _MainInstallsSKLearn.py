
#            Clustering
from sklearn.cluster import KMeans, MeanShift, MiniBatchKMeans

#            Classification
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.linear_model import logistic

#            Regression
from sklearn.linear_model import ridge_regression, stochastic_gradient, sag
from sklearn.ensemble import  RandomForestRegressor

#            Classification Metrics
from sklearn.metrics import accuracy_score, auc, roc_auc_score, roc_curve
from sklearn.metrics import classification, confusion_matrix, precision_score

#            Clustering Metrics
from sklearn.metrics import homogeneity_score, mutual_info_score, fowlkes_mallows_score


#            Regression Metrics
from sklearn.metrics import r2_score, explained_variance_score
from sklearn.metrics import mean_squared_error, mean_absolute_error
