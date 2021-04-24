function getlocation() {
    if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(success, failure)
            }
    else {
                alert("Geolocation is not supported in your browser")
            }
}


function success(position) {
    var values = position.coords
    console.log("Your location is ")
    console.log(`Latitude is ${values.latitude}`)
    console.log(`Longitude is ${values.longitude}`)
    datafile={
        'latitute':values.latitude,
        'longitude':values.longitude,
}
    const url = `https://www.latlong.net/c/?lat=${values.latitude}&long=${values.longitude}`
    //const url=`https://maps.google.com/?q=${values.latitude},${values.longitude}`
    document.querySelector('a').setAttribute('href', url)
    document.querySelector('div').style.display = "block";
    
    $(document).ready(function($){
        console.log("I am called the first time")
        var csrf=$("input[name=csrfmiddlewaretoken]").val();
        $("button").click(function(){
            console.log("I am called the first time222")
        $.ajax({
            url:'',
            type:'POST',
            data:{
                csrfmiddlewaretoken:csrf,
                latitude:values.latitude,
                longitude:values.longitude,
                
            },
            success:function(){
                alert("You will now be seen in the map"),
                location.reload(true);
                console.log("I was loaded")

            },
            error:function(){
                alert("Error")
            } 

            })
        })
    })
    
    
}
function failure() {
    console.log("It failed bro.")
}
        


/*
*/