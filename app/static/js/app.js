async function checkHealth() {

    const button = document.querySelector("button");

    button.innerHTML = "Checking...";

    const start = performance.now();

    try {

        const response = await fetch("/health");

        const data = await response.json();

        const end = performance.now();

        document.getElementById("api").innerHTML =
            "🟢 " + data.status;

        document.getElementById("db").innerHTML =
            "🟢 " + data.database;

        document.getElementById("redis").innerHTML =
            "🟢 " + data.redis;

        document.getElementById("environment").innerHTML =
            data.environment;

        document.getElementById("version").innerHTML =
            data.version;

        document.getElementById("checked").innerHTML =
            new Date().toLocaleTimeString();

        document.getElementById("server").innerHTML =
            data.server_time;

        document.getElementById("response").innerHTML =
            Math.round(end - start) + " ms";

        button.innerHTML = "Refresh Health";

    } catch (err) {

        button.innerHTML = "Failed";

        console.log(err);

    }

}

checkHealth();

setInterval(checkHealth,30000);