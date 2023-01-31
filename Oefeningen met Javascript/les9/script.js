const myTitle = document.getElementById("myTitle");
const myImage = document.getElementById("myImage");
const myInput = document.getElementById("myInput");

let = lokaties = [
    {
        "titel": "plaats0",
        "image": "img/0.jpg"
    },

    {
        "titel": "plaats1",
        "image": "img/1.jpg"
    },

    {
        "titel": "plaats2",
        "image": "img/2.jpg"
    },

    {
        "titel": "plaats3",
        "image": "img/3.jpg"
    },

    {
        "titel": "plaats4",
        "image": "img/4.jpg"
    },

    {
        "titel": "plaats5",
        "image": "img/5.jpg"
    },


    {
        "titel": "plaats6",
        "image": "img/6.jpg"
    },


    {
        "titel": "plaats7",
        "image": "img/7.jpg"
    },

    {
        "titel": "plaats8",
        "image": "img/8.jpg"
    },

    {
        "titel": "plaats9",
        "image": "img/9.jpg"
    },

    {
        "titel": "plaats10",
        "image": "img/10.jpg"
    },

    {
        "titel": "plaats11",
        "image": "img/11.jpg"
    },

]
myTitle.innerHTML = "Dit is door het script ";
/*myImage.src = "img/1.jpg";*/

function show(index) {
    myTitle.innerHTML = lokaties[index].titel;
    myImage.src = lokaties[index].image;
}

function getInput() {
    show(myInput.value)
    console.log(myInput.value);
}
