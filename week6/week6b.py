#: Imports
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import shortuuid
import re

#: Global settings
sns.set_theme(style="whitegrid", palette="pastel")
# sns.set_style("whitegrid")

# method: plotForAll
# Creates plots for all
# @dataFrame, pd.DataFrame: The input dataframe
# @projectCode, str: The code of the project, which will be used to store files
# @return, dict: The dictionary of each variables and the file where is it stored
# @completed
def plotForAll( dataFrame: pd.DataFrame, projectCode: str ) -> dict:
    output = {}
    #: Compute the correlation matrix
    corr = dataFrame.corr()
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))
    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    # Draw the heatmap with the mask and correct aspect ratio
    fig = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})
    fname = 'projects/' + projectCode + '/' + str(shortuuid.uuid()) + '.png'
    fig = fig.get_figure()
    output[ f'all_corrmap' ] = fname
    fig.savefig(fname)
    plt.clf()
    #: Return
    return output

# method: plotN
# Creates plots for n
# @dataFrame, pd.DataFrame: The input dataframe
# @variable, str: The variable
# @projectCode, str: The code of the project, which will be used to store files
# @return, dict: The dictionary of each variables and the file where is it stored
# @completed
def plotN( dataFrame: pd.DataFrame, variable: str, projectCode: str ) -> dict:
    #: Declare variables
    output = {}
    #: Plot
    fig = sns.histplot(data=dataFrame, x=variable)
    fname = 'projects/' + projectCode + '/' + str(shortuuid.uuid()) + '.png'
    fig = fig.get_figure()
    output[ f'n_hist_{variable}' ] = fname
    fig.savefig(fname)
    plt.clf()
    #: Return
    return output

# method: plotC
# Creates plots for C
# @dataFrame, pd.DataFrame: The input dataframe
# @variable, str: The variable
# @projectCode, str: The code of the project, which will be used to store files
# @return, dict: The dictionary of each variables and the file where is it stored
# @completed
def plotC( dataFrame: pd.DataFrame, variable: str, projectCode: str ) -> dict:
    #: Declare variables
    output = {}
    #: Plot
    data = dataFrame[variable].value_counts().to_dict()
    plt.pie( data.values(), labels=data.keys())
    fname = 'projects/' + projectCode + '/' + str(shortuuid.uuid()) + '.png'
    output[ f'c_pie_{variable}' ] = fname
    plt.savefig(fname)
    plt.clf()
    #: Return
    return output

# method: plotCNN
# Creates plots for CNN
# @dataFrame, pd.DataFrame: The input dataframe
# @variable, str: The variable
# @projectCode, str: The code of the project, which will be used to store files
# @return, dict: The dictionary of each variables and the file where is it stored
# @completed
def plotCNN( dataFrame: pd.DataFrame, variable: tuple, projectCode: str ) -> dict:
    #: Declare variables
    output = {}
    #: Plot
    fig = sns.jointplot(data=dataFrame, x=variable[1], y=variable[2], hue=variable[0], kind="kde")
    fname = 'projects/' + projectCode + '/' + str(shortuuid.uuid()) + '.png'
    output[ f'cnn_joint_{variable}' ] = fname
    fig.savefig(fname)
    plt.clf()
    #: Return
    return output

# method: plotCCN
# Creates plots for CCN
# @dataFrame, pd.DataFrame: The input dataframe
# @variable, str: The variable
# @projectCode, str: The code of the project, which will be used to store files
# @return, dict: The dictionary of each variables and the file where is it stored
# @completed
def plotCCN( dataFrame: pd.DataFrame, variable: tuple, projectCode: str ) -> dict:
    #: Declare variables
    output = {}
    #: Plot
    fig = sns.displot(
        dataFrame, x=variable[2], col=variable[0], row=variable[1],
        facet_kws=dict(margin_titles=True),
    )
    fname = 'projects/' + projectCode + '/' + str(shortuuid.uuid()) + '.png'
    output[ f'ccn_displot_{variable}' ] = fname
    fig.savefig(fname)
    plt.clf()
    #: Return
    return output

