document.addEventListener("DOMContentLoaded", function() {
    const audioPlayer = document.getElementById('audioPlayer');
    const progress = document.getElementById('progress');
    const currentTimeElem = document.getElementById('currentTime');
    const durationTimeElem = document.getElementById('durationTime');
    const playPauseBtn = document.getElementById('playPauseBtn');
    const backwardButton = document.getElementById('backwardButton');
    const forwardButton = document.getElementById('forwardButton');
    const progressBar = document.getElementById('progressBar');
    const shareButton = document.getElementById('shareButton');

    let isReady = false; // برای بررسی این که موزیک آماده پخش است یا خیر

    const updatePlayPauseBtn = () => {
        playPauseBtn.innerHTML = audioPlayer.paused ? '<i class="fas fa-play"></i>' : '<i class="fas fa-pause"></i>';
    };

    const updateProgress = () => {
        const percent = (audioPlayer.currentTime / audioPlayer.duration) * 100;
        progress.style.width = isNaN(percent) ? '0%' : percent + '%';
        currentTimeElem.textContent = formatTime(audioPlayer.currentTime);
    };

    const setAudioCurrentTime = (changeInSeconds) => {
        // فقط زمانی که موزیک بارگذاری شده است و آماده است
        if (isReady) {
            audioPlayer.currentTime = Math.min(Math.max(0, audioPlayer.currentTime + changeInSeconds), audioPlayer.duration);
        }
    };

    const formatTime = (seconds) => {
        const minutes = Math.floor(seconds / 60);
        const secs = Math.floor(seconds % 60).toString().padStart(2, '0');
        return `${minutes}:${secs}`;
    };

    const shareInTelegram = () => {
        const url = window.location.href;
        const telegramUrl = `https://t.me/share/url?url=${encodeURIComponent(url)}`;
        window.open(telegramUrl, '_blank');
    };

    playPauseBtn.addEventListener('click', () => {
        audioPlayer.paused ? audioPlayer.play() : audioPlayer.pause();
        updatePlayPauseBtn();
    });

    // دکمه‌های عقب و جلو
    backwardButton.addEventListener('click', () => setAudioCurrentTime(-5));
    forwardButton.addEventListener('click', () => setAudioCurrentTime(5));

    audioPlayer.addEventListener('timeupdate', updateProgress);
    audioPlayer.addEventListener('loadedmetadata', () => {
        durationTimeElem.textContent = formatTime(audioPlayer.duration);
        isReady = true; // موزیک آماده پخش است
    });

    audioPlayer.addEventListener('canplay', () => {
        isReady = true; // موزیک اکنون آماده پخش است
    });

    audioPlayer.addEventListener('playing', updatePlayPauseBtn);
    audioPlayer.addEventListener('pause', updatePlayPauseBtn);
    audioPlayer.addEventListener('ended', () => {
        updatePlayPauseBtn();
    });

    progressBar.addEventListener('click', (event) => {
        if (isReady) {
            const percent = (event.offsetX / progressBar.offsetWidth);
            audioPlayer.currentTime = percent * audioPlayer.duration;
        }
    });

    audioPlayer.addEventListener('error', () => {
        console.error('Error occurred while trying to play the audio.');
    });

    shareButton.addEventListener('click', shareInTelegram);
});