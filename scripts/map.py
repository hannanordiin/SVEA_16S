import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# skapa figur
fig = plt.figure(figsize=(8, 10))
ax = plt.axes(projection=ccrs.PlateCarree())

# zoom på södra Sverige
ax.set_extent([10, 22, 54, 60])

# snyggare färger
ax.add_feature(cfeature.LAND, facecolor='#e6f2e6')
ax.add_feature(cfeature.OCEAN, facecolor='#cce6ff')
ax.coastlines(resolution='10m')

# stationer (uppdaterade koordinater)
stations = {
    "ANHOLT": (12.1167, 56.6667),
    "SLÄGGÖ": (11.416, 58.283),
    "N14": (12.2300, 56.9200),
    "BY2": (14.1, 55.0),
    "BY5": (16.0, 55.3),
    "BY15": (20.0, 57.3),
    "BY20": (19.8667, 57.9333),
    "BY38": (17.6667, 57.1167),
    "REFM1V1": (16.24, 56.355),
    "Å17": (11.0, 58.5)
}

# plotta stationer + labels
for name, (lon, lat) in stations.items():
    ax.plot(lon, lat, 'o', color='darkred', markersize=6,
            transform=ccrs.PlateCarree())

    # vit bakgrund för vissa stationer
    if name in ["SLÄGGÖ", "REFM1V1"]:
        bbox_settings = dict(facecolor='white', alpha=0.8, edgecolor='none')
    else:
        bbox_settings = None

    if name == "N14":
        # ovanför höger
        ax.text(lon + 0.1, lat + 0.1, name,
                fontsize=8,
                fontweight='bold',
                bbox=bbox_settings,
                transform=ccrs.PlateCarree())

    elif name == "Å17":
        # vänster/övre vänster
        ax.text(lon - 0.15, lat + 0.05, name,
                fontsize=8,
                fontweight='bold',
                ha='right',
                va='bottom',
                bbox=bbox_settings,
                transform=ccrs.PlateCarree())

    else:
        # under punkten
        ax.text(lon, lat - 0.15, name,
                fontsize=8,
                fontweight='bold',
                ha='center',
                va='top',
                bbox=bbox_settings,
                transform=ccrs.PlateCarree())

# havsnamn (valfritt men snyggt)
ax.text(11, 57.5, "Kattegat", fontsize=10, alpha=0.6)
ax.text(12, 58.5, "Skagerrak", fontsize=10, alpha=0.6)
ax.text(17, 56.5, "Baltic Sea", fontsize=10, alpha=0.6)

# titel (valfri – kan tas bort)
# plt.title("Sampling stations")

# spara (PNG + PDF)
plt.savefig("figure_map_stations.png", dpi=300, bbox_inches='tight')
plt.savefig("figure_map_stations.pdf", bbox_inches='tight')

# visa
plt.show()