# method: plotNN
# Creates plots for NN
# @dataFrame, pd.DataFrame: The input dataframe
# @variable, str: The variable
# @projectCode, str: The code of the project, which will be used to store files
# @return, dict: The dictionary of each variables and the file where is it stored
# @completed
def plotNN( dataFrame: pd.DataFrame, variable: tuple, projectCode: str ) -> dict:
    #: Declare variables
    output = {}
    #: Plot

    fig = sns.JointGrid(data=dataFrame, x=variable[0], y=variable[1])
    fig.plot_joint(sns.scatterplot)
    fig.plot_marginals(sns.rugplot, height=1, color="g", alpha=.6)

    fname = 'projects/' + projectCode + '/' + str(shortuuid.uuid()) + '.png'
    output[ f'nn_joint_{variable}' ] = fname
    fig.savefig(fname)
    plt.clf()
    #: Return
    return output

# method: plotCN
# Creates plots for CN
# @dataFrame, pd.DataFrame: The input dataframe
# @variable, str: The variable
# @projectCode, str: The code of the project, which will be used to store files
# @return, dict: The dictionary of each variables and the file where is it stored
# @completed
def plotCN( dataFrame: pd.DataFrame, variable: tuple, projectCode: str ) -> dict:
    #: Declare variables
    output = {}
    #: Plot
    fig = sns.boxplot(x=variable[0], y=variable[1],data=dataFrame)
    fname = 'projects/' + projectCode + '/' + str(shortuuid.uuid()) + '.png'
    output[ f'cn_boxplot_{variable}' ] = fname
    fig = fig.get_figure()
    fig.savefig(fname)
    plt.clf()
    #: Return
    return output

# method: plotCC
# Creates plots for CC
# @dataFrame, pd.DataFrame: The input dataframe
# @variable, str: The variable
# @projectCode, str: The code of the project, which will be used to store files
# @return, dict: The dictionary of each variables and the file where is it stored
# @completed
def plotCC( dataFrame: pd.DataFrame, variable: tuple, projectCode: str ) -> dict:
    #: Declare variables
    output = {}
    #: Plot
    g = sns.JointGrid(data=dataFrame, x=variable[0], y=variable[1], marginal_ticks=True)
    g.plot_joint(
    sns.histplot, discrete=(False, False),
        cmap="light:#03012d", pmax=.8
    )
    g.plot_marginals(sns.histplot, element="step", color="#03012d", discrete = False)
    fig = g
    fname = 'projects/' + projectCode + '/' + str(shortuuid.uuid()) + '.png'
    output[ f'cc_histplot_{variable}' ] = fname
    fig.savefig(fname)
    plt.clf()
    #: Return
    return output

# method: plotCNP
# Creates plots for CNP
# @dataFrame, pd.DataFrame: The input dataframe
# @variable, str: The variable
# @projectCode, str: The code of the project, which will be used to store files
# @return, dict: The dictionary of each variables and the file where is it stored
# @completed
def plotCNP( dataFrame: pd.DataFrame, variable: tuple, projectCode: str ) -> dict:
    #: Declare variables
    output = {}
    #: Plot
    # Use semantically meaningful titles for the columns
    titles = list(variable)
    data = dataFrame[titles]
    titles = titles[1:]
    g = sns.PairGrid(data,x_vars=titles, y_vars=[ variable[0] ],
                    height=10, aspect=.25)
    # Draw a dot plot using the stripplot function
    g.map(sns.stripplot, size=10, orient="h", jitter=False,
        palette="flare_r", linewidth=1, edgecolor="w")

    # Use the same x axis limits on all columns and add better labels
    g.set(xlim=(0, 25), ylabel="")
    for ax, title in zip(g.axes.flat, titles):
        # Set a different title for each axes
        ax.set(title=title)

        # Make the grid horizontal instead of vertical
        ax.xaxis.grid(False)
        ax.yaxis.grid(True)
    fname = 'projects/' + projectCode + '/' + str(shortuuid.uuid()) + '.png'
    output[ f'cnp_strip_{variable}' ] = fname
    g.savefig(fname)
    plt.clf()
    #: Return
    return output

