
from transformers import pipeline


sentiment_pipeline = pipeline("sentiment-analysis")

data = ['fuck you', "I love you", "you don't deserve anything", "Genuinely, Abrams is the stinkiest guy", "Why do viscous players do this?", "Seven is a menace", "Mcginnis is soooooo good in lane :("]


print(sentiment_pipeline(data))