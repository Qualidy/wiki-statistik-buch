<html><head><base href="https://example.com"><style>
    body {
        font-family: 'Segoe UI', Arial, sans-serif;
        background: #f5f7fa;
        padding: 2rem;
        color: #2c3e50;
    }
    .container {
        display: flex;
        flex-wrap: wrap;
        gap: 2rem;
    }
    .canvas-group {
        background: white;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 1.5rem;
        display: flex;
        align-items: start;
        transition: transform 0.2s;
    }
    .canvas-group:hover {
        transform: translateY(-5px);
    }
    canvas {
        border: 1px solid #e1e8ed;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .controls {
        display: flex;
        flex-direction: column;
        gap: 0.8rem;
        margin-bottom: 1rem;
    }
    .controls label {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        cursor: pointer;
        font-size: 0.9rem;
        color: #546e7a;
    }
    .controls input[type="checkbox"] {
        width: 18px;
        height: 18px;
        accent-color: #3498db;
    }
    .std-dev-box {
        border: 2px solid #3498db;
        border-radius: 0;
        margin: 1.5rem;
        background: rgba(52, 152, 219, 0.1);
        transition: all 0.3s ease;
    }
    .clear-points-btn {
        background: #e74c3c;
        color: white;
        border: none;
        padding: 12px 24px;
        font-size: 1rem;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s;
        margin-bottom: 2rem;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .clear-points-btn:hover {
        background: #c0392b;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    .stats {
        margin: 1rem 0;
        padding: 1rem;
        background: #f8f9fa;
        border-radius: 8px;
        font-size: 0.9rem;
        color: #546e7a;
        border-left: 4px solid #3498db;
    }
</style></head>
<body>
    <div class="container" id="container">
        <div class="canvas-group">
            <div>
                <div class="controls">
                    <label>
                        <input type="checkbox" class="show-lines"> Absolute Abstände anzeigen
                    </label>
                    <label>
                        <input type="checkbox" class="show-squares"> Quadrate anzeigen
                    </label>
                    <label>
                        <input type="checkbox" class="show-std-dev-lines"> Standardabweichungslinien anzeigen
                    </label>
                    <button class="clear-points-btn">Alle Punkte löschen</button>
                </div>
                <canvas width="800" height="600"></canvas>
                <div class="stats"></div>
            </div>
            <div class="std-dev-box"></div>
        </div>
    </div>

<script>
function initializeCanvas(canvasGroup) {
    const canvas = canvasGroup.querySelector('canvas');
    const ctx = canvas.getContext('2d');
    const showLinesCheckbox = canvasGroup.querySelector('.show-lines');
    const showSquaresCheckbox = canvasGroup.querySelector('.show-squares');
    const showStdDevLinesCheckbox = canvasGroup.querySelector('.show-std-dev-lines');
    const clearPointsBtn = canvasGroup.querySelector('.clear-points-btn');
    const stdDevBox = canvasGroup.querySelector('.std-dev-box');
    const statsDiv = canvasGroup.querySelector('.stats');

    let points = [];
    let draggedPoint = null;
    const pointRadius = 6;

    // Add initial 5 points
    const initialPoints = [
        {x: 100, y: 300},
        {x: 250, y: 200},
        {x: 400, y: 400},
        {x: 550, y: 150},
        {x: 700, y: 350}
    ];
    points = [...initialPoints];

    function drawPoint(x, y) {
        ctx.beginPath();
        ctx.arc(x, y, pointRadius, 0, Math.PI * 2);
        ctx.fillStyle = '#3498db';
        ctx.fill();
        ctx.strokeStyle = '#2980b9';
        ctx.lineWidth = 2;
        ctx.stroke();
        ctx.closePath();
    }

    function calculateMean() {
        if (points.length === 0) return null;
        return points.reduce((sum, point) => sum + point.y, 0) / points.length;
    }

    function calculateStdDev() {
        if (points.length < 2) return 0;
        const mean = calculateMean();
        const variance = points.reduce((sum, point) => {
            return sum + Math.pow(point.y - mean, 2);
        }, 0) / (points.length - 1);
        return Math.sqrt(variance);
    }

    function updateStdDevBox() {
        const stdDev = calculateStdDev();
        const size = Math.max(stdDev, 20);
        stdDevBox.style.width = size + 'px';
        stdDevBox.style.height = size + 'px';
    }

    function updateStats() {
        if (points.length === 0) {
            statsDiv.textContent = '';
            return;
        }

        const mean = calculateMean();
        const stdDev = calculateStdDev();
        const pointsWithinStdDev = points.filter(point =>
            Math.abs(point.y - mean) <= stdDev
        ).length;

        const percentage = ((pointsWithinStdDev / points.length) * 100).toFixed(1);

        statsDiv.innerHTML = `
            <strong>${pointsWithinStdDev}</strong> von <strong>${points.length}</strong> Werten liegen innerhalb einer Standardabweichung (<strong>${percentage}%</strong>)
        `;
    }

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        const mean = calculateMean();
        if (mean !== null) {
            // Draw mean line
            ctx.beginPath();
            ctx.moveTo(0, mean);
            ctx.lineTo(canvas.width, mean);
            ctx.strokeStyle = '#e74c3c';
            ctx.lineWidth = 2;
            ctx.stroke();

            // Draw standard deviation lines if enabled
            if (showStdDevLinesCheckbox.checked) {
                const stdDev = calculateStdDev();

                // Draw variance square on the mean line
                const squareSize = stdDev;
                const squareX = canvas.width - squareSize - 50; // Position from right
                ctx.strokeStyle = '#3498db';
                ctx.lineWidth = 2;
                ctx.strokeRect(squareX, mean - squareSize, squareSize, squareSize);
                ctx.fillStyle = 'rgba(52, 152, 219, 0.1)';
                ctx.fillRect(squareX, mean - squareSize, squareSize, squareSize);

                ctx.setLineDash([8, 4]);
                ctx.lineWidth = 1;

                // Upper std dev line
                ctx.beginPath();
                ctx.moveTo(0, mean - stdDev);
                ctx.lineTo(canvas.width, mean - stdDev);
                ctx.strokeStyle = '#9b59b6';
                ctx.stroke();

                // Lower std dev line
                ctx.beginPath();
                ctx.moveTo(0, mean + stdDev);
                ctx.lineTo(canvas.width, mean + stdDev);
                ctx.strokeStyle = '#9b59b6';
                ctx.stroke();

                ctx.setLineDash([]);
            }

            if (showLinesCheckbox.checked || showSquaresCheckbox.checked) {
                points.forEach(point => {
                    ctx.beginPath();
                    ctx.moveTo(point.x, point.y);
                    ctx.lineTo(point.x, mean);
                    ctx.strokeStyle = '#2ecc71';
                    ctx.lineWidth = 1;
                    ctx.stroke();

                    if (showSquaresCheckbox.checked) {
                        const height = Math.abs(point.y - mean);
                        ctx.strokeStyle = '#9b59b6';
                        ctx.strokeRect(point.x - height/2, Math.min(point.y, mean), height, height);
                    }
                });
            }
        }

        points.forEach(point => drawPoint(point.x, point.y));
        updateStdDevBox();
        updateStats();
    }

    canvas.addEventListener('mousedown', (e) => {
        const rect = canvas.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;

        if (e.button === 2) {
            points = points.filter(point =>
                Math.hypot(point.x - x, point.y - y) > pointRadius);
        } else {
            draggedPoint = points.find(point =>
                Math.hypot(point.x - x, point.y - y) < pointRadius);

            if (!draggedPoint) {
                points.push({x, y});
            }
        }
        draw();
    });

    canvas.addEventListener('mousemove', (e) => {
        if (draggedPoint) {
            const rect = canvas.getBoundingClientRect();
            draggedPoint.x = e.clientX - rect.left;
            draggedPoint.y = e.clientY - rect.top;
            draw();
        }
    });

    canvas.addEventListener('mouseup', () => {
        draggedPoint = null;
    });

    canvas.addEventListener('contextmenu', (e) => {
        e.preventDefault();
    });

    clearPointsBtn.addEventListener('click', () => {
        points = [];
        draw();
    });

    showLinesCheckbox.addEventListener('change', draw);
    showSquaresCheckbox.addEventListener('change', draw);
    showStdDevLinesCheckbox.addEventListener('change', draw);

    draw();
}

// Initialize the canvas
initializeCanvas(document.querySelector('.canvas-group'));
</script>
</body></html>
