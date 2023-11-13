let elements = document.querySelectorAll('.container .row .col-md-3');

for (let i = 0; i < elements.length; i++) {
    elements[i].style.display = 'none';
}

elements = document.querySelectorAll('.container .row .col-md-9');

for (let i = 0; i < elements.length; i++) {
    elements[i].classList.replace("col-md-9", "col-md-12")
}

let element = document.querySelector('#navbar-collapse');
if (element != null) {
    element.setAttribute('style', 'display: none !important')
}

