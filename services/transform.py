import pandas as pd
from json import dumps, loads, load


class transform():
        
    def read_data(self):
        self.df_2015 = pd.read_csv('..\data\df_2015.csv')
        self.df_2016 = pd.read_csv('..\data\df_2016.csv')
        self.df_2017 = pd.read_csv('../data/df_2017.csv')
        self.df_2018 = pd.read_csv('../data/df_2018.csv')
        self.df_2019 = pd.read_csv('../data/df_2019.csv')

    def drop_columns(self):
        self.df_2015.drop(["Dystopia Residual","Family","Region","Standard Error"], axis="columns", inplace=True)
        self.df_2016.drop(["Dystopia Residual","Family","Region","Lower Confidence Interval", "Upper Confidence Interval"], axis="columns", inplace=True)
        self.df_2017.drop(["Dystopia.Residual","Family","Whisker.high", "Whisker.low"], axis="columns", inplace= True)
        self.df_2018.drop(["Social support"], axis="columns", inplace=True)
        self.df_2019.drop(["Social support"], axis="columns", inplace=True)

    def rename_columns(self):
        columnas1 = {
        "Happiness.Rank":"Happiness Rank",
        "Happiness.Score":"Happiness Score",
        "Economy..GDP.per.Capita.":"Economy (GDP per Capita)",
        "Health..Life.Expectancy.":"Health (Life Expectancy)",
        "Trust..Government.Corruption.":"Trust (Government Corruption)",
        "Dystopia.Residual":"Dystopia Residual"
        }
        self.df_2017.rename(columns=columnas1, inplace = True)
        # ----------------------
        columnas2 = {
        "Overall rank":"Happiness Rank",
        "Country or region":"Country",
        "Score":"Happiness Score",
        "GDP per capita":"Economy (GDP per Capita)",
        "Healthy life expectancy":"Health (Life Expectancy)",
        "Freedom to make life choices":"Freedom",
        "Perceptions of corruption":"Trust (Government Corruption)"
        }
        self.df_2018.rename(columns=columnas2, inplace = True)
        # -----------------------
        columnas3 = {
        "Overall rank":"Happiness Rank",
        "Country or region":"Country",
        "Score":"Happiness Score",
        "GDP per capita":"Economy (GDP per Capita)",
        "Healthy life expectancy":"Health (Life Expectancy)",
        "Freedom to make life choices":"Freedom",
        "Perceptions of corruption":"Trust (Government Corruption)"
        }
        self.df_2019.rename(columns=columnas3, inplace = True)

    def merge (self):
        self.df = pd.concat([self.df_2016,self.df_2017,self.df_2018,self.df_2019])
        self.df['Trust (Government Corruption)'].fillna(0.120874, inplace=True)

    def send_csv(self):
        self.df.to_csv("datos_eda")


