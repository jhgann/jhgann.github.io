import math

# Coordinates in (longitude, latitude)
coords = [
    (7.072529, 51.493264),
    (7.072292, 51.493194),
    (7.072355, 51.493113),
    (7.072593, 51.493183),
    (7.072529, 51.493264),
]

# coords = [
#     (12.382663, 51.364215),
#     (12.382609, 51.364073),
#     (12.382749, 51.364052),
#     (12.382804, 51.364195),
#     (12.382663, 51.364215),
# ]

# coords = [
#     (7.558342, 51.430368),
#     (7.558201, 51.430216),
#     (7.55834, 51.430165),
#     (7.558487, 51.430316),
#     (7.558342, 51.430368),
# ]

# coords = [
#     (13.693258, 51.012643),
#     (13.693039, 51.012636),
#     (13.693048, 51.012534),
#     (13.693109, 51.012536),
#     (13.693111, 51.012523),
#     (13.693189, 51.012525),
#     (13.693188, 51.012538),
#     (13.693266, 51.012541),
#     (13.693258, 51.012643),
# ]
# Constants
lat_to_m = 111000
avg_lat = sum(lat for lon, lat in coords) / len(coords)
lon_to_m = 111000 * math.cos(math.radians(avg_lat))

# Convert to meters
coords_m = [(lon * lon_to_m, lat * lat_to_m) for lon, lat in coords]


# Calculate perimeter
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


perimeter = sum(
    distance(coords_m[i], coords_m[i + 1]) for i in range(len(coords_m) - 1)
)

# Calculate area using Shoelace formula
area = 0.5 * abs(
    sum(
        coords_m[i][0] * coords_m[i + 1][1] - coords_m[i][1] * coords_m[i + 1][0]
        for i in range(len(coords_m) - 1)
    )
)

print(f"Perimeter: {perimeter} meters")
print(f"Area: {area} square meters")
