let elements = document.querySelectorAll('.container .row .col-md-9');

for (let i = 0; i < elements.length; i++) {
    elements[i].classList.replace("col-md-9", "col-md-12")
}

elements = document.querySelectorAll('.container');
for (let i = 0; i < elements.length; i++) {
    console.log("CONTIANER", elements[i])
    elements[i].classList.replace("container", "container-fluid")
}