const data = fetch('./static/MOCK_DATA.json')
.then(response => {
    const fetched_data = response.json();
    console.log(fetched_data);
});

let dataBlock = document.getElementById('pageData');

// console.log(data[0]['activity_name'])

//let block = document.createElement('div');

//block.setAttribute('class', 'data_node')

//dataBlock.appendChild(block);

dataBlock.innerHTML += "<h3>This is the text which has been inserted by JS</h3>";