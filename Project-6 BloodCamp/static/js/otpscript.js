let timeLeft = 300;
let countdownTimer = setInterval(function() {
    let minutes = Math.floor(timeLeft / 60);
    let seconds = timeLeft % 60;
    let formattedTime = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

    document.getElementById('timer').textContent = formattedTime;
    timeLeft--;
    if (timeLeft < 0) {
        clearInterval(countdownTimer);
        document.getElementById('timer').textContent = '00:00'; 
        alert('Countdown timer has ended!');
    }
}, 1000);