var map;

function initialize(mapID, coords)
{
    var mapCanvas = document.getElementById(mapID);
    var mapOptions = {
        center: new google.maps.LatLng(45.381,-71.92),
        zoom: 8,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(mapCanvas, mapOptions);

    addMarkerArray(coords);
}

function addMarker(info, lat, lng)
{
    /*var marker = new google.maps.Marker({
        position: new google.maps.LatLng(45.3818837,-71.923479321),
        map: map,
        title: "mDevs"
    });*/
    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(lat,lng),
        title: info,
        map: map
    });
}

function addMarkerArray(locations)
{
  for (i in locations) {
    addMarker(""+locations[i][0], locations[i][1], locations[i][2]);
  }
}