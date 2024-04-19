
// const test_div = document.getElementById('test'); 
// test_div.innerHTML = 'test ok'; 

// On initialise la latitude et la longitude de Paris (centre de la carte)
var lat = 45.64800;
var lon = 5.10220;
// Paris : 
// var lat = 48.852969;
// var lon = 2.349903;
var macarte = null;
// Fonction d'initialisation de la carte
function initMap() {
    // Créer l'objet "macarte" et l'insèrer dans l'élément HTML qui a l'ID "map"
    macarte = L.map('map').setView([lat, lon], 15);
    // macarte = L.map('map').setView([lat, lon], 11);
    // Leaflet ne récupère pas les cartes (tiles) sur un serveur par défaut. Nous devons lui préciser où nous souhaitons les récupérer. Ici, openstreetmap.fr
    L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
        // Il est toujours bien de laisser le lien vers la source des données
        attribution: 'données © <a href="//osm.org/copyright">OpenStreetMap</a>/ODbL - rendu <a href="//openstreetmap.fr">OSM France</a>',
        minZoom: 1,
        maxZoom: 20
    }).addTo(macarte); 
    // Nous ajoutons un marqueur
    var marker = L.marker([lat, lon]).addTo(macarte);
}
window.onload = function(){
    // Fonction d'initialisation qui s'exécute lorsque le DOM est chargé
    initMap(); 
}; 



/* 
<script>
    // ----  
    // let x = document.getElementById("demo"); 
    // function getLocation() {
    //     if (navigator.geolocation) {
    //         navigator.geolocation.getCurrentPosition(showPosition);
    //     } else {
    //         x.innerHTML = "Geolocation is not supported by this browser.";
    //     }
    // }
    // function showPosition(position) {
    //     let orig_lat = position.coords.latitude; 
    //     let orig_lng = position.coords.longitude; 
    //     x.innerHTML = "Latitude: " + orig_lat + 
    //     "<br>Longitude: " + orig_lng; 
    //     // x.innerHTML = "Latitude: " + position.coords.latitude + 
    //     // "<br>Longitude: " + position.coords.longitude; 
    // } 
    // getLocation() 
    // // showPosition() 

    // url : http://192.168.1.11:9000/home/ 

</script> 
*/ 

