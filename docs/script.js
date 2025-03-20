document.addEventListener("DOMContentLoaded", function () {
    fetch("../data/kohtulahendid.csv")
        .then(response => response.text())
        .then(data => {
            let rows = data.split("\n").map(row => row.split(","));
            let header = rows.shift(); // Eemaldab päise
            let yearIndex = header.indexOf("Aasta"); // Otsib veeru nime "Aasta"
            let countByYear = {};

            // Loeb lahendite arvu aastate lõikes
            rows.forEach(row => {
                let year = row[yearIndex];
                if (year) {
                    countByYear[year] = (countByYear[year] || 0) + 1;
                }
            });

            // Andmete teisendamine graafiku jaoks
            let labels = Object.keys(countByYear).sort();
            let values = labels.map(year => countByYear[year]);

            // Joonista graafik
            let ctx = document.getElementById("chart").getContext("2d");
            new Chart(ctx, {
                type: "bar",
                data: {
                    labels: labels,
                    datasets: [{
                        label: "Kohtulahendite arv aastate lõikes",
                        data: values,
                        backgroundColor: "rgba(75, 192, 192, 0.5)"
                    }]
                }
            });
        })
        .catch(error => console.error("Viga CSV laadimisel:", error));
});
