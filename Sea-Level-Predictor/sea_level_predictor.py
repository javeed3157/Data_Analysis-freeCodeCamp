import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv(r'D:\Data_Analysis-freeCodeCamp\Sea-Level-Predictor\epa-sea-level.csv')

    # Create scatter plot
    x=df['Year'] 
    y=df['CSIRO Adjusted Sea Level']
    fig,ax=plt.subplots()
    plt.scatter(x,y)
    # Create first line of best fit
    out=linregress(x,y)
    x_predic=pd.Series([i for i in range(1880,2051)])
    # y=mx+c
    y_predic=out.slope*x_predic+out.intercept
    plt.plot(x_predic,y_predic,'g')

    # Create second line of best fit
    df2=df[df['Year']>=2000]
    x2=df2['Year']
    y2=df2['CSIRO Adjusted Sea Level']
    out2=linregress(x2,y2)
    x_predic2=pd.Series([i for i in range(2000,2051)])
    # y=mx+c
    y_predic2=out2.slope*x_predic2+out2.intercept
    plt.plot(x_predic2,y_predic2,'b')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()