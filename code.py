import json

def get_articles():
    with open("articles.Json", "r", encoding="utf-8") as file:
        json_file = json.load(file)


def save_articles(name, text):
    with open("articles.Json", "r", encoding="utf-8") as file:
        json_file = json.load(file)
    with open("articles.Json", "w", encoding="utf-8") as outfile:
        json_file[name] = text
        json.dump(json_file, outfile, ensure_ascii=False)


def delete_article(name):
    with open("articles.Json","r",encoding="utf-8") as file:
        json_file = json.load(file)
    del json_file[name]
    with open("articles.Json", "w", encoding="utf-8") as file:

        json.dump(json_file,file, ensure_ascii=False)


