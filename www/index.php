<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Recomendaciones - Peliculas</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
</head>

<body class="container">
    <h1>Pelicula API</h1>

    <?php
    $api_endpoint_movies = $_ENV["API_ENDPOINT"] ?: "http://localhost:5000/api/movies";
    $json_movies = @file_get_contents($api_endpoint_movies);

    if ($json_movies !== false) {
        $movies = json_decode($json_movies, true);

        if (is_array($movies) && !empty($movies)) {
            echo "<h2>Movies:</h2>";
            echo "<div class='table-responsive'>";
            echo "<table class='table table-bordered table-striped'>";
            echo "<thead><tr><th>Title</th><th>Genres</th></tr></thead>";
            echo "<tbody>";

            foreach ($movies as $movie) {
                echo "<tr>";
                echo "<td>{$movie['title']}</td>";
                echo "<td>{$movie['genres']}</td>";
                echo "</tr>";
            }

            echo "</tbody>";
            echo "</table>";
            echo "</div>";
        } else {
            echo "<p>Pelicula no encontrada</p>";
        }
    } else {
        $err_movies = "ERROR CON ENDPOINT: " . $api_endpoint_movies;
        echo "<p>Error API: {$err_movies}</p>";
    }
    ?>
</body>

</html>