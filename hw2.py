x =article = input("Введите газетную статью\n")
if "Styopa" in article:
    article2 = article.replace("Styopa", "Kirill")
    print(article2)
elif "Стёпа" in article:
    article2 = article.replace("Стёпа", "Кирилл")
    print(article2)
else:
    print("Стёпы здесь нет")
