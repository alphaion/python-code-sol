import pandas as pd
import numpy as np


# Source Data
confirmed_url = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"
recovered_url = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv"
deaths_url = "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv"


# Read source into DataFrame

conf_df = pd.read_csv(confirmed_url)
recv_df = pd.read_csv(recovered_url)
death_df = pd.read_csv(deaths_url)

# create a differenced series function

def difference(dataset, interval=1):
    return pd.Series([dataset[i] - dataset[i - interval] for i in range(interval, len(dataset))])


# Create reusable series objects 
conf_sum = conf_df.loc[:,'1/22/20':].sum()
recv_sum = recv_df.loc[:,'1/22/20':].sum()
death_sum = death_df.loc[:,'1/22/20':].sum()

conf_sum_dif = difference(conf_sum, 1).values
recv_sum_dif = difference(recv_sum, 1).values
death_sum_dif = difference(death_sum, 1).values


# Print world report
print("World numbers current as of {}".format(conf_df.columns[-1]))
print("New cases:                         {}".format(conf_sum_dif[-1]))
print("Total confirmed cases:            {}".format(conf_sum[-1]))
print("New case rate:                         {0:2.3%}".format(conf_sum_dif[-1] / conf_sum[-2]))
print("New Recovered cases:                {}".format(recv_sum_dif[-1]))
print("Total recovered cases:             {}".format(recv_sum[-1]))
print("Recovery rate:                        {0:2.3%}".format(recv_sum[-1]/conf_sum[-1]))
print("New Deaths:                          {}".format(death_sum_dif[-1]))
print("Total deaths:                       {}".format(death_sum[-1]))
print("Death rate:                            {0:2.3%}".format(death_sum[-1]/conf_sum[-1]))
print()
print("Growth rate above 1.0 is sign of exponential growth, but also skewed by increased testing.")
print("World Growth rate:                     {0:.4}".format((conf_sum_dif[-1])/(conf_sum_dif[-2])))
print()
print()


# define report function
def report(country):
    # Create reusable series objects 
    country_conf_sum = conf_df.loc[:,'1/22/20':].loc[conf_df['Country/Region'] == country].sum()
    country_recv_sum = recv_df.loc[:,'1/22/20':].loc[conf_df['Country/Region'] == country].sum()
    country_death_sum = death_df.loc[:,'1/22/20':].loc[conf_df['Country/Region'] == country].sum()

    country_conf_sum_dif = difference(country_conf_sum, 1).values
    country_recv_sum_dif = difference(country_recv_sum, 1).values
    country_death_sum_dif = difference(country_death_sum, 1).values

    print()
    print('_'*50)
    print("Numbers for {} current as of {}".format(country, conf_df.columns[-1]))
    print()
    print("New cases:                          {}".format(country_conf_sum_dif[-1]))
    print("Total confirmed cases:             {}".format(country_conf_sum[-1]))
    print("New case rate:                        {0:2.3%}".format(country_conf_sum_dif[-1]/country_conf_sum[-1]))
    print("New Recovered cases:                 {}".format(country_recv_sum_dif[-1]))
    print("Total recovered cases:              {}".format(country_recv_sum[-1]))
    print("Recovery rate:                         {0:2.3%}".format(country_recv_sum_dif[-1]/country_recv_sum[-1]))
    print("New Deaths:                          {}".format(country_death_sum_dif[-1]))
    print("Total deaths:                       {}".format(country_death_sum[-1]))
    print("Death rate:                            {0:2.3%}".format(country_death_sum_dif[-1]/country_conf_sum[-1]))
    print()
    print("Growth rate:                           {0:.4}".format(country_conf_sum_dif[-1]/country_conf_sum_dif[-2]))
    print("_"*50)

#############

#dif_ = difference(conf_df.loc[:,'1/22/20':].sum(),1)
#print(dif_.rolling(7).mean())


# The lines below print the chronological sum from each source

# print(conf_sum)
# print(recv_sum)
# print(death_sum)


# Print a report for each country

for country in conf_df['Country/Region'].sort_values().unique():
    report(country)



# Report for individual countries
#report('US')
#report('Italy')
