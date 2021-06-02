# The Broad Institute - DSP Engineering Interview

## MBTA Challenge

### Background
The MBTA serves as Boston's transportation system (http://mbta.com/) and has a website containing APIs for software engineers/developers to access transportation information [here](https://api-v3.mbta.com/docs/swagger/index.html).

### Coding Exercise Questions

## Question 1
````
Write a program that retrieves data representing all, what we'll call "subway" routes: "Light Rail" (type 0) and“Heavy Rail” (type 1). The program should list their “long names” on the console. Partial example of long name output: Red Line, Blue Line, Orange Line...There are two ways to filter results for subway-only routes. Think about the two options below and choose:
1. Download all results from https://api-v3.mbta.com/routes then filter locally
2. Rely on the server API (i.e., https://api-v3.mbta.com/routes?filter[type]=0,1) to filter before results are received. Please document your decision and your reasons for it.
````
