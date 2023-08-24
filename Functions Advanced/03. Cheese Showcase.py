def sorting_cheeses(**kwargs):
    result = ""
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for i in sorted_cheeses:
        result += i[0] + "\n"
        sorted_quantities = sorted(i[1], reverse=True)
        for j in sorted_quantities:
            result += str(j) + "\n"
    return result


print(
    sorting_cheeses(
    Parmesan =[102, 120, 135],
    Camembert=[100, 100, 105, 500, 430],
    Mozzarella=[50, 125]
 )
)

print(
    sorting_cheeses(
    Parmigiano=[165, 215],
    Feta=[150, 515],
    Brie=[150, 125]
 )
)
