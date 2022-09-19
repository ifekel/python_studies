alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# This will give a keyError
# print(alien_0['strength'])

earned_points = alien_0['points']
print(f"You've earned '{earned_points}' points")

print(f"The color of the alien is '{alien_0['color'].title()}'")

# Modifying the alien value
new_color = alien_0['color'] = 'yellow'
print(f"The color of the alien is now '{alien_0['color'].title()}'")
