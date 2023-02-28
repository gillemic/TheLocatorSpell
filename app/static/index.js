function quickSearch(query) {
    let input, filter, events, h, text, others, otherText, show, hits = 0;
    input = query
    filter = input.toUpperCase();
    events = document.getElementsByClassName('event');

    for (const i in events) {
        show = false;
        h = events[i].getElementsByTagName("h2")[0];
        others = events[i].getElementsByTagName("b");

        text = h.textContent || h.innerText;
        if (text.toUpperCase().indexOf(filter) > -1) {
            show = true;
        }

        for (let j = 0; j < 3; j++) {
            otherText = others[j].textContent || others[j].innerText;
            if (otherText.toUpperCase().indexOf(filter) > -1) {
                show = true;
            }
        }

        if (show) {
            events[i].style.display = "";
            hits++;
        }
        else {
            events[i].style.display = "none";
        }

        if (hits) {
            let results = document.getElementById('no-results');
            results.style.display = 'none';
        }
        else {
            let noResults = document.getElementById('no-results');
            noResults.style.display = 'block';
        }
    }
}

function advancedSearch() {
    let events, name, location, distance, type, localCheckbox, minorCheckbox, majorCheckbox, show, h, others, text, hits = 0;
    name = document.getElementById('activity').value ?? '';
    location = document.getElementById('location').value ?? '';
    distance = document.getElementById('withinRange').value ?? '';
    type = document.getElementById('type').value ?? '';
    localCheckbox = document.getElementById('localCheckbox').checked ?? false;
    minorCheckbox = document.getElementById('minorCheckbox').checked ?? false;
    majorCheckbox = document.getElementById('majorCheckbox').checked ?? false;
    price = document.getElementById('price').value ?? '';

    events = document.getElementsByClassName('event');

    for (const i in events) {
        show = true;

        h = events[i].getElementsByTagName("h2")[0];
        others = events[i].getElementsByTagName("b");

        // activity name
        if (name) {
            text = h.textContent || h.innerText;
            if (!(text.toUpperCase().indexOf(name.toUpperCase()) > -1)) {
                show = false;
            }
        }

        // location
        if (show && location) {
            text = others[0].textContent || others[0].innerText;
            if (!(text.toUpperCase().indexOf(location.toUpperCase()) > -1)) {
                show = false;
            }
        }
        
        if (show && type) {
            text = others[1].textContent || others[1].innerText;
            if (!(text.toUpperCase().indexOf(type.toUpperCase()) > -1)) {
                show = false;
            }
        }

        // checkboxes
        if (show && (localCheckbox || minorCheckbox || majorCheckbox)) {
            //todo
            const checkboxes = [];

            if (localCheckbox) {
                checkboxes.push('Local');
            }

            if (minorCheckbox) {
                checkboxes.push('Minor');
            }

            if (majorCheckbox) {
                checkboxes.push('Major');
            }

            text = others[2].textContent || others[2].innerText;
            if (!checkboxes.includes(text)) {
                show = false;
            }
        }

        // price
        if (show && price) {
            text = others[3].textContent || others[3].innerText;
            if (price < parseInt(text)) {
                show = false;
            }
        }

        if (show) {
            events[i].style.display = "";
            hits++;
        }
        else {
            events[i].style.display = "none";
        }

        if (!hits) {
            let noResults = document.getElementById('no-results');
            noResults.style.visibility = 'show';
        }
    }
}

function clearFields() {
    let events = document.getElementsByClassName('event');

    for (const i in events) {
        events[i].style.display = "";
    }
}

function hideSearch() {
    let form = document.getElementById('main-form');
    let hideButton = document.getElementById('hide-button');
    let showButton = document.getElementById('show-button');
    
    form.style.display = 'none';
    hideButton.style.display = 'none';
    showButton.style.display = 'block';
}

function showSearch() {
    let form = document.getElementById('main-form');
    let hideButton = document.getElementById('hide-button');
    let showButton = document.getElementById('show-button');
    
    form.style.display = 'block';
    hideButton.style.display = 'block';
    showButton.style.display = 'none';
}

function calcPrice(price) {
    if (price > 0) {
        return `$${price}`;
    }
    else {
        return 'Free';
    }
}

function eventsClickable() {
    // Get the modal
    // var modal = document.getElementById("myModal");

    // // Get the events
    // var events = document.getElementsByClassName("event");

    // // iterate through and make them clickable and bring up relevant info
    // for (let i in events) {
    //     events[i].onclick = function(){
    //         modal.style.display = "block";
            
    //         /*var children = events[i].getElementsByTagName('*');
    //         var arr =[];
    //         for (i = 0; i < children.length-1; i++){
    //             if(children[i].id){
    //                 arr.push(children[i].getAttribute("id"));
    //             } else if (children[i].className){
    //                 arr.push(children[i].getAttribute("class"));
    //             }
    //         }

    //         document.getElementById('myModal').innerHTML = arr; */
    //     } 
}

function hideModal() {

}

function showModal() {

}

var modal = document.getElementById("myModal");

// Get the events
var events = document.getElementsByClassName("event");

// iterate through and make them clickable and bring up relevant info
for (let i in events) {
    events[i].onclick = function(){
        modal.style.display = "block";
        
        // var children = events[i].children;
        // var arr =[];
        // for (i = 0; i < children.length-1; i++){
        //     if (children[i].innerHTML) {
        //         arr.push(children[i].innerHTML)
        //     }
        // }
        // arr.join('<br>')
        document.getElementById('modal-content').innerHTML = events[i].innerHTML; 
    }
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks on the modal itself, close the modal
modal.onclick = function() {
    modal.style.display = "none";
  }