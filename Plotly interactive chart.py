# 13. Plotly interactive chart
import plotly.express as px
df = px.data.gapminder().query("year==2007")
fig = px.scatter(df, x="gdpPercap", y="lifeExp", size="pop", color="continent")
fig.show()
