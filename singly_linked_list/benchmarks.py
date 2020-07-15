import time
from singly_linked_list import LinkedList

n = 400000

l = [i for i in range(n)]

ll = LinkedList()

for i in range(n):
    ll.add_to_tail(i)


for i in range(n):
    ll.add_to_tail(i)

start_time = time.time()
for i in range(n):
    ll.remove_head()
end_time = time.time()
print(f"Linked list remove head took {end_time - start_time}")

start_time = time.time()
for i in range(n):
    l.pop(0)
end_time = time.time()
print(f"array list remove head took {end_time - start_time}")
