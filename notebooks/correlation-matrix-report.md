## Correlation Analysis

### What the Heatmap Shows
A correlation matrix shows the pairwise relationship between all numerical 
features in the dataset. The values range from -1 to +1, where values 
close to +1 mean the features move in the same direction (strong positive 
relationship), values close to -1 mean they move in opposite directions 
(strong negative relationship), and values close to 0 mean there is no 
meaningful relationship between them. Feature pairs with values beyond 
+0.5 or below -0.5 are strong enough to investigate for multicollinearity.

### Strong Positive Correlations
fixed acidity & citric acid = +0.67
fixed acidity & density = +0.68
free sulfur dioxide & total sulfur dioxide = +0.66

### Strong Negative Correlations
fixed acidity & pH = -0.69
citric acid & volatile acidity = -0.54
citric acid & pH = -0.55

All strong correlations found have chemical explanations that make sense 
for wine data, which confirms they are genuine relationships and not 
accidental patterns in this specific dataset.

### Impact on Model Performance
When two input features are strongly correlated, they carry overlapping 
information. This is called multicollinearity. Linear models like logistic 
regression are most affected because they try to assign an independent 
weight to every feature simultaneously. When features are correlated, 
those weights become unstable and change unpredictably with small changes 
in training data, making the model unreliable. Tree-based models like 
Random Forest and XGBoost handle this better because they select one 
feature at a time per split, so a correlated feature may simply never 
get chosen if another one already carries the same information.

### Key Finding - Correlation With Quality
No feature has a strong correlation with quality, all values are below 
+0.5 or above -0.5. The closest are alcohol at +0.48, meaning higher 
alcohol tends toward higher quality, and volatile acidity at -0.41, 
meaning higher volatile acidity which gives wine a vinegar character 
tends toward lower quality. Weak individual correlations do not mean 
the features are useless, as models can find combined patterns across 
multiple features that simple pairwise correlation cannot capture alone.

### Decisions
The Id column will be dropped before training because it is a meaningless 
row identifier with no predictive value. Its correlations with real 
features like density suggest it could introduce spurious patterns during 
training. The correlated feature pairs will be retained for now and 
revisited after baseline model performance is established, since 
tree-based models are less sensitive to multicollinearity and dropping 
features prematurely may remove useful signal.