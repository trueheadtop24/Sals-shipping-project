weight = 9.2
ground_flat = 20.00

# Ground Shipping

if weight <= 2:
  ground_cost = 1.50
elif weight > 2 and weight <= 6:
  ground_cost = 3.00
elif weight > 6 and weight <= 10:
  ground_cost = 4.00 
else:
  ground_cost = 4.75

cost = weight * ground_cost + ground_flat
print("Ground Shipping price is","$"+"%.2f" % cost)

# Ground Shipping Premium

groundpre_flat = 125.00

# Drone Shipping 
drone_flat = 0.00

if weight <= 2:
  drone_cost = 4.50
elif weight > 2 and weight <= 6:
  drone_cost = 9.00
elif weight > 6 and weight <= 10:
  drone_cost = 12.00
else:
  drone_cost = 14.25

pre_cost = weight * ground_cost + groundpre_flat
droneship_cost = weight * drone_cost + drone_flat
print("Ground Shipping Premium price is", "$"+"%.2f" % pre_cost)
print("Drone Shipping price is","$"+"%.2f" % droneship_cost)


