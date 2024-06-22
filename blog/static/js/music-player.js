document.addEventListener("DOMContentLoaded", function() {
    // عناصر مورد نیاز را انتخاب کنید
    var audioPlayer = document.getElementById('audioPlayer');
    var progress = document.getElementById('progress');
    var progressBar = document.getElementById('progressBar');
    var currentTimeElem = document.getElementById('currentTime');
    var durationTimeElem = document.getElementById('durationTime');
    var playPauseBtn = document.getElementById('playPauseBtn');
    var backwardButton = document.getElementById('backwardButton');
    var forwardButton = document.getElementById('forwardButton');
    var shareButton = document.getElementById('shareButton');

    // پخش و توقف صدا
    playPauseBtn.addEventListener('click', function() {
        if (audioPlayer.paused || audioPlayer.ended) {
            audioPlayer.play();
            playPauseBtn.innerHTML = '<i class="fas fa-pause"></i>';
        } else {
            audioPlayer.pause();
            playPauseBtn.innerHTML = '<i class="fas fa-play"></i>';
        }
    });

    // عقب و جلو بردن صدا
    backwardButton.addEventListener('click', function() {
        audioPlayer.currentTime = Math.max(0, audioPlayer.currentTime - 5);
    });

    forwardButton.addEventListener('click', function() {
        audioPlayer.currentTime = Math.min(audioPlayer.duration, audioPlayer.currentTime + 5);
    });

    // بروزرسانی زمان پخش و نوار پیشرفت
    audioPlayer.addEventListener('timeupdate', function() {
        var percent = (audioPlayer.currentTime / audioPlayer.duration) * 100;
        progress.style.width = percent + '%';
        currentTimeElem.textContent = formatTime(audioPlayer.currentTime);
    });

    audioPlayer.addEventListener('loadedmetadata', function() {
        durationTimeElem.textContent = formatTime(audioPlayer.duration);
    });

    // جلو بردن صدا با کلیک روی نوار پیشرفت
    progressBar.addEventListener('click', function(event) {
        var percent = (event.offsetX / progressBar.offsetWidth);
        audioPlayer.currentTime = percent * audioPlayer.duration;
    });

    // فرمت کردن زمان به دقیقه و ثانیه
    function formatTime(seconds) {
        var minutes = Math.floor(seconds / 60);
        var seconds = Math.floor(seconds % 60);
        if (seconds < 10) {
            seconds = '0' + seconds;
        }
        return minutes + ':' + seconds;
    }

    // اشتراک‌گذاری در تلگرام
    shareButton.addEventListener('click', function() {
        var url = window.location.href;
        var telegramUrl = 'https://t.me/share/url?url=' + encodeURIComponent(url);
        window.open(telegramUrl, '_blank');
    });
});
