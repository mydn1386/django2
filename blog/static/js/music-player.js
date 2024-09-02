document.addEventListener("DOMContentLoaded", function() {
    const audioPlayer = document.getElementById('audioPlayer');
    const progress = document.getElementById('progress');
    const bufferedBar = document.getElementById('buffered');
    const currentTimeElem = document.getElementById('currentTime');
    const durationTimeElem = document.getElementById('durationTime');
    const playPauseBtn = document.getElementById('playPauseBtn');
    const backwardButton = document.getElementById('backwardButton');
    const forwardButton = document.getElementById('forwardButton');
    const progressBar = document.getElementById('progressBar');
    const shareButton = document.getElementById('shareButton');

    let isReady = false;
    let desiredTime = null;

    const updatePlayPauseBtn = () => {
        playPauseBtn.innerHTML = audioPlayer.paused ? '<i class="fas fa-play"></i>' : '<i class="fas fa-pause"></i>';
    };

    const updateProgress = () => {
        const percent = (audioPlayer.currentTime / audioPlayer.duration) * 100;
        progress.style.width = isNaN(percent) ? '0%' : percent + '%';
        currentTimeElem.textContent = formatTime(audioPlayer.currentTime);
    };

    const updateBuffered = () => {
        const buffered = audioPlayer.buffered;
        if (buffered.length > 0) {
            const bufferedEnd = buffered.end(buffered.length - 1);
            const percentBuffered = (bufferedEnd / audioPlayer.duration) * 100;
            bufferedBar.style.width = isNaN(percentBuffered) ? '0%' : percentBuffered + '%';
        }
    };

    const setAudioCurrentTime = (changeInSeconds) => {
        if (isReady) {
            desiredTime = Math.min(Math.max(0, audioPlayer.currentTime + changeInSeconds), audioPlayer.duration);
            checkBufferedAndPlay(desiredTime);
        }
    };

    const checkBufferedAndPlay = (time) => {
        const buffered = audioPlayer.buffered;
        let isBuffered = false;

        for (let i = 0; i < buffered.length; i++) {
            const start = buffered.start(i);
            const end = buffered.end(i);
            if (time >= start && time <= end) {
                isBuffered = true;
                break;
            }
        }

        if (isBuffered) {
            audioPlayer.currentTime = time;
            audioPlayer.play();
        } else {
            console.log("این قسمت هنوز دانلود نشده است. منتظر بمانید تا دانلود شود.");
            audioPlayer.pause();
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
        if (isReady) {
            audioPlayer.paused ? audioPlayer.play() : audioPlayer.pause();
            updatePlayPauseBtn();
        }
    });

    backwardButton.addEventListener('click', () => setAudioCurrentTime(-5));
    forwardButton.addEventListener('click', () => setAudioCurrentTime(5));

    audioPlayer.addEventListener('timeupdate', updateProgress);
    audioPlayer.addEventListener('progress', updateBuffered);
    audioPlayer.addEventListener('loadedmetadata', () => {
        durationTimeElem.textContent = formatTime(audioPlayer.duration);
        isReady = true;
    });

    audioPlayer.addEventListener('canplay', () => {
        if (desiredTime !== null) {
            checkBufferedAndPlay(desiredTime);
            desiredTime = null;
        }
        isReady = true;
    });

    audioPlayer.addEventListener('playing', updatePlayPauseBtn);
    audioPlayer.addEventListener('pause', updatePlayPauseBtn);
    audioPlayer.addEventListener('ended', updatePlayPauseBtn);

    progressBar.addEventListener('click', (event) => {
        if (isReady) {
            const percent = (event.offsetX / progressBar.offsetWidth);
            const time = percent * audioPlayer.duration;
            checkBufferedAndPlay(time);
        }
    });

    audioPlayer.addEventListener('error', () => {
        console.error('Error occurred while trying to play the audio.');
    });

    shareButton.addEventListener('click', shareInTelegram);
});