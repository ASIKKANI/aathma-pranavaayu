async function fetchMetrics() {
    try {
        // Fetch from the live Render backend
        const response = await fetch('https://pranavaayu-backend-sgtm.onrender.com/metrics');
        const data = await response.json();
        updateUI(data);
    } catch (error) {
        console.error('Error fetching metrics:', error);
    }
}

function updateUI(data) {
    // Basic validation to prevent UI flicker with empty data
    if (!data || data.error || (data.AQI === "0" && data["PM2.5"] === "0")) {
        console.warn('Skipping UI update due to invalid or empty data');
        return;
    }
    // Update labels and values
    document.getElementById('aqi-val').textContent = data.AQI || '--';
    document.getElementById('pm1-val').textContent = data.PM1 || '--';
    document.getElementById('pm25-val').textContent = data["PM2.5"] || '--';
    document.getElementById('pm4-val').textContent = data.PM4 || '--';
    document.getElementById('pm10-val').textContent = data.PM10 || '--';
    document.getElementById('co2-val').textContent = data.CO2 || '--';
    document.getElementById('tvoc-val').textContent = data.TVOC || '--';
    document.getElementById('nox-val').textContent = data.NOx || '--';
    document.getElementById('temp-val').textContent = data.Temperature || '--';
    document.getElementById('hum-val').textContent = data.Humidity || '--';
    document.getElementById('humidity-hero').textContent = (data.Humidity || '0') + '%';

    // Update AQI Status and Gauge
    const aqi = parseInt(data.AQI) || 0;
    const statusElem = document.getElementById('aqi-status');
    const gaugeElem = document.getElementById('aqi-gauge');
    const heroTitle = document.getElementById('hero-title');
    const heroDesc = document.getElementById('hero-desc');

    const circumference = 283;
    const offset = circumference - (aqi / 500) * circumference; // Assuming 500 is max scale
    gaugeElem.style.strokeDashoffset = Math.max(0, offset);

    if (aqi <= 50) {
        statusElem.textContent = 'Good';
        statusElem.style.color = 'var(--status-good)';
        gaugeElem.style.stroke = 'var(--status-good)';
        heroTitle.textContent = 'Air quality is excellent today.';
        heroDesc.textContent = 'Your Pranavaayu system is operating at peak efficiency. Breathing is effortless.';
    } else if (aqi <= 100) {
        statusElem.textContent = 'Satisfactory';
        statusElem.style.color = 'var(--status-satisfactory)';
        gaugeElem.style.stroke = 'var(--status-satisfactory)';
        heroTitle.textContent = 'Air quality is moderate.';
        heroDesc.textContent = 'Pranavaayu is working to reduce allergens. Keep the windows closed for better results.';
    } else {
        statusElem.textContent = 'Poor';
        statusElem.style.color = 'var(--status-poor)';
        gaugeElem.style.stroke = 'var(--status-poor)';
        heroTitle.textContent = 'Air quality is poor.';
        heroDesc.textContent = 'Purifier is running at high speed to clear the air. Avoid outdoor activity.';
    }
}

// Initial fetch and set interval
fetchMetrics();
setInterval(fetchMetrics, 5000); // Update every 5 seconds for ultra-real-time sync
