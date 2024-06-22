import math


total_items = int(input("Enter the size: "))   # 100  

data = list(range(1, total_items + 1))

page_size = int(input("Enter the page size: "))

page_number_start = int(input("Enter the page number: "))

total_pages = math.ceil(total_items / page_size)

start = (page_number_start - 1) * page_size 

end = start + page_size

specif_page = math.ceil(page_number_start / page_size)

page_data = data[start: end]



print("Total items:", total_items)
print("Total pages:", total_pages)
print("Start index:", start)
print("End index:", end)
print("page_content", page_data)

print("size for page : ",len(page_data))
