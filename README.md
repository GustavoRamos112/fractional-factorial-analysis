# General Information

Program written in python using the libraries: pandas, pyDOE2 (fracfact), statsmodels.formula.api.ols, statsmodels.stats.anova.anova_lm and pingouin.

#Purpose

Help eliminate irrelevant interactions in the model.

#Guide

Install the necessary libraries:
```
pip install pandas pyDOE2 statsmodels pingouin
```

Download the repository:
```
git clone https://github.com/GustavoRamos112/fractional-factorial-analysis.git
```
 In the main.py, there are five variables after importing the libraries: Y, discriminador, tolerancia, maximo y factor_names.
 Y = Response variable
 discriminador = Minimum number that the sum of squares must have to be considered the interaction in the end
 tolerancia = It is not necessary to move this variable, it may disappear in future versions
 maximo = Maximum number for interactions (2; x1:x2, 3; x1:x2:x3, ..., n; x1:x2:...:xn-1:xn) **More information at the end
 factor_names = Names of the factors that will be used in the model **More information at the end

 The "maximo" variable, I hypothesize that it has to be of the form k-1, where k is the number of individual factors (A,B, C, ..., X, Y, Z, not A:B, BSD = B:SD, etc).
 For factor_names, the letters will be used in alphabetical order, however, to avoid problems later, the C will be changed to F, I will add a function to change it to taste if it creates a conflict

Execute main.py:
If you use my powershell profile:
```
py main
```
If you don't use my powershell profile
```
python main.py
```
