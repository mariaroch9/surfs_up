# Overview of the analysis
## Background
W. Avy wants additional information about temperature trends before he decides whether opening the surf shop is a lucrative business idea. Therefore, he is keen to assess the temperature data for the months of June and December in Oahu. June and December are months of significance in terms of temperature since that’s when the seasons in Hawaii change.

## Process
In this analysis, I have used Python, Pandas functions and methods, and SQLAlchemy. I filtered the date column of the Measurements table in the database to retrieve all the temperatures for the months of June and December. I then converted those temperatures to a list, created a DataFrame from the list, and generated the summary statistics.
```

/Users/Rochelle/Desktop/Surfs_up/surfs_up/Screen Shot 2022-10-26 at 1.49.56 PM.png

```

# Results

## June Analysis
Looking at the 1700 data points for the month of June over the years, the mean temperature was approx. 75°. However, the mean being a measure of central tendency is not sufficient to give us an accurate picture of the temperatures for the month. Because the mean is drastically impacted by outliers. The std. deviation which determines the spread /distribution of the data from the mean is a more accurate measure. The std dev. for the month of June is 3.25 which signifies that approximately 99% of the data is within 3 std dev points from the mean. 

The maximum temperature was 85° whereas the minimum temperature was approximately 20° lower at 64°.


## December Analysis
Contrary to the popular belief that December will be chilly the analysis using approx. 1500 data points revealed that the mean for the month of December was just 3° lower than the mean temperature for the month of June. The std. deviation was a tad higher at 3.75. 

While the maximum temperatures were approximately the same, June had max temperatures of 85° and Dec recorded max temperatures of approximately 83°. Expectedly, the minimum temperatures for the month of December were much lower at 56°. 


# Summary 

Looking the temperature analysis reveals that the temperatures are approximately the same throughout the months of June and December. This is definitely good news for W.Avy! It seems like the surf and ice cream shop business is sustainable year-round.

Along with the temperature analysis, two additional queries that could deepen this insight are looking at the precipitation for the months of June and December and evaluating how many stations are there and generating a list and count of each station. Then conducting a temperature analysis on the stations could give a better understanding of the best station to set up the surf and ice cream shop. 

The most active station is USC00519281. The maximum temperature for the month of June is 82° and for December it is 79°. Whereas the minimum temperature for the month of June is 65° and for December it is 58°. Which is higher than the overall minimum temperatures when we consider all the stations. 

I would highly recommend that Mr. W. Avy sets up his shop at the most active station since it is ideal temperature-wise!


