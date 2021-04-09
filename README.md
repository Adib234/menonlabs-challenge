# Solution

- Connect to **a weather forecast API** to get your data!
  > We established a connection through our backend as this was a backend challenge and presented it in our frontend!

Here's how it looks like (a check means we intend not to see it)
![](res/2021-03-16-20-49-25.png)

- Create a **data visualization** (don't worry about making it pretty! A table, graph or any form of chart is fine!). Make sure users are able to **filter** through the data based on a parameter of your choice.
  > We create two data visualizations, one table which shows the current weather forecast and has checkboxes to filter the data. Our graph which shows a weather forecast has a dropdown menu to specifically choose what data you want.

Here's how it looks like!
![](res/2021-03-16-20-49-54.png)

# Challenges

- Figuring out a backend we could use and how we would go about dividing up the work according to our strengths

# Things we learned

## Adib

- Django requires a lot of setup so we ended up choosing FastAPI
- Learned how to create my own way to log requests to better debug
- Never ever mutate computed properties!
- To push to Docker Hub, first tag the local image to the repo created in docker hub, (getting the local image is `docker images`)
