//
// document.addEventListener("DOMContentLoaded", function() {
//     // Select necessary elements
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
//     // Variable to track playing state
//     var isPlaying = false;
//
//     // Event listeners
//     if (audioPlayer) {
//         // Update progress bar on timeupdate
//         audioPlayer.addEventListener('timeupdate', function() {
//             var percent = (audioPlayer.currentTime / audioPlayer.duration) * 100;
//             progress.style.width = percent + '%';
//             currentTimeElem.textContent = formatTime(audioPlayer.currentTime);
//         });
//
//         // Set duration time when metadata is loaded
//         audioPlayer.addEventListener('loadedmetadata', function() {
//             durationTimeElem.textContent = formatTime(audioPlayer.duration);
//         });
//
//         // Play/pause button click handler
//         playPauseBtn.addEventListener('click', function() {
//             if (audioPlayer.paused || audioPlayer.ended) {
//                 audioPlayer.play();
//                 playPauseBtn.innerHTML = '<i class="fas fa-pause"></i>';
//             } else {
//                 audioPlayer.pause();
//                 playPauseBtn.innerHTML = '<i class="fas fa-play"></i>';
//             }
//             isPlaying = !audioPlayer.paused;
//         });
//
//         // Progress bar click to seek
//         progressBar.addEventListener('click', function(event) {
//             var percent = (event.offsetX / progressBar.offsetWidth);
//             audioPlayer.currentTime = percent * audioPlayer.duration;
//         });
//
//         // Backward button click to seek backward
//         backwardButton.addEventListener('click', function() {
//             var newTime = audioPlayer.currentTime - 5;
//             audioPlayer.currentTime = newTime >= 0 ? newTime : 0;
//         });
//
//         // Forward button click to seek forward
//         forwardButton.addEventListener('click', function() {
//             var newTime = audioPlayer.currentTime + 5;
//             audioPlayer.currentTime = newTime <= audioPlayer.duration ? newTime : audioPlayer.duration;
//         });
//
//         // Share button click to open Telegram share link
//         if (shareButton) {
//             shareButton.addEventListener('click', function() {
//                 var url = window.location.href;
//                 var telegramUrl = 'https://t.me/share/url?url=' + encodeURIComponent(url);
//                 window.open(telegramUrl, '_blank');
//             });
//         }
//
//         // Format time function
//         function formatTime(seconds) {
//             var minutes = Math.floor(seconds / 60);
//             var seconds = Math.floor(seconds % 60);
//             if (seconds < 10) {
//                 seconds = '0' + seconds;
//             }
//             return minutes + ':' + seconds;
//         }
//     }
// });
// $(document).ready(function(){
//   $("#comment_form").submit(function(event){
//     event.preventDefault();
//     $.ajax({
//       type: "POST",
//       url: "{% url 'blog:post_detail' slug=post.slug pk=post.pk %}",
//       data: $(this).serialize(),
//       success: function(data){
//         $("#comments").append(data.new_comment);
//       },
//       error: function(error){
//         console.log(error);
//       }
//     });
//   });
// });