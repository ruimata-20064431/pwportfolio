const TABLES = {    
    'My Courses'                : ['Curso', 0]          ,
    'My Course Disciplines'     : ['Disciplina', 5]     , 
    'My Discipline projects'    : ['projeto', 2]        ,
    'My Beloved Teachers'       : ['Pessoa', 0]         ,
}

const TABLE_DEFS                = [[], [5,[0, 0]], [2, [1,0]], [0, [1, 4]]];  // table relations info
const CLASS_BOX                 = 'item-box'            ;
const CLASS_TITLE               = 'item-box-title-text' ;
const TAG_TABLE                 = 'tbody'               ;
const TAG_TABLE_ROW             = 'tr'                  ;
const LEAD_TABLE                = 'My Courses'          ;
const TEACHER_TABLE             = 'My Beloved Teachers' ;
const TEACHER_TABLE_idx         = 3                     ;

const TEXT_COLOR                = '#5E639E'             ;
const TEXT_COLOR_SELECTED       = '#0014ff'             ;
const TEXT_FORMAT               = 'normal'              ;
const TEXT_FORMAT_SELECTED      = 'bold'                ;

const TEXT_STYLE_NORMAL_CLASS   = 'unselected-line'     ;
const TEXT_STYLE_SELECTED_CLASS = 'selected-line'       ;

const TABLE_ROW_VISIBLE         = 'table-row'           ;
const TABLE_ROW_INVISIBLE       = 'none'                ;

const NO_LINE_SELECTED          = -1                    ;
const FIRST_ELEMENT             = 0                     ;

const NULL                      = 'null'                ;

var boxes                                               ;                       // TBD in "DOMContentLoaded"
var tables                      = []                    ;                       // array of DataContainers class

// --- classes ---


class DataContainer {
    constructor(title, data, idx, selected = 0, filterColumn = 0){
        this.title = title                                      ;               // data table name ("title")
        this.data = data                                        ;               // a <tbody> element
        this.idx = idx                                          ;               // table relative sequence index
        this.filterColumn = filterColumn                        ;               // table column (String) identifying line relations
        this.selected = (data.length != NO_LINE_SELECTED) ? selected : 0 ;

        this.markSelected(this.selected);
    }

    markSelected(selected = this.selected){
        this.selected = selected;

        if (this.selected == -1) return;
        for (var i = 0; i < this.data.children.length; i++){
            this.data.children[i].classList.remove(TEXT_STYLE_SELECTED_CLASS);
            if (i == this.selected){
                this.data.children[i].classList.add(TEXT_STYLE_SELECTED_CLASS);
            }
        }
    }

    defVisibility(){
        var indexes = TABLE_DEFS[this.idx];
        var filterString = tables[indexes[1][0]].data.children[tables[indexes[1][0]].selected].children[indexes[1][1]].innerHTML;

        for (var i = 0; i < this.data.children.length; i++){
            this.data.children[i].style.display = TABLE_ROW_VISIBLE;

            if (this.idx != TEACHER_TABLE_idx) {
                if (this.data.children[i].children[indexes[0]].innerHTML != filterString  ){
                    this.data.children[i].style.display = TABLE_ROW_INVISIBLE;
                }
            } else {
                var newFilterString = filterString.split(',').map( (it) => it.trim() );
                if (!newFilterString.includes( this.data.children[i].children[indexes[0]].innerHTML)){
                    this.data.children[i].style.display = TABLE_ROW_INVISIBLE;
                }
            }
        }

        this.selected = this.isVisible(this.selected) ? this.selected : this.firstVisible(); 
        this.markSelected();
    }

    // update selected (index) for clicked line
    clicked(e){
        for (var i = 0; i < this.data.length; i++){
            if (this.data.children[i] == e.currentTarget){
                this.selected = i;
                return;
            }
        }
    }

    isVisible(pos){
        return this.data.children[pos].style.display != TABLE_ROW_INVISIBLE;
    }

    firstVisible(){
        for (var i = 0; i < this.data.children.length; i++){
            var result = this.isVisible(i);
            if (result){ 
                return i;
            }
        }
        return 0;
    }

    // return currently selected filter
    selectedFilter(pos = 0){
        return this.isVisible(pos) ? 
            this.data.children[this.selected].children[pos].innerHTML : 
            this.data.children[this.selected].children[this.firstVisible()].innerHTML ;
    }
}


// --- divs ---

function currentTableIndx(e){
    for (const table in tables)
        if (tables[table].data == e.currentTarget) return tables[table];
    return null;
}


function getData(box){
    var title = box.getElementsByClassName(CLASS_TITLE);                        // find the title (identify the container)
    if (title.length == 0) return NULL;

    var data = box.getElementsByTagName(TAG_TABLE);                             // look for the data table
    if (data.length == 0) return NULL;

    var lines = data[0].getElementsByTagName(TAG_TABLE_ROW);                    // get table rows
    if (lines.length == 0) return NULL;

    return [title[0].innerHTML, lines];

}

function filterTable(e, tableData, filterString) 
{
    for (var i = 0; i < boxes.length; i++){
        var data = getData(boxes[i]);
        if (data == NULL || data[0] == LEAD_TABLE) continue;                    // skip main table

        var position = TABLES[data[0]][1];
        for (var j = 0; j < data[1].length; j++){                               // hide lines not matching filter
            var row = data[1][j];
            if (row.children[position].innerHTML == filterString){
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        }
    }
}

// apply filter to remaining tables
function cascadeFilter(){
    for (var i = 1; i < tables.length; i++){                                    // skip main table
        tables[i].defVisibility();
    }
}

function detIndex(element){
    var parent = element.parentElement;
    for (var i = 0; i < parent.children.length; i++) if (parent.children[i] == element) return i;
    return -1
}

function clickLineEvent(e, title){
    var currTable = currentTableIndx(e);                                        // determine in which of the tables the user clickes
    var filterSting = e.target.parentElement.children[0].innerHTML;             // the relevant columnt of clicked line
    var title = e.currentTarget.parentElement.parentElement.parentElement.
        parentElement.getElementsByClassName(CLASS_TITLE)[0].innerHTML;         // the identification of the data block clicked
    var pos = detIndex (e.target.parentElement);                                // determine clicked element's position in data table
    currTable.markSelected(pos);
    cascadeFilter();                                                            // filter remainig
}


// --- listeners ---


document.addEventListener('DOMContentLoaded', function() {
    boxes = document.getElementsByClassName(CLASS_BOX);                         // get table containers

    for (var i = 0; i < boxes.length; i++){                                     // cycle through containers
        var box = boxes[i];

        var title = box.getElementsByClassName(CLASS_TITLE);                    // find the title (identify the container)
        if (title.length == 0) continue;

        var data = box.getElementsByTagName(TAG_TABLE);                         // look for the data table
        if (data.length == 0) continue;

        tables[i] = new DataContainer(title, data[0], i, FIRST_ELEMENT);        // array of table class objects

        data[0].addEventListener('click', (e) => {
            clickLineEvent(e , title);    
        });
    }
});



/***
    https://stackoverflow.com/questions/59054548/js-get-the-clicked-element-with-event-target
    
    div.addEventListener('click', (e) => {
        console.log(e.target) // the p that was clicked
        console.log(e.currentTarget) // this div
    })

 ***/

