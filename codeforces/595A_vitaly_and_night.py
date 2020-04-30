floors, flats = map(int, input().split())

flats_with_lights_on = 0

for floor in range(0, floors):
	lights = list(map(int, input().split()))

	for l in range(0, len(lights), 2):
		if lights[l] == 1 or lights[l+1] == 1:
			flats_with_lights_on += 1

print(flats_with_lights_on)