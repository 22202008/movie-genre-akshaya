
function predictGenre() {
    const plotSummary = document.getElementById('plotSummary').value;

    // Simple validation
    if (!plotSummary) {
        alert('Please enter a plot summary');
        return;
    }

    // Send the plot summary to the server for prediction
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ plotSummary }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `Predicted Genre: ${data.genre}`;
    })
    .catch(error => console.error('Error:', error));
}
