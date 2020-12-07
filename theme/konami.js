(function () {
  function konamiCode(callback) {
    // The famous Konami sequence in keycodes
    // up up down down left right left right b a
    var sequence = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65];
    var ko = Array.from(sequence);

    // Get the rest of this function's arguments (if any).
    // These will be used as the callback's arguments.
    var args = [];
    for (var i = 1; i < arguments.length; i++) {
      args.push(arguments[i]);
    }

    document.addEventListener("keydown", function (e) {
      if (e.keyCode === ko[0]) {
        ko.splice(0, 1);
        if (ko.length === 0) {
          callback.apply(null, args);
        }
      } else {
        ko = Array.from(sequence);
      }
    });
  }

  function showClip() {
    var video = document.createElement("video");
    video.setAttribute("controls", "");
    video.setAttribute("autoplay", "autoplay");
    video.style.position = "fixed";
    video.style.right = "0";
    video.style.bottom = "0";
    video.style.width = "100%";
    video.style.height = "100%";
    video.style["object-fit"] = "cover";
    video.style.opacity = "0.6";

    var src = document.createElement("source");
    src.setAttribute("src", "https://junk.imnhan.com/rain-480-cropped.mp4");
    src.setAttribute("type", "video/mp4");
    video.appendChild(src);

    document.body.appendChild(video);
  }

  window.addEventListener("DOMContentLoaded", function () {
    konamiCode(showClip);
  });
})();
