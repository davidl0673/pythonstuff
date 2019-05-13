
let bt = document.querySelector('#bt');
bt.addEventListener('click', function() {
    alert('hello world!');
    let randomsites = [
        "https://old.reddit.com/r/gifs/",
        "https://www.youtube.com/",
        "https://www.cnn.com/",
        "https://www0.solarmovies.co/",
        "https://pythoncheatsheet.org/"
    ]
    
    let randomsite = randomsites[Math.floor(Math.random()*randomsites.length)];
    let pushbutton = document.getElementById ("pushy");
    // pushbutton.addEventListener("pushy", changePage());
        
    window.location.href = randomsite

});