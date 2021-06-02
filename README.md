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
**Answer to above:**
I would choose option 2, as using the server to filter results rather than filtering locally is more efficient. By filtering through the server, you greatly reduce the amount of information returned that is then used in a program. Having to download and parse a potentially large file is also tedious and time consuming, and should be avoided if possible.

## Question 2
````
Extend your program so it displays the following additional information.
1. The name of the subway route with the most stops as well as a count of its stops.
2. The name of the subway route with the fewest stops as well as a count of its stops.
3. A list of the stops that connect two or more subway routes along with the relevant route names foreach of those stops.
````
**Explanation of above:**
I first filtered a list of subway stops: https://api-v3.mbta.com/stops?filter[route_type]=0,1&include=route,parent_station. With this specific filter, I then used the known list of subway routes to tally frequency and get the total number of stops for each subway route. With this data, I then sorted the route counts in ascending order to then display the name of route with the greatest number of stops as well as the route with the least amount of stops. I was not able to get to the 3rd part of this question in the allotted time, but I would complete this step by finding an attribute/paramter that would give me the connections. I would then find the stops that had 2 or more connections and return a list of stops that fit these parameters.

## Question 3
````
Extend your program again such that the user can provide any two stops on the subway routes you listed forquestion 
1.List a rail route you could travel to get from one stop to the other. We will not evaluate your solution based upon the efficiency or cleverness of your route-finding solution. Pick a simple solution that answers thequestion. We will want you to understand and be able to explain how your algorithm performs.
Examples:
1. Davis to Kendall/MIT -> Red Line
2. Ashmont to Arlington -> Red Line, Green Line B
````
**Explanation of above:**
As of this writing this questions has not been fully completed. My logic behind this question is to ask for user input twice: one for the first stop and the second for the second stop. With this information, I would then use information for the first stop to parse through the API and find the first instance of that stop. Then, I would repeat these steps and get the first instance of the second stop to then create a potential rail route that could be used by the user. This solution does have flaws, such as a rail route not connecting directly (i.e. the Red Line to the Blue Line).
