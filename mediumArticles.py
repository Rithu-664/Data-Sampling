from os import stat
import pandas as p
import plotly.figure_factory as pff
import statistics
import random

sampleData = []

df = p.read_csv('.\medium_data.csv')
readingTime = df["reading_time"].tolist()

mean = statistics.mean(readingTime)
print("Mean of the given data:",mean)

std = statistics.stdev(readingTime)
print("Standard deviation of the given data:",std)

def sampleDataAnalysis(count):
    for i in range(0,count):
        index = random.randint(0,len(readingTime))
        value = readingTime[index]
        sampleData.append(value)

    sdMean = statistics.mean(sampleData)
    print("Mean of the sample data:",sdMean)

    sd_std = statistics.stdev(sampleData)
    print("Standard deviation of the sample data:",sd_std)

    fig = pff.create_distplot([sampleData],["Sample Data"],show_hist=False)
    fig.show()

sampleDataAnalysis(30)
sampleDataAnalysis(100)

figure = pff.create_distplot([readingTime],["Reading Time"],show_hist=False)
figure.show()
