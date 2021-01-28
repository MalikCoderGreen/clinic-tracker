             
            //Create map options.
            var mapOptions = {
                center: ["{{latitude}}", "{{longitude}}"],
                zoom: 12
            }
            
            
            //Map object.
            var map = new L.map('map', mapOptions);
        
            //Create a layer object. 
            var layer = new L.TileLayer("http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png");
            
            //Add layer to the map. 
            map.addLayer(layer);
            
            var marker = L.marker([center[0], center[1]]).addTo(map);

            
            document.write(map.getCenter());
            document.write(center[0], center[1]);