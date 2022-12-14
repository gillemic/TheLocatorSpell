// console.log(data[0]['activity_name'])

//let block = document.createElement('div');

//block.setAttribute('class', 'data_node')

//dataBlock.appendChild(block);

//dataBlock.innerHTML += "<h3>This is the text which has been inserted by JS</h3>";

function quickSearch() {
    let input, filter, events, h, text, others, otherText;
    input = document.getElementById('quickSearch');
    filter = input.value.toUpperCase();
    events = document.getElementsByClassName('event');

    for (const i in events) {
        show = false;
        h = events[i].getElementsByTagName("h1")[0];
        others = events[i].getElementsByTagName("small");

        console.log(others);

        text = h.textContent || h.innerText;
        if (text.toUpperCase().indexOf(filter) > -1) {
            events[i].style.display = "";
        } else {
            events[i].style.display = "none";
        }

        /*for (const j in others) {
            otherText = others[j].textContent || others[j].innerText;
            console.log(otherText);
            if (otherText.toUpperCase().indexOf(filter) > -1) {
                events[i].style.display = "";
            } else {
                events[i].style.display = "none";
            }
        }*/
    }
}