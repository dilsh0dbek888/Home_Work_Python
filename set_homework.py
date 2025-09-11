"""add() -- To‘plamga element qo‘shadi."""

s = {1, 2}
s.add(3)        # {1, 2, 3}
s.add(5)        # {1, 2, 3, 5}
s.add(2)        # {1, 2, 3, 5}

""" clear() -- To‘plamni butunlay bo‘shatadi. """


s = {1, 2, 3}
s.clear()
t = {"a", "b"}
t.clear()
x = set([4, 5])
x.clear()

"""copy() -  To‘plamning nusxasini qaytaradi."""

s = {1, 2, 3}
c = s.copy()
a = {"a", "b"}
b = a.copy()
nums = {10, 20}
dup = nums.copy()

"""difference() Birinchi to‘plamdagi, ikkinchisida bo‘lmagan elementlarni qaytaradi."""

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.difference(s2))
print(s2 - s1)
print({5, 6, 7} - {7})

"""difference_update() - Birinchi to‘plamdan, ikkinchisidagi elementlarni olib tashlaydi."""

s1 = {1, 2, 3}
s1.difference_update({2})
s2 = {4, 5, 6}
s2 -= {5}
s3 = {7, 8, 9}
s3.difference_update({7, 9})

"""discard()  -  Element bo‘lsa o‘chiradi, bo‘lmasa xato chiqarmaydi."""

s = {1, 2, 3}
s.discard(2)
s.discard(5)
s.discard(1)

"""intersection() - Ikki to‘plamning umumiy elementlarini qaytaradi."""

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.intersection(s2))
print({5, 6}.intersection({6, 7}))
print({"a", "b"}.intersection({"b", "c"}))

"""intersection_update() - Birinchi to‘plamni umumiy elementlar bilan yangilaydi."""

s1 = {1, 2, 3}
s1.intersection_update({2, 3, 4})
s2 = {5, 6}
s2.intersection_update({6, 7})
s3 = {"a", "b"}
s3.intersection_update({"b"})


"""isdisjoint() - Ikki to‘plamda umumiy element bormi, yo‘qmi (True/False)."""

print({1, 2}.isdisjoint({3, 4}))
print({1, 2}.isdisjoint({2, 3}))
print({"a"}.isdisjoint({"b"}))

"""issubset() - Birinchi to‘plam ikkinchisining ichida bo‘lsa True."""

print({1, 2}.issubset({1, 2, 3}))
print({1, 2}.issubset({1, 2, 3}) )
print({1, 2}.issubset({1, 2}))



"""issuperset() - Birinchi to‘plam ikkinchisini o‘z ichiga olsa True."""

print({1, 2, 3}.issuperset({2, 3}))
print({1, 2, 3}.issuperset({1, 2}) )
print({1, 2, 3}.issuperset({1, 2, 3}))



"""pop() -  To‘plamdan tasodifiy elementni olib tashlaydi."""

s = {1, 2, 3}
print(s.pop())
print(s)
t = {"a", "b"}
t.pop()
nums = {10}
nums.pop()



"""remove() - Elementni o‘chiradi (bo‘lmasa KeyError)."""

s = {1, 2, 3}
s.remove(2)

letters = {"a", "b"}
letters.remove("a")
nums = {10, 20}
nums.remove(20)



"""symmetric_difference() - Faqat birida bor, ikkinchisida yo‘q elementlarni qaytaradi."""

print({1, 2, 3}.symmetric_difference({3, 4, 5}))
print({"a", "b"}.symmetric_difference({"b", "c"}))
print({10, 20}.symmetric_difference({20, 30}) )



""""symmetric_difference_update()   - To‘plamni simmetrik farqlar bilan yangilaydi."""

s1 = {1, 2, 3}
s1.symmetric_difference_update({3, 4})
s2 = {"a", "b"}
s2.symmetric_difference_update({"b", "c"})
s3 = {10}
s3.symmetric_difference_update({10, 20})



"""union()  - To‘plamlarni birlashtiradi."""

print({1, 2}.union({2, 3}))
print({"a"}.union({"b", "c"}))
print({10} | {20}.union({30}))



"""update() - Birinchi to‘plamni boshqa to‘plam elementlari bilan to‘ldiradi."""

s1 = {1, 2}
s1.update({3, 4})
s2 = {"a"}
s2.update({"b", "c"} )
s3 = {10}
s3.update({20, 30})