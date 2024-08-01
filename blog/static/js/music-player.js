// document.addEventListener("DOMContentLoaded", function() {
//     var audioPlayer = document.getElementById('audioPlayer');
//     var progress = document.getElementById('progress');
//     var progressBar = document.getElementById('progressBar');
//     var currentTimeElem = document.getElementById('currentTime');
//     var durationTimeElem = document.getElementById('durationTime');
//     var playPauseBtn = document.getElementById('playPauseBtn');
//     var backwardButton = document.getElementById('backwardButton');
//     var forwardButton = document.getElementById('forwardButton');
//     var shareButton = document.getElementById('shareButton');
//
//     playPauseBtn.addEventListener('click', function() {
//         if (audioPlayer.paused || audioPlayer.ended) {
//             audioPlayer.play();
//             playPauseBtn.innerHTML = '<i class="fas fa-pause"></i>';
//         } else {
//             audioPlayer.pause();
//             playPauseBtn.innerHTML = '<i class="fas fa-play"></i>';
//         }
//     });
//
//     backwardButton.addEventListener('click', function() {
//         if (audioPlayer.readyState >= 3) {
//             audioPlayer.currentTime = Math.max(0, audioPlayer.currentTime - 5);
//         }
//     });
//
//     forwardButton.addEventListener('click', function() {
//         if (audioPlayer.readyState >= 3) {
//             audioPlayer.currentTime = Math.min(audioPlayer.duration, audioPlayer.currentTime + 5);
//         }
//     });
//
//     audioPlayer.addEventListener('timeupdate', function() {
//         if (audioPlayer.readyState >= 3) {
//             var percent = (audioPlayer.currentTime / audioPlayer.duration) * 100;
//             progress.style.width = percent + '%';
//             currentTimeElem.textContent = formatTime(audioPlayer.currentTime);
//         }
//     });
//
//     audioPlayer.addEventListener('loadedmetadata', function() {
//         durationTimeElem.textContent = formatTime(audioPlayer.duration);
//     });
//
//     progressBar.addEventListener('click', function(event) {
//         if (audioPlayer.readyState >= 3) {
//             var percent = (event.offsetX / progressBar.offsetWidth);
//             audioPlayer.currentTime = percent * audioPlayer.duration;
//         }
//     });
//
//     function formatTime(seconds) {
//         var minutes = Math.floor(seconds / 60);
//         var seconds = Math.floor(seconds % 60);
//         if (seconds < 10) {
//             seconds = '0' + seconds;
//         }
//         return minutes + ':' + seconds;
//     }
//
//     shareButton.addEventListener('click', function() {
//         var url = window.location.href;
//         var telegramUrl = 'https://t.me/share/url?url=' + encodeURIComponent(url);
//         window.open(telegramUrl, '_blank');
//     });
// });
//
// document.getElementById('likeBtn').addEventListener('click', function() {
//     var btn = this;
//     var postId = btn.getAttribute('data-post-id');
//     fetch(`/like/${postId}/`, {
//         method: 'POST',
//         headers: {
//             'X-CSRFToken': '{{ csrf_token }}',
//             'Content-Type': 'application/json'
//         }
//     })
//     .then(response => {
//         if (!response.ok) {
//             throw new Error('Network response was not ok');
//         }
//         return response.json();
//     })
//     .then(data => {
//         if (data.liked) {
//             btn.classList.remove('far');
//             btn.classList.add('fas');
//         } else {
//             btn.classList.remove('fas');
//             btn.classList.add('far');
//         }
//         document.getElementById('likesCount').innerText = data.likes_count;
//     })
//     .catch(error => console.error('Error:', error));
// });