# method: plotNP
# Creates plots for NP
# @dataFrame, pd.DataFrame: The input dataframe
# @variable, str: The variable
# @projectCode, str: The code of the project, which will be used to store files
# @return, dict: The dictionary of each variables and the file where is it stored
# @completed
def plotNP( dataFrame: pd.DataFrame, variable: tuple, projectCode: str ) -> dict:
    #: Declare variables
    output = {}
    #: Plot
    fig = sns.pairplot(dataFrame[list(variable)])
    fname = 'projects/' + projectCode + '/' + str(shortuuid.uuid()) + '.png'
    output[ f'np_pairplot_{variable}' ] = fname
    fig.savefig(fname)
    plt.clf()
    #: Return
    return output

# method: plotter
# Plots all data
# @dataFrame, pd.DataFrame: The input dataframe
# @roles, dict: The roles
# @variable, list: The variable
# @projectCode, str: The code of the project, which will be used to store files
# @return, dict: The dictionary of each variables and the file where is it store
# @completed
def plotter( dataFrame: pd.DataFrame, roles: dict, vars: list, projectCode: str ) -> dict:
    #: Declare variables
    output = {}
    #: Loop 
    for v in vars:
        #: Chart type
        charttype = ""
        #: Switch
        if type(v) is str:
            if charttype == "flag": 
                charttype = "categoric"
            charttype = roles[ v ][0]
        else:
            charttype = ['c' if roles[i] == 'flag' else roles[i][0] for i in v]
            charttype.sort()
            charttype = "".join(charttype)
        #: Regex operations
        charttype = re.sub(r"([cn])\1{2,}", r"\1+", charttype)
        #: Switch again
        if charttype == 'n':
            output.update( plotN( dataFrame, v, projectCode ) )
        elif charttype == 'c':
            output.update( plotC( dataFrame, v, projectCode ) )
        elif charttype == 'cnn':
            output.update( plotCNN( dataFrame, v, projectCode ) )
        elif charttype == 'ccn':
            output.update( plotCCN( dataFrame, v, projectCode ) )
        elif charttype == 'nn':
            output.update( plotNN( dataFrame, v, projectCode ) )
        elif charttype == 'cn':
            output.update( plotCN( dataFrame, v, projectCode ) )
        elif charttype == 'cc':
            output.update( plotCC( dataFrame, v, projectCode ) )
        elif charttype == 'cn+':
            output.update( plotCNP( dataFrame, v, projectCode ) )
        elif charttype == 'n+':
            output.update( plotNP( dataFrame, v, projectCode ) )
    #: Return
    return output







df = pd.read_csv("Telecom_customer churn.csv", nrows = 10000)
roles =  {
	'prizm_social_one': 'categoric',
	'rev_Mean': 'numeric',
	'da_Mean': 'numeric',
	'crclscod': 'categoric',
	'marital': 'categoric',
    'totcalls': 'numeric'
}

plotter( df, roles, 
    [
        #('totcalls'), # N
        #('marital'), # C
        #('totcalls', 'marital'), # CN
        #('prizm_social_one', 'marital'), # CC
        
        ('marital', 'prizm_social_one'), # NCC
        #('totcalls', 'marital', 'rev_Mean'), # CNN
    ], 
    'figures' 
)


"""


df = pd.read_csv("week6-quiz1.csv")
roles =  {
	'Gender': 'categoric',
	'Age': 'numeric',
	'Driving_License': 'numeric',
	'Region_Code': 'categoric',
	'Previously_Insured': 'numeric',
	'Vehicle_Age': 'categoric',
	'Vehicle_Damage': 'categoric',
	'Annual_Premium': 'numeric',
	'Policy_Sales_Channel': 'categoric',
	'Vintage': 'numeric',
	'Response': 'numeric'
}

df = df.sample(5000)
plotForAll( df, 'myproject1')
plotter( df, roles, 
    [
        ('Age', 'Annual_Premium', 'Vintage'),
        ('Vehicle_Age', 'Age', 'Annual_Premium', 'Vintage')
        #('Vehicle_Age', 'Policy_Sales_Channel')
        #('Vehicle_Age', 'Annual_Premium')
        #('Previously_Insured', 'Age'),
        #('Gender', 'Vehicle_Age', 'Annual_Premium'),
        #'Age', 
        #('Vehicle_Age', 'Age', 'Vintage'), 
        #'Vehicle_Damage', 
        #('Age', 'Annual_Premium'), 
        #('Age', 'Annual_Premium', 'Response')
    ], 
    'myproject1' 
)


"""

