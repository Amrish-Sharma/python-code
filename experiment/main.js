
function searchcustomer(tableName) {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    var count = 0;
    input = document.getElementById("keyword");
    //console.log(input);
    filter = input.value.toUpperCase();
    // console.log(filter);
    table = document.getElementById(tableName);
    // console.log(table);
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those which doesn't match the search query
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td")[0];
        if (td) {

            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                count = count + 1;
                tr[i].style.display = "";
            } else {
                tr[i].style.display = "none";
            }
        }
    }
    document.getElementById('count').innerHTML = count;
    console.log(count);
}



function exportToExcel(tableName, filename = '') {
    var downloadurl;
    var dataFileType = 'application/vnd.ms-excel';
    var tableSelect = document.getElementById(tableName);
    var tableHTMLData = tableSelect.outerHTML.replace(/ /g, '%20');

    // Specify file name
    filename = filename ? filename + '.xlsx' : 'export_excel_data.xlsx';

    // Create download link element
    downloadurl = document.createElement("a");

    document.body.appendChild(downloadurl);

    if (navigator.msSaveOrOpenBlob) {
        var blob = new Blob(['\ufeff', tableHTMLData], {
            type: dataFileType
        });
        navigator.msSaveOrOpenBlob(blob, filename);
    } else {
        // Create a link to the file
        downloadurl.href = 'data:' + dataFileType + ', ' + tableHTMLData;

        // Setting the file name
        downloadurl.download = filename;

        //triggering the function
        downloadurl.click();
    }
}
