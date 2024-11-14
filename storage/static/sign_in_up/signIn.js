$(document).ready(function() {
  $("#make-new-acc").click(function() {
    $("#sign-in-up").html("Sign up");
    $(".sign-in").fadeOut();
    $(".sign-up").css({
      "display": "block"
    });
  });
});