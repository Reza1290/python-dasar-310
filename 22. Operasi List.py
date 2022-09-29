#counting sebuah list #
# > mencari ada berapa di list sebuah Entry

data_list = [1,2,8,7,7,5,6,4,8,5,1,2,6,3,4,8,7,5,6]

print(data_list.count(4))
print(data_list.count(7))
print(data_list.count(1))


# mencari di urutan keberapa entry itu
data_list_str = ["badut","boneka","random"] # 0 - 2

print("\n",data_list_str.index("boneka"))

# mengurutkan data dengan sort() sortir Tanpa def, data di sort maka diprint lagi udah jadi

data_list.sort()
print(data_list)

data_list_str.sort()
print(data_list_str)

#setelah di urutkan bisa dibalik urutannya reverse

data_list.reverse()
print(data_list)

data_list_str.reverse()
print(data_list_str)

