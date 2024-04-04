<?php

// PHP code to send a handshake request to the Python middleware
$url = 'http://localhost:8000/query'; // Assuming the middleware is running on localhost:8000
$data = array('query' => 'SELECT * FROM users;');
$options = array(
    'http' => array(
        'header'  => "Content-Type: application/json\r\n",
        'method'  => 'POST',
        'content' => json_encode($data)
    )
);
$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);
if ($result === FALSE) {
    die('Error');
}
var_dump($result);
?>
