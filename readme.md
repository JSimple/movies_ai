# movies_ai is a twitterbot
She generates movie pitches and then tweets them via [this account](https://twitter.com/movies_ai).

# how does movies_ai work?
- It scrapes imdb loglines for tv shows and movies,
- extracts key phrases from these loglines,
- feeds random key phrases into a text generation prompt template,
- uses the resulting prompt to generate text via a GPT-2 model trained on movie summaries,
- posts the result to twitter.