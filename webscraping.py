# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"
# response = requests.get(url)
# html_content = response.content


# #listas com os títulos, as quantidades de estrelas e os tipos de livros

# soup = BeautifulSoup(html_content, "html.parser")

# titles = [title.text for title in soup.find_all("h3", class_="title")]
# star_ratings = [rating.attrs["class"][-1] for rating in soup.find_all("p", class_="star-rating")]
# genres = [genre.text.strip() for genre in soup.find_all("p", class_="genre")]

# for title, rating, genre in zip(titles, star_ratings, genres):
#     print(f"{title} ({genre}) - {rating}")

import requests
import re

response = requests.get('http://books.toscrape.com/')
content = response.content.decode('utf-8')

titles = re.findall(r'<h3><a.*?>(.*?)</a></h3>', content)
print(titles)

ratings = re.findall(r'<p class="star-rating (.*?)">', content)
print(ratings)

genres = re.findall(r'<a href=".*?/catalogue/category/books/(.*?)/index.html">(.*?)</a>', content)
print(genres)

#!pip install plotly pandas
#!pip install dash
#!pip install jupyter-dash

import requests
import re
import pandas as pd
import plotly.express as px
import dash
#from jupyter_dash import JupyterDash
from dash import  dash_table
from dash import html
from dash import dcc

print("Estou aqui 0")
response = requests.get('http://books.toscrape.com/')
content = response.content.decode('utf-8')
print("Estou aqui 1")
pattern = r'<h3><a.*?>(.*?)</a></h3>.*?<p class="star-rating (\w+)".*?<a href=".*?/catalogue/category/books/(.*?)/index.html">'
print("Estou aqui 2")
matches = re.findall(pattern, content, re.DOTALL)
print("Estou aqui 3")
titles = [match[0] for match in matches]
ratings = [match[1] for match in matches]
genres = [match[2] for match in matches]
print("Estou aqui 4")
data = {'Title': titles, 'Rating': ratings, 'Genre': genres}
df = pd.DataFrame(data)
print("Estou aqui 5")
genre_counts = df['Genre'].value_counts()
genre_counts_df = pd.DataFrame({'Genre': genre_counts.index, 'Count': genre_counts.values})
fig = px.bar(genre_counts_df, x='Genre', y='Count', labels={'x': 'Genre', 'y': 'Count'})
print("Estou aqui 6")
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('Book Catalog'),
    dcc.Graph(figure=fig),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    )
])

if __name__ == '__main__':
    app.run(debug=True)
