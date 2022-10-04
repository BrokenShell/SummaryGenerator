""" Summary Generator
Today's objective: Take a json file of descriptions and create a new json file of summaries.
- The output should have the same format as the input.
- We will not be using the pandas.
- Summary size should be 1-2 sentences.
"""
import json

from app.summary import summary

with open("descriptions.json", "r") as file:
    descriptions = json.load(file)

summaries = [{
    "Sign": obj["Sign"],
    "Summary": summary(obj["Description"], 0.17)
} for obj in descriptions]

with open("summaries.json", "w") as file:
    json.dump(summaries, file)

print("Number of sentences for each category summary:")
for summary in summaries:
    print(summary["Sign"], summary["Summary"].count("."))
