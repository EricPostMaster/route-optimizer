# Creating a Route Optimizer for conducting health inspections efficiently

In 2014, I was working as a health inspector for the Salt Lake County Health Department.  I was in charge of managing inspections for hundreds of food establishments in my assigned area, and other than a CSV file export from our database, there was no standard tool for managing the workload.  It was a mess.  At the time, I didn’t know how to program, so I used Excel and macros to create a very basic tool for myself and my cubicle roommate to clean up our data and rank the inspections by due date.  That minimum viable product (MVP) was so helpful that I decided to continue developing it into something more robust.

Eventually I created a tool (still based in Excel) that would color code by inspection due date, clean street names and put them on a grid system using public street data, and allow the user to define a starting point and radius around which to sort results to better plan their inspection route and reduce waste.  I was proud of my work because it made my life easier as well as the co-workers that I shared it with.  Also, because it only required use of public street record information, it was completely free, which is always nice when working on a tight, taxpayer-funded budget.

Now that I know Python and have a much better understanding of data quality and management, I have decided to re-do this project.  I am making use of several tools I was not aware of (or that may not have existed) back in 2014.  A few major differences:
* I don't have to convert street names to the underlying grid coordinates (#hallelujah!). In the intiial version I had to manually add new streets when new real estate was developed and add them to the grid system. It was a tedious process that I didn’t have the skills to automate back then.
* I am using Google OR-tools to create a route optimizer. This will take the previous tool one step further to suggest the order in which the inspections should be conducted instead of just creating a cluster of inspections.
* Lastly, I would love to get the whole thing into an web app or other self-contained format so the end user can just see what they need instead of seeing all of the underlying data.  Ideally, I will connect it to Google Maps and actually plot a route for the end user.

As of the beginning of this project, this is the most uncertain part of the work for me.  I have some familiarity with RShiny, so even though I am going to be building this in Python, that experience will serve as a helpful base.  I think Plotly Dash and/or Flask will be the best tools for the final product.

If you've made it this far in the README document, thank you! :)
