async function fetchData(url) {
    try {
        const res = await fetch(url);
        if (!res.ok) throw new Error(`Error al obtener ${url}: ${res.status}`);
        return await res.json();
    } catch (e) {
        console.error(e);
        return {}; // Devuelve objeto vacío si falla
    }
}

// Función para crear un gráfico seguro
function createChart(id, type, labels, datasets) {
    const ctx = document.getElementById(id);
    if (!ctx) {
        console.warn(`No se encontró canvas con id ${id}`);
        return;
    }
    new Chart(ctx, {
        type: type,
        data: { labels, datasets },
        options: {
            responsive: true,
            plugins: { legend: { display: true } },
            scales: {
                x: { title: { display: true, text: 'Fecha' } },
                y: { beginAtZero: true }
            }
        }
    });
}

// ---------------- ECONOMÍA ----------------
fetchData("../ECONOMIA/data/dolar.json").then(data => {
    const valor = data.dolar_oficial ? parseFloat(data.dolar_oficial.replace(',', '.')) : 0;
    createChart("chartEconomia", "line", [data.fecha || 'sin fecha'], [
        {
            label: 'Dólar Oficial',
            data: [valor],
            borderColor: 'blue',
            backgroundColor: 'rgba(0,0,255,0.1)',
            fill: true
        }
    ]);
});

// ---------------- POLÍTICA ----------------
fetchData("../POLITICA/data/boletin.json").then(data => {
    const cantidad = data.cantidad || 0;
    createChart("chartPolitica", "bar", [data.fecha || 'sin fecha'], [
        {
            label: 'Boletines publicados',
            data: [cantidad],
            backgroundColor: 'orange'
        }
    ]);
});

// ---------------- SOCIEDAD ----------------
fetchData("../SOCIEDAD/data/seguridad.json").then(data => {
    const alertas = data.alertas || 0;
    createChart("chartSociedad", "bar", [data.fecha || 'sin fecha'], [
        {
            label: 'Alertas de seguridad',
            data: [alertas],
            backgroundColor: 'red'
        }
    ]);
});

// ---------------- AMBIENTE ----------------
fetchData("../AMBIENTE/data/ambiente.json").then(data => {
    const aqi = data.aqi ? parseFloat(data.aqi) : 0;
    const alertas = data.alerta_ambiental ? 1 : 0;
    createChart("chartAmbiente", "line", [data.fecha || 'sin fecha'], [
        {
            label: 'AQI (Calidad del aire)',
            data: [aqi],
            borderColor: 'green',
            backgroundColor: 'rgba(0,255,0,0.1)',
            fill: true
        },
        {
            label: 'Alertas ambientales',
            data: [alertas],
            borderColor: 'purple',
            backgroundColor: 'rgba(128,0,128,0.1)',
            fill: true
        }
    ]);
});

// ---------------- CULTURA ----------------
fetchData("../CULTURA/data/agenda.json").then(data => {
    const eventos = data.eventos || 0;
    createChart("chartCultura", "bar", [data.fecha || 'sin fecha'], [
        {
            label: 'Eventos culturales',
            data: [eventos],
            backgroundColor: 'teal'
        }
    ]);
});
