<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css" type="text/css">

    <title>Document</title>
</head>

<body>

    <form action="site.php" method="POST">

        <div id="left">

            <div class="data_l">
                Ime i prezime
            </div>
            <div class="data_r">
                <input type="text" name="ime" class="input">
            </div>

            <div class="data_l">
                Autor
            </div>
            <div class="data_r">
                <input type="text" name="autor" class="input">
            </div>

            <div class="data_l">
                Naziv
            </div>
            <div class="data_r">
                <input type="text" name="naziv" class="input">
            </div>

        </div>

        <div id="right">

            <h3 class="zanr">Žanr:</h3>
            <input class="checkbox" type="checkbox" name="zanr[]" value="- Komedija">Komedija <br>
            <input class="checkbox" type="checkbox" name="zanr[]" value="- Ljubavni">Ljubavni <br>
            <input class="checkbox" type="checkbox" name="zanr[]" value="- Horor">Horor <br>

            <input id="button" type="submit" value="Pošalji">
            
        </div>

        </form>
    
    <div id="result">
            
    <?php
       
        if(isset($_POST["ime"])){
            echo "<br>Ime i prezime je: " . $_POST["ime"] . "<hr>";
        }
        if(isset($_POST["autor"])){
            echo "<br>Autor djela je: " . $_POST["autor"] . "<hr>";
        }
        if(isset($_POST["naziv"])){
            echo "<br>Naziv djela je: " . $_POST["naziv"] . "<hr>";
        }

        echo "<br>Djelo spada u žanrove:";
        if(isset($_POST["zanr"])){
            foreach($_POST["zanr"] as $nazivZanra){
                echo "<br>" . $nazivZanra;
            }
        }

    ?>

    </div>

</body>
</html>
    
    

     

     