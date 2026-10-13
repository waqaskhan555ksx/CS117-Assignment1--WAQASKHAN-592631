#C4. Loaded Voltage Divider
def loaded_divider(vs, r1, r2, rl):
    r_parallel = (r2 * rl) / (r2 + rl)
    unloaded = vs * r2 / (r1 + r2)
    loaded = vs * r_parallel / (r1 + r_parallel)
    return unloaded, loaded


print(loaded_divider(12, 1000, 1000, 500))

unloaded, loaded = loaded_divider(12, 1000, 1000, 500)
print("Unloaded voltage:", unloaded, "V")
print("Loaded voltage:", loaded, "V")
