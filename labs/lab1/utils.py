import glob
import os

import requests
import folium
from shapely.geometry import Point
from datetime import datetime
import polyline
import pandas as pd
import geopandas as gpd
import sys


def plot(plan, color='green'):
    """
    Plots the returned path in readable formand plots it on the map"""
    ret_str = "Trip from ({:.4f},{:.4f}) to ({:.4f},{:.4f}) at {}. \n{} connections found. \nBest one is {:.0f}min ({:.0f}m walk, {} transfer(s), wait time {:.2f}min)".format(
        plan['from']['lon'], plan['from']['lat'],
        plan['to']['lon'], plan['to']['lat'],
        plan['date'],
        len(plan['itineraries']),
        plan['itineraries'][0]['duration'] / 60,
        plan['itineraries'][0]['walkDistance'],
        plan['itineraries'][0]['transfers'],
        plan['itineraries'][0]['waitingTime'] / 60)

    print(ret_str)
    print()
    print("LEG \t MODE \tDIST \tTIME")
    print('-----------------------------')
    i = 1
    for leg in plan['itineraries'][0]['legs']:
        print("{}\t{}\t{:.0f}\t{:.0f}".format(i, leg['mode'], leg['distance'], leg['duration']))
        i += 1

    ret = list()
    tile = 'Stamen Toner'  # 'StamenTerrain'
    tile = "https://tile.thunderforest.com/transport/{z}/{x}/{y}.png?apikey=54d9f38859864044ae1906a121f1e942"
    markers = list()
    for leg in plan['itineraries'][0]['legs']:
        decoded = polyline.decode(leg['legGeometry']['points'])
        ret += decoded
        markers.append(decoded[0])
    points = folium.PolyLine(locations=ret, color=color, weight=5, opacity=0.6)

    # points = folium.features.GeoJson()
    CENTER = ((plan['from']['lat'] + plan['to']['lat']) / 2, (plan['from']['lon'] + plan['to']['lon']) / 2)
    map_osm = folium.Map(location=CENTER,
                         zoom_start=13, tiles=tile, attr="toner-bcg", control_scale=True)
    for marker in markers:
        folium.CircleMarker(marker, radius=5, color=color, opacity=0.7).add_to(map_osm)
    map_osm.add_child(points)
    return map_osm


def get_latest(path):
    """
    returns the id of the last succesffully queried requests
    useful to warm restart after server is down
    :param path:
    :return:
    """
    try:
        df = pd.read_csv(path, index_col=[0])  # load the csv
        return int(df[df.success].index.max()+1)  # last one with success
    except:
        return 0




def merge_batches(path, out_path, remove=True):
    """
    walks through directory and merges all csv files into one
    :param path:
    :param out_path:
    :param remove:
    :return: none
    """

    all_files = glob.glob(path + "/*.csv")
    df = pd.concat((pd.read_csv(f) for f in all_files), sort=False).set_index('id')
    df.to_csv(os.path.join(out_path))
    if remove:
        for f in all_files:
            os.remove(f)