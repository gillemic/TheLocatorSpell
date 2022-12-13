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

    loop1:
    for (const i in events) {
        h = events[i].getElementsByTagName("h1")[0];
        others = events[i].getElementsByTagName("small");

        text = h.textContent || h.innerText;
        if (text.toUpperCase().indexOf(filter) > -1) {
            events[i].style.display = "";
            continue;
        } else {
            events[i].style.display = "none";
        }

        // loop2:
        // for (const j in others) {
        //     otherText = others[j].textContent || others[j].innerText;
        //     if (otherText.toUpperCase().indexOf(filter) > -1) {
        //         events[i].style.display = "";
        //     } else {
        //         events[i].style.display = "none";
        //     }
        // }
    }
}