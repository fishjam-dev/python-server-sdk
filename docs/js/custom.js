elements = document.querySelectorAll('.container .row .col-md-9');

for (let i = 0; i < elements.length; i++) {
    elements[i].classList.replace("col-md-9", "col-md-12")
}

