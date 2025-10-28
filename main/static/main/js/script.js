let menuToggler = document.getElementById("menuToggler");

menuToggler.addEventListener("click", function(){
    document.getElementById("menu").classList.toggle("active");
});

let themeLight = document.getElementById("themeLight");
let themeDark = document.getElementById("themeDark");

function enableDark() {
    document.body.classList.add("dark");
    localStorage.setItem("dark", "active");
}

function disableDark() {
    document.body.classList.remove("dark");
    localStorage.setItem("dark", "disabled");
}

let mode = localStorage.getItem("dark");

if (mode == "active") {
    enableDark();
}

themeLight.addEventListener("click", function(){
    enableDark();
});

themeDark.addEventListener("click", function(){
    disableDark();
});