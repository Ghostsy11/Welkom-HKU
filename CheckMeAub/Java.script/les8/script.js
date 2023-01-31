console.log("Script is geladen");

const groentevak = document.getElementById('groenten');
const fruitval = document.getElementById("fruit");


function zetInFruitLa(fruit) {
    console.log(fruit);

    const nieuwElement = document.createElement('h2');
    nieuwElement.innerHTML = fruit;
    nieuwElement.className = 'rood'
    fruitval.appendChild(nieuwElement);


}


function zetInGroentenLa(groenten) {
    console.log(groenten);


    const NieuwElement = document.createElement('h2');
    NieuwElement.innerHTML = groenten;
    NieuwElement.className = 'rood'
    groentevak.appendChild(NieuwElement);
}