from memcourt.heap import snapshot, diff

print("Taking snapshot A")
snap_a = snapshot("A")

a = []
b = a          # aliasing happens here

print("\nBefore mutation:")
print("a =", a)
print("b =", b)
print("a is b ->", a is b)

print("\nMutating a (a.append(10))")
a.append(10)

print("\nAfter mutation:")
print("a =", a)
print("b =", b)
print("a is b ->", a is b)

print("\nTaking snapshot B")
snap_b = snapshot("B")

print("\nSnapshot A:", snap_a.summary())
print("Snapshot B:", snap_b.summary())
print("Diff:", diff(snap_a, snap_b))

print
