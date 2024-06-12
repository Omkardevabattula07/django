document.getElementById("password").addEventListener("focus", function() {
    document.getElementById("login-img").src = "{% static 'videos_images/image2.jpg' %}";
});
console.log("hello");