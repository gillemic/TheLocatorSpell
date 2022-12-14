// console.log(data[0]['activity_name'])

//let block = document.createElement('div');

//block.setAttribute('class', 'data_node')

//dataBlock.appendChild(block);

//dataBlock.innerHTML += "<h3>This is the text which has been inserted by JS</h3>";

function quickSearch() {
    let input, filter, events, h, text, others, otherText, show;
    input = document.getElementById('quickSearch');
    filter = input.value.toUpperCase();
    events = document.getElementsByClassName('event');

    for (const i in events) {
        show = false;
        h = events[i].getElementsByTagName("h1")[0];
        others = events[i].getElementsByTagName("p");

        console.log(others);

        text = h.textContent || h.innerText;
        if (text.toUpperCase().indexOf(filter) > -1) {
            // events[i].style.display = "";
            show = true;
        } else {
            // events[i].style.display = "none";
        }

        for (let j = 0; j < 3; j++) {
            otherText = others[j].textContent || others[j].innerText;
            console.log(otherText);
            if (otherText.toUpperCase().indexOf(filter) > -1) {
                // events[i].style.display = "";
                show = true;
            } else {
                // events[i].style.display = "none";
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

function mainSearch() {
    let name, location, disatnce, category, price, h, others, show, text;
    name = document.forms["main-form"]["activity"].value ?? '';
    location = document.forms["main-form"]["location"].value ?? '';
    distance = document.forms["main-form"]["withinRange"].value ?? '';
    category = document.forms["main-form"]["category"].value ?? '';
    price = document.forms["main-form"]["price"].value ?? '';

    events = document.getElementsByClassName('event');

    for (const i in events) {
        console.log(i);
    }

    return false;
}