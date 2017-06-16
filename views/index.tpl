<html>
    <head>
        <title>HRE Control</title>
        <link rel='stylesheet' type='text/css' href='/static/index_style.css'>
    </head>
    <body>
            <input type='range' id='fuel-slider' min='0' max='100'/>
            <div id='info-container'>
                <p id='actuator-speed-display'>NUMBERS</p>
                <p id='volume-output-display'>MILLILITERS</p>
                <p id='igniter-state-display'>IGNITER ON</p>
            </div>
            <button id='abort-button'><p id='abort-text'>ABORT</p></button>
            <button id='igniter-button'><p id='igniter-button-text'>IGNITE</p></button>
    </body>
</html>
