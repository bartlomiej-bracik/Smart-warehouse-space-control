from flask import Flask

app = Flask(__name__)

web = """
<!DOCTYPE html>
<html lang="el">

<head>
    <meta cahrset="UTF-8">
    <title>IPM Lab6</title>
</head>


<style>
    .imputClass:valid {
        border: 2px solid green;
    }
    .imputClass:invalid{
        border: 2px solid red;
    }
    table, th, td {
  border: 1px solid;
}

</style>


<body>

<p>Imię</p>
<input id="firstname" class="imputClass" pattern="^[A-Z][a-z]{1,29}$" placeholder="Bartek" required><br>

<p>Nazwisko</p>
<input id="lastname" class="imputClass" pattern="^[A-Z][a-z]{1,29}$" placeholder="Nowak" required><br>

<p>Nick</p>
<input id="nick" class="imputClass" pattern="^[A-Za-z0-9]+$" placeholder="Bartek" required><br>

<p>email</p>
<input type="email" class="imputClass" id="email" placeholder="abc@gmail" required><br>

<p>Kod pocztowy</p>
<input id="zip" class="imputClass" pattern="^[0-9]{2}-[0-9]{3}$" placeholder="26-200" required><br>

<p>Numer nip</p>
<input id="nip" class="imputClass" pattern="^[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}$" placeholder="022-41-11-111" required><br>

<p>Strona www</p>
<input id="www" class="imputClass" type="url" placeholder="https://www.abc.pl" required><br>

<p>Numer telefonu</p>
<input id="phone" class="imputClass" pattern="^[0-9]{9}$" placeholder="123456789"required><br>
<p>Adres Ipv4</p>
<input id="ipv4" class="imputClass" pattern="^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$" placeholder="203.0.113.12"required><br>

<p>Scieżka windows lowecase</p>
<input id="winpath1" class="imputClass" pattern="^[a-zA-Z]:\([a-z]*\\?)*$" placeholder="c:\windows\temp"required><br>

<p>Scieżka windows allcase</p>
<input id="winpath2" class="imputClass" pattern="^[A-Za-z]:\([A-Za-z]*\\?)*$" placeholder="C:\Windows\temp "required><br>

<p>Scieżka linux</p>
<input id="linuxpath" class="imputClass" pattern="^/etc/[^/]+$" placeholder="123456789"required><br><br>

<button id="generate" onclick=" Generuj()">Generuj</button>
<button id="add_data" onclick="DodajDane()">Dodaj</button>
<button id="save_data" onclick="Zapisz()">Zapisz</button>
<button id="load_data" onclick="Wczytaj()">Wczytaj</button>


<table id="clients_data_table">
    <thead>
       <tr>
          <th>Imię</th> <th>Nazwisko</th> <th>email</th> <th>Kod pocztowy</th> <th>nip</th> <th>telefon</th> <th>Akcje</th>
       </tr>
    </thead>
    <tbody id="clients_data_table_body">

    </tbody>

</table>





</body>

<script>
    var nr = 0;

    function Generuj(){
       
       
        const imie0 = ["Bartek","Jan","Anna","Piotr","Barbara"];
        const nazwisko0 = ["Nowak","Kowalski","Xksinski", "Mickiewicz","Sienkiewicz"];
        const email0 =["abc@gmail.com","kowlski@wp.pl","xyz@gmail.com","abc123@edu.p.lodz.pl","bs123@gmail.com"];
        const poczta0 = ["26-200","10-100","20-200","43-300","23-150","12-345"];
        const strona0 =["https://www.abc.pl","https://www.google.com","https://www.nowak.pl","https://www.edu.pl","https://www.barbara.pl"];
        const telefon0=["123456789","987654321","321321321","121212121","222333111"];
        const nip0 = ["022-411-11-11","363-261-27-91","156-844-74-17","942-351-15-34","343-893-78-16"];

        const nick0 =["bartek123","jan123","anna22","piotr01","barbara21"];
        const ipv40 =["203.0.113.12","10.0.0.1","172.16.0.1","192.168.1.100","224.0.0.1"];
        const winpath10 = ["c:\\windows\\temp","d:\\msdos","C:\\windows\\temp\\app","C:\\windows\\temp\\win","D:\\msdos\\temp"];
        const winpath20 =["C:\\Windows\\Temp","D:\\msdos","C:\\Windows\\Temp\\app","C:\\Windows\\Temp\\win","D:\\msdos\\Temp"];
        const linuxpath0 = ["/etc/passwd","/etc/hosts","/etc/hosts/temp","/etc/katalog","/etc/users"];
    

        if(nr < 4)
        {
            nr++;
        }
        else{
            nr = 0;
        }

        document.getElementById("firstname").value = imie0[nr];
        document.getElementById("lastname").value = nazwisko0[nr];
        document.getElementById("email").value = email0[nr];
        document.getElementById("zip").value = poczta0[nr];
        document.getElementById("www").value = strona0[nr];
        document.getElementById("nip").value = nip0[nr];
        document.getElementById("phone").value = telefon0[nr];
        document.getElementById("nick").value = nick0[nr];
        document.getElementById("ipv4").value = ipv40[nr];
        document.getElementById("winpath1").value = winpath10[nr];
        document.getElementById("winpath2").value = winpath20[nr];
        document.getElementById("linuxpath").value = linuxpath0[nr];
        
    }

    function DodajDane()
    {
        var imieValue = document.getElementById("firstname").value;
        var nazwiskoValue = document.getElementById("lastname").value;
        var emailValue = document.getElementById("email").value;
        var pocztaValue = document.getElementById("zip").value;
        var telefonValue= document.getElementById("phone").value;
        var nipValue = document.getElementById("nip").value;
       
       
       
       
        
        var table1 = document.getElementById("clients_data_table");
        const tbody = document.getElementById("");
        var wiersz = table1.insertRow();

        var komorka_imie = wiersz.insertCell(0);
        var komorka_nazwisko = wiersz.insertCell(1);
        var komorka_email = wiersz.insertCell(2);
        var komorka_poczta = wiersz.insertCell(3);
        var komorka_nip = wiersz.insertCell(4);
        var komorka_tel = wiersz.insertCell(5);
        var komurka_akcja = wiersz.insertCell(6)

        komorka_imie.innerHTML = imieValue;
        komorka_nazwisko.innerHTML = nazwiskoValue;
        komorka_email.innerHTML = emailValue;
        komorka_poczta.innerHTML = pocztaValue;
        komorka_nip.innerHTML = nipValue;
        komorka_tel.innerHTML = telefonValue;
        komurka_akcja.innerHTML = "<button class=\"delete_row\" onclick=\"UsunWiersz(this)\">Usuń</button> <button class=\"move_up\" onclick=\"przesun(this,-1)\">W górę</button> <button class=\"move_down\" onclick=\"przesun(this,1)\">W dół</button> "
        
    }

    function UsunWiersz(btn)
    {
        var rowDel = btn.parentNode.parentNode;
        rowDel.remove();
        
    }


    var data = [];

    function Zapisz()
    {
        PobierzDane();
        data_len = data.length;
        for(var i = 0; i < data_len; i++)
        {
            var data_to_add = data[i];
            ZapiszDane(data_to_add);
        }
        data = [];

    }
    function ZapiszDane(d)
    {
        // alert(d);
        //alert("Działa 1 ");
        let idb = indexedDB.open('mydbbb',1);
            idb.onupgradeneeded=()=>{
                let res = idb.result;
                res.createObjectStore('data',{autoIncrement:true});
               // alert("Działa 2 ");
            }
            idb.onsuccess=()=>{
                //alert("Sukces")
                let res = idb.result;
                let tx = res.transaction('data','readwrite');
                let store = tx.objectStore('data');
                //alert("Działa 3 ");
                store.add({
                    name: d[0],
                    surname: d[1],
                    email: d[2],
                    post: d[3],
                    nip: d[4],
                    phone: d[5]
                });
                
                

            }
    }

    function Wczytaj()
    {
        var body1 =document.getElementById("clients_data_table_body");
        body1.innerHTML="";

        let idb = indexedDB.open('mydbbb',1)
        idb.onupgradeneeded=()=>{
                let res = idb.result;
                res.createObjectStore('data',{autoIncrement:true});
               // alert("Działa 2 ");
            }
        idb.onsuccess=()=>{
            let res = idb.result;
            let tx = res.transaction('data','readonly');
            let store = tx.objectStore('data');
            let cursor = store.openCursor();
            cursor.onsuccess=()=>{
                let curRes = cursor.result;
                
                if(curRes)
                {
                 //   console.log(curRes.value.name);
                    body1.innerHTML +=`
                    <tr>
                        <td>${curRes.value.name}</td>
                        <td>${curRes.value.surname}</td>
                        <td>${curRes.value.email}</td>
                        <td>${curRes.value.post}</td>
                        <td>${curRes.value.nip}</td>
                        <td>${curRes.value.phone}</td>
                        <td> <button class="delete_row" onclick="UsunWiersz(this)">Usuń</button> <button class="move_up" onclick="przesun(this,-1)">W góre</button>  <button class="move_down" onclick="przesun(this,1)">W dół</button> </td>
                    </tr>
                    `;
                    curRes.continue();
                }
            }
        }    
    }


    function PobierzDane(){
    var table = document.getElementById('clients_data_table');
    for (var i = 1; i < table.rows.length; i++) {
        var row = table.rows[i];
        var rowData = [];
        for (var j = 0; j < row.cells.length; j++) {
            rowData.push(row.cells[j].innerText);
        }
        data.push(rowData);
        }
       // console.log(data);
    }




  function przesun(button,kierunek) {
  
  var wiersz = button.parentNode.parentNode; 
  var tabela = wiersz.parentNode; 
  var indeks = wiersz.rowIndex; 
 
  if ((kierunek === -1 && indeks > 1) || (kierunek === 1 && indeks < tabela.rows.length - 1)) {
    var docelowyIndeks = indeks + kierunek;
    var docelowyWiersz = tabela.rows[docelowyIndeks];
    }
  


    var kopiaWiersza = wiersz.cloneNode(true);

    for (var i = 0; i < wiersz.cells.length; i++) {
      var temp = wiersz.cells[i].innerHTML;
      wiersz.cells[i].innerHTML = docelowyWiersz.cells[i].innerHTML;
      docelowyWiersz.cells[i].innerHTML = temp;
    }

    wiersz.rowIndex = indeks + kierunek;
    docelowyWiersz.rowIndex = indeks;
  }
}

</script>

</html>


</html>


"""



@app.route('/')
def home():
    return web

@app.route('/about')
def about():
    return 'About'