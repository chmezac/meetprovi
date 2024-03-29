localStorage.removeItem('lugar');
$(document).ready(
    function cargar(){
        var xhttp = new XMLHttpRequest();
        var url = 'http://127.0.0.1:8000/api/lugares/';
    
        xhttp.onreadystatechange = function() {
            if( this.readyState == 4 && this.status == 200 ){
                var data = JSON.parse(this.responseText);
                var contador = 0;
                for (i = 0; i < data.count; i++) { 
                    if (!data.results[i].estado){
                        contador+=1;
                        $('#tableinfo').append(
                            '<tr>'+
                                '<th scope="row">'+contador+'</th>'+
                                '<td>'+data.results[i].nombre+'</td>'+
                                '<td>'+data.results[i].direccion+'</td>'+
                                '<td>'+data.results[i].comuna+'</td>'+
                                '<td><button type="button" class="btn btn-info" id="btnEdit" lugar="'+data.results[i].url+'" onclick="editar(this)">Editar</button></td>'+
                            '</tr>'
                        );
                    }
                }
            }
        }
        xhttp.open("GET", url, true);
        xhttp.send();
    },
);

function editar(elem){
    localStorage.setItem('lugar',$(elem).attr('lugar'))
    location.replace('../editar/')
}