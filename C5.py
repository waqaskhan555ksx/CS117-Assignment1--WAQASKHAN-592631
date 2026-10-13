#C5. Star-Delta (Y-Δ) Transformation
def star_to_delta(ra, rb, rc):
    n = ra * rb + rb * rc + rc * ra
    r_ab = n / rc
    r_bc = n / ra
    r_ca = n / rb
    return round(r_ab, 2), round(r_bc, 2), round(r_ca, 2)


print(star_to_delta(10, 20, 30))
