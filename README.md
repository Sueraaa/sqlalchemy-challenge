# sqlalchemy-challenge

## Precipitation Analysis

- Design a query to retrieve the last 12 months of precipitation data and plot the results.
- Starting from the most recent data point in the database.
- Use Pandas Plotting with Matplotlib to plot the data.
- Use Pandas to print the summary statistics for the precipitation data.

## Station Analysis
- Design a query to calculate the total number of stations.
- Design a query to find the most active stations 
- Design a query to get the previous 12 months of temperature observation (TOBS) data.
- Plot the results as a histogram with bins=12.

## Design Your Climate App

- Design a Flask API based on the queries.
- List all the available routes.

 Start at the homepage,
   - /api/v1.0/precipitation
   - /api/v1.0/stations
   - /api/v1.0/tobs
   - /api/v1.0/<start>
   - /api/v1.0/<start>/<end>

## References
1. Used the scalars() function which returns the first value of the first result row. [scalars()]
(https://blog.miguelgrinberg.com/post/what-s-new-in-sqlalchemy-2-0#:~:text=scalars()%20returns%20a%20ScalarResult,of%20the%20first%20result%20row.)
2. func.min(), func.max(), and func.avg() to calculate the lowest, highest, and average temperature.
3. I have received support from support staff at ask BCS staff.
4. Menne, M.J., I. Durre, R.S. Vose, B.E. Gleason, and T.G. Houston, 2012: An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910, (https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml)

