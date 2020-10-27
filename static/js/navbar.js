function logout(){
  document.cookie = "access_token_cookie=";
  window.location.href = "/";
}
