const myTitle = document.getElementById('myTitle');
const myImage = document.getElementById('myImage');


let seizoenen = [

    {
        "title": "seIzoenen",
        "image": "img/seasons.jpg",
        "backGround": "blue"
    },

    {
        "title": "Spring",
        "image": "img/spring.jpg",
        "backGround": "yellow"
    },

    {
        "title": "Summer",
        "image": "img/summer.jpg",
        "backGround": "red"
    },

    {
        "title": "Winter",
        "image": "img/winter.jpg",
        "backGround": "white"
    },

    {
        "title": "Autumn",
        "image": "img/autumn.jpg",
        "backGround": "pink"
    },


]

/*let seizoen = {
    "title": "lente",
    "image": "img/spring.jpg"
};*/


function show(index) {

    myTitle.innerHTML = seizoenen[index].title;
    myImage.src = seizoenen[index].image;
    document.body.style.backgroundColor = seizoenen[index].backGround;

}