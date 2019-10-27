// from data.js
var tableData = data;
var table = d3.select('tbody');
var columns = ['datetime',
'city',
'state',
'country',
'shape',
'durationMinutes',
'comments']

// Add data from the array to the html
var rows = table.selectAll('tr').data(tableData).enter().append('tr');

var cells = rows.selectAll("td").data(function(d){
    return columns.map(function(column)
    {
        return {column:column,value:d[column]}
    })
}).enter().append("td").text(function(d){
return d.value;
});

// check the input filter
function checkdata()
{
    var input = d3.select('#datetime');
//var inputElems = d3.selectAll("input");
//inputElems.on("change", inputChange);

    var input = d3.select("#datetime").property("value");
    var filtered = tableData.filter(function (a) { 
        return a.datetime === input });
    
console.log(filtered.length);
// rewtite the filtered content
var tbody = d3.select('tbody');

   
   tbody.selectAll("tr").remove()
   var rows = tbody.selectAll("tr")
    .data(filtered)
    .enter()
    .append("tr");

    var cells = rows.selectAll("td").data(function(d){
        return columns.map(function(column)
        {
            return {column:column,value:d[column]}
        })
    }).enter().append("td").text(function(d){
    return d.value;
    });
