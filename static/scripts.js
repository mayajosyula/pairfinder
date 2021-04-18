$(document).ready(function () {
    var counter = 3;
    var rowcounter = 2;

    $("#addrow").on("click", function () {
       var len = $("#myTable").find("tr:first td").length;
       var newRow = $("<tr>");
       var cols = "";
       cols += '<td style="width:75px"><button type="button" class = "button del" id="delete">Delete</button></td>';
       cols += '<td><input type="text" placeholder="Name" name="row ' + rowcounter + '" style="width:150px"/></td>';
       for(let v=2; v < len; v++) {
        var colval = v - 1
        cols += '<td><input type="checkbox" name="row ' + rowcounter + '" value="' + rowcounter + '-' + colval + '"></td>';
       }
       cols += '</tr>';
       newRow.append(cols);
       $("#myTable").append(newRow);
       rowcounter++; 
    });

    $("#addcol").on("click", function () {
        var len = $("#myTable tr").length;
        var done = false;
        var rowval = 1; 
        $("#myTable").find('tr').each(function() {
          var trow = $(this);
          if (!done && trow.index() === 0) {
            trow.append('<td><input type="text" style="width:75px" placeholder="Pref ' + counter + '"/></td>');
            done = true;
          } else if (trow.index() >= 0 && trow.index() < len-1) {
            trow.append('<td><input type="checkbox" name="row ' + rowval + '" value="' + rowval + '-' + counter + '"/></td>');
            rowval++;
          }
        });
        counter++; 
    });


    $("#myTable").on("click", "#delete", function () {   
        $(this).closest('tr').remove();
    });

    /*$('.custom-file-input').on('change',function(){
    var fileName = $(this).val();
    fileName = fileName.split('\\').pop().split('/').pop();
    document.getElementById('custom-file-label').innerHTML = fileName;

})*/


});