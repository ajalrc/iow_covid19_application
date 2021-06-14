from django.shortcuts import render
import geopandas as gpd
import pandas as pd
import matplotlib
import io
from django.http import HttpResponse
matplotlib.use("Agg")
from django.shortcuts import render,redirect
import matplotlib.pyplot as plt
import urllib, base64

Location={'latitude':0,
    'longitude':1}

def confirmed_cases(request):
    
    if request.method=="POST":
        latitude=request.POST.get('latitude')
        print("the latitude is ",request.POST.get('latitude'))
        longtitude=request.POST.get('longitude')
        print("the longitude is ",request.POST.get('longitude'))
        Location['latitude']=latitude
        Location['longitude']=longtitude
        return confirmed_cases2(request,Location)
    else:
        return confirmed_cases2(request,Location)
    
    
    #Creating a dataframe to plot the points like a Marker

def confirmed_cases2(request,Location):
    print(Location['latitude'])
    print(Location['longitude'])
    df=pd.DataFrame(
    {
     'location':'My home',
     'Latitude':[Location['latitude']],
     'Longitude':[Location['longitude']]
     })
    
    gdf = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
    #Creating the map of Iowa using the shape file and reading the online infected
    #data in  geojson format
    iowa_cases= gpd.read_file('https://opendata.arcgis.com/datasets/6a84756c2e444a87828bb7ce699fdac6_0.geojson')
    county=iowa_cases[['Name','State','Confirmed']]

    combined=iowa_cases.merge(county, on="Name")
    fig, (ax1,ax2,ax3)=plt.subplots(3,figsize=(38,38),gridspec_kw={'hspace': 0.5})


    #Plotting the map and making the map a bit prettier
    combined.plot(
        column="Confirmed_x",
        ax=ax1,legend=True,
        cmap="OrRd",
        scheme="Quantiles")
    ax1.set_title("Total Confirmed Cases in Iowa", fontdict=
                {'fontsize':20}, pad=30)
    ax1.get_legend().set_bbox_to_anchor((1,1))
    

    ##################################

    county2=iowa_cases[['Name','State','Recovered']]

    combined2=iowa_cases.merge(county2, on="Name")


    #Plotting the map and making the map a bit prettier
    combined2.plot(
        column="Recovered_x",
        ax=ax2,legend=True,
        cmap="Blues",
        scheme="Quantiles")
    ax2.set_title("Total Recovered Cases in Iowa", fontdict=
                {'fontsize':20}, pad=30)
    ax2.get_legend().set_bbox_to_anchor((1,1))
    

    ####################################
    county3=iowa_cases[['Name','State','Deaths']]

    combined3=iowa_cases.merge(county3, on="Name")


    #Plotting the map and making the map a bit prettier
    combined3.plot(
        column="Deaths_x",
        ax=ax3,legend=True,
        cmap="Greens",
        scheme="Quantiles")
    ax3.set_title("Total Death Cases in Iowa", fontdict=
                {'fontsize':20}, pad=30)
    ax3.get_legend().set_bbox_to_anchor((1,1))
    
    
    if(Location['latitude']!=0):
         gdf.plot(ax=ax1, color="green",markersize=85)
         gdf.plot(ax=ax2, color="yellow",markersize=85)
         gdf.plot(ax=ax3, color="black",markersize=85)

    
    
    buf=io.BytesIO()
    fig.savefig(buf,format='jpg',dpi=500)
    buf.seek(0)
    string=base64.b64encode(buf.read())
    uri=urllib.parse.quote(string)
    
    #uri= plotly.offline.plot(fig, auto_open = False, output_type="div")
    return render(request, 'cases/index.html',{'data':uri})