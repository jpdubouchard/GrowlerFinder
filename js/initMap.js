var map;
function initMap() 
{
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 48.517471, lng: -123.491598}, zoom: 11
    });
}