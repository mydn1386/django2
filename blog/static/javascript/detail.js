
        var audioPlayer = document.getElementById('audioPlayer');
        var progress = document.getElementById('progress');
        var progressBar = document.getElementById('progressBar');
        var currentTimeElem = document.getElementById('currentTime');
        var durationTimeElem = document.getElementById('durationTime');
        var playPauseBtn = document.getElementById('playPauseBtn');
        var isPlaying = false;

        audioPlayer.addEventListener('timeupdate', updateProgress);
        audioPlayer.addEventListener('loadedmetadata', () => {
            durationTimeElem.textContent = formatTime(audioPlayer.duration);
        });

        function playPause() {
            if (isPlaying) {
                audioPlayer.pause();
                playPauseBtn.innerHTML = '<i class="fas fa-play"></i>';
            } else {
                audioPlayer.play();
                playPauseBtn.innerHTML = '<i class="fas fa-pause"></i>';
            }
            isPlaying = !isPlaying;
        }

        function updateProgress() {
            var percent = (audioPlayer.currentTime / audioPlayer.duration) * 100;
            progress.style.width = percent + '%';
            currentTimeElem.textContent = formatTime(audioPlayer.currentTime);
        }

        function seek(event) {
            var percent = event.offsetX / progressBar.offsetWidth;
            audioPlayer.currentTime = percent * audioPlayer.duration;
        }

        function seekBackward() {
            audioPlayer.currentTime = Math.max(0, audioPlayer.currentTime - 5);
        }

        function seekForward() {
            audioPlayer.currentTime = Math.min(audioPlayer.duration, audioPlayer.currentTime + 5);
        }

        function formatTime(seconds) {
            var minutes = Math.floor(seconds / 60);
            var seconds = Math.floor(seconds % 60);
            if (seconds < 10) {
                seconds = '0' + seconds;
            }
            return minutes + ':' + seconds;
        }
