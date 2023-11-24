from django.shortcuts import render, redirect
import os
import folium


# Create your views here.
def home(request):
    shp_dir = os.path.join(os.getcwd(), "media", "shp")
    # folium
    m = folium.Map(location=[21.752086, -82.843738], zoom_start=10)
    ## style
    style_provincia = {"fillColor": "#228B22", "color": "#228B22"}
    style_rio = {"color": "blue"}
    ## adding to view
    folium.GeoJson(
        os.path.join(shp_dir, "provincia.geojson"),
        name="Provincia",
        style_function=lambda x: style_provincia,
    ).add_to(m)
    folium.GeoJson(
        os.path.join(shp_dir, "rio.geojson"),
        name="Río",
        style_function=lambda x: style_rio,
    ).add_to(m)
    folium.LayerControl().add_to(m)
    ## exporting
    m = m._repr_html_()
    context = {"my_map": m}
    ## rendering
    return render(request, "geoApp/home.html", context)
