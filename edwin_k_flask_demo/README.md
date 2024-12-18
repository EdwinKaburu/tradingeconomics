## Geography Finance Selector Demo
- Below are screenshot of the demo. The User interaction comprises of selecting individual countries to retrieve indicators information, which shall be displayed on the right most column alongside the global credit ratings.
 - Prior to this you would need to enter your api key to fetch such information. Though not required to interact with the mapping interface.
 
 This is python flask project for back end server processing. Most of implementation will be in the front end section.
 The geojson dataset can be found in the **~/finance_flask_demo/static** folder and was sourced and cleaned from [1][2].
 Leaflet library is employed for the cartography [3]. 

*Default User Interface View*
![](https://github.com/EdwinKaburu/tradingeconomics/blob/master/edwin_k_flask_demo/Screen_Img1.png)
*Selected Country View*
![](https://github.com/EdwinKaburu/tradingeconomics/blob/master/edwin_k_flask_demo/Screen_Img2.png)
 
 ### References
1. https://osm-countries-geojson.monicz.dev/
2. https://wiki.openstreetmap.org/wiki/GeoJSON
3. https://leafletjs.com/
