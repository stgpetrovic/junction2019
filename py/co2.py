import product_metadata
import distance

# https://www.ecta.com/resources/Documents/Best%20Practices%20Guidelines/guideline_for_measuring_and_managing_co2.pdf
kg_co2_per_kg_km = { # mile to km, tonne to kg
    'road': 0.14645*0.621371/1000,
    'rail': 0.0242 *0.621371/1000,
    'maritime': 0.0603*0.621371/1000,
}

def mode_transport_heuristic(dist):
    if dist < 350:
        return 'road';
    elif dist < 800:
        return 'rail';
    elif dist < 1500:
        return 'road';
    else:
        return 'maritime'

def product_shipping_distance(p):
    return distance.finland_dist(p.country)

def emissions_g(p):
  d = product_shipping_distance(p)
  if not d:
      d = 50  # in-land, truck skladiste
  if p.weight == 0:
     p.weight = 0.16  # 16 deka, MOZE
  print("w=%s"%p.weight)
  print("d=%s"%d)
  emit = p.weight * d * kg_co2_per_kg_km[mode_transport_heuristic(d)] * 1000 # gram
  return emit
