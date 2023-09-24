const TABLES = {
    'My Courses': ['Curso', 0],
    'My Course Disciplines': ['Disciplina', 5], 
    'My Discipline projects': ['projeto', 2],
    'My Beloved Teachers': ['Pessoa', 0],
}
const CLASS_BOX =  'item-box';
const CLASS_TITLE = 'item-box-title-text';
const TAG_TABLE = 'tbody';
const TAG_TABLE_ROW = 'tr'
const LEAD_TABLE = 'My Courses'
const NULL = 'null'

var boxes;

function getData(box){
    var title = box.getElementsByClassName(CLASS_TITLE);                    // find the title (identify the container)
    if (title.length == 0) return NULL;

    var data = box.getElementsByTagName(TAG_TABLE);                         // look for the data table
    if (data.length == 0) return NULL;

    var lines = data[0].getElementsByTagName(TAG_TABLE_ROW);                // get table rows
    if (lines.length == 0) return NULL;

    return [title[0].innerHTML, lines];

}

function filterTable(e, tableData, filterString) 
{
    for (var i = 0; i < boxes.length; i++){
        var data = getData(boxes[i]);
        if (data == NULL || data[0] == LEAD_TABLE) continue;            // skip main table

        var position = TABLES[data[0]][1];
        for (var j = 0; j < data[1].length; j++){                           // hide lines not matching filter
            var row = data[1][j];
            if (row.children[position].innerHTML == filterString){
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        }

    }
}


document.addEventListener('DOMContentLoaded', function() {
    boxes = document.getElementsByClassName(CLASS_BOX);                         // get table containers

    for (var i = 0; i < boxes.length; i++){                                     // cycle through containers
        var box = boxes[i];

        var title = box.getElementsByClassName(CLASS_TITLE);                    // find the title (identify the container)
        if (title.length == 0) continue;

        /*
        console.log(title[0].innerHTML, ' || ', title[0].innerText); 
        console.log(TABLES[title[0].innerHTML]);
        */

        var data = box.getElementsByTagName(TAG_TABLE);                         // look for the data table
        if (data.length == 0) continue;

        var lines = data[0].getElementsByTagName(TAG_TABLE_ROW);                // get table rows

        // go through table lines to set listeners
        for ( var i = 0; i < lines.length; i++){
            if (title[0].innerHTML != LEAD_TABLE){                              // Main table - never filter
                // set record selection listener
                /*
                lines[i].addEventListener('click', () => {
                    setLineSelected
                })*/
            } else {
                // set filtering listener
                lines[i].addEventListener('click', (e, data) => {               
                    //console.log('taget: ', e.target);
                    //console.log('taget: ', e.currentTarget);  //--> the line
                    var filterSting = e.currentTarget.children[0].innerHTML;

                    filterTable(e, data, filterSting);
                });
            }
        }






/*
        var filterString = data[0].children[0].innerHTML;

        // set filtering listener
        lines[i].addEventListener('click', 
            (e, data, filterString,  pos = TABLES[title[0].innerHTML][1]) => { 
                filterTable(data, filterString, pos);
            });

        
        
            // set listener (accountable for the filtering in other tables)

    } 
        /*else {
            // set clicked line as "selected"
            null;
        }*/


        

        /*filterTable(data, 'Licenciatura em Engenharia Informática', TABLES[title[0].innerHTML][1]);*/

    }

});



/***
    https://stackoverflow.com/questions/59054548/js-get-the-clicked-element-with-event-target
    
    div.addEventListener('click', (e) => {
        console.log(e.target) // the p that was clicked
        console.log(e.currentTarget) // this div
    })

 ***/

