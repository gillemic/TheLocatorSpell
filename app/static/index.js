function quickSearch() {
    let input, filter, events, h, text, others, otherText, show;
    input = document.getElementById('quickSearch');
    filter = input.value.toUpperCase();
    events = document.getElementsByClassName('event');

    for (const i in events) {
        show = false;
        h = events[i].getElementsByTagName("h1")[0];
        others = events[i].getElementsByTagName("b");

        console.log(others);

        text = h.textContent || h.innerText;
        if (text.toUpperCase().indexOf(filter) > -1) {
            show = true;
        }

        for (let j = 0; j < 3; j++) {
            otherText = others[j].textContent || others[j].innerText;
            console.log(otherText);
            if (otherText.toUpperCase().indexOf(filter) > -1) {
                show = true;
            }
        }

        if (show) {
            events[i].style.display = "";
        }
        else {
            events[i].style.display = "none";
        }
    }
}

function advancedSearch() {
    let name, location, distance, localCheckbox, minorCheckbox, majorCheckbox;
    name = document.getElementById('activity').value ?? '';
    location = document.getElementById('location').value ?? '';
    distance = document.getElementById('withinRange').value ?? '';
    localCheckbox = document.getElementById('localCheckbox').checked ?? false;
    minorCheckbox = document.getElementById('minorCheckbox').checked ?? false;
    majorCheckbox = document.getElementById('majorCheckbox').checked ?? false;
    price = document.getElementById('price').value ?? '';

    events = document.getElementsByClassName('event');

    console.log(`${name}, ${location}, ${distance}, ${localCheckbox}, ${minorCheckbox}, ${majorCheckbox}, ${price}`);
}