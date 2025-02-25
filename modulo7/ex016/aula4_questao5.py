import csv

livros = [
    ["A Revolução dos Bichos", "George Orwell", "1945", "152"],
    ["1984", "George Orwell", "1949", "328"],
    ["As 5 Linguagens do Amor", "Gary Chapman", "1992", "208"],
    ["A Metamorfose", "Franz Kafka", "1915", "128"],
    ["O Poder do Hábito", "Charles Duhigg", "2012", "371"],
    ["A Sutil Arte de Ligar o F*da-se", "Mark Manson", "2016", "224"],
    ["Batman: O Cavaleiro das Trevas", "Frank Miller", "1986", "372"],
    ["The Martian", "Andy Weir", "2011", "369"],
    ["Project Hail Mary", "Andy Weir", "2021", "496"]
]

with open("meus_livros.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])

    for livro in livros:
        writer.writerow(livro)
print("Arquivo 'meus_livros.csv' criado com sucesso!")
