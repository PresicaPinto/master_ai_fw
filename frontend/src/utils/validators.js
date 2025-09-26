export function isValidEmail(email) {
  const re = /^(([^<>()[\\]\\.,;:\s@\"]+(\\.[^<>()[\\]\\.,;:\s@\"]+)*)|(\".+\"))@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
}

export function isStrongPassword(password) {
  // At least 8 characters, one uppercase, one lowercase, one number, one special character
  const re = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[!@#$%^&*()_+}{\":;?/>.<,])(?=.{8,})/;
  return re.test(password);
}
