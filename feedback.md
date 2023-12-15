### Part 2 - Blog Post on Data Collection

*Mary Nydegger*: Good read and very clear and simply describes your analysis which is awesome. I liked how you showed the specific steps you did for each thing to gather and clean your data. I also liked how clear your ethical considerations section was. One recommendation would be to actually link your websites so people can click on them to take them somewhere. You can do that by typing this: [whatever words you want to link to the website](website url).

*Brady Heinig*: I thought this was really good, you went into great detail about the process of retrieving your data which helped me understand the thinking behind your project. I like that you defined different techniques and packages that you used, that piqued my interest and made me want to check those out. It would be helpful to see the page on KSL that you scraped, but other than that I think it was a well written post.

*Byron*: You could do a screenshot of your code if you wanted to get more into the details but other than that it looks great.

### Part 3 - Blog Post on EDA

*Brady Heinig*: I thought you included some really cool visualizations, specifically the candlestick bar plot. When analyzing some of the plots, it could be helpful to hypothesize why some towns had higher prices than others or why the houses are bigger (park city for example is a big ski town so it makes sense). Overall you did a good job explain the results of your charts.

*Byron*: It looked really good, super simple and clear. Nothing looked like it needed to be fixed and everything looks great

*Camilla*: I like all your graphics, they’re interesting. You explanations are clear and not too lengthy. The summary at the end was good, maybe add something more specific from your findings rather than generalizing. You could also hyperlink to your first post when you mention it at the beginning


### Part 4 - Streamlit App

*Mary Nydegger*: I really like how you had the filters on the side, and how your entire dashboard would update with those filters. I think that was the perfect approach for this kind of project in being able to view the data and distributions. I think this genuinely is a type of app that people would find helpful when looking for neighborhoods to fit their interests… whether they’re looking for houses available or certain styles or things. One thing someone recommended to me that also could be useful is adding a sentence or 2 with st.write() to each visualization to describe what you’re looking at and how the results apply. I think that would be more helpful for those who don’t have a technical background. 

*Ryan*: I spoke with Ryan in person and he asked about the number of homes for sale in each location. I did not have that chart added, so that could be something to include. He said the functionality looked great and overall was a solid app. 

*Brady Heinig*: I like that you can apply all of your filters from the side, it made it easy to adjust the graphs to what I wanted. Something that could be useful to add is when I select a county to look at, the select box for city would only include cities in that county. I don’t know utah super well so I sometimes would select cities in the wrong county. That could be a useful feature to add

*Jeffry Troll*: Hey Justin, I might sound repetitive but I also think that it needs more context, a brief explanation of the dashboard will be beneficial. Also, I don't know how important is to have those decimal points, it will remove it since it doesnt tell you more about the data with them. For the filter by price, usually, it is better to have categories like less than 400K or between 500k and 600k and so on. You could check Zillow and see how they do it.

### Changes

#### Ideas
I cycled through a few different ideas from analyzing sports betting to exploring differences between In-Season Tournament and Season stats for the NBA to eventually analyzing home prices. Home prices was something I was very curious about especially since the market has continued to rise consistently for some years now. I wanted to see the differences between cities and counties. 

#### Post on Data Collection
Based off of my feedback there wasn't much to change besides making my links accessible. I fixed that by linking KSL to the exact webpage that I pulled all my homes data from. Byron said it could be helpful to see the code for my data extraction, but the code is kind of long so I will leave it out. 

#### Post on EDA
The first piece of feedback I recieved told me to add some more written analysis below my graphs. I made sure to go through and add some more insights or reasons why the data looked the way it did. 

#### Streamlit App
Ryan said asked if I knew how many houses were for sale in each are so I made sure to add a counts chart at the bottom of the dashboard. I also received lots of feedback saying I could add in more context to the charts and the dashboard in general, so I included a statement at the beginning of the dashboard to explain what the dashboard was exploring. 

I was told it would be nice to adjust the price filter so that it wasn't a slider but rather something like zillow where you could choose a min and max that went up by increments of $50,000. I tried to implement this but it was more complex than I thought and I couldn't figure it out. 

Other things I did to improve my app included ordering the data in certain visuals so you could easily see the min and max. I also removed some huge outliers in some of the plots so that the data was more visible. The last thing I did was a map visualization so that I could put to use the lat and long coordinates that I worked so hard for haha. 
