function formBlock() {
    if (document.getElementById('f12').style.display == 'none') {
        document.getElementById('f12').style.display = 'block'
        window.scrollTo(0, document.body.scrollHeight);
    } else document.getElementById('f12').style.display = 'none'
}

function confirmF() {
    if (confirm("RLY?")) {
        alert("yes")
    } else {
        alert("no")
    }
}


