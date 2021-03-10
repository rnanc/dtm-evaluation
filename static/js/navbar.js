function logout(){
  document.cookie = "access_token_cookie=";
  document.cookie = "patient_id=";
  document.cookie = "user_id=";
  document.cookie = "username=";
  window.location.href = "/";
}
